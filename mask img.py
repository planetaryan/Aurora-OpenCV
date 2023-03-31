import cv2
import numpy as np

lg=np.array([5,50,50])
hg=np.array([15,255,255])
cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    
    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    mask=cv2.inRange(hsv,lg,hg)
    cv2.imshow("masked frame",mask)
    contours,hierarchy=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame,contours,-1,(0,0,255),2)
    cv2.imshow("frame",frame)

    for c in contours:
        area=cv2.contourArea(c)
        if area>400:
            x,y,w,h=cv2.boundingRect(c)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.drawContours(frame,c,-1,(255,0,155),2)
        print(area)
        cv2.imshow("frame",frame)
    key=cv2.waitKey(1)
    if key==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
