import pandas as pd

def outlierRowRemoval(dtst,newdtst):
    #IMPORTING LIBRARIES
    import numpy as np
    import math
    
    dtst=pd.DataFrame(dtst)
    h = dtst.shape[0]
    #CALCULATING ROWS AND COLUMNS
    row_cnt=dtst.shape[0]
    col_cnt=dtst.shape[1]
    
    for i in range(0,col_cnt):
        x=list(dtst.columns)
        j=dtst.sort_values(by=x[i])
        y=j.iloc[:,i].values
        
        #CALCULATING ROWS AND COLUMNS
        row_cnt=dtst.shape[0]
        col_cnt=dtst.shape[1]
        
        #FINDING QUANTILES Q1 and Q3
        a=math.floor((row_cnt+1)/4)
        b=math.ceil((row_cnt+1)/4)
        Q1=(y[a-1]+y[b-1])/2
        
        d=math.floor(3*(row_cnt+1)/4)
        f=math.ceil(3*(row_cnt+1)/4)
        Q3=(y[d-1]+y[f-1])/2
        
        #FINDING IQR (INTER QUANTILE RANGE)
        IQR=Q3-Q1
        
        #FINDING MIN AND MAX
        MIN=Q1-1.5*IQR
        MAX=Q3+1.5*IQR
    
        for k in range(0,row_cnt):
            if y[k]<MIN:
                dtst = dtst.drop([k])
            if y[k]>MAX:
                dtst = dtst.drop([k])
        dtst.index = np.arange(0,len(dtst))
    print("No. of rows removed are:",h-dtst.shape[0])
    dtst.to_csv(newdtst)

import sys 
dtst=pd.read_csv(sys.argv[1]).values
newdtst=sys.argv[2]
outlier_row_removal(dtst,newdtst)


            