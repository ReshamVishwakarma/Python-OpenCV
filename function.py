import cv2 as cv

img = cv.imread('images/cat 2.jpg')

cv.imshow('cat', img)

#converting image to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

#blur
# blur = cv.GaussianBlur(img,(3, 3), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)


#Edge Cascade
# canny = cv.Canny(img, 125, 175)
# cv.imshow('canny', canny)


#Dilating the image(edges more thicker than canny)
# dilated  = cv.dilate(canny, (3,3), iterations=1)
# cv.imshow('dilated', dilated)


#Resize - (aspect ration is changed)
# resize = cv.resize(img, (400, 400))
# cv.imshow('resize', resize)

#cropping

cropped = img[10:100, 10:100]
cv.imshow('cropped', cropped)
cv.waitKey(0)