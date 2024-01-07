import cv2
import numpy as np

# Load the foreground ( green screen ) video and background video
foreground_video = cv2.VideoCapture("Videos/Flamingo.mp4")
background_video = cv2.VideoCapture("Videos/NatureVideo.mp4")

# Check if both videos were opened successfully
if not foreground_video.isOpened() or not background_video.isOpened() :
    print (" Error : Could not open one or both videos .")
    exit ()

while True :
    ret_fg , frame_fg = foreground_video . read ()
    ret_bg , frame_bg = background_video . read ()

    # Check if both frames are read correctly
    if not ret_fg or not ret_bg :
        break
    
    # Convert the foreground image to HSV (Hue , Saturation , Value ) color space
    hsv = cv2 . cvtColor ( frame_fg , cv2 . COLOR_BGR2HSV )
    
    # Define the range of the green color in HSV
    lower_green = np.array([40 , 40, 40])
    upper_green = np.array([70 , 255, 255])
    
    # Create a mask to keep the non - green areas of the foreground
    mask = cv2 . inRange ( hsv , lower_green , upper_green )
    mask_inv = cv2 . bitwise_not ( mask )
    # Bitwise - AND mask and original image to extract the non - green parts of the foreground
    fg = cv2 . bitwise_and ( frame_fg , frame_fg , mask = mask_inv )
    # Resize background to match the size of the foreground
    frame_bg = cv2 . resize ( frame_bg , ( fg . shape [1] , fg . shape [0]) )
    # Bitwise - AND mask with the background image
    bg = cv2 . bitwise_and ( frame_bg , frame_bg , mask = mask )
    # Combine the foreground and background
    combined = cv2 . add (fg , bg )
    # Display the resulting frame
    cv2 . imshow ("Chroma Keying", combined )
    # Break the loop if ’q’ is pressed
    if cv2 . waitKey (1) & 0xFF == ord ("q") :
        break

# Release everything when done
foreground_video . release ()
background_video . release ()
cv2 . destroyAllWindows ()