import cv2
import numpy

image = cv2.imread("resim1.png")
image1 = cv2.imread("resim.png")

bit_And = cv2.bitwise_and(image, image1)
bit_Or = cv2.bitwise_or(image, image1)
bit_Xor = cv2.bitwise_xor(image, image1)
bit_Not = cv2.bitwise_not(image, image1)

cv2.imshow("original", image)
cv2.imshow("bitwise_and", bit_And)
cv2.imshow("bitwise_or", bit_Or)
cv2.imshow("xor", bit_Xor)
cv2.imshow("not", bit_Not)

cv2.waitKey(0)
cv2.destroyAllWindows()