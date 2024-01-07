import cv2
import matplotlib.pyplot as plt
import numpy as np

#Read image
image = cv2.imread("Images/mario.jpg")

#Convert BGR to RGB (OpenCV loads images in BGR format)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#Calculate histograms for each channel
hist_r = cv2.calcHist([image], [0], None, [256], [0,256])
hist_g = cv2.calcHist([image], [1], None, [256], [0,256])
hist_b = cv2.calcHist([image], [2], None, [256], [0,256])

#Generate X values (0-255 for each channel)
x_values = np.arange(256)

# Plot the histograms
plt.figure()
plt.bar(x_values, hist_r.ravel(), color='red', alpha=0.5, label='Red channel')
plt.bar(x_values, hist_g.ravel(), color='green', alpha=0.5, label='Green channel')
plt.bar(x_values, hist_b.ravel(), color='blue', alpha=0.5, label='Blue channel')
plt.title("RGB Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.legend()
plt.show()