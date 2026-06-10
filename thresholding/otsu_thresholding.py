import cv2

image = cv2.imread("resim.png", 0)

ret1,thresh1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY) # simple threshold
ret2,thresh2 = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
                            # min ve max değerler girilerek eşik gerilim kendisi tarafından tamamlanır

cv2.imshow("original", image)
cv2.imshow("simple threshold", thresh1)
cv2.imshow("otsu threshold", thresh2)

cv2.waitKey(0)
cv2.destroyAllWindows()
