# First we import opencv and matplotlib 
# (we will use the latter to display our image)
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Now we specify where our image is in relation to this script
# Since it's in the same folder, we write './image_name.jpg'
image_path = 'Images/mario.jpg'
# We then use the cv2.imread function to load the image from the specified path
image = cv2.imread(image_path)

# OpenCV reads images in BGR instead of RGB by default,
# so we will convert from BGR to RGB so that colours look right 
# when we visualise the image below.
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 

# This multiplies the RGB values of each pixel by 5 and subtracts 100
processed_image = image * 5.0 - 100

# Now we ensure that no pixel values exceed the range 0-255 
# (the allowed range for an 8-bit image)
processed_image = np.clip(processed_image, 0, 255)

# The multiplication operation implicitly converts our image from integer 
# to floating point values, so we need to convert it back to 
# 8-bit integer values, before we display it.
processed_image = processed_image.astype('uint8')

# Now we need to update our visualisation code to show the images side by side
fig, ax = plt.subplots(1,2) # This makes a figure with two subfigures

# In the first subfigure we display the original image
ax[0].imshow(image) 
ax[0].set_xlabel('The original image')
ax[0].set_xticks([]) # removes the x axis ticks (so it looks pretty)
ax[0].set_yticks([]) # removes the y axis ticks

# In the second subfigure we display the processed image
ax[1].imshow(processed_image) 

ax[1].set_xlabel('The processed image')
ax[1].set_xticks([]) # removes the x axis ticks (so it looks pretty)
ax[1].set_yticks([]) # removes the y axis ticks

plt.show() # Display the figures we just created on-screen

processed_image = cv2.cvtColor(processed_image, cv2.COLOR_RGB2BGR)
cv2.imwrite('Outputs/dank.png', processed_image)

