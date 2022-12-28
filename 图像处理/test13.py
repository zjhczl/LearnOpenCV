# 直方图
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
# 所以现在我们使用cv.calcHist()函数来查找直方图。让我们熟悉一下函数及其参数：
# cv.calcHist（图像，通道，掩码，histSize，范围[，hist [，累积]]）
# images : uint8 或 float32 类型的源图像。它应该在方括号中给出，即“[img]”。
# channels ：它也在方括号中给出。它是我们计算直方图的通道索引。例如，如果输入是灰度图像，则其值为[0]。对于彩色图像，可以传入[0]、[1]或[2]分别计算蓝色、绿色或红色通道的直方图。
# 掩码：掩码图像。要找到完整图像的直方图，它被指定为“无”。但是如果你想找到图像特定区域的直方图，你必须为此创建一个蒙版图像并将其作为蒙版。（我稍后会展示一个例子。）
# histSize ：这代表我们的 BIN 计数。需要在方括号中给出。对于全尺寸，我们通过 [256]。
# 范围：这是我们的范围。通常，它是 [0,256]。
img = cv.imread('img/1.jpeg', 0)
hist = cv.calcHist([img], [0], None, [256], [0, 256])
# Numpy also provides you a function, np.histogram(). So instead of calcHist() function, you can try below line :
hist, bins = np.histogram(img.ravel(), 256, [0, 256])

# # plt直接绘制直方图
# plt.hist(img.ravel(), 256, [0, 256])
# plt.show()

img = cv.imread('img/1.jpeg')
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()