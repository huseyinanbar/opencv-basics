import cv2 as cv

path = "path"

img = cv.imread(path)

print(type(img))                # veri okuma

# nameWindow

cv.namedWindow("test", cv.WINDOW_AUTOSIZE)
cv.imshow("test", img)

cv.waitKey(0)
cv.destroyAllWindows()