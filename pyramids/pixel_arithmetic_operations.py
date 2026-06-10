import cv2 as cv
import numpy as np

path = "path"
path1 = "path"

src1 = cv.imread(path)
src2 = cv.imread(path1)

h, w, ch = src1.shape
h1, w1, ch1 = src2.shape

print(h, w, ch)
print(h1, w1, ch1)

src2 = cv.resize(src2, dsize=(w, h))

# operations

add_result = np.zeros(src1.shape, src1.dtype)
cv.add(src1, src2, add_result)
cv.imshow("add_result", add_result)

sub_result = np.zeros(src1.shape, src1.dtype)
cv.subtract(src1, src2, sub_result)
cv.imshow("sub_result", sub_result)

mul_result = np.zeros(src1.shape, src1.dtype)
cv.multiply(src1, src2, mul_result)
cv.imshow("mul_result", mul_result)

div_result = np.zeros(src1.shape, src1.dtype)
cv.divide(src1, src2, div_result)
cv.imshow("div_result", div_result)

cv.waitKey(0)

