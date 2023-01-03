# 透视变换
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

img = cv.imread('img/1.jpeg')
rows, cols, ch = img.shape
# 透视变换矩阵
pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
M4 = cv.getPerspectiveTransform(pts1, pts2)
dst = cv.warpPerspective(img, M4, (2000, 1000))

plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()
