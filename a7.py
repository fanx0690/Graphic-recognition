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

def distance(v,vt):
    v1 = np.array(v)
    v2 = np.array(vt)
    sq = np.square(v1 - v2)
    sum = np.sum(sq)
    dist = np.sqrt(sum)
    return dist
    

     

img = cv2.imread("5.png",0)
r, c = img.shape
plt.imshow(img,cmap ='gray')
plt.show()
for m in range(0,r):
    for n in range (0,c):
        if (img[m][n] == 255):
            img[m][n] = 1
        else:
            img[m][n] = 0
            

a_l = f_symbol(img)
num = 0

list = [[0.32, 0.27, 0.51, 0.39, 0.00, 0.39, 0.43, 0.25, 0.38],
        [0.04, 20.75, 20.75, 0.74, 87.00, 0.61, 2.65, 83.00, 0.35],
        [0.34, 0.36, 0.19, 0.00, 0.36, 0.09, 0.69, 0.40, 0.31],
        [0.23, 0.30, 0.68, 0.02, 0.46, 0.52, 0.33, 0.31, 0.40],
        [0.11, 0.76, 0.00, 0.59, 0.64, 0.28, 0.00, 0.34, 0.00],
        [0.50, 0.25, 0.24, 0.33, 0.23, 0.45, 0.31, 0.28, 0.49],
        [0.15, 0.50, 0.00, 0.96, 0.28, 0.46, 0.66, 0.31, 0.61],
        [0.30, 0.30, 0.98, 0.00, 0.12, 0.31, 0.00, 0.47, 0.00],
        [0.70, 0.34, 0.77, 0.29, 0.89, 0.52, 0.63, 0.30, 0.66],
        [0.87, 0.27, 1.69, 0.13, 0.22, 1.19, 0.00, 0.00, 1.00]]

tp = a_l[0]
sp = [tp[0],tp[1]]
ep = [tp[2],tp[3]]
out  = ratio_martix(img,sp,ep)

d_min = 10000
a = -1
i = 0
print("distance (to 0 - 9)")
for l in list:
    d = distance(out,l)
    print(d)
    if (d<d_min):
        d_min = d
        a = i        
    i+=1
print("")
print("number recognition:")
print(a)    
         