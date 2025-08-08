import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('images/cat 2.jpg')

cv.imshow('cat', img)

# plt.imshow(img)
# plt.show() ##rgb mode(default of matplotlib)


#BGR to GrayScale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# BGR to HSV(huge saturation value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

#BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('lab', lab)


#bgr to rgb
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow("rgb", rgb)

#We cant convert, Grayscale to HSV, HSV to LAB directly

#HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv_bgr', hsv_bgr)

# plt.imshow(rgb)
# plt.show()

cv.waitKey(0)