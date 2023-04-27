import tensorflow as tf
import numpy as np
import cv2
from PIL import Image

image_path = '/home/yu/Colin Powell.jpeg'
image = Image.open(image_path)
resized_image = image.resize((37,50))
grayscale_image = resized_image.convert('L')
image_array = np.array(grayscale_image)
image_array = image_array.astype(np.float32)

input_data = np.expand_dims(image_array, axis=(0,-1))
input_data = np.expand_dims(input_data, axis=0)
input_data = np.squeeze(input_data, axis=0)


model_path = '/home/yu/my_model.tflite'



interpreter = tf.lite.Interpreter(model_path=model_path)

# Load the TFLite model and allocate tensors.
interpreter = tf.lite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

print(input_details)

# Test the model on random input data.
#input_shape = input_details[0]['shape']
#input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)
interpreter.set_tensor(input_details[0]['index'], input_data)

interpreter.invoke()

# The function `get_tensor()` returns a copy of the tensor data.
# Use `tensor()` in order to get a pointer to the tensor.
output_data = interpreter.get_tensor(output_details[0]['index'])
print(output_data)
