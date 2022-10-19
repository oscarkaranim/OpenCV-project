import cv2 as cv

img = cv.imread('Photos/Capture.png')
cv.imshow('Capture', img)

cv.waitKey(0)
