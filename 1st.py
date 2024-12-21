
from PIL import Image
import os
# read the input image
img = Image.open('lenna.jpg')
# convert to png and save
img.save('lenna.png', 'png')
# convert to tif and save
img.save('lenna.tif', 'tif')
# get the file sizes
jpg_size = os.path.getsize('lenna.jpg')
png_size = os.path.getsize('lenna.png')
tif_size = os.path.getsize('lenna.tiff')
# display the file sizes
print("JPG size: {} bytes".format(jpg_size))
print("PNG size: {} bytes".format(png_size))
print("TIF size: {} bytes".format(tif_size))
# display the actual size of jpg without using any library
with open('lenna.jpg', 'rb') as f:
 data = f.read()
jpg_actual_size = len(data)
print("Actual JPG size: {} bytes".format(jpg_actual_size))