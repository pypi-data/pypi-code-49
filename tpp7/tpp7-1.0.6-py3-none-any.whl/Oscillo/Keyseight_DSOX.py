from .Keyseight import Keyseight


class DSOX(Keyseight):
    __version__ = 'DSOX-1.0.0'

    modelDict = {
        "1102A": (0x2a8d, 0x1787),
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
        
