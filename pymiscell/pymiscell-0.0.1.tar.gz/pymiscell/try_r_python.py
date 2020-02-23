import pandas as pd
from rpy2.robjects.packages import importr
from rpy2.robjects import r as R

utils = importr('rsm')
print(utils.__rdata__)
print(type(R('pi')[0]))
ChemReact = R['ChemReact']
print(ChemReact)
print(type(ChemReact))

bbd = R['bbd']
print(bbd(3, 2)[5])
