import os, sys
from icrawler.builtin import BingImageCrawler, BaiduImageCrawler
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import CLASSES , DATA_DIR 


# download images 

def dawnload_image (img_nums = 500) :
    os.makedirs(DATA_DIR , exist_ok=True)
    
    for class_name ,query  in CLASSES.items():
        folder = os.path.join(DATA_DIR , class_name)
        os.makedirs(folder , exist_ok=True)
        
        # check how many images currently exist
        current_count = len(os.listdir(folder))
        
        # if we already have enough images skip
        if current_count >= img_nums:
            print (f" {class_name} already has {current_count} images (target: {img_nums})")
            continue
        
        # calculate how many more images we need
        images_needed = img_nums - current_count
        
        print (f"Downloading {class_name}  ({images_needed} more needed to reach {img_nums})")
        
        # Try Bing first
        try:
            crawler = BingImageCrawler(storage={"root_dir": folder})
            crawler.crawl(keyword=query, max_num=images_needed)
        except Exception as e:
            print(f"  Bing error: {e}")
        
        # Check if we still need more images
        current_count = len(os.listdir(folder))
        remaining = img_nums - current_count
        
        # If Bing didn't get enough, try Baidu
        if remaining > 0:
            print(f"  Trying Baidu for {remaining} more images...")
            try:
                crawler = BaiduImageCrawler(storage={"root_dir": folder})
                crawler.crawl(keyword=query, max_num=remaining)
            except Exception as e:
                print(f"  Baidu error: {e}")
        
        print (f"{class_name} Done! Total: {len(os.listdir(folder))} images")


if __name__ == "__main__" :
    dawnload_image()
    