# gives intensity of pixels in images
#Bins - intervals of pixels intensity

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('images/cat 2.jpg')

cv.imshow('cat', img)

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')

colors = ('b', 'g', 'r')

for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 255])
    plt.plot(hist, color= col)
    plt.xlim([0, 256])

plt.show()

#we can create a mask, and plot histogram for specific areas

cv.waitKey(0)