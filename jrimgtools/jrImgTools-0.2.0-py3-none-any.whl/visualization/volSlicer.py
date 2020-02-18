# Run tkinter code in another thread
# Source: https://stackoverflow.com/questions/459083/how-do-you-run-your-own-code-alongside-tkinters-event-loop
"""
+------------------------------------------------+
|   +----------------------------------------+   |
|   |                                        |   |
|   |                                        |   |
|   |                                        |   |
|   |                                        |   |
|   |                                        |   |
|   |                                        |   |
|   |                 Slice                  |   |
|   |                                        |   |
|   |                                        |   |
|   |                                        |   |
|   |                                        |   |
|   |                                        |   |
|   |                                        |   |
|   |                                        |   |
|   |                                        |   |
|   |                                        |   |
|   |                                        |   |
|   |                                        |   |
|   +----------------------------------------+   |
|                                                |
|   +----------------------------------------+   |
|   |                                        |   |
|   |      Stem plot of Dice per slice       |   |
|   |                                        |   |
|   +----------------------------------------+   |
|                                                |
|   +----------------+Slider+----------------+   |
|                                                |
|   Vol Info                                     |
|   +----------------------------------------+   |
|   |                                        |   |
|   +----------------------------------------+   |
|                                                |
|   Slice Info                                   |
|   +----------------------------------------+   |
|   |                                        |   |
|   +----------------------------------------+   |
|                                                |
+------------------------------------------------+

"""
import sys
if sys.version_info.major == 2:
    import Tkinter as tk
else:
    import tkinter as tk
import threading
import numpy as np

# from tkinter import StringVar
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
# from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

# from ..process.imgProcess import bwperim
# from ..imgIO import safeLoadMedicalImg
from process.imgProcess import bwperim
# from imgIO import safeLoadMedicalImg

import numpy.ma as ma

def normVol(vol):
    vol = vol.astype(float)
    return (vol - np.min(vol)) / (np.max(vol) - np.min(vol))

def getVolSlicing(ndim, sliceIdx, sliceDim = 0):
    slc = [slice(None)] * ndim
    if ndim in [3,4]:
        # [D, H, W]
        # [D, H, W, C]
        slc[sliceDim] = slice(sliceIdx, sliceIdx + 1)
    elif ndim == 5:
        # [N, D, H, W, C]
        slc[sliceDim+1] = slice(sliceIdx, sliceIdx + 1)
    return slc

def sliceVol(vol, sliceIdx, sliceDim=0):
    slc = getVolSlicing(np.ndim(vol), sliceIdx, sliceDim)
    return np.squeeze(vol[tuple(slc)])
    # slc = [slice(None)] * np.ndim(vol)
    # if np.ndim(vol) in [3,4]:
    #     # [D, H, W]
    #     # [D, H, W, C]
    #     slc[sliceDim] = slice(sliceIdx, sliceIdx + 1)
    # elif np.ndim(vol) == 5:
    #     # [N, D, H, W, C]
    #     slc[sliceDim+1] = slice(sliceIdx, sliceIdx + 1)
    # return np.squeeze(vol[tuple(slc)])

def getSliceNum(vol, sliceDim):
    if np.ndim(vol) in [3,4]:
        # [D, H, W]
        # [D, H, W, C]
        return vol.shape[sliceDim]
    elif np.ndim(vol) == 5:
        # [N, D, H, W, C]
        return vol.shape[sliceDim + 1]
    else:
        raise ValueError('!')


class VolSlicer(threading.Thread):

    def __init__(self, vol, volInfo = {}, segs = [], slicesInfo = None, DicePerSlice = None):
        threading.Thread.__init__(self)
        self.vol = normVol(vol)
        self.volInfo = volInfo        
        # self.segs = segs
        self.segs = [seg > 0 for seg in segs]
        self.ann = None
        
        self.showSeg = True
        self.showAnnotation = True
        
        self.sliceDim = volInfo.get('sliceDim', 0)
        self.sliceNum = getSliceNum(vol, self.sliceDim)
        # self.slicesInfo = slicesInfo if slicesInfo != None else [{}]*self.sliceNum
        self.slicesInfo = slicesInfo
        self.DicePerSlice = DicePerSlice
        
        self.sliceIdx = self.sliceNum//2    
        
        self.clicked = False
        
        self.start()

    def callback(self):
        self.root.quit()
        self.root.destroy()
        
    def run(self):
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        
        # def resize(event):
        #     print(self.root.winfo_width())
        # self.root.bind('<Configure>', resize)
        
        def updateSlice():
            # print(c1.state())
            # Show image
            # sliceAx.imshow(np.squeeze(self.vol[0,self.sliceIdx-1,:,:,:]), cmap='gray')
            sliceAx.cla()
            sliceAx.imshow(sliceVol(self.vol, self.sliceIdx-1, self.sliceDim), cmap='gray', vmax = 1)
            sliceAx.set_title('Slice {}/{} in dim {}'.format(self.sliceIdx, self.sliceNum, self.sliceDim))
            sliceFig.canvas.draw_idle()
            sliceSlider.set(self.sliceIdx)
            
            cmaps = ['autumn', 'winter', 'summer', 'spring', 'cool', 'Wistia']
            if self.showSeg:
                for segIdx, seg in enumerate(self.segs):
                    # segSlice = seg[0,self.sliceIdx, :,:,:].squeeze()
                    # segSlice = bwperim(seg[0,self.sliceIdx, :,:,:].squeeze(), 2, 4)
                    segSlice = sliceVol(seg, self.sliceIdx-1, self.sliceDim)
                    segSlice = bwperim(segSlice, 2, 4)
                    
                    segSliceMask = ma.masked_array(data = np.ones(segSlice.shape), mask = 1-segSlice)
                    # maskedImg = ma.masked_array(data = np.ones(seg.shape), mask = 1-seg)
                    # maskedImgSlice = np.squeeze(maskedImg[0,self.sliceIdx-1, :,:,:])
                    sliceAx.imshow(segSliceMask, alpha=0.6, cmap = cmaps[segIdx])
            
            if self.showAnnotation and self.ann is not None:
                annSlice = sliceVol(self.ann, self.sliceIdx-1, self.sliceDim)
                annSlice = bwperim(annSlice, 2, 4)
                
                annSliceMask = ma.masked_array(data = np.ones(annSlice.shape), mask = 1-annSlice)
                # maskedImg = ma.masked_array(data = np.ones(seg.shape), mask = 1-seg)
                # maskedImgSlice = np.squeeze(maskedImg[0,self.sliceIdx-1, :,:,:])
                sliceAx.imshow(annSliceMask, alpha=0.6, cmap = cmaps[-3])
            
            # Update slice Info            
            if self.slicesInfo is not None:
                sliceInfoStr = ''
                sliceInfoStr += 'Slice {}/{}\n'.format(self.sliceIdx, self.sliceNum)
                # print(len(self.slicesInfo))
                for sliceInfoKey in self.slicesInfo[self.sliceIdx-1].keys():
                    sliceInfoStr += sliceInfoKey + ':\t' + str(self.slicesInfo[self.sliceIdx-1][sliceInfoKey]) + '\n'
                sliceInfoLabel['text'] = sliceInfoStr
        
        def onLeftArrowKey(event):
            self.sliceIdx = max(1, self.sliceIdx - 1)
            updateSlice()
        def onRightArrowKey(event):
            self.sliceIdx = min(self.sliceNum, self.sliceIdx + 1)
            updateSlice()
        
        
        self.root.bind('<Left>', onLeftArrowKey)
        self.root.bind('<Right>', onRightArrowKey)
        
        # [N, D, H, W, C] = self.vol.shape
        sliceFig = Figure(figsize=(5, 4), dpi=100)
        sliceAx = sliceFig.add_subplot(111)
        # sliceAx = sliceFig.add_subplot(311)
        # sliceAx.imshow(np.squeeze(self.vol[0,self.sliceIdx, :,:,:]), cmap='gray')
        # sliceAx.imshow(np.squeeze(self.vol[0,self.sliceIdx, :,:,:]), cmap='gray')
        sliceAx.imshow(sliceVol(self.vol, self.sliceIdx-1, self.sliceDim), cmap='gray')

        sliceCanvas = FigureCanvasTkAgg(sliceFig, master=self.root)  # A tk.DrawingArea.
        sliceCanvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        sliceCanvas.draw()
        
        # def annVolInSlice(x, y, sliceIdx, sliceDim):
        #     slc = getVolSlicing(np.ndim(self.ann), sliceIdx, sliceDim)
            
        #     print(slc)
        #     print(np.shape(self.ann[slc]))
        #     self.ann[slc][y,x] = 1
        def clicked(event):
            self.clicked = True
            annotate(int(event.xdata), int(event.ydata))
            
        def released(event):
            self.clicked = False
        
        def annotate(x,y):
            if self.ann is None:
                self.ann = np.zeros(self.vol.shape)
            # print(int(event.xdata))
            # x, y = int(event.xdata), int(event.ydata)
            slc = getVolSlicing(np.ndim(self.ann), self.sliceIdx-1, self.sliceDim)
            # print(slc)
            # print(self.ann.shape)
            slc2D = [y,x];  slc2D.insert(0,self.sliceDim)
            # print(self.ann[slc].shape)
            self.ann[tuple(slc)][slc2D[0],slc2D[1],slc2D[2]] = 1
            updateSlice()
            # annVolInSlice(x,y,self.sliceIdx, self.sliceDim)
            # print(event.button==tk.MouseButton.LEFT)
            # print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
            #       ('double' if event.dblclick else 'single', event.button,
            #        event.x, event.y, event.xdata, event.ydata))
        
        def annotating(event):
            if self.clicked == True:
                annotate(int(event.xdata), int(event.ydata))
        
        
        sliceFig.canvas.mpl_connect('motion_notify_event', annotating)
        sliceFig.canvas.mpl_connect('button_press_event', clicked)
        sliceFig.canvas.mpl_connect('button_release_event', released)
        
        def switchSeg(event=None):
            self.showSeg = not self.showSeg
            updateSlice()
        
        def switchAnnotate(event=None):
            self.showAnnotation = not self.showAnnotation
            updateSlice()
            
        showSegButton = tk.Button(self.root, text="Show/hide Segmentation", command=switchSeg)
        showSegButton.pack()
        showAnnButton = tk.Button(self.root, text="Show/hide Annotation", command=switchAnnotate)
        showAnnButton.pack()
        
        def switchSliceDim(event=None):
            # https://stackoverflow.com/questions/40589834/how-do-i-get-tkinter-scale-widget-to-set-its-upper-limit-to-an-updated-variable
            self.sliceDim = (self.sliceDim + 1) % 3
            
            self.sliceNum = getSliceNum(self.vol, self.sliceDim)
            self.sliceIdx = self.sliceNum//2
            
            # self.scale.configure(from_=0)
            sliceSlider.configure(to=self.sliceNum)
            #self.sliceSlider = tk.Scale(master = self.root, from_= 1, to_=self.sliceNum, orient=tk.HORIZONTAL, command=sliceSliderChange, length=350)
            #self.sliceSlider.set(self.sliceIdx)
            # self.sliceSlider.place(relwidth=1)
            # self.sliceSlider.pack(side = tk.TOP, expand = False)
            
            updateSlice()
            
        switchSliceDimButton = tk.Button(self.root, text="Switch slice dim", command=switchSliceDim)
        switchSliceDimButton.pack()
        # c1 = tk.Checkbutton(self.root, text='Show Segmentations',variable=self.showSeg, onvalue=1, offvalue=0, command=ppp)
        # c1.state(['disabled'])
        # c1.pack(side = tk.TOP)
        # c2 = tk.Checkbutton(self.root, text='Show Annotations',variable=self.showAnnotation, onvalue=1, offvalue=0, command=ppp)
        # c2.pack(side = tk.TOP)
        
        toolbar = NavigationToolbar2Tk(sliceCanvas, self.root)
        toolbar.update()
              
        # def on_key_press(event):
        #     print("you pressed {}".format(event.key))
        #     key_press_handler(event, sliceCanvas, toolbar)
        # sliceCanvas.mpl_connect("key_press_event", on_key_press)
        
        
        # def _quit():
        #     root.quit()     # stops mainloop
        #     root.destroy()  # this is necessary on Windows to prevent
        #                     # Fatal Python Error: PyEval_RestoreThread: NULL tstate
        
        
        
        def sliceSliderChange(event):            
            self.sliceIdx = int(event)
            updateSlice()
            
        # button = tk.Button(master=self.root, text="Quit", command=pp)
        # button.pack(side=tk.BOTTOM)
        
        # Plot Dice per slice if provided
        if self.DicePerSlice is not None:            
            dicePlotFig = Figure(figsize = (1,1))
            dicePlotAx = dicePlotFig.add_subplot(111)
            dicePlotAx.stem(self.DicePerSlice, use_line_collection = True)
            dicePlotAx.set_xlabel('SliceIdx')
            dicePlotAx.set_ylabel('Dice')
            dicePlotCanvas = FigureCanvasTkAgg(dicePlotFig, master=self.root)
            dicePlotCanvas.get_tk_widget().pack(side=tk.TOP, fill='x', expand=0)
            dicePlotCanvas.draw()
                
        
        # Choose slice to show
        sliceSlider = tk.Scale(master = self.root, from_= 1, to_=self.sliceNum, orient=tk.HORIZONTAL, command=sliceSliderChange, length=350)
        sliceSlider.set(self.sliceIdx)
        sliceSlider.place(relwidth=1)
        sliceSlider.pack(side = tk.TOP, expand = False)
        
        
        # print(sliceSlider.from_)
        
        # Show information of current slice
        sliceInfoHeaderLabel = tk.Label(self.root, text='Slice Info')
        sliceInfoHeaderLabel.pack(side=tk.TOP)        
                
        sliceInfoLabel = tk.Label(self.root, text = '')
        sliceInfoLabel.pack(side=tk.TOP)
        
        # Show information of whole volume
        volInfoHeaderLabel = tk.Label(self.root, text='Volume Info')
        volInfoHeaderLabel.pack(side=tk.TOP)
        
        volInfoStr = ''
        for volInfoKey in self.volInfo.keys():
            if volInfoKey.lower() != 'diceperslice':
                volInfoStr += volInfoKey + '\t' + str(self.volInfo[volInfoKey]) + '\n'
        volInfoLabel = tk.Label(self.root, text=volInfoStr)
        volInfoLabel.pack(side=tk.TOP)
        
        

        self.root.mainloop()


if __name__ == '__main__':
    vol = np.random.rand(1, 50, 128, 128, 1)
    volInfo = {
        'DicePerSlice': np.random.rand(50),
        'Seg Method': 'Graph Cut'
        }
    slicesInfo = [{'Dice': 0.5}]*50
    app = VolSlicer(vol, volInfo = volInfo, slicesInfo = slicesInfo)