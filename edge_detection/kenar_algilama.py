import cv2
import numpy

image = cv2.imread("kurtresmi.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0) # blurlama işlemini arttırarak algılanan kenarlar azaltılabilir

def auto_canny(blur, sigma = 0.33): # fonksiyon oluşturma
    median = numpy.median(blur) # piksel yoğunluklarının medianı hesaplanır
    lower = int(max(0,(1.0 - sigma)*median)) # alt eşik değeri
    upper = int(min(255, (1.0 + sigma) * median))  # alt eşik değeri
    canny = cv2.Canny(blur, 250, 50)  # kenar algılama

    return canny

wide = cv2.Canny(blur, 10, 220) # eşik değerleri geniş alınır
tight = cv2.Canny(blur, 200, 230) # eşik değerleri dar alınır
auto = auto_canny(blur) # eşik değerleri sigma değerine bağlı olarak alınır

cv2.imshow("blurred image", blur)
cv2.imshow("edge", numpy.hstack([wide, tight, auto])) # aynı karere birden fazla resim görüntüleme

cv2.waitKey(0)
cv2.destroyAllWindows()