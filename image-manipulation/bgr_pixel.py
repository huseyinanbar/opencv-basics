import cv2
import numpy as np

kurt_resmi = cv2.imread("resim1.png") # resmi okur
cv2.imshow("resim1", resim) # resmi görüntüler(show)

print(resim1[(222,180)]) # resmin belirtilen pikselindeki BGR değerlerini verir

cv2.waitKey(0)
cv2.destroyAllWindows()
