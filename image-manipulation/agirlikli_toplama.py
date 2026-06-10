import cv2
import numpy as np

resim1 = cv2.imread("resim1.png")
resim2 = cv2.imread("resim2.png")

print(resim1[200,100]) # belirtiler pikselin BGR değeri
print(resim2[200,400]) # belirtiler pikselin BGR değeri

cv2.imshow("a", resim1)
cv2.imshow("b", resim2)

print(resim1[200,100] + resim2[200,400]) # iki resimden belirtilen piksellerin BGR değerlerini toplar
#(Bizim değerimiz 0 dan başlayıp 255 e gittiğinden (toplam-255-1 yaparız)(toplam ≤ 255))

cv2.waitKey(0)
cv2.destroyAllWindows()