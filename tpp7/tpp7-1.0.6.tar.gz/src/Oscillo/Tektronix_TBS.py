from .Tektronix import Tektronix
    

class TBS(Tektronix):
    __version__ = 'TBS-1.0.0'

    modelDict = {
        "1064": (0x0699, 0x03b3),
    }

    def __init__(self, device = None, ident = (None, None), model= None):
        if model is None:
            super().__init__(device, ident)
            return
        if model in self.modelDict:
            super().__init__(ident = self.modelDict[model])
            return
        
        print('Liste des modèmles de '+self.__class__.__name__+' référencés')
        print(self.modelDict)
        raise NameError("le modèle {} n'est pour le moment pas référencé".format(model))
        
