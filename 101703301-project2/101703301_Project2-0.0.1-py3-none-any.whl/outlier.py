import sys
import numpy as np
import logging

if(sys.argv[1] is None):
    logging.error("Input datafile missing!!")
    sys.exit()
    
if(sys.argv[2] is None):
    logging.error("Output datafile missing!!")
    sys.exit()


import pandas as pd
    
df=pd.read_csv(sys.argv[1])

cols=df.columns

lim=dict()
for col in cols:
    q1,q3=np.percentile(data[col],[25,75])
    iqr=q3-q1
    high=q3+(1.5*iqr)
    low=q1-(1.5*iqr)
    
    lim[col]=[low,high]
    


fg=np.ones(len(df))

for i in range(len(df)):
    if(fg[i]==1):
        for col in cols:
            if(df[col][i]<lim[col][0] or df[col][i]>lim[col][1]):
                fg[i]=0
                break
            
rows=list()

for i in range(len(fg)):
    if(fg[i]==1):
        rows.append(i)


new_data=df.iloc[rows,:]
new_data=new_data.reset_index(drop=True)
new_data.to_csv(sys.argv[2],index=False)