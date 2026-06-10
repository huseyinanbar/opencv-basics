import cv2
import numpy as np

resim = cv2.imread("resim1.png")

cv2.rectangle(resim, (2400, 1500), (2500, 1300), [0, 0, 255], 2) #dikdörtgen oluşturur

cv2.imshow("resim1", resim)

cv2.waitKey(0)
cv2.destroyAllWindows()
