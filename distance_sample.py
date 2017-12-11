
# coding: utf-8

# In[ ]:

from PIL import Image
import imagehash
import imageio
import numpy as np
import random
from joblib import Parallel, delayed
import pickle
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
get_ipython().magic("config InlineBackend.figure_format = 'retina'")
def distance_sample(name1,name2):
    hashes=[]
    arrays = []
    for num,filename in enumerate([name1,name2]):
        with imageio.get_reader("./videos/%s.mp4"%filename,'ffmpeg') as video:
            N,w,c=video.get_data(0).shape
            arr = np.zeros((N,w,3),np.float)
            for img in video:
                arr += np.array(img)
            arr = np.array(np.round(1.0*arr/N),dtype=np.uint8)
            arrays.append(arr)
            hashes.append(imagehash.phash(Image.fromarray(arr)))
    plt.figure(figsize=(14,7))
    sub1= plt.subplot(121)
    sub1.axis("off")
    sub2 = plt.subplot(122)
    sub2.axis("off")
    sub1.imshow(np.asarray(arrays[0]))
    sub1.set_title("fig1 name: %s hash: %s "%(name1,hashes[0]))
    sub2.imshow(np.asarray(arrays[1]))
    sub2.set_title("fig2 name: %s hash: %s"%(name2,hashes[1]))
    plt.show()
    print("Hamming Distance: %s"%(hashes[0]-hashes[1]))

