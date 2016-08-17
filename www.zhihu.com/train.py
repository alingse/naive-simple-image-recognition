#coding=utf-8
#author@alingse
#2016.08.17


from PIL import Image
import numpy as np

import os

def load_data(lablepath):
    data = np.empty((200,1,60,150),dtype="float32")
    label = np.empty((200,),dtype="uint8")

    files = os.listdir(lablepath)
    for i,file in enumerate(files):
        img = Image.open('{}/{}'.format(lablepath,file))
        data[i,:,:,:] = np.asarray(img)
        label[i] = int(file.split('.')[-2])
    return data,label

if __name__ == '__main__':
    lablepath='./label_image/'
    load_data(lablepath)
