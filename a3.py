# coding=gbk
'''
@author: fan fan
@id:    136800690
'''

import numpy as np
import matplotlib.pyplot as plt
import pylab

def conv(image, kernel):
    Hi, Wi = image.shape
    Hk, Wk = kernel.shape
    
    rev_m = np.zeros((Hk,Wk))
    
    for m in range (Hk):
        for n in range (Wk):
            rev_m[m][n] = kernel[Hk-1-m][Wk-1-n]
    kernel = rev_m
    print(kernel)
    out = np.zeros((Hi, Wi)) 
    temp_m = np.zeros((Hi+Hk-1, Wi+Wk-1)) 
    for i in range(Hi+Hk-1):
        for j in range(Wi+Wk-1):
            temp = 0
            for m in range(Hk):
                for n in range(Wk):
                    if ((i-m)>=0 and (i-m)<Hi and (j-n)>=0 and (j-n)<Wi):
                        temp += image[i-m][j-n] * kernel[m][n]
            temp_m[i][j] = temp
    return temp_m
            
    
              



img = plt.imread("photo.jpg")                        
plt.imshow(img,cmap ='gray')                                     
print(img.shape)
print(img)
pylab.show()


matrix1 = np.array([[1/3,1/3,1/3]])

matrix2 = np.array([[ 1/3],                        
                   [ 1/3],
                   [ 1/3]])
mtest = np.array([[1/9,1/9,1/9],
                  [1/9,1/9,1/9],
                  [1/9,1/9,1/9]])

temp = conv(img, matrix1)
plt.imshow(temp,cmap ='gray')  
pylab.show()
res = conv(temp, matrix2)
plt.imshow(res,cmap ='gray')  
pylab.show()
