import pandas as pd
import sys
import numpy as np
     
def delete_outliers(data):
    try:
        data = pd.read_csv(sys.argv[1])

        for i in data.columns:
            sum = 0
            for t in data[i].values :
                if(not np.isnan(t)):
                    sum = sum + t
            sum = sum/len(data[i].values)
            for j,k in enumerate(data[i].values):
                if np.isnan(k) :
                    data[i][j] = sum
        return data
    except:
        print("Make sure you don't have any categorical data")   




def main():
    if(len(sys.argv)<2):
        print("Usage:-  python test.py Data.csv")
        sys.exit(0)
    filename = sys.argv[1]
    try:
        data = pd.read_csv(filename)
    except OSError:
        print('cannot open', filename)
        sys.exit(0)
        
    data = delete_outliers(data)

    try:
        data.to_csv("out.csv",index=False)   
    except OSError:
        print('cannot open', filename)
        sys.exit(0)
        
if __name__=="__main__":
    main()