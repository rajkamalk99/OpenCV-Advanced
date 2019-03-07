import cv2
import numpy as np
import matplotlib.pyplot as plt

imgpath = "/home/raj/Documents/AI/OpenCV/standard_test_images/cameraman.tif"
img = cv2.imread(imgpath, 0)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
th = 0
max_val = 255
ret, o1 = cv2.threshold(img, th, max_val, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
ret, o2 = cv2.threshold(img, th, max_val, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
ret, o3 = cv2.threshold(img, th, max_val, cv2.THRESH_TOZERO + cv2.THRESH_OTSU)
ret, o4 = cv2.threshold(img, th, max_val, cv2.THRESH_TOZERO_INV + cv2.THRESH_OTSU)
ret, o5 = cv2.threshold(img, th, max_val, cv2.THRESH_TRUNC + cv2.THRESH_OTSU)

images = [img,o1,o2,o3,o4,o5]
titles = ["Original Image", "Binary", "Binary Inverted", "Zero", "Zero Inverted", "Truncated"]
for i in range(len(titles)):
    plt.subplot(2,3,i+1)
    plt.title(titles[i])
    plt.imshow(images[i], cmap='gray')
    plt.xticks([])
    plt.yticks([])


plt.show()