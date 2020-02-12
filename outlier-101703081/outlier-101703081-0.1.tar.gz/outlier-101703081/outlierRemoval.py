import sys
import pandas as pd
import numpy as np

def remove_outlier(dataset,file="Final.csv"):
    data=pd.read_csv(dataset)
    x=data.iloc[:,:-1].values
    y=data.iloc[:,-1].values
    numOutliers=0
    outliers=[]
    initialRows=x.shape[0]
    
    for i in range(np.shape(x)[1]):
        temp=[]
        for j in range(np.shape(x)[0]):
            temp.append(x[j][i])
        Q1,Q3=np.percentile(temp,[25,75])
       
        iqr=Q3-Q1
        min=Q1-(1.5*iqr)
        max=Q3+(1.5*iqr)
        for j in range(0,np.shape(x)[0]):
            if(x[j][i]<min or x[j][i]>max):
                numOutliers+=1
                outliers.append(j)
                
        x=np.delete(x,outliers,axis=0)
        y=np.delete(y,outliers,axis=0)
    
    finalRows=x.shape[0]
    deleted=initialRows - finalRows
    col=list(data.columns)
    
    print('Rows removed={}'.format(deleted))
    
    newdata={}
    j=0
    for i in range(len(col)-1):
        newdata[col[i]]=x[:,j]
        j+=1
        
    newdata[col[len(col)-1]]=y
    new=pd.DataFrame(newdata)    
    new.to_csv(file,index=False)

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
        
        