import cv2
import numpy as np
import random
import matplotlib.pyplot as plt

# Salt and Pepper Noise Implementation


def Noise():
    imgpath = "/home/raj/Documents/AI/OpenCV/standard_test_images/lena_color_256.tif"
    img = cv2.imread(imgpath)
    rows, columns, channels = img.shape

    new_img = np.zeros(img.shape, np.uint8)

    p = 0.05

    for i in range(rows):
        for j in range(columns):
            r = random.random()
            if r < p/2:
                # pepper sprinkeled
                new_img[i][j] = [0,0,0]
            elif r < p:
                # salt sprinkeled
                new_img[i][j] = [255,255,255]
            else:
                new_img[i][j] = img[i][j]
    dnoised_image = cv2.medianBlur()
    
    cv2.imshow("Noised Image", new_img)
    cv2.waitKey(0) 
    cv2.destroyAllWindows()


Noise()

