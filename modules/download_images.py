import os

def download_images(directory, image_ids):
    if not os.path.exists(directory):
        os.makedirs(directory)
    for idx, img_id in enumerate(image_ids, start=1):
        img_url = f"https://encrypted-tbn0.gstatic.com/images?q=tbn:{img_id}"
        try:
            import requests
            img_data = requests.get(img_url).content
            file_path = os.path.join(directory, f"image_{idx}.jpg")
            with open(file_path, "wb") as f:
                f.write(img_data)
            print(f"Downloaded image {idx}: {file_path}")
        except Exception as e:
            print(f"Error downloading image {idx}: {e}")