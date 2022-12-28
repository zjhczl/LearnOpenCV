# 基本的图片读取显示写入操作
import cv2 as cv
import sys

# print(cv.samples.findFile("./img/1.jpeg"))
img = cv.imread("./img/1.jpeg")
if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("starry_night.png", img)
