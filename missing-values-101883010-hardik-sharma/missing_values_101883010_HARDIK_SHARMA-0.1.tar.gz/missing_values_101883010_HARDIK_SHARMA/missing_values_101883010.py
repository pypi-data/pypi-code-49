'''
Name    - HARDIK SHARMA
ROLL NO - 101883010
GROUP   - COE5
'''

#import sys
import pandas as pd

#filename = sys.argv[1]


def remove_rows(da, col):
    
    nr,nc=da.shape
    nor=[]    
    
    for row in range(0,nr):
        if (pd.isna(da.iloc[row,col])):
            nor.append(row)
                 
    da=da.drop(nor, axis = 0)
    nrr=da.shape[0]

    return da,nr-nrr,nor
    
    
def remove_missing_values(dataset):
    da=pd.read_csv(dataset)
    nr,nc=da.shape

    null_n = da.isnull().sum()
    co = 0
    for val in null_n.iteritems():
        if val[1] != 0:
            
            row=0
            for i in range(0,nr):
                if (pd.isna(da.iloc[i,co])):
                    continue
                else:
                    row = i
                    break
            
            
            if(type(da.iloc[row,co]) == str):
                da,norr,ror = remove_rows(da, co)
            else:
                da.fillna(da.mean(), inplace = True)
                
        co=co+1
        
    return da,norr,ror
    
#a,b,c=remove_missing_values("te.csv")
#print("Data after missing values removal = ",a)
#print("\n No of rows removed = ",b)
#print("\n Index of Rows Removed = ",c)