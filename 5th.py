import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
# read the input image
img = Image.open('lenna.jpg')
# get the pixel values as a flattened array
pixels = img.getdata()
pixels = np.array(img)
pixels = pixels.flatten()

# plot the histogram
plt.hist(pixels, bins=256, range=(0, 255), color='gray', alpha=0.8)
plt.xlabel('Pixel value')
plt.ylabel('Frequency')
plt.title('Histogram of Lenna.jpg')
plt.show()