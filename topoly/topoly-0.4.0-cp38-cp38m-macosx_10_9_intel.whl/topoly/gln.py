from .graph import Graph
from topoly.topoly_gln import c_gln, c_gln_max, c_gln_average, c_gln_matrix

class GLN(Graph):
    name = "GLN"
    def __init__(self, chain1, chain2, indices1=(-1,-1), indices2=(-1,-1)):
        super().__init__(chain1)
        self.orig_input2 = chain2                                              
        if type(chain2) is str and os.path.isfile(chain2):                 
            with open(chain2, 'r') as myfile:                                 
                chain2 = myfile.read()                                        
        self.chain2 = chain2                                               
        data2 = InputData.read_format(self.chain2, self.orig_input2, chain,
                                      bridges, breaks, debug)
        self.coordinates2 = data2['coordinates']
        self.ndx1 = indices1
        self.ndx2 = indices2
        self.chain1_list = self.get_coords()
        self.chain2_list = self.coords2list(self.coordinates2)
    
    def gln(self):
        return c_gln(self.chain1_list, self.chain2_list, self.ndx1[0],
                     self.ndx1[1], self.ndx2[0], self.ndx2[1])

    def gln_max(self, density = -1, precision = 3):
        return c_gln_max(self.chain1_list, self.chain2_list, self.ndx1[0],
                         self.ndx1[1], self.ndx2[0], self.ndx2[1], density,
                         precision)
                                                                                     
    def gln_average(self, tryamount = 200):
        return c_gln_average(self.chain1_list, self.chain2_list, self.ndx1[0],
                             self.ndx1[1], self.ndx2[0], self.ndx2[1], tryamount)

    def gln_matrix(self):
        return c_gln_matrix(self.chain1_list, self.chain2_list, self.ndx1[0],
                            self.ndx1[1], self.ndx2[0], self.ndx2[1])
