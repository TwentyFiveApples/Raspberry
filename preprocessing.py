import numpy
import cv2

face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

img = cv2.imread('image_path.jpeg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detecMultiScale(gray, 1.3, 3)

for (x, y, w, h) in faces:
    cropped = img[y:y+h, x:x+h]
    cv2.imwrite("save_path", img)
