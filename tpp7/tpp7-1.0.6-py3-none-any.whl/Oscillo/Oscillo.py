import usbtmc
import matplotlib.pyplot as plt


class Oscillo:
    __version__ = "1.1.0-0"

    def openKeyseightDevice(device, model):
        
        if (serie == 'DSO-X'):
            return DSOX(device)
        raise NameError('Série {} de Keyseight non géré'.format(serie))

    
    def openDevice(device):
        from .Tektronix_TDS import TDS
        from .Tektronix_TBS import TBS
        from .Keyseight_DSOX import DSOX

        (vendor, model) = usbtmc.Instrument(device).ask('*IDN?').split(',')[0:2]
        (serie, model) = model.split(' ')
        if vendor == 'TEKTRONIX':
            if serie == 'TDS':
                return TDS(device)
            if serie == 'TBS':
                return TBS(device)
            raise NameError('Série {} de Keyseight non géré'.format(serie))
        if vendor == 'KEYSIGHT TECHNOLOGIES':
            if (serie == 'DSO-X'):
                return DSOX(device)
            raise NameError('Série {} de Keyseight non géré'.format(serie))
        raise NameError('Vendeur {} non géré'.format(vendor))
        
    def getVersion():
        return Oscillo.__version__

    def getDeviceList():
        devList = usbtmc.list_devices()
        return devList
    
    def getDeviceListId(devList):
        IdList = [usbtmc.Instrument(dev).ask('*IDN?') for dev in devList]
        return IdList
    
    
class _Oscillo:
    __version__ = "0.0.1-0"
    
    colorList = ('orange', 'lightgreen', 'blue', 'lightpink', 'lightcoral')
    rightDec = (0.95, 0.90, 0.75, 0.65, 0.60)
    axesDec =  (0.00, 0.00, 0.20, 0.20, 0.20)
    
    def getVersion(self):
        return self.__version__
    
    def __init__(self, device = None, ident = (None, None), model= None):
        """ Initialisation de l'instrument
        
            utilisation :
            devList = Oscillo.getDeviceList()            
            osc = Oscillo(ident=(0x0699, 0x03aa))
            ou
            osc = Oscillo(devList[0])
            
        """
        if device is None:
            self.instr =  usbtmc.Instrument(ident[0], ident[1]) 
        else:
            self.instr = usbtmc.Instrument(device)            
        
        
    def getId(self):
        return self.instr.ask('*IDN?')
            
    def getChannelList(self):
        raise NameError("getChannelList n'est pas encore implémenté pour cet oscilloscope")

    def getActiveChannelList(self):
        raise NameError("getActiveChannelList n'est pas encore implémenté pour cet oscilloscope")
        
    def getHardcopy(self):
        raise NameError("getHardcopy n'est pas encore implémenté pour cet oscilloscope")
        
    def getChannelData(self):
        raise NameError("getChannelData n'est pas encore implémenté pour cet oscilloscope")
        
    def getChannelListData(self, channelList):
        res = {}
        for channel in channelList:
            (t, V) = self.getChannelData(channel)        
            if 't' not in res:
                res['t'] = t
            res[channel]= V
        return res
            
    
    def plotData(self, data):
        axesIndex = len(data)-1;
        fig, ax = plt.subplots(1,1)
        fig.subplots_adjust(right=self.rightDec[axesIndex])
        count = 0;
        for ch in data:
            if ch == 't':
                t = data['t']
            else:
                if count > 0:
                    tax = ax.twinx()
                else:
                    tax = ax 

                tax.plot(t, data[ch], color=self.colorList[count], linestyle='solid')
                tax.set_xlabel('time (s)')
                tax.set_ylabel(ch, color=self.colorList[count])
                tax.tick_params(axis='y', colors=self.colorList[count])
                if count>0:
                    tax.spines['right'].set_position(('axes', 1.0+(count-1)*self.axesDec[axesIndex]))
                count += 1

                tax.set_frame_on(True)
                tax.patch.set_visible(False)
        
