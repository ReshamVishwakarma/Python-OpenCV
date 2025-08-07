import cv2 as cv

img = cv.imread('images/cat 2.jpg')

cv.imshow('cat', img)

cv.waitKey(0)