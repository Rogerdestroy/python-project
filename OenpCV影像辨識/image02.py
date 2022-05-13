import cv2
import numpy as np
import random


#img = cv2.imread('pet_annotations.jpg')
#print(type(img))  #<class 'numpy.ndarray'> nd->多維
#print(img.shape)  #(352, 693, 3) / [B] [G] [R] !!!

#----------------------------------

img = np.empty((300, 300, 3), np.uint8)

for row in range(300):
    for col in range(300):
        img[row][col] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
    
cv2.imshow('img' , img)        
cv2.waitKey(0)


#----------------------------------

img2 = cv2.imread('pet_annotations.jpg')
img3 = img2[:150, :200]
img4 = img2[:150, 200:400]


cv2.imshow('img2' , img2)        
cv2.imshow('img3' , img3)   
cv2.imshow('img4' , img4)  
cv2.waitKey(0)