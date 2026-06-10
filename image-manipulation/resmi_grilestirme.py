import cv2
import numpy as np

resim = cv2.imread("kurtresmi.png")
gri_resim = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)

yukseklik, genislik, kanal_sayisi = resim.shape
yukseklik1, genislik1 = gri_resim.shape

print("orijinal:" ,yukseklik, genislik, kanal_sayisi)
print("gri_resim: ", yukseklik1, genislik1)

cv2.imshow("orijinal", resim)
cv2.imshow("gri", gri_resim)

cv2.waitKey(0)
cv2.destroyAllWindows()