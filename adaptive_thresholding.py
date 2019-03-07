import cv2
import numpy as np
import matplotlib.pyplot as plt

imgpath = "/home/raj/Documents/AI/OpenCV/standard_test_images/cameraman.tif"
img = cv2.imread(imgpath, 0)

block_size = 11
constant = 2

th1 = cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, constant)
th2 = cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, constant)

images = [th1, th2]
titles = ["Mean adaptive", "Gaussian adaptive"]
for i in range(len(titles)):
    plt.subplot(1,2,i+1)
    plt.title(titles[i])
    plt.imshow(images[i], cmap='gray')
    plt.xticks([])
    plt.yticks([])


plt.show()