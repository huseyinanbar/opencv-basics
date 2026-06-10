import cv2
import numpy as np

from morphological_operations import erosion

image = cv2.imread("resim1.png")

kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(image, kernel, iterations = 1) # aşınma işlemi yapılıyor
dilation = cv2.dilate(erosion, kernel, iterations = 1) # genişletme yapıyor, ancak gürültüler de genişletiliyor

cv2.imshow("original", image)
cv2.imshow("dilate", dilation)
cv2.imshow("erosion", erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()
