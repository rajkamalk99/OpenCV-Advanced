import cv2
import matplotlib.pyplot as plt
import numpy as np

imgpath1 = "/home/raj/Documents/AI/OpenCV/standard_test_images/cameraman.tif"
img1 = cv2.imread(imgpath1)


img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

T = np.float32([[1,0,50],[0,1,-50]])
rows, columns, channels = img1.shape

output = cv2.warpAffine(img1, T, (columns, rows))

plt.plot()
plt.imshow(output)
plt.show()