import cv2 as cv

img = cv.imread('images/cat 2.jpg')

cv.imshow('cat', img)

#middle pixel is the average of surrounding pixel

#Average blur
average = cv.blur(img, (7, 7)) #pass higher kernel value for more blurr
cv.imshow('Average', average)

#Gaussian Blur
gauss = cv.GaussianBlur(img,(7, 7), 0)
cv.imshow('Gaussian', gauss)

#Here, Average is more blurr, but gaussian looks natural blur, so most of time we use gaussian

#Median Blur
Median = cv.medianBlur(img, 7)
cv.imshow('Median', Median)

#Bilateral Blur - (least blur)filter for noise removal while keeping edges sharp
bilateral = cv.bilateralFilter(img, 7, 35, 35)
cv.imshow('bilateral', bilateral)


cv.waitKey(0)