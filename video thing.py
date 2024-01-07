import cv2

cap = cv2.VideoCapture('Images/Video1.avi')

if not cap.isOpened():
    print ("error: could not open video")
    exit()
   
   
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow('frame', frame)
       
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
       
    else:
        break
   
cap.release()
cv2.destroyAllWindows()