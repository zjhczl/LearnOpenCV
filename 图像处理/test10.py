# 寻找并绘制轮廓
import numpy as np
import cv2 as cv
img = cv.imread('./img/1.jpg')
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
# cv.findContours()函数中有三个参数，第一个是源图像，第二个是轮廓检索模式，第三个是轮廓近似方法。它输出轮廓和层次结构。
# Contours 是图像中所有轮廓的 Python 列表。每个单独的轮廓都是对象边界点的 (x,y) 坐标的 Numpy 数组。
contours, hierarchy = cv.findContours(
    thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
# print(contours)
# 要绘制轮廓，使用cv.drawContours函数。如果您有边界点，它也可以用来绘制任何形状。它的第一个参数是源图像，
# 第二个参数是应该作为 Python 列表传递的轮廓，第三个参数是轮廓的索引（在绘制单个轮廓时很有用。要绘制所有轮廓，传递 -1），其余参数是颜色、厚度等等
# cv.drawContours(img, contours, -1, (255, 0, 0), 3)
cnt = contours[0]
cv.drawContours(img, [cnt], -1, (0, 255, 0), 3)
cv.imshow("zj2", img)
cv.waitKey(0)
# 这是cv.findContours函数中的第三个参数。它实际上表示什么？

# 上面，我们告诉轮廓是具有相同强度的形状的边界。它存储形状边界的 (x,y) 坐标。但它存储所有坐标吗？这是由这种轮廓近似方法指定的。

# 如果你传递cv.CHAIN_APPROX_NONE，所有的边界点都会被存储。但实际上我们需要所有的点吗？例如，您找到了一条直线的轮廓。你需要线上的所有点来代表那条线吗？不，我们只需要那条线的两个端点。这就是cv.CHAIN_APPROX_SIMPLE所做的。它删除所有冗余点并压缩轮廓，从而节省内存。

# 下面的矩形图像展示了这种技术。只需在轮廓数组中的所有坐标上绘制一个圆圈（以蓝色绘制）。第一张图显示了我用cv.CHAIN_APPROX_NONE得到的点（734 点），第二张图显示了用cv.CHAIN_APPROX_SIMPLE得到的点（只有 4 点）。看，它节省了多少内存！！！
