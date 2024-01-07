import cv2 
import numpy as np


video = cv2.VideoCapture(0)


while True:
    ret, frame = video.read()
    if not ret:
        break


    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    h, s, v = cv2.split(hsv)
    s = cv2.multiply(s,1.2) # incease saturation
    v = cv2.multiply(v, 0.8) #increase exposure by 20%
    adjusted_hsv = cv2.merge([h,s,v])

    adjusted_frame = cv2.cvtColor(adjusted_hsv,cv2.COLOR_HSV2BGR)

    combined_frame = np.hstack((frame,adjusted_frame))
    cv2.imshow('original vs adjusted',combined_frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

video.release()
cv2.destroyAllWindows