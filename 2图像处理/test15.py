# 直方图均衡化(提高对比度)
import cv2 as cv
img = cv.imread('./img/1.jpeg', 0)
equ = cv.equalizeHist(img)
res = np.hstack((img, equ))  # stacking images side-by-side
cv.imwrite('res.png', res)
