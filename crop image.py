import cv2

import matplotlib.pyplot as plt

image=cv2.imread("ab.jpg")

plt.title('original image')
plt.imshow(image)
plt.show()
cropped=image[25:175,20:120]

plt.title('croppeed image')
plt.imshow(cropped)
plt.show()
