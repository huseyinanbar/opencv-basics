import cv2

image = cv2.imread("tren.png")

meanfilter = cv2.blur(image,(7,7)) # ksize olarak verilen değerlerden oluşturulan matrislerin ortalaması alınarak blur işlemi yapılır

cv2.imshow("Original", image)
cv2.imshow("blur", meanfilter)

cv2.waitKey(0)
cv2.destroyAllWindows()