import cv2
import matplotlib.pyplot as plt
import numpy as np

#Read image
image = cv2.imread("Images/mario.jpg")

#Convert BGR to RGB (OpenCV loads images in BGR format)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#Calculate histograms for each channel
hist = cv2.calcHist([image], [0], None, [256], [0, 256])
hist_r = cv2.calcHist([image], [0], None, [256], [0,256])
hist_g = cv2.calcHist([image], [1], None, [256], [0,256])
hist_b = cv2.calcHist([image], [2], None, [256], [0,256])

#Generate X values (0-255 for each channel)
x_values = np.arange(256)

plt.subplot(2,2,1)
plt.title("Grayscale Histogram")
plt.bar(x_values, hist.ravel(), color='gray')
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")

plt.subplot(2,2,2)
plt.title("Red Histogram")
plt.bar(x_values, hist_r.ravel(), color='red')
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")

plt.subplot(2,2,3)
plt.title("Green Histogram")
plt.bar(x_values, hist_g.ravel(), color='green')
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")

plt.subplot(2,2,4)
plt.title("Blue Histogram")
plt.bar(x_values, hist_b.ravel(), color='blue')
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()