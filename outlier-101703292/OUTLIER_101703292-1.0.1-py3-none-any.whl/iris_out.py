import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data=pd.read_csv("Iris.csv")
x = data.iloc[:,:-1].values
y = data.iloc[:,-1:].values
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_y = LabelEncoder()
y= labelencoder_y.fit_transform(y)

col=list(data.columns.values.tolist())
df = pd.DataFrame(data)
df.columns = col
df.head()

threshold=3
from scipy import stats
z = np.abs(stats.zscore(df.iloc[:,:-1]))

print(np.where(z>threshold))

df_o = df[(z < threshold).all(axis=1)]
count=df.shape[0]-df_o.shape[0]
print(count)

