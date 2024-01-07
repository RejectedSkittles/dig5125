import cv2

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('dig5125-main/Videos/output2.mp4', fourcc , 20.0 , (640 , 480))

#open the camera
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret , frame = cap.read()
    if ret:
#write the frame into the file 'output.avi'
        out.write(frame)

#display resulting frame
        cv2.imshow("frame", frame)

#Press q to stop recording
        if cv2.waitKey(1) & 0xFF == ord("q") :
            break
    else:
        break

    #Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()