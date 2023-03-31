import cv2
import time

# scaleFactor – This tells how much the object’s size is reduced to the original image.
# minNeighbors – This parameter tells how many neighbors should contribute in a single bounding box.
# minSize — This signifies the minimum possible size of the object in our image. if our object is smaller than the minSize it will be ignored.



class selfie:

    def __init__(self):

        self.cap=cv2.VideoCapture(0)
        self.time_started = False
        self.count=1
        self.detect_face()
        

    def take_snapshot(self,frame):
        
        self.time_started=True
        print("Press s to save the image")
        ch =  cv2.waitKey(3000)  #3000ms
        if ch==ord('s'):
            cv2.imwrite(str(self.count)+'.jpg',frame)
            self.count=self.count+1
            print("saved")


    def detect_face(self):

        while True:

            ret,frame=self.cap.read()

            if frame is None:
                print("No frame detected! ")

            else:
                gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
                faces_rect = haar_cascade.detectMultiScale(gray_img, scaleFactor=1.05,minNeighbors=9, minSize=(30, 30),flags=cv2.CASCADE_SCALE_IMAGE)
                for (x, y, w, h) in faces_rect:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
                
                if len(faces_rect)>0 and self.time_started == False:
                    prev_time=int(time.time())
                    self.take_snapshot(frame)
                
                curr_time=int(time.time())

                if self.time_started:
                    if(curr_time-prev_time>10):
                        self.time_started=False
                        cv2.destroyAllWindows()
                        prev_time=time.time()
                    
            cv2.imshow("",frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.cap.release()
        cv2.destroyAllWindows()

if __name__=='__main__':
    selfie()
