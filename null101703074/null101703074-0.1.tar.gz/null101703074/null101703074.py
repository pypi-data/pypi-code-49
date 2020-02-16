import sys
import pandas as pd

filename = sys.argv[1]


def remove_row(data, col):
    
    nrows, ncols = data.shape
    inds = []     
    for row in range(0,nrows):
        if (pd.isna(data.iloc[row,col])):
            inds.append(row)
                 
    print('Rows removed: ', inds)
    data = data.drop(inds, axis = 0)
    nrows2 = data.shape[0]
    print('No. of rows removed: ',nrows-nrows2)
    return data
    
    
def replace_null_val(filename):
    data = pd.read_csv(filename)
    nrows, ncols = data.shape

    null_n = data.isnull().sum()
    col = 0
    for val in null_n.iteritems():
        if val[1] != 0:  #if column has null values
            
            row=0 # find first non-null value in column
            for i in range(0,nrows):
                if (pd.isna(data.iloc[i,col])):
                    continue
                else:
                    row = i
                    break
            
            
            # replace with previous value in categorical column
            if(type(data.iloc[row,col]) == str):
                data = remove_row(data, col)
            else: # replace with mean in numeric column
                data.fillna(data.mean(), inplace = True)
                
        col = col+1
        
    return data
    
            
replace_null_val(filename)