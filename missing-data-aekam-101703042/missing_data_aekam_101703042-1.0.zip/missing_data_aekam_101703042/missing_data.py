
@author: aekam
"""


import pandas as pd
import sys
from sklearn.impute import SimpleImputer

def missing_values(inputf,outputf):
    dataset=pd.read_csv(inputf)
    head=dataset.columns
    columns_null=dataset.columns[dataset.isnull().any()]
    print("Columns having null values are-",columns_null)
    for i in columns_null:
        null=dataset[i].isnull()
        count=sum(null)
        print(i," has ",count," missing values")
    imputer=SimpleImputer(strategy='median') 
    imputer.fit_transform(dataset)  
    data=pd.DataFrame(imputer.transform(dataset))  
    data.columns=head  
    data.to_csv(outputf,index=False)
    print("Success")


argList=sys.argv  
infile=argList[1]   
outfile=argList[2]  
missing_values(infile,outfile) 