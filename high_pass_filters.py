import cv2
import numpy as np
import matplotlib.pyplot as plt


def kernel():
    imgpath = "/home/raj/Documents/AI/OpenCV/standard_test_images/peppers_color.tif"
    img = cv2.imread(imgpath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    edges = cv2.Laplacian(img, -1, ksize=17, scale=1, delta=0, borderType=cv2.BORDER_DEFAULT)

    images = [img, edges]
    titles = ["Original Images", "Detected Edges"]

    for i in range(len(titles)):
        plt.subplot(1,2,i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    
    plt.show()
kernel()
