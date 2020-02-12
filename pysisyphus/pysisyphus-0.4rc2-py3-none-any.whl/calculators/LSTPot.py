from pysisyphus.calculators.AnaPotBase import AnaPotBase

# See https://www.sciencedirect.com/science/article/pii/0009261477805745
# Fig. (1) and Eq. (1)

class LSTPot(AnaPotBase):

    def __init__(self): 
        V_str = "((x-y)**2 - (5/3)**2)**2 + 4*(x*y-4)**2 + x -y"
        x_lim = (0, 4)
        y_lim = (0, 4)
        super().__init__(V_str, x_lim, y_lim)

    def __str__(self):
        return "LSTPot calculator"
