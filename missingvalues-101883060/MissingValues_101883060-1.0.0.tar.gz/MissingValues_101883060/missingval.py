import numpy as np 
import pandas as pd 
import sys 

def replace_values(data):
    try:
        data=pd.read_csv(sys.argv[1])

        for i in data.columns:
            sum=0
            for count in data[i].values:
                if(not np.isnan(count)):
                    sum=sum+count
            sum=sum/len(data[i].values)
            
            for j,k in enumerate(data[i].values):
                if(np.isnan(k)):
                    data[i][j]=sum
        return data
    except:
        print('Error!')

def main():
    filename=sys.argv[1]
    try:
        data=pd.read_csv(filename)
    except OSError:
        print('Cannot open ',filename)
        sys.exit(0)
    
    data=replace_values(data)

    try:
        data.to_csv("Output.csv",index=False)
    
    except OSError:
        print('Cannot open ',filename)
        sys.exit(0)
    
if __name__=="__main__":
    main()