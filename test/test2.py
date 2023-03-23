import cv2 as cv
import numpy as np

img = cv.imread('./img/1.jpeg', 0)
for i in range(255):
    edges = cv.Canny(img, 100, i)
    cv.imshow("zj00", edges)
    cv.waitKey(50)
