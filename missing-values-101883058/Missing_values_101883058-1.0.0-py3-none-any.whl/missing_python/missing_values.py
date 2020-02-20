#importing libraries
import numpy as np
import pandas as pd
import sys
from sklearn.impute import SimpleImputer

def missing(dataset):
   
    if dataset.shape[0]==0:
        return print("empty dataset")
    else:
        X=dataset.iloc[:,0:3].values
        imputer = SimpleImputer(missing_values = np.nan, strategy = "median")
        imputer = imputer.fit(X[:, 0:3])
        X[:,0:3 ] = imputer.fit_transform(X[:, 0:3]) 
        file={'a':X[:,0],'b':X[:,1],'c':X[:,2]}
        df=pd.DataFrame(file)
        df.to_csv('new.csv')

def main():
    if len(sys.argv)!=2:
        print("Incorrect parameters.Input format:python <programName> <InputDataFile>")
        exit(1)
    else:
        data=pd.read_csv(sys.argv[1]) 
        missing(data)

if __name__ == "__main__":
    main()

