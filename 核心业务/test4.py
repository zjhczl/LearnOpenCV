import cv2 as cv
# Load two images
img1 = cv.imread('./img/1.jpeg')
logo = cv.imread('1.png')
# I want to put logo on top-left corner, So I create a ROI
rows, cols, channels = logo.shape
roi = img1[0:rows, 0:cols]
# Now create a mask of logo and create its inverse mask also
logogray = cv.cvtColor(logo, cv.COLOR_BGR2GRAY)

ret, mask = cv.threshold(logogray, 10, 255, cv.THRESH_BINARY)

mask_inv = cv.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv.bitwise_and(roi, roi, mask=mask_inv)

# Take only region of logo from logo image.
logo_fg = cv.bitwise_and(logo, logo, mask=mask)
cv.imshow('sa', logo_fg)
# Put logo in ROI and modify the main image
dst = cv.add(img1_bg, logo_fg)
img1[0:rows, 0:cols] = dst
cv.imshow('res', img1)
cv.waitKey(0)
cv.destroyAllWindows()
