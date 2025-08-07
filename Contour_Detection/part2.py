import cv2 as cv
import numpy as np

img = cv.imread('images/cat 2.jpg')

# cv.imshow('cat', img)

blank = np.zeros(img.shape, dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)


contours, hierarchise = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
print(len(contours))

cv.drawContours(blank, contours, -1, (0,0,255),1)
cv.imshow('blank', blank)

cv.waitKey(0)