import pandas as pd #Importing pandas
import numpy as np  #Importing numpy
import math         #Importing math

def row_removal_outlier(dataset,ndataset):
    import numpy as np
    import math
    
    dataset=pd.DataFrame(dataset)
    total_row=dataset.shape[0] #Total number of rows
    total_col=dataset.shape[1] #Total number of columns
    
    for i in range(0,total_col):
        x=list(dataset.columns)
        j=dataset.sort_values(by=x[i])
        y=j.iloc[:,i].values
        
        total_row=dataset.shape[0]
        total_col=dataset.shape[1]
        
        x1=math.floor((total_row+1)/4)
        x2=math.ceil((total_row+1)/4)
        q1=(y[x1-1]+y[x2-1])/2  #Calculating quartile q1
        
        x3=math.floor(3*(total_row+1)/4)
        x4=math.ceil(3*(total_row+1)/4)
        q3=(y[x3-1]+y[x4-1])/2  #Calculating quartile q3
        
        IQR=q3-q1 #Calculating inter quantile range
        
        low=q1-1.5*IQR  #Calculating lower range
        upp=q3+1.5*IQR  #Calculating upper range
    
        for k in range(0,total_row):
            if y[k]<low:
                dataset = dataset.drop([k])
            if y[k]>upp:
                dataset = dataset.drop([k])
        dataset.index = np.arange(0,len(dataset))
    dataset.to_csv(ndataset)

import sys

def main():
    dataset=pd.read_csv(sys.argv[1]).values
    ndataset=sys.argv[2]
    row_removal_outlier(dataset,ndataset)
    
if __name__=="__main__":
     main()

            
