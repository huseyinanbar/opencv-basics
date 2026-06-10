import cv2 as cv
import numpy as np

path = "path"
path1 = "path"

img = cv.imread(path)
cv.imshow("img", img)


m1 = np.copy(img)
m2 = img

print(type(img))

img[100:200, 200:300, :] = [100, 150, 180]

cv.imshow("m2", m2)

cv.waitKey(0)