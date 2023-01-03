# 使用 SIFT 描述符和比率测试进行暴力匹配
# 这一次，我们将使用 BFMatcher.knnMatch() 来获得 k 个最佳匹配。在此示例中，
# 我们将取 k=2，以便我们可以应用 D.Lowe 在他的论文中解释的比率检验。
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
img1 = cv.imread('./img/test1.JPG', cv.IMREAD_GRAYSCALE)          # queryImage
img2 = cv.imread('./img/test2.JPG', cv.IMREAD_GRAYSCALE)  # trainImage
# Initiate SIFT detector
sift = cv.SIFT_create()
# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)
# BFMatcher with default params
bf = cv.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)
# Apply ratio test
good = []
for m, n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])
# cv.drawMatchesKnn expects list of lists as matches.
img3 = cv.drawMatchesKnn(img1, kp1, img2, kp2, good,
                         None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
plt.imshow(img3), plt.show()
