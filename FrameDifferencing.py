import cv2
import numpy as np
import time

# Initialize the video capture object
cap = cv2.VideoCapture("Videos/Cars.mp4")
                          
# Read the first frame
ret , prev_frame = cap . read ()
if not ret :
    print (" Failed to read the video ")
    cap . release ()
    exit ()

# Get the FPS of the video
fps = cap . get ( cv2 . CAP_PROP_FPS )
# Calculate the interval between each frame in seconds
frame_interval = 1.0 / fps

# Convert the first frame to grayscale
prev_frame = cv2 . cvtColor ( prev_frame , cv2 . COLOR_BGR2GRAY )

# Loop over all frames in the video
while True :
    start_time = time . time () # Start time of the frame
    ret , curr_frame = cap . read ()
    if not ret :
        break
        
    # Calculate remaining time for the frame
    elapsed_time = time . time () - start_time
    delay = max (int (( frame_interval - elapsed_time ) * 1000) , 1) #Delay in milliseconds

    # Convert to grayscale and apply Gaussian blur
    curr_frame_gray = cv2 . cvtColor ( curr_frame , cv2 . COLOR_BGR2GRAY )
    dst = cv2.GaussianBlur(curr_frame_gray,(5,5),cv2.BORDER_DEFAULT)

    # Frame differencing
    frame_diff = cv2 . absdiff ( prev_frame , curr_frame_gray )

    #set threshold
    _, thresh_frame_diff = cv2.threshold(frame_diff, 20, 255, cv2.THRESH_BINARY)

    #dilation
    kernel = np.ones((7,7), np.uint8)
    thresh_frame_diff = cv2.dilate(thresh_frame_diff, kernel, iterations=5)

    # Display the result
    cv2 . imshow ("Frame Difference", thresh_frame_diff)

    # Up date previous frame
    prev_frame = curr_frame_gray

    # Break the loop if ’q’ is pressed
    if cv2 . waitKey (delay) & 0xFF == ord("q") :
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()