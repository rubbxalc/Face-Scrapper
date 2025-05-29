import os
from modules.google_images import search_google_images
from modules.download_images import download_images
from modules.extract_faces_wrapper import extract_faces

class ImageScraper:
    def __init__(self, search_term):
        self.search_term = search_term
        self.directory = os.path.join("assets", search_term.replace(" ", "_"))

    def run(self):
        images = search_google_images(self.search_term)
        print(f"Found {len(images)} images for search term '{self.search_term}':")
        download_images(self.directory, images)
        extract_faces(self.directory)