import cv2
import numpy as np

cap = cv2.VideoCapture('Videos/Cars.mp4')
ret , prev_frame = cap.read ()
while cap.isOpened () :
    ret , frame = cap.read ()
    if not ret :
        break

    frame = cv2.GaussianBlur(frame,(5,5),cv2.BORDER_DEFAULT)
    diff = cv2.absdiff ( prev_frame , frame )
    #set threshold
    _, thresh_diff = cv2.threshold(diff, 20, 255, cv2.THRESH_BINARY)
    kernel = np.ones((7,7), np.uint8)
    thresh_diff = cv2.dilate(thresh_diff, kernel, iterations=5)

    cv2.imshow('Frame Difference', thresh_diff )
    prev_frame = frame.copy()
    if cv2.waitKey(30) & 0xFF == ord ('q'):
        break

cap.release ()
cv2.destroyAllWindows ()
