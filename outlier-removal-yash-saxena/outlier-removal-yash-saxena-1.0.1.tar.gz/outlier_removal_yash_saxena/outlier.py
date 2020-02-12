import sys

import pandas as pd
import numpy as np

def remove_outlier(Infile,Outfile="Output.csv"):
    dataset=pd.read_csv(Infile)
    X=dataset.iloc[:,:-1].values
    Y=dataset.iloc[:,-1].values
    outliers_present=0
    outliers=[]
    initial_rows=X.shape[0]
    
    for i in range(np.shape(X)[1]):
        temp=[]
        for j in range(np.shape(X)[0]):
            temp.append(X[j][i])
        Q1,Q3=np.percentile(temp,[25,75])
       
        IQR=Q3-Q1
        lower=Q1-(1.5*IQR)
        upper=Q3+(1.5*IQR)
        for j in range(0,np.shape(X)[0]):
            if(X[j][i]<lower or X[j][i]>upper):
                outliers_present+=1
                outliers.append(j)
        X=np.delete(X,outliers,axis=0)
        Y=np.delete(Y,outliers,axis=0)
    
    final_rows=X.shape[0]
    deleted=initial_rows-final_rows
    col=list(dataset.columns)
    
    
    
    print('Rows removed={}'.format(deleted))
    
    
    
    newdata={}
    j=0
    for i in range(len(col)-1):
        newdata[col[i]]=X[:,j]
        j+=1
        
    newdata[col[len(col)-1]]=Y
        
    
    
    new=pd.DataFrame(newdata)
    
    
    new.to_csv(Outfile,index=False)

def main():
    if len (sys.argv) <2 :
        print("Invalid number of arguements passed:atleast 1(source file name) and atmost two(source file name, destination file name) arguements are permitted")
        sys.exit (1)
    
    if len(sys.argv)>3:
        print("Invalid number of arguements passed:atleast 1(source file name) and atmost two(source file name, destination file name) arguements are permitted")
        sys.exit(1)    
    
    file1=sys.argv[1]
    final=""
    if len(sys.argv)==3:
        final=sys.argv[2]
    else:
        final="OutlierRemoved"+file1
        
    if(remove_outlier(file1,final)==None):
        print("Successfully executed")

        
if __name__=='__main__':
    
   main()