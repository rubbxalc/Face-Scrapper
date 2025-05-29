import os
from modules.extract_faces import extract_faces_from_directory

def extract_faces(directory):
    try:
        faces_dir = os.path.join(directory, "faces")
        extract_faces_from_directory(directory, faces_dir)
    except Exception as e:
        print(f"Error extracting faces: {e}")