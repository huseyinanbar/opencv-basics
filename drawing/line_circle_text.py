import cv2
import numpy as np

resim = np.zeros((300, 300,3),dtype = "uint8")

cv2.line(resim, (100,100),(240,280),(255,0,0),5)
cv2.circle(resim,(100,100),25,(0,200,200),1)
cv2.putText(resim,"HUSEYIN ANBAR", (50,50),cv2.FONT_HERSHEY_PLAIN,1,(255,255,255),2)
cv2.imshow("resim", resim)

cv2.waitKey(0)
cv2.destroyAllWindows()