import requests
import re

def search_google_images(query):
    if not query:
        raise ValueError('Query parameter "q" is required.')

    url = f"https://www.google.com/search?q={query}&oq={query}&sclient=img&udm=2"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-site"
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            raise Exception("Failed to fetch from Google")

        html = response.text

        image_ids = re.findall(r'https://encrypted-tbn0\.gstatic\.com/images\?q\\u003dtbn:([A-Za-z0-9-_]+)', html)
        
        return image_ids

    except Exception as e:
        print(f"Error while searching Google Images: {e}")
        return []