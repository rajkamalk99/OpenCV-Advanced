import cv2
import matplotlib.pyplot as plt
import numpy as np

imgpath1 = "/home/raj/Documents/AI/OpenCV/standard_test_images/cameraman.tif"
img1 = cv2.imread(imgpath1)


img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

rows, columns, channels = img1.shape
R = cv2.getRotationMatrix2D((columns/2, rows/2), 45, 0.5)

output = cv2.warpAffine(img1, R, (columns, rows))

plt.plot()
plt.imshow(output)
plt.show()