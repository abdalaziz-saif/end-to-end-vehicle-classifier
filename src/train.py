import sys ,os 
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow import keras
from tensorflow.keras import layers
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import DATA_DIR , CLASSES , EPOCHS , BATCH_SIZE , IMG_SIZE

def train_model ():
    # training
    train_ds = tf.keras.utils.image_dataset_from_directory(
        DATA_DIR,
        validation_split=0.2,
        subset="training",
        seed=42,
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE
    )

    # validation set
    val_ds = tf.keras.utils.image_dataset_from_directory(
        DATA_DIR,
        validation_split=0.2,
        subset="validation",
        seed=42,
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE
    )

    class_names = train_ds.class_names
    num_classes = len(class_names)
    print("Classes:", class_names)


    # augmentation
    data_aug = keras.Sequential([
            layers.RandomFlip("horizontal"),
            layers.RandomRotation(0.1),
        ])

    # model usnig transfer learning (mobileNetv2) model 

    base_model = keras.applications.MobileNetV2(
        input_shape=(224,224,3),
        include_top=False,
        weights='imagenet'
        )
    base_model.trainable = False  # freez base 

    model = keras.Sequential([
            layers.Rescaling(1./255),
            data_aug,
            base_model,
            layers.GlobalAveragePooling2D(),
            layers.Dense(128, activation='relu'),
            layers.Dense(num_classes, activation='softmax')
        ])

    # compile 
    model.compile(
            optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy']
        )

    # fit the model 
    history = model.fit(train_ds, validation_data=val_ds, epochs=EPOCHS)
    # save the model 
    os.makedirs("./models", exist_ok=True)
    model.save("models/vehicle_model.keras")

    return class_names ,history , val_ds


