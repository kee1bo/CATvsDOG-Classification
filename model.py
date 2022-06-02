import tensoflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
dog_train = 'train/classb'
cat_train = 'train/classa'
test_dir = 'test1/test'
valid_dir = 'test1/validation'

IMG_SIZE = 64
LR = 1e-3

def label_img(img):
    word_label = img.split('.')[-3]
    if word_label=='cat':
        return [1,0]
    else:
        return [0,1]


def create_train_data(dir_name):
    training_data = []
    for img in os.listdir(dir_name):
        label=label_img(img)



def convert_image_data(img):

