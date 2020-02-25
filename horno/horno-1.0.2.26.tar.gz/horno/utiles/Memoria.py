import psutil
from horno.utiles.Singleton import Singleton


#==========================================================================================
@Singleton
class Memoria (metaclass=Singleton):
    
    #------------------------------------------------------------------------------------------
    def GetInfoMem(self):
        return psutil.virtual_memory().total / 1024 ** 2
        
