import pandas as pd

def outlier_row_removal(data,newdata):
    #IMPORTING LIBRARIES
    import numpy as np
    import math
    
    data=pd.DataFrame(data)
    #CALCULATING ROWS AND COLUMNS
    row_cont=data.shape[0]
    col_cont=data.shape[1]
    
    for i in range(0,col_cont):
        x=list(data.columns)
        j=data.sort_values(by=x[i])
        y=j.iloc[:,i].values
        
        #CALCULATING ROWS AND COLUMNS
        row_cont=data.shape[0]
        col_cont=data.shape[1]
        
        #FINDING QUANTILES Q1 and Q3
        a=math.floor((row_cont+1)/4)
        b=math.ceil((row_cont+1)/4)
        Q1=(y[a-1]+y[b-1])/2
        
        d=math.floor(3*(row_cont+1)/4)
        f=math.ceil(3*(row_cont+1)/4)
        Q3=(y[d-1]+y[f-1])/2
        
        #FINDING IQR (INTER QUANTILE RANGE)
        Iqr=Q3-Q1
        
        #FINDING MIN AND MAX
        MIN=Q1-1.5*Iqr
        MAX=Q3+1.5*Iqr
    
        for k in range(0,row_cont):
            if y[k]<MIN:
                data = data.drop([k])
            if y[k]>MAX:
                data = data.drop([k])
        data.index = np.arange(0,len(data))
                
    data.to_csv(newdata)

import sys 


data=pd.read_csv(sys.argv[1]).values
newdata=sys.argv[2]
outlier_row_removal(data,newdata)
    
