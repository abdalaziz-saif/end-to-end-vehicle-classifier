from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt 
import numpy as np
from tensorflow.keras.models import load_model
import json


def evaluate_model(class_names, history, val_ds):
    # Load the model inside the function
    model = load_model("models/vehicle_model.keras")
   
    y_pred = []
    y_true = []
   
    # predict On the val_ds to see model performance 
    for image, label in val_ds:
        pred  = model.predict(image)
        y_pred.extend(np.argmax(pred , axis = 1))
        y_true.extend(label.numpy())

    # Confusion Matrix 
    cm = confusion_matrix(y_true, y_pred)

    plt.figure(figsize=(8,6))
    sns.heatmap(cm, annot=True, fmt='d',
                xticklabels=class_names,
                yticklabels=class_names)

    plt.savefig("outputs/confusion_matrix.png")
    plt.close()


    # Classification Report 
    
    report = classification_report(y_true, y_pred)

    with open("outputs/report.txt", "w") as f:
        f.write(report)

    # Model Summary 
    with open("outputs/model_summary.txt", "w", encoding="utf-8") as f:
        model.summary(print_fn=lambda x: f.write(x + "\n"))

    # save Model performance as json 
    metrics = {
        "train_accuracy": float(history.history['accuracy'][-1]),
        "val_accuracy": float(history.history['val_accuracy'][-1])
    }

    with open("outputs/metrics.json", "w") as f:
        json.dump(metrics, f, indent=4)