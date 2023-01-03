# 腐蚀与膨胀
import cv2 as cv
import numpy as np
img = cv.imread('./img/1.jpeg', 0)
kernel = np.ones((5, 5), np.uint8)
# 腐蚀
res1 = cv.erode(img, kernel, iterations=1)
# 膨胀
res2 = cv.dilate(img, kernel, iterations=1)
# 先腐蚀后膨胀
res3 = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
# 先膨胀后腐蚀。
res4 = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
# 形态梯度
res5 = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
cv.imshow("zj", res5)
cv.waitKey(0)
