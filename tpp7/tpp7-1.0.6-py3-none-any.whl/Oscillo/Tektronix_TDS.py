from .Tektronix import Tektronix


class TDS(Tektronix):
    __version__ = 'TDS-1.0.0'

    modelDict = {
        "1001B": (0x0699, 0x0362),
        "1001C-EDU": (0x0699, 0x03aa),
        "2004B": (0x0699, 0x0365),
        "2024B": (0x0699, 0x036a), # Non testé
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
        
