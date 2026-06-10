import cv2

image = cv2.imread("tren.png")

gauss_filter = cv2.GaussianBlur(image, (5,5),0)
cv2.imshow("original", image)
cv2.imshow("gauss filter", gauss_filter)

cv2.waitKey(0)
cv2.destroyAllWindows()