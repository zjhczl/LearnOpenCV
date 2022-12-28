# 几种滤波
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('./img/1.jpeg')
# 平均值滤波
blur = cv.blur(img, (5, 5))
# 高斯滤波
blur2 = cv.GaussianBlur(img, (5, 5), 0)
# 中值模糊
blur3 = cv.medianBlur(img, 5)
# 双边过滤
blur4 = cv.bilateralFilter(img, 9, 75, 75)
cv.imshow("s", blur4)
cv.waitKey(0)
