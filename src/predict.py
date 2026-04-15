import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import sys, os
import tensorflow as tf
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import DATA_DIR, IMG_SIZE, BATCH_SIZE

Model_path =  "models/vehicle_model.keras"

def predict(img_path, class_names=None):
    # Load class names from data directory if not provided
    if class_names is None:
        train_ds = tf.keras.utils.image_dataset_from_directory(
            DATA_DIR,
            image_size=IMG_SIZE,
            batch_size=BATCH_SIZE
        )
        class_names = train_ds.class_names
    elif isinstance(class_names, dict):
        # If class_names is a dict, extract just the keys as a list
        class_names = sorted(class_names.keys())
    
    # Load the model from the path 
    model = load_model(Model_path)

    img = image.load_img(img_path, target_size=(224,224))
    # covert the img to an array 
    arr = image.img_to_array(img)
    arr = np.expand_dims(arr, 0)

    pred = model.predict(arr)
    pred_idx = np.argmax(pred)
    cls = class_names[pred_idx]
    conf = np.max(pred)

    print(f"THIS IS A {cls.upper()}")
    print(f"CONFIDENCE: {conf:.2%}")
