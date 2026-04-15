

DATA_DIR = "data/raw"   # data path 
IMG_SIZE = (224, 224)
BATCH_SIZE = 32
EPOCHS = 30  # Increased for better training


# vehicle types 
CLASSES = {
    "car": "car on road",
    "motorcycle": "motorcycle on road",
    "truck": "truck vehicle",
    "bus": "bus on road",
    "bicycle": "bicycle"
}