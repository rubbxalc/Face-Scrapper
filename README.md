# Face-Scrapper

Face-Scrapper is an automated tool to search images on Google, download them, and extract faces using OpenCV. It's ideal for creating face datasets from custom search terms.

## Features

- Search for images on Google using a given term.
- Automatically download the found images.
- Extract faces from the downloaded images using Haar Cascade detection.
- Organize results in folders by search term.

## Requirements

- Python 3.8 or higher
- [requests](https://pypi.org/project/requests/)
- [opencv-python](https://pypi.org/project/opencv-python/)

Install dependencies with:

```sh
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file, create one with:

```
requests
opencv-python
```

## Usage

Run the main script with your search term as an argument:

```sh
python main.py "person name"
```

This will:

1. Search Google Images for the given term.
2. Download the images to `assets/person_name/`.
3. Extract detected faces and save them in `assets/person_name/faces/`.

## Project Structure

```
Face-Scrapper/
├── assets/
├── modules/
│   ├── download_images.py
│   ├── extract_faces.py
│   ├── extract_faces_wrapper.py
│   ├── google_images.py
│   └── image_scraper.py
├── main.py
└── README.md
```

## Credits

- Uses [OpenCV](https://opencv.org/) for face detection.
- Inspired by web scraping and image processing techniques.

## Warning

- Scraping images from Google may be subject to changes in page structure and legal restrictions. Use this project at your own risk and respect Google's terms of service.
- This project is for educational and research purposes only.