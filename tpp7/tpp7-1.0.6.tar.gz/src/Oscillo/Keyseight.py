import numpy as np
import pandas as pd
import scipy as sc
import matplotlib.pyplot as plt
import usbtmc
import uuid, os

from .Oscillo import _Oscillo
    

class Keyseight(_Oscillo):
    __version__ = 'Keyseight-1.0.0'
    
    modelDict = {
    }
            
    def __init__(self, device = None, ident = (None, None)):
        super().__init__(device, ident)
        ## Get Number of analog channels on scope
        IDN = self.instr.ask("*IDN?")
        ## Parse IDN
        IDN = IDN.split(',') # IDN parts are separated by commas, so parse on the commas
        MODEL = IDN[1]
        if list(MODEL[1]) == "9": # This is the test for the PXIe scope, M942xA)
            self.NUMBER_ANALOG_CHS = 2
        else:
            self.NUMBER_ANALOG_CHS = int(MODEL[len(MODEL)-2])
        
    def isActiveChannel(self, ch):
        return self.instr.ask(":STATus? {}".format(ch))=="1"
    
    
    def getChannelList(self):
        channelList = ["CHAN{}".format(ch+1) for ch in range(self.NUMBER_ANALOG_CHS)]
        channelList.append("MATH")
        channelList.append("FFT")
        #[channelList.append("MEM{}".format(ch+1)) for ch in range(self.NUMBER_ANALOG_CHS)]
        return channelList
    
    def getActiveChannelList(self):
        activeChannelList = [ ch for ch in self.getChannelList()  if self.isActiveChannel(ch) ]
        return activeChannelList
        
    
    def getChannelData(self, channel='CHAN1'): 
        self.instr.write(":WAVeform:SOURce {}".format(channel))
        # print(self.instr.ask(":WAVeform:POINts?"))
        self.instr.write(":WAVeform:FORMat WORD")
        self.instr.write(":WAVeform:BYTeorder LSBFirst")
        self.instr.write(":WAVeform:UNSigned 0")        
        
        tmp = self.instr.ask(":WAVeform:PREamble?")
        preamble = tmp.split(',')
        (format, type, points, count, xincr, xorg, xref, yincr, yorg, yref) = [eval(st) for st in preamble ]         
        self.instr.write(":WAVeform:DATA?")
        raw = self.instr.read_raw()
        Header = str(raw[0:12])
        startpos = Header.find("#")
        Size_of_Length = int(Header[startpos+1])
        Image_Size = int(Header[startpos+2:startpos+2+Size_of_Length])
        offset = startpos+2+Size_of_Length
        raw = raw[offset:offset+Image_Size-2]
        V = (np.frombuffer(raw, dtype=np.int16)-yref)*yincr+yorg
        t = (np.arange(0,len(V)) - xref) * xincr + xorg
        return (t,V)        
    
    def getHardcopy(self):
        self.instr.write(":SYSTEM:DSP")
        self.instr.write(":HARDCOPY:INKSAVER OFF")
        self.instr.write(":DISPlAY:DATA? PNG, COLOR")
        raw=self.instr.read_raw()
        Header = str(raw[0:12])
        startpos = Header.find("#")
        Size_of_Length = int(Header[startpos+1])
        Image_Size = int(Header[startpos+2:startpos+2+Size_of_Length])
        offset = startpos+Size_of_Length
        raw = raw[offset:offset+Image_Size]        
        filename = "/tmp/{}.bmp".format(uuid.uuid4())
        f = open(filename, "w+b")
        f.write(raw)
        f.close()
        im = plt.imread(filename)
        os.remove(filename)
        return im
       
