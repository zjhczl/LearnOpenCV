# 霍夫直线变换
import cv2 as cv
import numpy as np

img = cv.imread('1.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 50, 150, apertureSize=3)
cv.imshow("huofu", edges)
cv.waitKey(0)
# 霍夫变换参数说明：1.输出二值图像 2.ρ的精度 3.θ精度 4.阈值（线的长度）
# 返回符合要求ρ，θ的列表
# lines = cv.HoughLines(edges, 1, np.pi / 180, 200)
# for line in lines:
#     rho, theta = line[0]
#     a = np.cos(theta)
#     b = np.sin(theta)
#     x0 = a * rho
#     y0 = b * rho
#     x1 = int(x0 + 1000 * (-b))
#     y1 = int(y0 + 1000 * (a))
#     x2 = int(x0 - 1000 * (-b))
#     y2 = int(y0 - 1000 * (a))
#     cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
# cv.imshow("huofu", img)
# cv.waitKey(0)

# 改进版的霍夫变换
# minLineLength：线的最小长度 maxLineGap线与线之间的距离
lines = cv.HoughLinesP(edges,
                       1,
                       np.pi / 180,
                       100,
                       minLineLength=100,
                       maxLineGap=10)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
cv.imshow('huofu', img)
cv.waitKey(0)