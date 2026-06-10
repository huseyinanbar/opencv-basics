import cv2
import numpy as np

resim = cv2.imread("kurtresmi.png")

resim[50,30] = [255,255,255] # resmin belirtilen pikseline karşısındaki [] renk değerini uygular

for i in range(1800): # dikeyde belirtilen 'range()' piksele kadar döngü döndürür
    for j in range(2880): # yatayda belirtilen 'range()' piksele kadar döngü döndürür
        resim[i,j] = [100,0,150]

cv2.imshow("kurtresmi", resim)

cv2.waitKey(0)
cv2.destroyAllWindows()