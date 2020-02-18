# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 08:09:25 2020

@author: Jerry
"""

#%% 0. Make fake data
import numpy as np
import matplotlib.pyplot as plt
vol = np.zeros((50, 128, 128))
vol[20:30, 40:88, 40:88] = 1
vol += 0.1*np.random.rand(*vol.shape)
# plt.imshow(vol[25,:,:], cmap='gray')

seg1 = np.zeros((50, 128, 128))
seg1[20:30, 40:88, 40:88] = 1

seg2 = np.zeros((50, 128, 128))
seg2[20:29, 45:95, 45:95] = 1
seg2[29, 40:88, 40:88] = 1

# fig, axs = plt.subplots(1,3)
# axs[0].imshow(np.squeeze(vol[25,:,:]), cmap='gray')
# axs[1].imshow(np.squeeze(seg1[25,:,:]), cmap='gray')
# axs[2].imshow(np.squeeze(seg2[25,:,:]), cmap='gray')

# 1. Processing

#%% 
# from jximgtools.metric import dicePerSlice, dice
# from jximgtools.visualization.volSlicer import VolSlicer
from metric import dicePerSlice, dice
from visualization.volSlicer import VolSlicer

# slicesInfo = [{'info':'Slice # {}'.format(sliceIdx+1) for sliceIdx in range(50)}]
dicee = dice(seg1, seg2)
dices = dicePerSlice(seg1, seg2)
volInfo = {'Name': 'Test Volume', 'DicePerSlice': dices}
slicesInfo = [{'Dice': dices[sliceIdx]} for sliceIdx in range(50)]
# VolSlicer(vol, volInfo = volInfo, segs = [seg1, seg2], slicesInfo = slicesInfo)
VolSlicer(vol, volInfo = volInfo, segs = [seg1, seg2])
# VolSlicer(vol)