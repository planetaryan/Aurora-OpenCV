import cv2
from datetime import datetime
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    now=datetime.now()
    curtime=now.strftime("%d/%m/%y,%H:%M:%S")
    cv2.putText(frame,curtime,(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    if ret==True:
        
        cv2.imshow("frame",frame)

    key=cv2.waitKey(1)
    if key==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
