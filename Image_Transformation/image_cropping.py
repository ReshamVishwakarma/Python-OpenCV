import cv2 as cv
import numpy as np

img = cv.imread('images/cat 2.jpg')

cv.imshow('cat', img)

resized = cv.resize(img, (300, 300), interpolation=cv.INTER_CUBIC)
# cv.imshow('resized', resized)

#Flipping
# 0 --> vertical, 1 --> horizontal -1 --> both direction
flip = cv.flip(img, 0)
# cv.imshow('flip', flip)

#cropping
crop = img[10:100, 20:100]
cv.imshow('crop', crop)
cv.waitKey(0)