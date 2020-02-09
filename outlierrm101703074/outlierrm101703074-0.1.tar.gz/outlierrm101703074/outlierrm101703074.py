import pandas as pd
import sys
import numpy as np

filename = sys.argv[1]
#filename = 'outlier.csv'

def iqr_row_removal(filename):
    
    data = pd.read_csv(filename)
    nrows, ncols = data.shape
    
    data2 = [[val for val in data[col]] for col in data]
    data2.insert(0,list(data.keys()))
    
    for num in range(1, ncols+1):
        if(type(data2[num][0]) != int and type(data2[num][0]) != float):
            data = data.drop(data2[0][num-1], axis=1)
    ncols = data.shape[1]
    
    
    
    row_hash = [0] * nrows
    for i in range(ncols):
        col = data.iloc[:,i]
        
        q25, q75 = np.percentile(col, [25,75])
        iqr = q75 - q25
        
        lower_bound = q25 - (iqr * 1.5)
        upper_bound = q75 + (iqr * 1.5)
        for row in range(nrows):
            if (data.iloc[row,i] < lower_bound or data.iloc[row,i] > upper_bound):
                row_hash[row] = 1
            
            
            
    inds = []
    for row in range(nrows):
        if(row_hash[row]):
            inds.append(row)

    data = data.drop(inds, axis = 0)
    nrows2 = data.shape[0]
    print('No. of rows removed by IQR method: ',nrows-nrows2)
    return data
    
    
def zscore_row_removal(filename, threshold = 2):
    
    data = pd.read_csv(filename)
    nrows, ncols = data.shape
    
    data2 = [[val for val in data[col]] for col in data]
    data2.insert(0,list(data.keys()))
    
    for num in range(1, ncols+1):
        if(type(data2[num][0]) != int and type(data2[num][0]) != float):
            data = data.drop(data2[0][num-1], axis=1)
    ncols = data.shape[1]
    
    
    
    row_hash = [0] * nrows
    for i in range(ncols):
        col = data.iloc[:,i]
        
        mean1 = np.mean(col)
        std_dev = np.std(col)
        for row in range(nrows):
            z_score = (data.iloc[row,i] - mean1)/std_dev
            
            if abs(z_score) > threshold:
                row_hash[row] = 1
    
    
    
    inds = []
    for row in range(nrows):
        if(row_hash[row]):
            inds.append(row)

    data = data.drop(inds, axis = 0)
    nrows2 = data.shape[0]
    print('No. of rows removed by z-score method: ',nrows-nrows2)
    return data
    
    
    
print(iqr_row_removal(filename))
print(zscore_row_removal(filename))