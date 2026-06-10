import cv2
import matplotlib.pyplot as plt

img = cv2.imread("resim1.png")

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5, 5), 0)

edges = cv2.Canny(blur, 100, 200)

plt.figure(figsize=(12, 6), dpi = 200)

plt.subplot(1, 3, 1)
plt.title("Orijinal")
plt.imshow(img_rgb)
plt.axis("off")

plt.subplot(1, 3, 2)
plt.title("Gri Tonlama")
plt.imshow(gray, cmap="gray")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.title("Kenar Algılama")
plt.imshow(edges, cmap="gray")
plt.axis("off")

plt.show()
