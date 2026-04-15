import os, sys
from icrawler.builtin import BingImageCrawler
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import CLASSES , DATA_DIR 


# download images 

def dawnload_image (img_nums = 500) :
    os.makedirs(DATA_DIR , exist_ok=True)
    
    for class_name ,query  in CLASSES.items():
        folder = os.path.join(DATA_DIR , class_name)
        os.makedirs(folder , exist_ok=True)
        
        # check if the images exist dont crawl
        if os.path.exists(DATA_DIR) and len(os.listdir(folder)) > 0 :
            print (f"the {class_name} images already exist ")
            continue

        print (f"Downloading  {class_name}  ... ")

        crawler = BingImageCrawler(storage={"root_dir": folder})
        crawler.crawl(keyword=query, max_num=img_nums)


        print (f"{class_name}Done")


if __name__ == "__main__" :
    dawnload_image()
    