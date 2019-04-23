import inspect
import os
import numpy as np 
import tensorflow as tf 
import time
import matplotlib.pyplot as plt 

VGG_MEAN = [103.939, 116.779, 123.68]

vgg16_path = '../data'

class Vgg16():
    def __init__(self, vgg16_path = None):
        if vgg16_path is None:
            vgg16_path = os.path.join(os.getcwd(), vgg16_path)