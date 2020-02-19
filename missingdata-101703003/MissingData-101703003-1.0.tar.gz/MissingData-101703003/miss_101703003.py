import pandas as pd
import sys
import numpy as np
from sklearn.impute import SimpleImputer

def miss_values(dataframe,newdataset):
    df=pd.read_csv(dataframe)
    cols=df.columns
    null_col=df.columns[df.isnull().any()] 
    print("Null vaued columns: ",null_col)
    for itr in null_col:
        nullcell=df[itr].isnull()
        count=sum(nullcell)
        print(itr," has ",count," missing values")
    imputer=SimpleImputer(strategy='mean') 
    imputer.fit_transform(df) 
    data=pd.DataFrame(imputer.transform(df))  
    data.columns=cols 
    data.to_csv(newdataset)
    print("New file generated")
    

argList=sys.argv 
df=argList[1]
newdataset=argList[2] 
missing_values(df,newdataset) 