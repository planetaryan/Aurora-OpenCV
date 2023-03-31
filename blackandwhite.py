import cv2
image=cv2.imread("image.png")
cv2.imshow("frame",image)
cv2.waitKey()
cv2.destroyAllWindows()

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("frame",gray)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imwrite("grayimage.png",gray)
