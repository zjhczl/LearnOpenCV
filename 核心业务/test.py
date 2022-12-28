import cv2 as cv
import numpy as np

img = cv.imread('./img/1.jpeg')
# for i in range(100):
#     for j in range(1000):
#         img[i, j] = [255, 255, 255]

# img[0:100, 0:1000] = [255, 255, 255]
# img[0:100, 0:1000] = img[100:200, 0:1000]
b, g, r = cv.split(img)

cv.imshow("zj", cv.merge((b, g, r)))


cv.waitKey(0)
