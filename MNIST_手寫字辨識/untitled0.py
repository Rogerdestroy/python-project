import keras
from keras.datasets import mnist

import os
from PIL import Image
import numpy as np

def load_data():
    
    train_data = np.empty((36000,1,28,28),dtype="float32")
    train_labels = np.empty((36000,),dtype="uint8")
    train_data = np.empty((6000,1,28,28),dtype="float32")
    train_labels = np.empty((6000,),dtype="uint8")
    
img_1 = os.listdir("./trainImg")
num_1 = len(imgs_1)
for i in range(num_1):
    img_1 = Image.open("./trainImg"+img_1[i])
    arr_1 = np.asarray(img_1,dtype="float32")
    train_data[i,:,:,:] = arr_1
    train_labels[i] = int(img_1[i].split('.')[0])
    

img_2 = os.listdir("./trainImg")
num_2 = len(imgs_2)
for i in range(num_2):
    img_1 = Image.open("./trainImg"+img_2[i])
    arr_1 = np.asarray(img_2,dtype="float32")
    train_data[i,:,:,:] = arr_2
    train_labels[i] = int(img_2[i].split('.')[0])
    
return (train data,train labels), (test data,train labels)