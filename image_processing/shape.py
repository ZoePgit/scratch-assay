from skimage import io
import os
import glob
import numpy as np

shape_list=[]
dtype_list=[]
path = "C:/Users/ThinkPad/Downloads/7.2.26"
for file in glob.glob(os.path.join(path, "*")):
    img = io.imread(file)
    shape = img.shape()
    dtype = img.dtype()
    shape_list.append(shape)
    dtype_list.append(dtype)
