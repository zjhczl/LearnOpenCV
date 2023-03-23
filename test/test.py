import cv2
import numpy as np

# 加载图像
img1 = cv2.imread('starry_night.png')
img2 = cv2.imread('1.png')
# I want to put logo on top-left corner, So I create a ROI
rows, cols, channels = img2.shape

roi = img1[0:rows, 0:cols]
# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
cv2.imshow("res", img2gray)
cv2.waitKey(0)
ret, mask = cv2.threshold(img2gray, 175, 255, cv2.THRESH_BINARY)
cv2.imshow("res", mask)
cv2.waitKey(0)
mask_inv = cv2.bitwise_not(mask)
cv2.imshow("res", mask_inv)
cv2.waitKey(0)
# Now black-out the area of logo in ROI
# 取 roi 中与 mask 中不为零的值对应的像素的值，其他值为 0
# 注意这里必须有 mask=mask 或者 mask=mask_inv, 其中的 mask= 不能忽略
img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
cv2.imshow("res", img1_bg)
cv2.waitKey(0)
# 取 roi 中与 mask_inv 中不为零的值对应的像素的值，其他值为 0。
# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2, img2, mask=mask_inv)
# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst
cv2.imshow('res', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()