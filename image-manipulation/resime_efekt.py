import cv2
import numpy as np

kitap = cv2.imread("kurtresmi.png")
kitap[500:1500,400:1600,0] = 255 # belirtilen pikseller arasında seçilen 0,1,2 ye göre efekt uygulanır
kitap[500:1500,400:1600,1] = 255
kitap[500:1500,400:1600,2] = 255

cv2.imshow("kitaplar", kitap)


cv2.waitKey(0)
cv2.destroyAllWindows()