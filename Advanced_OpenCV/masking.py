import cv2 as cv
import numpy as np

img = cv.imread('images/cat 2.jpg')
cv.imshow('cat', img)

#masking used to focus on specific area
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('blank', blank)

mask = cv.circle(blank, (img.shape[1]//2 + 45, img.shape[0]//2), 100, 255, -1)
cv.imshow('mask', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('masked', masked)

cv.waitKey(0)