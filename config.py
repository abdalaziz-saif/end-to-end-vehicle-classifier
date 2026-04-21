DATA_DIR = "data/raw"
IMG_SIZE = (224, 224)
BATCH_SIZE = 32
EPOCHS = 30

# vehicle Types 


CLASSES = {
    "car": [
        "car on road",
        "sedan automobile",
        "hatchback car street",
        "car driving highway"
    ],
    "motorcycle": [
        "motorcycle on road",
        "motorbike street",
        "sport motorcycle riding",
        "motorcycle highway"
    ],
    "truck": [
        "truck vehicle road",
        "cargo truck highway",
        "pickup truck",
        "semi truck freight"
    ],
    "bus": [
        "bus on road",
        "city bus street",
        "school bus",
        "public transport bus"
    ],
    "bicycle": [
        "bicycle on road",
        "bike cycling street",
        "mountain bike riding",
        "bicycle city"
    ],
    "plane": [
        "airplane flying sky",
        "commercial aircraft flight",
        "passenger plane airport",
        "jet airplane takeoff"
    ],
    "ship": [
        "cargo ship ocean",
        "large vessel sea",
        "container ship sailing",
        "cruise ship water"
    ],
    "auto_rickshaw": [
        "auto rickshaw street",
        "tuk tuk vehicle",
        "three wheeler rickshaw road",
        "auto rickshaw india traffic"
    ],
    "train": [
        "passenger train railway",
        "train on tracks",
        "freight train railroad",
        "high speed train"
    ]
}