import cv2 as cv

path = "test"

img = cv.imread(path)
cv.namedWindow("output", cv.WINDOW_NORMAL)

img = cv.resize(img,540,360)

# cvtColor

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("output", gray)

# imwrite

cv.imwrite("gray_output.png", gray)

cv.waitKey(0)
cv.destroyAllWindows()