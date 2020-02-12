import pandas as pd
import sys
import numpy as np
     
def delete_outliers(data):
    try:
        count = 0
        for i in data.columns:
            sorted_column = sorted(data[i].values)
            Q1 = sorted_column[int(len(sorted_column)/4)]
            Q3 = sorted_column[int(len(sorted_column)*3/4)]
            IQR = Q3-Q1
            for j,k in enumerate(data[i].values):
                if(k < Q1 -(1.5 * IQR) or k > Q3 + (1.5 * IQR)):
                    try:
                        data = data.drop([data.index[j]])
                        count = count+1
                    except:
                        pass
        return data,count
    except:
        print("Make sure you don't have any categorical data")       




def main():
    filename = sys.argv[1]
    try:
        data = pd.read_csv(filename)
    except OSError:
        print('cannot open', filename)
        sys.exit(0)
        
    data,count = delete_outliers(data)

    try:
        data.to_csv("out.csv",index=False)
        print("number of rows deleted: ",count)    
    except OSError:
        print('cannot open', filename)
        sys.exit(0)
        
if __name__=="__main__":
    main()