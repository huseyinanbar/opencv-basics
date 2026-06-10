import cv2
import numpy as np

resim = cv2.imread("resim1.png",0)

iki_kat_buyuk = cv2.pyrUp(resim)
iki_kat_kucuk = cv2.pyrDown(resim)

cv2.imshow("resim", resim)
cv2.imshow("iki kat buyuk", iki_kat_buyuk)
cv2.imshow("iki kat kucuk", iki_kat_kucuk)

cv2.waitKey(0)
cv2.destroyAllWindows()

