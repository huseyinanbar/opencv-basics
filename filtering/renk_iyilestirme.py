import cv2 as cv

path = "path"

src = cv.imread(path)

cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)


# applyColorMap

#COLORMAP_AUTUMN
#COLORMAP_BONE
#COLORMAP_WINTER
#COLORMAP_OCEAN
#COLORMAP_SUMMER
#COLORMAP_PINK
#COLORMAP_COOL
#COLORMAP_JET

dst = cv.applyColorMap(src, cv.COLORMAP_OCEAN)
cv.imshow("output", dst)

cv.waitKey(0)