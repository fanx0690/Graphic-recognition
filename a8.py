# coding=gbk
'''
@author: fan fan
@id:    136800690
'''
import numpy as np
import matplotlib.pyplot as plt
import pylab
from PIL import Image
import math
import cv2


"""
Return 8-neighbours of point p1 in picture, in order
"""
def neighbours(x, y, image):
    i = image
    x1, y1, x_1, y_1 = x+1, y-1, x-1, y+1
    #print ((x,y))
    return [i[y1][x],  i[y1][x1],   i[y][x1],  i[y_1][x1],  # P2,P3,P4,P5
            i[y_1][x], i[y_1][x_1], i[y][x_1], i[y1][x_1]]  # P6,P7,P8,P9
 
def transitions(neighbours):
    n = neighbours + neighbours[0:1]    # P2, ... P9, P2
    return sum((n1, n2) == (1, 0) for n1, n2 in zip(n, n[1:]))
 
"""
implement Zhang-Suen thinning algorithm
"""
def zhangSuen(image):
    changing1 = changing2 = [(-1, -1)]
    while changing1 or changing2:
        # Step 1
        changing1 = []
        for y in range(1, len(image) - 1):
            for x in range(1, len(image[0]) - 1):
                P2,P3,P4,P5,P6,P7,P8,P9 = n = neighbours(x, y, image)
                if (image[y][x] == 0 and    # (Condition 0)
                    P4 + P6 + P8 >= 1 and   # Condition 4
                    P2 + P4 + P6 >= 1 and   # Condition 3
                    transitions(n) == 1 and # Condition 2
                    2 <= sum(n) <= 6):      # Condition 1
                    changing1.append((x,y))
        for x, y in changing1: 
            image[y][x] = 1
        # Step 2
        changing2 = []
        for y in range(1, len(image) - 1):
            for x in range(1, len(image[0]) - 1):
                P2,P3,P4,P5,P6,P7,P8,P9 = n = neighbours(x, y, image)
                if (image[y][x] == 0 and    # (Condition 0)
                    P2 + P6 + P8 >= 1 and   # Condition 4
                    P2 + P4 + P8 >= 1 and   # Condition 3
                    transitions(n) == 1 and # Condition 2
                    2 <= sum(n) <= 6):      # Condition 1
                    changing2.append((x,y))
        for x, y in changing2: 
            image[y][x] = 1
        #print changing1
        #print changing2
    return image
 
 
     

img = cv2.imread("symbol.png",0)
r, c = img.shape
plt.imshow(img,cmap ='gray')
plt.show()
for m in range(0,r):
    for n in range (0,c):
        if (img[m][n] == 255):
            img[m][n] = 1
        else:
            img[m][n] = 0
out = np.zeros((r,c))
out = zhangSuen(img)
plt.imshow(out,cmap ='gray')
plt.show()


    
         