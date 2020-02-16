import pandas as pd

def outlier_row_removal(dataset,newdataset):
    #IMPORTING LIBRARIES
    import numpy as np
    import math
    
    dataset=pd.DataFrame(dataset)
    h = dataset.shape[0]
    #CALCULATING ROWS AND COLUMNS
    row_count=dataset.shape[0]
    col_count=dataset.shape[1]
    
    for i in range(0,col_count):
        x=list(dataset.columns)
        j=dataset.sort_values(by=x[i])
        y=j.iloc[:,i].values
        
        #CALCULATING ROWS AND COLUMNS
        row_count=dataset.shape[0]
        col_count=dataset.shape[1]
        
        #FINDING QUANTILES Q1 and Q3
        a=math.floor((row_count+1)/4)
        b=math.ceil((row_count+1)/4)
        Q1=(y[a-1]+y[b-1])/2
        
        d=math.floor(3*(row_count+1)/4)
        f=math.ceil(3*(row_count+1)/4)
        Q3=(y[d-1]+y[f-1])/2
        
        #FINDING IQR (INTER QUANTILE RANGE)
        IQR=Q3-Q1
        
        #FINDING MIN AND MAX
        MIN=Q1-1.5*IQR
        MAX=Q3+1.5*IQR
    
        for k in range(0,row_count):
            if y[k]<MIN:
                dataset = dataset.drop([k])
            if y[k]>MAX:
                dataset = dataset.drop([k])
        dataset.index = np.arange(0,len(dataset))
    print("No. of rows removed are:",h-dataset.shape[0])
    dataset.to_csv(newdataset)

import sys 
dataset=pd.read_csv(sys.argv[1]).values
newdataset=sys.argv[2]
outlier_row_removal(dataset,newdataset)


            