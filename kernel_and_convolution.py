import cv2
import numpy as np
import matplotlib.pyplot as plt


def kernel():
    imgpath = "/home/raj/Documents/AI/OpenCV/standard_test_images/peppers_color.tif"
    img = cv2.imread(imgpath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    k = np.array([[-1,-1,-1], [-1,8,-1], [-1,-1,-1]]) 

    filtered_image = cv2.filter2D(img, -1, k)

    plt.subplot(1,2,1)
    plt.title("Original image")
    plt.imshow(img)

    plt.subplot(1,2,2)
    plt.title("Filtered image")
    plt.imshow(filtered_image)

    plt.show()


kernel()



# refer this link for more filters = https://en.wikipedia.org/wiki/Kernel_(image_processing)

    