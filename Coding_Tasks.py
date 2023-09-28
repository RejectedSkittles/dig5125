import cv2
import matplotlib.pyplot as plt
image = cv2.imread('Images/mario.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

#ROWS | COLUMNS | CHANNELS

plt.subplot(1, 3, 1)
plt.imshow(image)
plt.axis('off')
plt.title('Original Image')

plt.subplot(1, 3, 2)
plt.imshow(gray_image)
plt.axis('off')
plt.title('Greyscale Image')

plt.subplot(1, 3, 3)
plt.imshow(binary_image)
plt.axis('off')
plt.title('Black and White Image')

plt.show()


