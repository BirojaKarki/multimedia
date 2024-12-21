import numpy as np
from PIL import Image
# generate random numpy array
arr = np.random.randint(0, 256, size=(400, 400), dtype=np.uint8)
# create image from numpy array
img = Image.fromarray(arr)
# save image
img.save('random_array.png')