import cv2
import numpy as np

resim = cv2.imread("kurtresmi.png")

kesit = resim[500:1500,400:1600] # resim[] şeklinde belirtilen piksellerden kesit oluşturur
cv2.imshow("kesit", kesit)

cv2.waitKey(0)
cv2.destroyAllWindows()
