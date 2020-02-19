from .invariants import Invariant
from .topoly_surfaces import c_lasso_type, c_make_surface
from .params import *

class Lasso(Invariant):
    name = 'Lasso'
    def __init__(self, coordinates, loop_indices):
        if loop_indices:
            super().__init__(coordinates)
            self.loop_indices = loop_indices
        else:
            super().__init__(coordinates, bridges=Bridges.SSBOND)
#            self.loop_indices = 

    def make_surface(self, precision=PrecisionSurface.HIGH, density=DensitySurface.MEDIUM, precision_output = 3):   
        coordinates = self.get_coords()
        loop_beg, loop_end = self.loop_indices
        surf = c_make_surface(coordinates, loop_beg, loop_end, precision, density)
        for T in surf:
	#T = {'A': {'x': 1.0, 'y': 2.0, 'z': 3.0}, 'B': {'x': 1.9123684942681682, 'y': 2.067676947660268, 'z': 3.735203234274578}, 'C': {'x': 2.0, 'y': 2.0, 'z': 5.0}}
        	for P,coord in T.items(): 
        		for ax in coord: coord[ax] = round(coord[ax],precision_output)        
        return surf


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
