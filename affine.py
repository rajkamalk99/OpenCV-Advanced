import cv2
import matplotlib.pyplot as plt
import numpy as np

imgpath1 = "/home/raj/Documents/AI/OpenCV/standard_test_images/cameraman.tif"
img1 = cv2.imread(imgpath1)


img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

rows, columns, channels = img1.shape
point1 = np.float32([[100,100], [300,100],[100,300]])
point2 = np.float32([[200,150], [400,150],[200,400]])
R = cv2.getAffineTransform(point1, point2)

output = cv2.warpAffine(img1, R, (columns, rows))

plt.plot()
plt.imshow(output)
plt.show()


# Affine transformation is a linear mapping method that preserves points, straight lines, and planes. 
# Sets of parallel lines remain parallel after an affine transformation. 
# The affine transformation technique is typically used to correct for geometric distortions or deformations that occur with non-ideal camera angles.