import os
import tensorflow as tf
from pathlib import Path
from PIL import Image

DATA_DIR = "data/raw"

print("Thorough image validation and cleanup...")
total_removed = 0

for class_folder in Path(DATA_DIR).iterdir():
    if not class_folder.is_dir():
        continue
    
    print(f"\nChecking {class_folder.name}...")
    corrupted = []
    
    for img_file in sorted(class_folder.glob('*')):
        try:
            # First try PIL
            with Image.open(img_file) as img:
                img.load()
                img_format = img.format
            
            # Then try TensorFlow decode
            img_data = tf.io.read_file(str(img_file))
            
            # Try JPEG
            try:
                tf.image.decode_jpeg(img_data, channels=3)
                continue
            except:
                pass
            
            # Try PNG
            try:
                tf.image.decode_png(img_data, channels=3)
                continue
            except:
                pass
            
            # Try GIF
            try:
                tf.image.decode_gif(img_data)
                continue
            except:
                pass
            
            # If all fail, it's corrupted
            corrupted.append(img_file)
            
        except Exception as e:
            corrupted.append(img_file)
    
    if corrupted:
        print(f"  Found {len(corrupted)} corrupted images:")
        for img_file in corrupted:
            print(f"    Removing: {img_file.name}")
            try:
                os.remove(img_file)
                total_removed += 1
            except:
                pass
    else:
        print(f"  All images OK!")

print(f"\nCleanup complete. Removed {total_removed} corrupted images.")
