import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

while True:
    ret,goruntu = kamera.read()
    cv2.rectangle(goruntu, (100,100), (200,200), (0,0,255),2)

    cv2.imshow("goruntu", goruntu)

    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

kamera.release()

cv2.destroyAllWindows()
