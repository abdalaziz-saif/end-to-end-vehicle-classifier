
import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
import argparse

from src.train import train_model
from src.predict import predict
from src.downloader import download_images
from src.evaluate_model import evaluate_model
from config import CLASSES

'''
 note for using the function :  go to the termenal then : 

    download_imges     ->   python  main.py --mode download
    train the model    ->   python  main.py --mode train 
    make a Prediction  ->   python  main.py --mode predict 

    
'''

parser = argparse.ArgumentParser()

parser.add_argument("--mode", type=str, required=True)

args = parser.parse_args()

if args.mode == "download":
    download_images(img_nums=800)

elif args.mode == "train":
    class_names, history, val_ds = train_model()
    evaluate_model(class_names , history , val_ds)

elif args.mode == "predict":
    predict("test_images/php 2(1).jpg", class_names=CLASSES)

