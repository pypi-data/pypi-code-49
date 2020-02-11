import numpy as np
import pandas as pd
import sys
import logging

if(sys.argv[1] is None):
    logging.error("Input datafile missing!!")
    sys.exit()
    
if(sys.argv[2] is None):
    logging.error("Output datafile missing!!")
    sys.exit()
    
data=pd.read_csv(sys.argv[1])

cols=data.columns

limits=dict()
for col in cols:
    q1,q3=np.percentile(data[col],[25,75])
    iqr=q3-q1
    low=q1-(1.5*iqr)
    high=q3+(1.5*iqr)
    limits[col]=[low,high]
    
    
fg=np.ones(len(data))
for i in range(len(data)):
    if(fg[i]==1):
        for col in cols:
            if(data[col][i]<limits[col][0] or data[col][i]>limits[col][1]):
                fg[i]=0
                break
cnt=0            
rows=list()
for i in range(len(fg)):
    if(fg[i]==1):
        rows.append(i)
    else:
        cnt+=1
        
new_data=data.iloc[rows,:]
new_data=new_data.reset_index(drop=True)
print("No of rows removed:",cnt)
new_data.to_csv(sys.argv[2],index=False)