# 为图像添加边框
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

BLUE = [255, 0, 0]
img = cv.imread("./img/1.jpeg")
img2 = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_CONSTANT, value=BLUE)
cv.imshow('zj', img2)
cv.waitKey(0)
