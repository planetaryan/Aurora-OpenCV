import cv2
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    
    cv2.imshow("live video",frame)
    if(cv2.waitKey(1)==ord('c')):
        cv2.imwrite(r"C:\Users\plane\OneDrive\Desktop\python\capture.jpg",frame)
        

    key=cv2.waitKey(1)
    if (key==ord("q")):
        
        
        
        cap.release()
        cv2.destroyAllWindows()
