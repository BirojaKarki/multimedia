from PIL import Image
import numpy as np

image=Image.open("lenna.jpg")

# Show image properties
print(image.size)
print(image.format)
print(image.mode)

# Convert image to NumPy array
nparray = np.array(image)
print(nparray.shape)
print(type(nparray))
print(nparray)

# Convert NumPy array back to image
pilImage = Image.fromarray(nparray)
print(pilImage.mode)
print(pilImage.size)

# Create and save a random image
x = np.random.randint(0, 256, (512, 512, 3), dtype=np.uint8)
img = Image.fromarray(x)
img.save("sample.jpg")
