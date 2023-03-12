import cv2
import numpy as np

img = cv2.imread('mp2.jpg',0)
equ = cv2.equalizeHist(img)

cv2.imshow('cv.jpg',equ)
cv2.waitKey(-1)
