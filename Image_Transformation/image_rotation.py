import cv2 as cv
import numpy as np

img = cv.imread('images/cat 2.jpg')

cv.imshow('boston', img)

#Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimension = (width, height)

    return cv.warpAffine(img, rotMat, dimension)

rotate = rotate(img, -45)
cv.imshow("rotated", rotate) 

cv.waitKey(0)