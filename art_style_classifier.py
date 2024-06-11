# I search wit the image with the greater size from the data folder using pillow and numpy
# Imports
import os
from PIL import Image
import numpy as np
import time

# Path to the data folder
data_path = 'data'

# List of all the files in the data folder
dirs = os.listdir(data_path)
print(dirs)
abs_path = os.path.abspath(__file__)
dir_path = os.path.dirname(abs_path)
#path = os.path.join(dir_path, data_path)

# Saving the images in a list
images = []
arr = []
for dir in dirs:
    path = os.path.join(dir_path, data_path, dir, dir)
    images = os.listdir(path)
    print(len(images))
    for img in images:
        with Image.open(os.path.join(path, img)) as pic:
            arr.append(np.array(pic))
        print("I'm going")
print("I'm done")
print(len(images))
cont = 0
time.sleep(2)

# converting the images to numpy arrays
'''for image in images:
    arr = np.array(np.array(Image.open(os.path.join(data_path, image))))
    print(cont)
    cont+=1
    if cont >= len(images):
        break
print("I'm done")'''
arr = np.stack(arr)
# arr = np.array(pics)
print('array: ', arr)
# greater side
print(arr.shape)
greater_side = max(arr.shape[:2])
print(f'The greater side is {greater_side}')
# printing the size of the image with the greater size and saving the size in a variable
'''max_size = 0
max_size_image = ''
for image in images:
    img = Image.open(os.path.join(data_path, image))
    size = img.size[0] * img.size[1]
    if size > max_size:
        max_size = size
        max_size_image = image
        
print(f'The image with the greater size is {max_size_image} with a size of {max_size} pixels')'''
