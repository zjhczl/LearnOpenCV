# 哈里斯角点检
# OpenCV 具有函数cv.cornerHarris()。它的参数是：
# img - 输入图像。应该是灰度和float32类型。
# blockSize - 这是用于角点检测的邻域大小
# ksize - 使用的 Sobel 导数的孔径参数。
# k - 方程中的 Harris 检测器自由参数。
import numpy as np
import cv2 as cv
filename = './img/1.jpeg'
img = cv.imread(filename)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv.cornerHarris(gray, 2, 3, 0.04)
# result is dilated for marking the corners, not important
dst = cv.dilate(dst, None)
# Threshold for an optimal value, it may vary depending on the image.
img[dst > 0.01*dst.max()] = [0, 0, 255]
cv.imshow('dst', img)
if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()
