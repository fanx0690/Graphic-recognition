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

def f_symbol(image):
    c_l = []
    a_l = []
    p_l = []
    r,c = image.shape
    for m in range(r):
        for n in range(c):
            if (image[m][n]==0):
                if ([m,n] not in c_l):
                    t_l = [m,n,m,n]
                    p_l.append([m,n])
                    p_find(p_l,image,c_l,t_l)
                    a_l.append(t_l)
                    print(t_l)
    return a_l
                    

def p_find(p_l,image,c_l,t_l):
    while (len(p_l) > 0):
        l = p_l.pop(0);
        r = l[0]
        c = l[1]
        if([r,c] not in c_l):
            c_l.append([r,c]);
            if (r < t_l[0]):
                t_l[0] = r
            if (c < t_l[1]):
                t_l[1] = c
            if (r > t_l[2]):
                t_l[2] = r
            if (c > t_l[3]):
                t_l[3] = c 
                
            if (image[r][c+1] == 0):
                if ([r,c+1] not in c_l): 
                    p_l.append([r,c+1])
                    
            if (image[r][c-1] == 0):
                if ([r,c-1] not in c_l): 
                    p_l.append([r,c-1])
                    
            if (image[r+1][c] == 0):
                if ([r+1,c] not in c_l): 
                    p_l.append([r+1,c])
            if (image[r+1][c+1] == 0):
                if ([r+1,c+1] not in c_l): 
                    p_l.append([r+1,c+1])
                    
            if (image[r+1][c-1] == 0):
                if ([r+1,c-1] not in c_l): 
                    p_l.append([r+1,c-1])
                    
            if (image[r-1][c] == 0):
                if ([r-1,c] not in c_l): 
                    p_l.append([r-1,c])
                    
            if (image[r-1][c+1] == 0):
                if ([r-1,c+1] not in c_l): 
                    p_l.append([r-1,c+1])
                    
            if (image[r-1][c-1] == 0):
                if ([r-1,c-1] not in c_l): 
                    p_l.append([r-1,c-1])
                
    return


def ratio_martix(image,sp,ep):
    out = []
    sy = sp[0]
    sx = sp[1]
    ey = ep[0]
    ex = ep[1]
    m = sy
    n = sx
    y = sy
    x = sx
    dy = math.ceil((ey-sy+1)/3)
    dx = math.ceil((ex-sx+1)/3)
    count = 0
    for m in range(3):
        #x = sx
        for n in range(3):
            ty=0
            cb=0
            cw=0
            y = m*dy + sy
            while (ty<dy and y<=ey):
                tx=0
                x = n*dx + sx
                while (tx<dx and x<=ex):
                    if image[y][x] == 0:
                        cb+=1
                    else:
                        cw+=1
                    tx+=1
                    x+=1
                    count+=1
                ty+=1
                y+=1  
            if (cw == 0):
                temp = cb
            else:
                temp = cb/cw                
            out.append(temp)
    return out
     
img = cv2.imread("tttt.png",0)
plt.imshow(img,cmap ='gray')
pylab.show()
r, c = img.shape
for m in range(0,r):
    for n in range (0,c):
        if (img[m][n] == 255):
            img[m][n] = 1
        else:
            img[m][n] = 0
            
a_l = f_symbol(img)

for tp in a_l:
    sp = [tp[0],tp[1]]
    ep = [tp[2],tp[3]]
    out  = ratio_martix(img,sp,ep)
    print("[", end = "")
    for i in out:
        print("{:.2f} ".format(i),end = "")
    print("]")

    
         