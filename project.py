import cv2
import numpy as np

face_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_classifier=cv2.CascadeClassifier('haarcascade_eye.xml')
cap=cv2.VideoCapture(0)
fps=0
while True:
    ret,frame=cap.read()
    if fps>=10:
        cv2.imshow("frame",frame)
        fps=0
        fps=fps+1
    
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=face_classifier.detectMultiScale(gray,1.2,7)

    """if faces is():
        
        print("face not found")"""
    for(x,y,w,h) in faces:
        gray_image=gray[y:y+h, x:x+w]
        color_image=frame[y:y+h, x:x+w]

        eyes=eye_classifier.detectMultiScale(gray_image)
        for(ex,ey,ew,eh) in eyes:
        
    
            cv2.rectangle(color_image,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            cv2.imshow("detected eyes",frame)
    
            cv2.waitKey(1)


cv2.destroyAllWindows()
