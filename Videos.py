import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture('Images/Video1.avi')

# Check if camera opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while cap.isOpened():
    # Capture frame-by-frame
    ret , frame = cap.read()
    if ret:
        # Display the resulting frame
        cv2.imshow('Frame', frame)

        # Press Q  on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
        else:
            break

# When everything done , release the video capture object
cap.release()
# Closese all the frames
cv2.destroyAllWindows()