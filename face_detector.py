import cv2

#load some pre-trained data on face frontals from opencv 
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#choose an image to detect faces
#img = cv2.imread('people.jpg')
#changing the video capture to show either webcam or videos
webcam = cv2.VideoCapture(0)

#Loop forever
while True:
    successful_frame_read, frame = webcam.read()


    #Must Convert to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
    
    #Detect Faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
   
    #print(face_coordinates)
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3 )
   
    cv2.imshow('Avila Programmer Face Detector', frame)
    key = cv2.waitKey(1)

    #stop using the letter  Q
    if key == 81 or key == 113:
        break

webcam.release()

print ("code complete")