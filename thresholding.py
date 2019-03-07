import cv2
import numpy as np
import matplotlib.pyplot as plt

imgpath = "/home/raj/Documents/AI/OpenCV/standard_test_images/grayscale.jpg"
img = cv2.imread(imgpath)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
th = 120
max_val = 255
ret, o1 = cv2.threshold(img, th, max_val, cv2.THRESH_BINARY)
ret, o2 = cv2.threshold(img, th, max_val, cv2.THRESH_BINARY_INV)
ret, o3 = cv2.threshold(img, th, max_val, cv2.THRESH_TOZERO)
ret, o4 = cv2.threshold(img, th, max_val, cv2.THRESH_TOZERO_INV)
ret, o5 = cv2.threshold(img, th, max_val, cv2.THRESH_TRUNC)

images = [img,o1,o2, o3,o4,o5]
titles = ["Original Image", "Binary", "Binary Inverted", "Zero", "Zero Inverted", "Truncated"]
for i in range(len(titles)):
    plt.subplot(2,3,i+1)
    plt.title(titles[i])
    plt.imshow(images[i])
    plt.xticks([])
    plt.yticks([])


plt.show()