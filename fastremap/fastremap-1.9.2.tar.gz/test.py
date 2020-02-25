import fastremap
import numpy as np 
import time 
from cloudvolume import CloudVolume

# cv = CloudVolume('gs://neuroglancer/basil_v0/basil_full/seg-aug')
# skel = cv.skeleton.get(2743092014128)
# # labels = cv.skeleton.spatial_index.query(cv.bounds * cv.resolution)
# # skel = cv.skeleton.spatial_index.file_locations_per_label([ 4957663529809 ])

# edges = skel.edges.flatten()
# mx = np.max(edges)

cv = CloudVolume('gs://neuroglancer/wms/skeletonization/pinky40subvol', mip=2, cache=True)
img = cv[:][...,0]
# img += img.size
# img[0,0,0] = 1
# img[1,0,0] = img.size + 1

s = time.time()
fastremap.unique(img)
print(time.time() - s)

# s = time.time()
# for i in range(1000):
#   fastremap.unique(skel.edges)
#   # fastremap.unique_via_array(edges, mx)
#   # np.unique(skel.edges)
# print(time.time() - s)

# @profile
# def run():
#   x = np.ones( (512,512,512), dtype=np.uint32, order='C')
#   x += 1
#   print(x.strides, x.flags)
#   y = np.asfortranarray(x)
#   print(x.strides, x.flags)

#   print("done.")

# run()