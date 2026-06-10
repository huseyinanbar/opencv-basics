import cv2
import numpy as np

resim1 = cv2.imread("resim1.png")
resim2 = cv2.imread("resim2.png")

cv2.imshow("resim1", resim1)
cv2.imshow("resim2", resim2)

toplam = cv2.add(resim1, resim2)
agirlikli_toplam = cv2.addWeighted(resim1, 0.8, resim2, 0.2, 0)
cv2.imshow("agirlikli", agirlikli_toplam)

cv2.imshow("toplam", toplam)

cv2.waitKey(0)
cv2.destroyAllWindows()