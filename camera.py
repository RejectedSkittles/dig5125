import cv2

# Start video capture , ’0 ’ is the default webcam
cap = cv2 . VideoCapture (0)

# Check if the webcam is opened correctly
if not cap.isOpened () :
    raise IOError(" Cannot open webcam ")

while True :
    ret , frame = cap . read ()
    if not ret :
        break

    # Display the resulting frame
    cv2.imshow('Webcam Live', frame )

    # Break the loop when ’q’ is pressed
    if cv2.waitKey(1) & 0xFF == ord('q') :
        break

# When everything is done , release the capture
cap.release()
cv2.destroyAllWindows()