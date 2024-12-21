
from PIL import Image
import numpy as np
# read the input image

img = Image.open('lenna.jpg')
# convert the image to a NumPy array
img_array = np.array(img)
# crop the image to the desired size
cropped_array = img_array[100:600, 100:600]
# convert the cropped array back to an image
cropped_img = Image.fromarray(cropped_array)
# display the cropped image
cropped_img.show()