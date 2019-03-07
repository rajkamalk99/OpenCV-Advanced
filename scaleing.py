import cv2
import matplotlib.pyplot as plt

imgpath1 = "/home/raj/Documents/AI/OpenCV/standard_test_images/cameraman.tif"
img1 = cv2.imread(imgpath1)


img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

output = cv2.resize(img1, None, fx=2.5, fy=1, interpolation=cv2.INTER_CUBIC)

plt.subplot(1, 2, 1)
plt.title("original")
plt.imshow(img1)
plt.xticks([])
plt.yticks([])

plt.subplot(1, 2, 2)
plt.title("resized")
plt.imshow(output)
plt.xticks([])
plt.yticks([])

plt.show()