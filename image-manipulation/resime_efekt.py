import cv2
import numpy as np

picture = cv2.imread("resim1.png")
picture[500:1500,400:1600,0] = 255 # belirtilen pikseller arasında seçilen 0,1,2 ye göre efekt uygulanır
picture[500:1500,400:1600,1] = 255
picture[500:1500,400:1600,2] = 255

cv2.imshow("objects", picture)


cv2.waitKey(0)
cv2.destroyAllWindows()
