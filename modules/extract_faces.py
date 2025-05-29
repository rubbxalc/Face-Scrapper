import cv2
import os

def extract_faces_from_directory(images_dir, faces_dir):
    if not os.path.exists(faces_dir):
        os.makedirs(faces_dir)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    count = 0

    for filename in os.listdir(images_dir):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            img_path = os.path.join(images_dir, filename)
            img = cv2.imread(img_path)
            if img is None:
                continue
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(64, 64))
            for i, (x, y, w, h) in enumerate(faces):
                face = img[y:y+h, x:x+w]
                face_filename = os.path.join(faces_dir, f"{os.path.splitext(filename)[0]}_face_{i+1}.jpg")
                cv2.imwrite(face_filename, face)
                count += 1
    print(f"Extracted {count} face(s) into '{faces_dir}'.")