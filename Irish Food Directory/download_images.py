import os
import requests
from urllib.parse import urlparse

def download_image(url, save_path):
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    # Download the image
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {save_path}")
    else:
        print(f"Failed to download: {url}")

# Image URLs and their save paths
images = {
    "images/irish-landscape.jpg": "https://images.unsplash.com/photo-1590086783191-a0694c7d1e6e?q=80&w=2000",
    "images/dishes/irish-stew.jpg": "https://images.unsplash.com/photo-1547592166-23ac45744acd?q=80&w=1200",
    "images/dishes/colcannon.jpg": "https://images.unsplash.com/photo-1482049016688-2d3e1b311543?q=80&w=1200",
    "images/dishes/boxty.jpg": "https://images.unsplash.com/photo-1506084868230-bb9d95c24759?q=80&w=1200",
    "images/restaurants/brazen-head.jpg": "https://images.unsplash.com/photo-1514933651103-005eec06c04b?q=80&w=1200",
    "images/restaurants/paradiso.jpg": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?q=80&w=1200",
    "images/restaurants/le-petit-pois.jpg": "https://images.unsplash.com/photo-1466978913421-dad2ebd01d17?q=80&w=1200",
    "images/blog/galway-food-trail.jpg": "https://images.unsplash.com/photo-1601050690597-df0568f70950?q=80&w=1200",
    "images/blog/dublin-seafood.jpg": "https://images.unsplash.com/photo-1599458252573-56ae36120de1?q=80&w=1200",
    "images/blog/cork-market.jpg": "https://images.unsplash.com/photo-1533900298318-6b8da08a523e?q=80&w=1200",
    "images/author/patrick-tobin.jpg": "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?q=80&w=800"
}

# Download all images
for save_path, url in images.items():
    download_image(url, save_path) 