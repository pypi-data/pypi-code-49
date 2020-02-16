import topsis_new as tp
import pandas as pd
import numpy as np
dataset= tp.topsis("data.csv")

weights=[1,2,1,1]
impacts=["+","+","-","+"]
result =tp.topsis.evaluate(dataset,weights,impacts)
x = result
seq = sorted(x)
index = [seq.index(v)+1 for v in x]

print(index)
