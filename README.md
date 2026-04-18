# Vehicle Type Classification

A deep learning project that classifies images into 5 vehicle types using transfer learning with MobileNetV2. The model achieves 75.83% validation accuracy on a dataset of 1,656 images collected through web scraping. Images were gathered using Baidu and Bing crawlers, followed by a preprocessing pipeline that cleaned and standardized the dataset using pathlib and PIL to ensure consistent formatting and quality.

## 🚗 Project Overview

This project automatically identifies vehicle types from images by leveraging:
- **Web scraping** (Bing/Baidu Image Crawler) to automatically gather 1,656+ training images
- **Transfer Learning** with pre-trained MobileNetV2 model for efficient training
- **Advanced data augmentation** (flip, rotation, zoom, brightness, contrast, translation)
- **Fine-tuning strategy** with learning rate scheduling
- **Early stopping** to prevent overfitting
- **evaluation metrics** and model summaries

### Supported Vehicle Types
- 🚗 **Cars** -  
- 🏍️ **Motorcycles** - 
- 🚛 **Trucks** 
- 🚌 **Buses**  
- 🚴 **Bicycles** -

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| Training Accuracy | 75.25% |
| Validation Accuracy | **75.83%** |
| Training Data | 1,325 images |
| Validation Data | 331 images |
| Model | MobileNetV2 (Transfer Learning) |
| Input Size | 224 × 224 |
| Batch Size | 32 |
| Epochs | ~30 (with early stopping) |
| Learning Rate | 1e-4 (adaptive scheduling) |

## 🛠️ Installation & Setup


### Step-by-Step Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd Vehicle-Type-Classification
```

2. **Create a virtual environment** 
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 🚀 Usage

The project uses **argparse** for easy command-line control with three main modes:

### 1. Download Images
Downloads vehicle images from web sources (Bing/Baidu Image Search):
```bash
python main.py --mode download
```
- Downloads ~1,500 images per vehicle class (configurable)
- Saves images to `data/raw/<class>/`
- Automatically removes corrupted images
- Skips download if images already exist

### 2. Train the Model
Trains the MobileNetV2 model with advanced techniques:
```bash
python main.py --mode train
```
Features:
- Automatic data validation and cleanup
- Advanced data augmentation (rotation, zoom, brightness, contrast, translation)
- Transfer learning with selective fine-tuning
- Learning rate scheduling for convergence
- Early stopping to prevent overfitting
- Saves best model to `models/vehicle_model.keras`
- Generates metrics and evaluation reports

**Training time:** ~20-30 minutes on CPU

### 3. Make Predictions
Classifies a vehicle image and returns the predicted type with confidence:
```bash
python main.py --mode predict
```
Example output:
```
THIS IS A CAR
CONFIDENCE: 87.5%
```

## 📁 Project Structure

```
Vehicle-Type-Classification/
├── main.py                 # Entry point with CLI
├── config.py              # Configuration (paths, hyperparameters)
├── requirements.txt       # Python dependencies
│
├── src/
│   ├── downloader.py      # Web scraping (Bing/Baidu crawler)
│   ├── train.py           # Model training with transfer learning
│   ├── evaluate_model.py  # Evaluation & visualizations
│   └── predict.py         # Single image prediction
│
├── data/
│   └── raw/               # Image dataset (~1,656 images)
│       ├── bicycle/
│       ├── bus/
│       ├── car/
│       ├── motorcycle/
│       └── truck/
│
├── models/
│   └── vehicle_model.keras    # Trained model
│
└── outputs/
    ├── metrics.json           # Accuracy metrics
    ├── model_summary.txt      # Model architecture
    └── report.txt             # Evaluation report
```

## ⚙️ Configuration

Edit `config.py` to customize parameters:

```python
DATA_DIR = "data/raw"           # Path to dataset
IMG_SIZE = (224, 224)           # Input image size
BATCH_SIZE = 32                 # Training batch size  
EPOCHS = 30                     # Max epochs (uses early stopping)

CLASSES = {
    "car": "car on road",
    "motorcycle": "motorcycle on road", 
    "truck": "truck vehicle",
    "bus": "bus on road",
    "bicycle": "bicycle"
}
```

## 🔧 Training Hyperparameters

The model uses optimized hyperparameters for best performance:

- **Base Model:**  Fine-tunied MobileNetV2
- **Frozen Layers:** First 50 layers (unfroze 85+ for fine-tuning)
- **Optimizer:** Adam
- **Loss:** Sparse Categorical Crossentropy
- **Augmentation:** Flip, Rotation, Zoom, Brightness, Contrast, Translation
- **Dropout:** 0.3 (prevent overfitting)
- **Early Stopping:** Patience of 5 epochs



## 🤖 Model Architecture

- **Base Model**: MobileNetV2 (pre-trained on ImageNet)
- **Transfer Learning**: Frozen base layers + custom top layers
- **Data Augmentation**: Random horizontal flip, random rotation
- **Custom Head**:
  - Global Average Pooling
  - Dense layer (128 units, ReLU activation)
  - Output layer (5 units, Softmax activation)

## 📈 Output Files

After running training mode, the following files are generated in `outputs/`:

- **confusion_matrix.png** - Heatmap showing prediction accuracy per class
- **metrics.json** - Training and validation accuracy scores
- **report.txt** - Detailed classification report with precision/recall
- **model_summary.txt** - Full model architecture and parameters

## ⚖️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋 Support

For issues or questions, please open an issue on GitHub.

---

**Made with ❤️ By Abdalaziz **
