# coding=gbk
'''
Created on 2018/9/17

@author: fan fan
@id:    136800690
'''

import numpy as np
import matplotlib.pyplot as plt
import pylab
import cv2

def bw(image):
    Hi, Wi = image.shape
    out = np.zeros((Hi,Wi))
    for m in range(Hi):
        for n in range(Wi):
            if image[m][n]<=122:
                out[m][n] = 0
            else:
                out[m][n] = 255
    
    return out
              

def black_count(image):
    c_l = []
    a_l = []
    p_l = []
    count = 0
    runtime = 0
    test = 10000000
    dl(runtime,test)
    r,c = image.shape
    for m in range(r):
        for n in range(c):
            if (image[m][n]==0):
                count += 1
                if ([m,n] not in c_l):
                    t_l = [m,n,m,n]
                    p_l.append([m,n])
                    a_l.append(t_l)
    return count
                    

def p_find(p_l,image,c_l,t_l,runtime):
    count = 0
    while (len(p_l) > 0 and runtime < 1):
        runtime += 1
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
def dl(runtime, test):
    while (runtime < test):
        runtime +=1
    return
    

img = plt.imread("testa2.jpg",0)  
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)                      
plt.imshow(img,cmap ='gray')                                     
pylab.show()
res = bw(img)

plt.imshow(res,cmap ='gray')
plt.imsave("res.jpg",res)
pylab.show()
a_l = black_count(res)
print(a_l)
    