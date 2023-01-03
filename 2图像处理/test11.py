# 轮廓的特征
import numpy as np
import cv2 as cv
img = cv.imread('./img/1.jpg', 0)
ret, thresh = cv.threshold(img, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, 1, 2)
cnt = contours[1]
# print(cnt)
#  Moments可以帮助您计算一些特征，例如物体的质心、物体的面积等。
M = cv.moments(cnt)
print(M)
# 计算轮廓面积
area = cv.contourArea(cnt)
print(area)
# 轮廓周长
perimeter = cv.arcLength(cnt, True)
print(perimeter)
# 轮廓近似
# 根据我们指定的精度，它将轮廓形状近似为具有较少顶点数的另一个形状。它是Douglas-Peucker 算法的一个实现。检查维基百科页面的算法和演示。
# 要理解这一点，假设您试图在图像中找到一个正方形，但由于图像中的一些问题，您没有得到一个完美的正方形，而是一个“坏形状”（如下图第一张所示）。
# 现在您可以使用此函数来近似形状。其中，第二个参数称为 epsilon，它是从轮廓到近似轮廓的最大距离。它是一个精度参数。
# 需要明智地选择 epsilon 以获得正确的输出。
epsilon = 0.1 * cv.arcLength(cnt, True)
approx = cv.approxPolyDP(cnt, epsilon, True)
# 凸包
hull = cv.convexHull(cnt)
cv.drawContours(img, hull, -1, (0, 255, 0), 3)

# 边界矩形
# 直线边界矩形
x, y, w, h = cv.boundingRect(cnt)
cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
# 旋转矩形
rect = cv.minAreaRect(cnt)
box = cv.boxPoints(rect)
box = np.int0(box)
cv.drawContours(img, [box], 0, (0, 0, 255), 2)
# 最小外接圆
(x, y), radius = cv.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
cv.circle(img, center, radius, (0, 255, 0), 2)


print(approx)
cv.imshow("zj2", img)
cv.waitKey(0)
