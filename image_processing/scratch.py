from skimage.filters.rank import entropy
from skimage.morphology import disk

from skimage import io
import matplotlib.pyplot as plt
import numpy as np

from skimage.filters import threshold_otsu

img0 = io.imread('C:/Users/ThinkPad/Downloads/3t3.16.0.5fbs.0h.tiff')
entropy_img0 = entropy(img0, disk(10))
thresh = threshold_otsu(entropy_img0)
binary = entropy_img0 <= thresh
plt.imshow(entropy_img0)


img24 = io.imread('C:/Users/ThinkPad/Downloads/3t3.16.0.5fbs.24h.2.tiff')
entropy_img24 = entropy(img24, disk(10))
thresh = threshold_otsu(entropy_img24)
binary = entropy_img24 <= thresh
plt.imshow(entropy_img24)

plt.show()
