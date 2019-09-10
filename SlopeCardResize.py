<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 16:03:36 2018

@author: 75129
"""

import scipy.io as sio
import numpy as np
import matplotlib as plt
import scipy.interpolate  as siInter

def resample(img,x_size,y_size,method):
#    plt.pyplot.figure()
#    plt.pyplot.imshow(img)
    (xOldSize,yOldSize)=img.shape
    newImg=np.zeros((x_size,y_size))
    pointsNew=np.where(newImg>-999999)
    pointsNew=np.array(pointsNew,dtype=float)
    pointsNew=pointsNew.T
    valueImg=img.reshape((xOldSize*yOldSize,1))
    pointsOld=np.where(img>-999999)
    pointsOld=np.array(pointsOld,dtype=float)
    pointsOld=pointsOld.T
    pointsOld[:,0]=pointsOld[:,0]/(xOldSize-1)*(x_size-1)
    pointsOld[:,1]=pointsOld[:,1]/(yOldSize-1)*(y_size-1)
    valueNewImg=siInter.griddata(pointsOld,valueImg,pointsNew,method)
    NewImg=np.reshape(valueNewImg,(x_size,y_size))
#    plt.pyplot.figure()
#    plt.pyplot.imshow(NewImg)
    return NewImg
    
    
    


#methoddict={0:'cubic',1:'nearest',2:'cubic',3:'nearest',4:'nearest',5:'cubic',6:'cubic',7:'cubic',8:'cubic',9:'cubic',10:'cubic',11:'cubic',12:'nearest',13:'cubic',14:'cubic',15:'cubic'}
#{'altitude','aspect','fault','landuse','lithology','ndvi','plan','profile','rainfall','river','road','slope','soil','spi','sti','twi'}
size_x=40
size_y=40
num_factos=16
num_samples=7598
img_new=np.zeros((num_samples,size_x,size_y,num_factos))

for it in range(num_samples):
    filename='C:/Users/75129/Desktop/mypy/demo_all/yushan_all_OriCard/'+str(it)
    img_resize=np.zeros((size_x,size_y,num_factos))
    img=np.load(filename+'.npy')
    (row,col)=img[:,:,0].shape
    if row==0 :
        img_resize=np.zeros(size_x,size_y,num_factos)
        print('row col ==  0')
    
    elif row==1 or col==1:
        img_resize=np.ones([size_x,size_y,num_factos])
        for i in range(num_factos):
            img_resize[:,:,i]=img_resize[:,:,i]*np.double(img[0,0,i])
        print('row col ==  1')
    else:        
        for i in range(num_factos):
            img_resize[:,:,i]=resample(img[:,:,i],size_x,size_y,'nearest')
            
#    newfilename='C:/Users/75129/Desktop/mypy/xp_kp_newsize8080/'+str(it)
#    np.save(newfilename,img_resize)
#    plt.pyplot.imshow(img_resize[:,:,0])
    
#    newfilename='C:/Users/75129/Desktop/mypy/xp_kp_newsize8080/'+str(it)
#    img_it=np.load(newfilename+'.npy')
    img_new[it,:,:,:]=img_resize
    print(str(it)+' is done')
#    print(it)
newfilename='C:/Users/75129/Desktop/mypy/demo_all/yushan_all_ResizeCard/all_yushan'
np.save(newfilename,img_new)


    
        
    
=======
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 16:03:36 2018

@author: 75129
"""

import scipy.io as sio
import numpy as np
import matplotlib as plt
import scipy.interpolate  as siInter

def resample(img,x_size,y_size,method):
#    plt.pyplot.figure()
#    plt.pyplot.imshow(img)
    (xOldSize,yOldSize)=img.shape
    newImg=np.zeros((x_size,y_size))
    pointsNew=np.where(newImg>-999999)
    pointsNew=np.array(pointsNew,dtype=float)
    pointsNew=pointsNew.T
    valueImg=img.reshape((xOldSize*yOldSize,1))
    pointsOld=np.where(img>-999999)
    pointsOld=np.array(pointsOld,dtype=float)
    pointsOld=pointsOld.T
    pointsOld[:,0]=pointsOld[:,0]/(xOldSize-1)*(x_size-1)
    pointsOld[:,1]=pointsOld[:,1]/(yOldSize-1)*(y_size-1)
    valueNewImg=siInter.griddata(pointsOld,valueImg,pointsNew,method)
    NewImg=np.reshape(valueNewImg,(x_size,y_size))
#    plt.pyplot.figure()
#    plt.pyplot.imshow(NewImg)
    return NewImg
    
    
    


#methoddict={0:'cubic',1:'nearest',2:'cubic',3:'nearest',4:'nearest',5:'cubic',6:'cubic',7:'cubic',8:'cubic',9:'cubic',10:'cubic',11:'cubic',12:'nearest',13:'cubic',14:'cubic',15:'cubic'}
#{'altitude','aspect','fault','landuse','lithology','ndvi','plan','profile','rainfall','river','road','slope','soil','spi','sti','twi'}
size_x=40
size_y=40
num_factos=16
num_samples=7598
img_new=np.zeros((num_samples,size_x,size_y,num_factos))

for it in range(num_samples):
    filename='C:/Users/75129/Desktop/mypy/demo_all/yushan_all_OriCard/'+str(it)
    img_resize=np.zeros((size_x,size_y,num_factos))
    img=np.load(filename+'.npy')
    (row,col)=img[:,:,0].shape
    if row==0 :
        img_resize=np.zeros(size_x,size_y,num_factos)
        print('row col ==  0')
    
    elif row==1 or col==1:
        img_resize=np.ones([size_x,size_y,num_factos])
        for i in range(num_factos):
            img_resize[:,:,i]=img_resize[:,:,i]*np.double(img[0,0,i])
        print('row col ==  1')
    else:        
        for i in range(num_factos):
            img_resize[:,:,i]=resample(img[:,:,i],size_x,size_y,'nearest')
            
#    newfilename='C:/Users/75129/Desktop/mypy/xp_kp_newsize8080/'+str(it)
#    np.save(newfilename,img_resize)
#    plt.pyplot.imshow(img_resize[:,:,0])
    
#    newfilename='C:/Users/75129/Desktop/mypy/xp_kp_newsize8080/'+str(it)
#    img_it=np.load(newfilename+'.npy')
    img_new[it,:,:,:]=img_resize
    print(str(it)+' is done')
#    print(it)
newfilename='C:/Users/75129/Desktop/mypy/demo_all/yushan_all_ResizeCard/all_yushan'
np.save(newfilename,img_new)


    
        
    
>>>>>>> fa3460930da77faa0dec54af7c5115b26a2311a0
    