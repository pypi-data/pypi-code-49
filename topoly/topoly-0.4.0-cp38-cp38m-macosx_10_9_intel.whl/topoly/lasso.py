from .invariants import Invariant
from .topoly_surfaces import c_lasso_type, c_make_surface
from .params import SurfacePlotFormat, Bridges

class Lasso(Invariant):
    name = 'Lasso'
    def __init__(self, coordinates, loop_indices):
        if loop_indices:
            super().__init__(coordinates)
            self.loop_indices = loop_indices
        else:
            super().__init__(coordinates, bridge=Bridges.SSBOND)
#            self.loop_indices = 

    def make_surface(self, precision=0, density=1):   
        coordinates = self.get_coords()
        loop_beg, loop_end = self.loop_indices
        return c_make_surface(coordinates, loop_beg, loop_end, precision, density)

    def lasso_type(self, smoothing=0, step=1, precision=0, dens=1, 
                   min_dist=[10,3,10], pic_files=SurfacePlotFormat.DONTPLOT, 
                   output_prefix='', output_type=1): 
        coordinates = self.get_coords()
        if pic_files == None:                                                        
            pic_files = 0                                                            
        elif type(pic_files) == int:                                                 
            pass                                                                     
        elif type(pic_files) == list:                                                
            summ = 0                                                                 
            for ext in pic_files:                                                    
                summ += ext                                                          
            pic_files = summ                                                         
        pic_files = int(bin(pic_files)[2:])
        if type(self.loop_indices[0]) == int:
            return c_lasso_type(coordinates, self.loop_indices[0], 
                      self.loop_indices[1], smoothing, step, precision, dens, 
                      min_dist[0], min_dist[1], min_dist[2], pic_files, 
                      output_prefix.encode('utf-8'), output_type).decode('UTF-8')
        if type(self.loop_indices[0]) == list:
            results = []
            for index in self.loop_indices:
                res = c_lasso_type(coordinates, index[0], index[1], smoothing, 
                          step, precision, dens, min_dist[0], min_dist[1], 
                          min_dist[2], pic_files, output_prefix.encode('utf-8'),
                          output_type).decode('UTF-8')
                res = 'loop {}-{}: {}'.format(index[0], index[1], res)
                results.append(res)
            return ''.join(results)
