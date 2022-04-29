# Python3 code to rotate any image by a fixed angle
# using 2x2 rotation matrix

# Code by:
# Danish Ahmed Mehmuda
# U19EC111

import cv2
import numpy as np
import math
import imageio
from PIL import Image


# Input the image
img = imageio.imread('./images/1.jfif')
rotation_amount_degree = 60

# Convert degree to radian
rotation_amount_rad = rotation_amount_degree * np.pi / 180.0

# Get Image dimensions
height, width, num_channels = img.shape

# Creating output image
# Max size of image will be in case of 45 degrees and its multiple
max_len = int(math.sqrt(height*height + width*width))
rotated_image = np.zeros((max_len, max_len, num_channels))

# Get the rotated height and width
rh, rw, _ = rotated_image.shape

# Get center
mrow = int((rh+1)/2)
mcol = int((rw+1)/2)

# Apply Transformation
for r in range(rh):
    for c in range(rw):
        # Apply 2x2 rotation matrix
        y = (r-mcol)*math.cos(rotation_amount_rad) + \
            (c-mrow)*math.sin(rotation_amount_rad)
        x = -(r-mcol)*math.sin(rotation_amount_rad) + \
            (c-mrow)*math.cos(rotation_amount_rad)

        # Add offset
        y += mcol
        x += mrow
        x = round(x)
        y = round(y)

        # Check if x and y are bounded between the image height and width
        if (x >= 0 and y >= 0 and x < width and y < height):
            rotated_image[r][c][:] = img[y][x][:]


# Save final output
# cv2.imshow(rotated_image)
output_image = Image.fromarray(rotated_image.astype("uint8"))
output_image.save("rotated_image.png")
