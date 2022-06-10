"""
Canny边缘检测的概念 - OpenCV函数: cv.Canny()
Canny算法
"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread(r'C:\Users\admin\Desktop\OpenCV\people.jpg', 0)
'''
Canny(image, threshold1, threshold2, edges=None, apertureSize=None, L2gradient=None):
.   @param image 8-bit input image.
.   @param edges output edge map; single channels 8-bit image, which has the same size as image.
.   @param threshold1 first threshold for the hysteresis procedure.(minVal)
.   @param threshold2 second threshold for the hysteresis procedure.(maxVal, >maxVal ---> 255)
.   @param apertureSize aperture size for the Sobel operator.
.   @param L2gradient a flag, indicating whether a more accurate \f$L_2\f$ norm\f$=\sqrt{(dI/dx)^2 + (dI/dy)^2}\f$
    should be used to calculate the image gradient magnitude (L2gradient=true ), 
    or whether the default \f$L_1\f$ norm \f$=|dI/dx|+|dI/dy|\f$ is enough (L2gradient=false ).
'''
edges = cv.Canny(img, 50, 60)
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
