from skimage.filters.rank import entropy
from skimage.morphology import disk

from skimage import io
import matplotlib.pyplot as plt
import numpy as np

from skimage.filters import threshold_otsu

import glob

time = 0
time_list=[]
area_list=[]
path = "C:/Users/ThinkPad/Downloads/7.2.26"
for file in glob.glob(path):
    dict={}
    img= io.imread(file)
    entropy_img = entropy(img, disk(3))
    thresh = threshold_otsu(entropy_img)
    binary = entropy_img <= thresh
    scratch_area = np.sum(binary == 1)
    print('time=', time, 'hr ', "Scratch area=", scratch_area)
    time_list.append(time)
    area_list.append(scratch_area)
    time +=1

plt.plot(time_list, area_list, 'bo')


