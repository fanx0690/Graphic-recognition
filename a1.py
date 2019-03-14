# coding=gbk
'''
@author: fan fan
@id:    136800690
'''

import numpy as np
import matplotlib.pyplot as plt
import pylab

def filt(image, kernel):
    Hi, Wi = image.shape
    Hk, Wk = kernel.shape
    out = np.zeros((Hi, Wi))

    for i in range(Hi):
        for j in range(Wi):
            temp = 0
            for m in range (Hk):
                for n in range (Wk):
                    px = i+-1+m
                    py = j+-1+n
                    if (px<0 or px >= Hi or py <0 or py >= Wi):
                        ni = 0
                    else:
                        ni = image[px][py]
                    nk = kernel[m][n]
                    temp += nk*ni
            out[i][j] = temp
    return out              



img = plt.imread("photo.jpg",0)                        
plt.imshow(img,cmap ='gray')                                     
print(img.shape)
print(img)
pylab.show()


matrix = np.array([[ 1/9, 1/9, 1/9],                        
                   [ 1/9, 1/9, 1/9],
                   [ 1/9, 1/9, 1/9]])

res = filt(img, matrix)
print("test\n")




print(res)
print("img shape :" + str(img.shape))
plt.imshow(res,cmap ='gray')
print("res shape :" + str(res.shape))
plt.imsave("res.jpg",res)
pylab.show()