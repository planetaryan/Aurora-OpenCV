import cv2
import numpy
print("imported")
#img=cv2.imread('ab.jpg')
#cv2.imshow('frame',img)
cv2.waitKey(0)
c=cv2.VideoCapture(0)
while True:
    ret,frame=c.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    
    #blur=cv2.GaussianBlur(gray,(7,7),8)
    #cv2.imshow('frame',blur)

    if cv2.waitKey(60)==ord('q'):
        break
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",648,240)
while True:
    h_min=cv2.TrackbarPos("Hue Min","Trackbars")
    h_max=cv2.TrackbarPos("Hue Max","Trackbars")
    s_min=cv2.TrackbarPos("Sat Min","Trackbars")
    s_max=cv2.TrackbarPos("Sat Min","Trackbars")
    v_min=cv2.TrackbarPos("Hue Min","Trackbars")
    v_max=cv2.TrackbarPos("Hue Min","Trackbars")
    

