from queue import Queue
from threading import Thread

from horno.utiles.Singleton import Singleton


#===================================================================================================
class ThreadManager (metaclass=Singleton):

    #------------------------------------------------------------------------------------------
    def __init__(self):

        self.cur_threads = 0
        self.max_threads = 1
        self.cola = Queue()

    #------------------------------------------------------------------------------------------
    def SetMaxThreads(self, valor):
        
        self.max_threads = valor

    #------------------------------------------------------------------------------------------
    def EjecutarProcesoBloqueante(self, func, params):

        self.Worker(func, params)

    #------------------------------------------------------------------------------------------
    def EncolarProceso(self, func, params, lanzar=True):

        if self.max_threads <= 1:
            
            self.Worker(func, params)
            
        else:

            t = Thread(target=self.Worker, args=(func, params))
            self.cola.put(t)
            if lanzar:
                self.LanzarProximoProceso()
        
    #------------------------------------------------------------------------------------------
    def LanzarProximoProceso(self):
        
        if not self.cola.empty() and self.cur_threads < self.max_threads:
            t = self.cola.get() 
            t.start()

    #------------------------------------------------------------------------------------------
    def EsperarFin(self):

        while not self.cola.empty() or self.cur_threads > 0:
            self.LanzarProximoProceso()
            pass

    #------------------------------------------------------------------------------------------
    def Worker(self, func, params):

        self.cur_threads = self.cur_threads+1
        try:
            func(*params)
        except Exception as e:
            print('%s: %s' % (str(type(e)), str(e)))
        finally:
            self.cur_threads = self.cur_threads-1
