import cv2
import matplotlib.pyplot as plt
import numpy as np

imgpath1 = "/home/raj/Documents/AI/OpenCV/standard_test_images/cameraman.tif"
img1 = cv2.imread(imgpath1)


img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

rows, columns, channels = img1.shape
point1 = np.float32([[0,0], [400,0],[0,400], [400,400]])
point2 = np.float32([[0,0], [300,0],[0,300], [300, 300]])
R = cv2.getPerspectiveTransform(point1, point2)

output = cv2.warpPerspective(img1, R, (columns, rows))

plt.plot()
plt.imshow(output)
plt.show()



# When human eyes see near things they look bigger as compare to those who are far away.
#  This is called perspective in a general way.
#  Whereas transformation is the transfer of an object e.t.c from one state to another.

# So overall, the perspective transformation deals with the conversion of 3d world into 2d image. 
# The same principle on which human vision works and the same principle on which the camera works.

