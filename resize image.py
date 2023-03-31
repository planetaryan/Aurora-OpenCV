import cv2

import matplotlib.pyplot as plt

image=cv2.imread("ab.jpg")

plt.title('original image')
plt.imshow(image)
plt.show()
resize=cv2.resize(image,(400,400))

plt.imshow(resize)
plt.show()
