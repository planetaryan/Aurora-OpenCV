import cv2

cap=cv2.VideoCapture(r"http://192.168.13.23:8080/video")
while(True):
    ret,frame=cap.read()
    fps=int(cap.get(cv2.CAP_PROP_FPS))
    
    resized=cv2.resize(frame,(600,400))
    cv2.putText(resized,str(fps),(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    cv2.imshow("frame",resized)

    key=cv2.waitKey(1)
    if key==ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
