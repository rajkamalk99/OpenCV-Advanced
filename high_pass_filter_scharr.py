import cv2
import numpy as np
import matplotlib.pyplot as plt


def kernel():
    imgpath = "/home/raj/Documents/AI/OpenCV/standard_test_images/peppers_color.tif"
    img = cv2.imread(imgpath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    edges_x = cv2.Scharr(img, -1, dx=1, dy=0, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)
    edges_y = cv2.Scharr(img, -1, dx=0, dy=1, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)

    edges = edges_x + edges_y

    images = [img, edges_x, edges_y, edges]
    titles = ["Original Images", "Detected x-Edges", "Detected y-Edges", "Detected Edges"]

    for i in range(len(titles)):
        plt.subplot(2,2,i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    
    plt.show()
kernel()
