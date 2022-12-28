# 我们在第二章关于等高线的部分看到了什么是凸包。物体与这个船体的任何偏差都可以被认为是凸面缺陷。

import cv2 as cv
import numpy as np
img = cv.imread('./img/1.jpg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(img_gray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, 2, 1)
cnt = contours[1]
hull = cv.convexHull(cnt, returnPoints=False)
# 请记住，我们必须在寻找凸包时传递 returnPoints = False，才能找到凸性缺陷。
# 它返回一个数组，其中每一行都包含这些值 - [起点、终点、最远点、到最远点的近似距离]。
# 我们可以使用图像将其可视化。我们画一条连接起点和终点的线，然后在最远的点画一个圆。
# 请记住，返回的前三个值是 cnt 的索引。所以我们必须从 cnt 中获取这些值。
defects = cv.convexityDefects(cnt, hull)
for i in range(defects.shape[0]):
    s, e, f, d = defects[i, 0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv.line(img, start, end, [0, 255, 0], 2)
    cv.circle(img, far, 5, [0, 0, 255], -1)
cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()
