# SIFT
import numpy as np
import cv2 as cv
img = cv.imread('./img/1.jpeg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
sift = cv.SIFT_create()
kp = sift.detect(gray, None)
img = cv.drawKeypoints(gray, kp, img)
cv.imshow("zj", img)
cv.waitKey(0)
# 现在要计算描述符，OpenCV 提供了两种方法。
# 因为你已经找到了关键点，你可以调用sift.compute()来计算我们找到的关键点的描述符。例如：kp,des = sift.compute(gray,kp)
# 如果您没有找到关键点，请使用函数sift.detectAndCompute()一步直接找到关键点和描述符。
kp, des = sift.compute(gray, kp)  # kp 关键点，des 特征向量
# sift = cv.SIFT_create()
# kp, des = sift.detectAndCompute(gray,None)
print(np.array(kp).shape)
print(des.shape)
print(des[0])
