import cv2 as cv
import numpy as np

img = cv.imread('images/pic.jpg')
# cv.imshow('image', img)

b, g, r = cv.split(img)

cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(img.shape) #3 color channel
print(g.shape) #zero color channel

merge = cv.merge([b, g, r])
cv.imshow('merge', merge)

cv.waitKey(0)