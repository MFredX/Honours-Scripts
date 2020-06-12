# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 19:35:07 2020

@author: sachi
"""

import cv2
import numpy as np

#filename = './Training/croppedDrive.jpg'
#filename='./Training/frameNumbers13.jpg'

img = cv2.imread('./Training/croppedDrive.jpg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#sift = cv2.SIFT()

sift = cv2.xfeatures2d.SIFT_create()
kp, des = sift.detectAndCompute(gray,None)
#kp = sift.detect(gray,None)

img=cv2.drawKeypoints(gray,kp, outImage = None)

cv2.imwrite('sift_keypoints2.jpg',img)

#kp,des = sift.compute(gray,kp)

print("done")