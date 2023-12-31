import cv2
# Load the pre - trained Haar Cascade model for face detection
face_cascade = cv2.CascadeClassifier (cv2.data.haarcascades + 'haarcascade_frontalface_default.xml ')
# Initialize video capture
cap = cv2.VideoCapture(0) # Use 0 for webcam . Replace with 'path_to_video . mp4 ' for a video file
while True :
    ret , frame = cap . read ()
    if not ret :
        break
    
    # Convert to grayscale for face detection
    gray = cv2.cvtColor( frame , cv2.COLOR_BGR2GRAY )
    # Detect faces
    faces = face_cascade.detectMultiScale (gray , 1.1 , 4)
    # Draw rectangles around the faces
    for (x , y , w , h) in faces :
        cv2 . rectangle ( frame , (x , y ) , (x+w , y+ h) , (255 , 0 , 0) , 2)
    # Display the output
    cv2.imshow('Face Tracking ', frame )
    if cv2.waitKey(1) & 0xFF == ord('q') :
        break

cap.release ()
cv2.destroyAllWindows ()
