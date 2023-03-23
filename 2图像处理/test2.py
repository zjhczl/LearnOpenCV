# 图像的平移与旋转
# 图像缩放
import numpy as np
import cv2 as cv

img = cv.imread('./img/1.jpeg', 0)
print(img.shape)

rows, cols = img.shape
# 平移矩阵
M = np.float32([[1, 0, 100], [0, 1, 50]])

# 旋转矩阵
M2 = cv.getRotationMatrix2D(((cols - 1) / 2.0, (rows - 1) / 2.0), 90, 1)
# 仿射变换矩阵
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
M3 = cv.getAffineTransform(pts1, pts2)

# 进行变换
dst = cv.warpAffine(img, M3, (cols, rows))

cv.imshow('img', dst)
cv.waitKey(0)
cv.destroyAllWindows()
