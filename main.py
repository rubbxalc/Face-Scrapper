import sys
from modules.image_scraper import ImageScraper

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <search term>")
        sys.exit(1)
    search_term = " ".join(sys.argv[1:])
    scraper = ImageScraper(search_term)
    scraper.run()