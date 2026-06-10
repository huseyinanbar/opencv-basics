import cv2 as cv

frameWidth = 640
frameHeight = 360

cap = cv.VideoCapture(0)

while True:
    success, img = cap.read()
    img = cv.resize(img, (frameWidth, frameHeight))
    cv.imshow("video", img)

    if cv.waitKey(10) & 0xFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()