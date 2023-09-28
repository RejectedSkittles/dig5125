import cv2
import matplotlib.pyplot as plt
image = cv2.imread('Images/mario.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

#access a single pixel
pixel_value = image[50,50]
#access a row
row_values = image[50, :]
#access a channel
red_channel = image[:, :, 0]

#increase intensity of the red channel by 50
image[:, :, 0] += 50

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()