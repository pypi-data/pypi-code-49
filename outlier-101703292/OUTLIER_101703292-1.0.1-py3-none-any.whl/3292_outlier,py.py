import numpy as np
import sys
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_boston
boston = load_boston()
x = boston.data
y = boston.target
columns = boston.feature_names

boston_df = pd.DataFrame(boston.data)
boston_df.columns = columns
boston_df.head()

threshold=3
from scipy import stats
z = np.abs(stats.zscore(boston_df))
print(z)
print(np.where(z>threshold))

boston_df_o = boston_df[(z < threshold).all(axis=1)]
count=boston_df.shape[0]-boston_df_o.shape[0]
print(count)





    
    