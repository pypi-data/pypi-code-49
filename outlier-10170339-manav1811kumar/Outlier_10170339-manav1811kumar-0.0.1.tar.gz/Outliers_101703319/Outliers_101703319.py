import sys
import pandas as pd
import csv
import numpy as np
import math
import os

def getPercentQuartile(D, per):
    data = sorted(np.copy(D))
    index = (per/100.00)*(len(data)-1)
    ele = data[math.floor(index)] + (data[math.ceil(index)] - data[math.floor(index)])*(math.modf(index)[0])
    return ele

df = pd.read_csv(sys.argv[1])
df.drop(df.columns[0], axis = 1, inplace = True)
D = df.iloc[:,:].values
Rows_To_Removed = np.zeros(len(D))
for i in range(D.shape[1]):
    data = np.copy(D[:,i])
    quart1 = getPercentQuartile(data, 25)
    quart3 = getPercentQuartile(data, 75)
    IQR = (quart3 - quart1)
    lower_bound = quart1 - IQR*1.5
    upper_bound = quart3 + IQR*1.5
    select_rows = (data >= lower_bound)*(data <= upper_bound)
    Rows_To_Removed[np.where(select_rows == False)[0]] = 1
indices = np.where(Rows_To_Removed == 1)[0]
df.drop(indices, inplace = True)
df.reset_index(inplace = True)
df.drop('index', axis = 1, inplace = True)

final_path = os.getcwd() + '/' + sys.argv[2]

df.to_csv(final_path)

