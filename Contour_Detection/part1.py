import cv2 as cv

img = cv.imread('images/cat 2.jpg')

cv.imshow('cat', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

blur = cv.GaussianBlur(gray,(5, 5), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

canny = cv.Canny(blur, 125,175)
cv.imshow('canny', canny)


contours, hierarchise = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
print(len(contours))

cv.waitKey(0)