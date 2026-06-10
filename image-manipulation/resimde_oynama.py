import cv2
import numpy as np

resim = cv2.imread("resim1.png")

ayna = cv2.copyMakeBorder(resim,1000,1000,1000,1000,cv2.BORDER_REFLECT)
uzatma = cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_REPLICATE)
tekrar = cv2.copyMakeBorder(resim,1000,1000,1000,1000,cv2.BORDER_WRAP)
sarma = cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_CONSTANT,value=(0,0,255))

cv2.imshow("ayna", ayna)
cv2.imshow("uzatma", uzatma)
cv2.imshow("tekrar", tekrar)
cv2.imshow("sarma", sarma)

cv2.waitKey(0)
cv2.destroyAllWindows()