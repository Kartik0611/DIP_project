# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 15:54:54 2019

@author: Kartik Vishnu Hegde
"""

import cv2
import numpy as np
title_window = 'Cartoonized Image'

src = cv2.imread(r'C:\Users\hp\bokeh2.jpg', cv2.IMREAD_UNCHANGED)
#src = cv2.imread(r'C:\Users\hp\sharath3.png', cv2.IMREAD_UNCHANGED)

height, width = src.shape[:2]

#levels = input("Enter the number of levels ")

def stepdown(pixel,levels):
    value = pixel - (pixel % (256/levels))
    return value

stepdownImg = np.zeros((height, width,3),dtype=np.uint8)

stepdownImg=stepdown(src,8)


def on_trackbar(lev):
    stepdownImg = src-(src%(256/lev))
    cv2.imshow(title_window, stepdownImg)
    



#cv2.imshow("src",src)
#cv2.imshow("stepdownImg",stepdownImg)

#cv2.waitKey(0) # waits until a key is pressed
#cv2.destroyAllWindows() # destroys the window showing image

cv2.namedWindow(title_window)
trackbar_name = 'step val :'
cv2.createTrackbar(trackbar_name, title_window , 8, 127, on_trackbar)
# Show some stuff
on_trackbar(8)
# Wait until user press some key
cv2.waitKey()

