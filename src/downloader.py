import os, sys
from icrawler.builtin import BingImageCrawler, BaiduImageCrawler, GoogleImageCrawler, FlickrImageCrawler
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import CLASSES, DATA_DIR
"""
Downloads images from the web using the iCrawler library.
     
- img_nums : Number of images to download per class. Default is 500.
- Before downloading, checks if the folder already contains enough images and skips if Yes.
- Each class has multiple search queries, and the number of images  split evenly across them.
- For each query, crawlers are tried in order (Bing -> Google -> Baidu -> Flickr) until the target is met.
"""


# crawlers 
CRAWLERS = [BingImageCrawler, GoogleImageCrawler, BaiduImageCrawler, FlickrImageCrawler]

def download_images(img_nums=500):
    os.makedirs(DATA_DIR, exist_ok=True)

    for class_name, queries in CLASSES.items():
        folder = os.path.join(DATA_DIR, class_name)
        os.makedirs(folder, exist_ok=True)

        # check how many images currently exist
        current_count = len(os.listdir(folder))

        # if we already have enough images skip
        if current_count >= img_nums:
            print(f"{class_name} already has {current_count} images (target: {img_nums})")
            continue

        # calculate how many more images we need
        images_needed = img_nums - current_count
        print(f"\nDownloading {class_name} ({images_needed} more needed to reach {img_nums})")

        # split number of images envenly across quieres  
        per_query = max(1, images_needed // len(queries))

        for query in queries:
            # check if we still need more images
            remaining = img_nums - len(os.listdir(folder))
            if remaining <= 0:
                break

            quota = min(per_query, remaining)
            print(f"  Searching: '{query}' — need {quota}")

            # try each crawler until we get enough images 
            for CrawlerClass in CRAWLERS:
                try:
                    CrawlerClass(storage={"root_dir": folder}).crawl(keyword=query, max_num=quota)
                except Exception as e:
                    print(f"  {CrawlerClass.__name__} error: {e}")

        print(f"{class_name} Done . Total: {len(os.listdir(folder))} images")

if __name__ == "__main__":
    download_images()