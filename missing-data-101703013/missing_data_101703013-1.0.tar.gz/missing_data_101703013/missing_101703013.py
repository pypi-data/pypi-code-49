import pandas as pd
import sys
import numpy as np
from sklearn.impute import SimpleImputer
def missing_values(df,newdataset):
    dataset=pd.read_csv(df)
    head=dataset.columns
    cols_null=dataset.columns[dataset.isnull().any()] 
    print("Columns having null values are-",cols_null)
    for target in cols_null:
        null_cells=dataset[target].isnull()
        count=sum(null_cells)
        print(target," has ",count," missing values")
    imputer=SimpleImputer(strategy='mean') 
    imputer.fit_transform(dataset) 
    data=pd.DataFrame(imputer.transform(dataset))  
    data.columns=head 
    data.to_csv(newdataset)
    print("New file generated")
    

argList=sys.argv 
df=argList[1]
newdataset=argList[2] 
missing_values(df,newdataset) 