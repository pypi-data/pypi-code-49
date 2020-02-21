# import os
# os.chdir("/Users/jameschen")
from PyQt5.QtWidgets import QApplication
# from .lib import *
from .gridGUI import *
from .lib import *
import matplotlib.pyplot as plt
import grid as gd
from grid import lib
import statistics
import cv2
import numpy as np
import pandas as pd
from tqdm import tqdm
app = QApplication(sys.argv)
# === === === === === === DEBUG === === === === === ===

grid = gd.GRID()
grid.loadData("/Users/jameschen/Dropbox/James_Git/FN/data/demo.png")
# grid.loadData("/Users/jameschen/Desktop/testGRID.png")
# grid.loadData(
#     pathImg="/Users/jameschen/Dropbox/James Chen/GRID/Prototype/PineApple.jpg")
grid.binarizeImg(k=3, lsSelect=[0,1], valShad=0, valSmth=0)
# grid.findPlots()
# grid.cpuSeg()

# grid.save(path="/Users/jameschen/", prefix="test")

g = GRID_GUI(grid, 3)  # 0:input, 1:crop, 2:kmean, 3:anchor, 4:output
app.exec_()



# return
# ========== peak searching ==========
# , prominence = (0.01, None)

# def findPeaks(img, nPeaks=0, axis=1, nSmooth=100):
#     """
#     ----------
#     Parameters
#     ----------
#     """
#     # compute 1-D signal
#     signal = img.mean(axis=(not axis)*1) # 0:nrow
#     # ignore signals from iamge frame
#     signal[:2] = 0
#     signal[-2:] = 0
#     # gaussian smooth
#     for _ in range(int(len(signal)/30)):
#         signal = np.convolve(
#             np.array([1, 2, 4, 2, 1])/10, signal, mode='same')
#     # find primary peaks
#     peaks, _ = find_peaks(signal)
#     lsDiff = np.diff(peaks)
#     medSig = statistics.median(signal[peaks])
#     stdSig = np.array(signal[peaks]).std()
#     medDiff = statistics.median(lsDiff)
#     stdDiff = np.array(lsDiff).std()
#     print(lsDiff)
#     print(medDiff)
#     print(stdDiff)
#     # get finalized peaks with distance constrain
#     peaks, _ = find_peaks(signal, distance=medDiff-stdDiff*4)
#     if nPeaks != 0:
#         if len(peaks) > nPeaks:
#             while len(peaks) > nPeaks:
#                 ls_diff = np.diff(peaks)
#                 idx_diff = np.argmin(ls_diff)
#                 idx_kick = idx_diff if (
#                     signal[peaks[idx_diff]] < signal[peaks[idx_diff+1]]) else (idx_diff+1)
#                 peaks = np.delete(peaks, idx_kick)
#         elif len(peaks) < nPeaks:
#             while len(peaks) < nPeaks:
#                 ls_diff = np.diff(peaks)
#                 idx_diff = np.argmax(ls_diff)
#                 peak_insert = (peaks[idx_diff]+peaks[idx_diff+1])/2
#                 peaks = np.sort(np.append(peaks, int(peak_insert)))
#     return peaks, signal


# pks, sig = findPeaks(grid.map.imgs[1])
# plt.plot(sig)
# plt.plot(pks, sig[pks], "x")
# plt.show()

# ========== peak searching ==========


# === === === detect default rank of K === === === ===
# import grid as gd
# import numpy as np
# import matplotlib.pyplot as plt

# grid = gd.GRID()
# grid.loadData("/Users/jameschen/Dropbox/James_Git/FN/data/demo.png")
# # grid.loadData("/Users/jameschen/Dropbox/James Chen/GRID/Modeling/Rhombus.jpg")

# k = 5
# row = k
# col = 4
# i = 0

# grid.binarizeImg(k=k, lsSelect=[0], valShad=0, valSmth=0, outplot=False)

# for i in range(row):
#     imgB = (np.isin(grid.imgs.get('kmean'), i)*1).astype(np.int)
#     sigs = imgB.mean(axis=0)
#     plt.subplot(row, col, 1+i*col+0)
#     plt.imshow(imgB)
#     plt.subplot(row, col, 1+i*col+1)
#     plt.ylim(0, 1)
#     plt.plot(sigs)
#     plt.subplot(row, col, 1+i*col+2)
#     sigf = gd.getFourierTransform(sigs)
#     plt.plot(sigf)
#     plt.subplot(row, col, 1+i*col+3)
#     # scMaxF = round(max(sigf)*5, 4)  # [0, 1]
#     scMaxF = round((max(sigf)/sigf.mean())/100, 4)  # [0, 1]
#     scMean = round(1-(sigs.mean()), 4) # [0, 1]
#     scPeaks = round(len(gd.find_peaks(sigs, height=(sigs.mean()))
#                   [0])/len(gd.find_peaks(sigs)[0]), 4)
#     # scPeaks = len(gd.find_peaks(sigs)[0])
#     score = scMaxF*.25 + scMean*.25 + scPeaks*.5
#     plt.text(.3, .8, str(score), fontsize=10)
#     plt.text(.3, .6, str(scMaxF), fontsize=10)
#     plt.text(.3, .4, str(scMean), fontsize=10)
#     plt.text(.3, .2, str(scPeaks), fontsize=10)

# plt.show()

# === === === detect default rank of K === === === ===


# max(getFourierTransform(sigs))


# plt.imshow()
# plt.show()

# grid = gd.GRID()
# grid.loadData("/Users/jameschen/Dropbox/James Chen/GRID/Modeling/Rhombus.jpg")
# grid.binarizeImg(k=5, lsSelect=[0], valShad=0, valSmth=0, outplot=False)
# grid.findPlots(outplot=False)
# grid.map.dt
# # grid.cpuSeg()
# # grid.save(prefix="Pumptree2")

# app = QApplication(sys.argv)
# g = GRID_GUI(grid, 4) # 0:input, 1:crop, 2:kmean, 3:anchor, 4:output
# app.exec_()


# # ========== kmean ==========
# array = numpy.array([4, 2, 7, 1])
# temp = array.argsort()
# ranks = numpy.empty_like(temp)
# ranks[temp] = numpy.arange(len(array))

# def getRank(array):
#     sort = array.argsort()
#     rank = np.zeros(len(sort), dtype=np.int)
#     rank[sort] = np.flip(np.arange(len(array)), axis=0)
#     return rank

# test = np.array([2, 6, 87,1, 3, 6])
# getRank(test)
# temp = test.argsort()
# np.zeros(len(temp))
# rank = np.empty_like(temp)
# rank[temp] = np.flip(np.arange(len(test)), axis=0)
# np.arange(1, 7, 1)
# np.arange(6, 2, 1)

# ========== plotting ==========

# FIXME: Wrong order for the second axis

# ========== peak searching ==========
# pks, sig = gd.findPeaks(grid.map.imgs[1])
# plt.plot(sig)
# plt.plot(pks, sig[pks], "x")
# plt.show()


# grid.save(prefix="Pumptree2")

# grid = gd.GRID()
# grid.loadData("/Users/jameschen/Dropbox/James Chen/GRID/Modeling/Rhombus.jpg")
# grid.binarizeImg(k=5, lsSelect=[0], valShad=0, valSmth=0, outplot=False)
# grid.findPlots(nRow=7, nCol=6, outplot=False)
# grid.cpuSeg(outplot=True)
# grid.save(prefix="Rhombus")
# # grid.run(pathImg="/Users/jameschen/Dropbox/James Chen/GRID/Modeling/Rhombus.jpg", k=5, lsSelect=[4], path="/Users/jameschen", prefix="letmesleep")

# # with open("/Users/jameschen/Dropbox/photo_grid/Outputter_1018.grid", "wb") as file:
# #     pickle.dump(grid, file, pickle.HIGHEST_PROTOCOL)

# # grid.loadData("/Users/jameschen/Dropbox/James_Git/FN/data/demo.png")
# # grid.binarizeImg(k=3, lsSelect=[0, 1], valShad=0, valSmth=0, outplot=False)


# g = GRID_GUI(grid, 4)
# app.exec_()

