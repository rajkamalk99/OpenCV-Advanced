import cv2
import numpy as np
import matplotlib.pyplot as plt


def kernel():
    imgpath = "/home/raj/Documents/AI/OpenCV/standard_test_images/peppers_color.tif"
    img = cv2.imread(imgpath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    box = cv2.boxFilter(img, -1, (53,53))
    blur = cv2.blur(img, (13,13))
    guassian_blur = cv2.GaussianBlur(img, (17,17), 0) 

    images = [img, box, blur, guassian_blur]
    titles = ["Original Images", "Box Blur", "Blur", "Guassian Blur"]

    for i in range(len(titles)):
        plt.subplot(2,2,i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    
    plt.show()
kernel()



# refer this link for more filters = https://en.wikipedia.org/wiki/Kernel_(image_processing)

    