import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('blank', blank)

# #paint image
# blank[:] = 0, 255, 0
# cv.imshow('green', blank)

#draw a rectangle
#we ca decide the size and color from here
# cv.rectangle(blank,(0, 0), (250, 250), (0, 255, 0), thickness = 2)
# cv.rectangle(blank,(0, 0), (250, 250), (0, 255, 0), thickness = cv.FILLED)

#square
# cv.rectangle(blank,(0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness = cv.FILLED)
# cv.imshow('rectangle', blank)

# img = cv.imread('images/cat 2.jpg')
# cv.imshow('cat', img)

#draw a circle 
#can fill using thickness = -1
# cv.circle(blank,(250, 250), 40, (0, 0, 255), thickness=3)
# cv.imshow('circle', blank)

#draw a line
#can change position from here
# cv.line(blank,(0, 0), (blank.shape[1]//2, blank.shape[0]//3), (255, 255, 255), thickness = 3)
# cv.imshow('line', blank)

#Write text on image
cv.putText(blank, 'hello world', (225, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0,(0, 255, 0), 2)
cv.imshow('Text', blank)
cv.waitKey(0)