import cv2
import numpy as np

kurt_resmi = cv2.imread("kurtresmi.png") # resmi okur
cv2.imshow("kurtresmi", kurt_resmi) # resmi görüntüler(show)

print(kurt_resmi[(222,180)]) # resmin belirtilen pikselindeki BGR değerlerini verir

cv2.waitKey(0)
cv2.destroyAllWindows()