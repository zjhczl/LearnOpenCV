# 两个图像相加
import cv2 as cv
img1 = cv.imread("./img/1.jpeg")
img2 = cv.imread("./img/2.jpeg")
img3 = cv.imread("1.png")

cv.imshow("opencv", cv.add(img1, img2))
cv.imshow("numpy", img1+img2)
cv.imshow("addweight", cv.addWeighted(img1, 0.3, img2, 0.7, 0))
cv.waitKey(0)
