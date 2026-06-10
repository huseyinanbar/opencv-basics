import cv2

image = cv2.imread("resim1.png")

medianfilter = cv2.medianBlur(image,9) # belirlediğimiz matristeki hücrelerin medyanı alınır ve orta matrise yerleştirilir
medianfilter2 = cv2.medianBlur(image,1)

cv2.imshow("tren.png",image)
cv2.imshow("medianfilter",medianfilter)
cv2.imshow("medianfilter2",medianfilter)

cv2.waitKey(0)
cv2.destroyAllWindows()
