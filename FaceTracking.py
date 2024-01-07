import cv2
import numpy as np
from tkinter import Tk, Button, Scale, Label, HORIZONTAL, filedialog
import time

def preprocess_frame ( frame ):
    # Convert to grayscale and apply a gaussian blur effect
    gray = cv2.cvtColor( frame , cv2 . COLOR_BGR2GRAY )
    blurred = cv2.GaussianBlur( gray , (21 , 21) , 0)
    return blurred

def absolute_difference(prev_frame, current_frame):
    # Retrieve the height and width of previous frame
    h, w, = prev_frame.shape
    # Create a copy of the previous frame to apply difference to
    frame_diff = prev_frame.copy() 

    # Iterate through the pixels and their channels
    for row in range(h):
        for column in range(w):
            # Store the pixel difference in frame_diff
                frame_diff[row, column] = abs(int(prev_frame[row, column]) - int(current_frame[row, column]))
                

    return frame_diff


def threshold_image(image):
    # Create a copy of the frame
    thresh_img = np.copy(image)
    # Set the pixel values lower than 10 to 0
    thresh_img[thresh_img <= 10] = 0
    # Set the pixel values higher than 10 to 255
    thresh_img[thresh_img > 10] = 255

    return thresh_img

def finalize(thresh):
    thresh = cv2.dilate( thresh , None , iterations =2)
    thresh = cv2.erode( thresh , None , iterations =2)
    return thresh

# Open video
path = filedialog.askopenfilename()
cap = cv2.VideoCapture(path)

# Check if a video has been opened
if not cap.isOpened() :
    print("Error opening video stream or file ")
    exit()

# Assign video fps
fps = cap.get(cv2.CAP_PROP_FPS )

# Read the first frame
ret , first_frame = cap.read()
if not ret :
    # Show error message if video fails to load
    print(" Failed to read the video ")
    cap.release()
    exit()

# Make the frame gray and blurred
prev_frame = preprocess_frame( first_frame )

while True:
    ret , frame = cap.read()
    if not ret :
        break

    # Make the frame gray and blurred
    current_frame = preprocess_frame( frame )

    # Assign frame_diff the differences between the current frame and the previous one
    frame_diff = absolute_difference(prev_frame,current_frame)

    # Apply thresholding to get a binary image
    thresh = threshold_image(frame_diff)

    # Apply morphological operations to remove noise and fill in holes
    thresh = finalize(thresh)

    # Find contours on the thresholded imag
    contours , _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE )

    for contour in contours :
        if cv2.contourArea (contour) < 1000: # Minimum area threshold
            continue
        # Create a rectangle around the contoured areas
        (x , y , w , h) = cv2.boundingRect (contour)
        cv2.rectangle( frame , (x , y ) , (x + w , y + h) , (0 , 255 , 0) , 2)

    # Display the resulting frame
    cv2.imshow("Frame", frame )
    #cv2.imshow("Threshold", thresh )

    # Quit if the q key is pressed
    key = cv2.waitKey(int (1000/ fps ) ) & 0xFF
    if key == ord('q'):
        break

    prev_frame = current_frame
cap.release()
