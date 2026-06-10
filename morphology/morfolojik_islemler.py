import cv2
import numpy as np

image = cv2.imread("yazı.png")
kernel = np.ones((5,5),np.uint8)

erosion = cv2.erode(image, kernel, iterations = 1) # gürültüleri azaltmak için önce aşınma işlemi yapılıyor
dilation = cv2.dilate(erosion, kernel, iterations = 1) # daha sonra 'erosion' kaynak alınarak genişletme yapılıyor

opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel) # önce erosion daha sonra dilation işlemi yapılıyor
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel) # önce dilation daha sonra erosion işlemi yapılır
gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel) # dilation resminden erosion resminden çıkartılmış görüntüsü
tophet = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel) # orijinal resimden opening resminin çıkartılmış görüntüsü
blackhat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel) # orijinal resimden closing resminin çıkartılmış görüntüsü

cv2.imshow("original", image)
cv2.imshow("erosion", erosion)
cv2.imshow("dilate", dilation)

cv2.imshow("opening", opening)
cv2.imshow("closing", closing)
cv2.imshow("gradient", gradient)
cv2.imshow("tophet", tophet)
cv2.imshow("blackhat", blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()