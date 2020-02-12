import numpy as np
import sys
import matplotlib.pyplot as plt
import pandas as pd

def outlier_remove(data):
    
    col=list(data.columns.values.tolist())
    df = pd.DataFrame(data)
    df.columns = col
    df.head()

    threshold=3
    from scipy import stats
    z = np.abs(stats.zscore(df.iloc[:,:-1]))
    print("Rows where Zscore is greater than 3")
    print(np.where(z>threshold))

    df_o = df[(z < threshold).all(axis=1)]
    count=df.shape[0]-df_o.shape[0]
    print('Rows removed={}'.format(count))

def main():
    
    if len (sys.argv) <2 :
        print("Invalid number of arguements passed:atleast 1(source file name) and atmost two(source file name, destination file name) arguements are permitted")
        sys.exit (1)
   
    if len(sys.argv)>3:
        print("Invalid number of arguements passed:atleast 1(source file name) and atmost two(source file name, destination file name) arguements are permitted")
        sys.exit(1)    
    file=sys.argv[1]

    data=pd.read_csv(file)
    
    if(outlier_remove(data)==None):
        print("Successfully executed")
   
main()
    
    
    
