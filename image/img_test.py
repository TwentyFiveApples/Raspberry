import numpy as np
import cv2
from PIL import Image

image = cv2.imread('/home/yu/Colin Powell.jpeg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image = np.array(image)
image = np.array(Image.fromarray(image).resize((50, 37)))
print(image.shape)
