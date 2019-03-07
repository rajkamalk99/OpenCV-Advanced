import cv2
import numpy as np
import random
import matplotlib.pyplot as plt

def main():
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
    denoised_image = cv2.medianBlur(new_img, 3)
    plt.subplot(1,3,1)
    plt.title("Original Image")
    plt.imshow(img)
    plt.xticks([])
    plt.yticks([])

    plt.subplot(1,3,2)
    plt.title("noised Image")
    plt.imshow(new_img)
    plt.xticks([])
    plt.yticks([])

    plt.subplot(1,3,3)
    plt.title("Denoised Image")
    plt.imshow(denoised_image)
    plt.xticks([])
    plt.yticks([])
    plt.show()


if __name__=="__main__":
    main()

