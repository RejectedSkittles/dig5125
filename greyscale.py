import cv2
import matplotlib.pyplot as plt
image = cv2.imread('Images/mario.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()