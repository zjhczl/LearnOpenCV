# 具有亚像素精度的角
# 有时，您可能需要以最高精度找到角点。OpenCV 带有一个函数cv.cornerSubPix()，
# 它进一步细化了以亚像素精度检测到的角点。下面是一个例子。和往常一样，
# 我们需要先找到哈里斯角。然后我们通过这些角的质心（一个角可能有
# 一堆像素，我们取它们的质心）来细化它们。Harris 角以红色像素标记，
# 细化角以绿色像素标记。对于这个函数，我们必须定义停止迭代的条件。
# 我们在指定的迭代次数或达到一定的精度后停止它，
# 以先发生者为准。我们还需要定义它搜索角点的邻域大小。
import numpy as np
import cv2 as cv
filename = '1.png'
img = cv.imread(filename)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# find Harris corners
gray = np.float32(gray)
dst = cv.cornerHarris(gray, 2, 3, 0.04)
dst = cv.dilate(dst, None)
ret, dst = cv.threshold(dst, 0.01*dst.max(), 255, 0)
dst = np.uint8(dst)
# find centroids
ret, labels, stats, centroids = cv.connectedComponentsWithStats(dst)
# define the criteria to stop and refine the corners
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv.cornerSubPix(gray, np.float32(
    centroids), (5, 5), (-1, -1), criteria)
# Now draw them
res = np.hstack((centroids, corners))
res = np.int0(res)
img[res[:, 1], res[:, 0]] = [0, 0, 255]
img[res[:, 3], res[:, 2]] = [0, 255, 0]
cv.imwrite('subpixel5.png', img)
