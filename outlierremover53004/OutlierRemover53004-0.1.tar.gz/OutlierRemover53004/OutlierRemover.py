# -*- coding: utf-8 -*-
import pandas as pd
import sys
def removeOutlier(fileName):
    data = pd.DataFrame(pd.read_csv(fileName))
    
    noneed = []
    for i in range(0,len(data.index)):
        for j in range(0,len(data.columns)):
            q1 = data.iloc[:,j].quantile(q = 0.25)
            q2 = data.iloc[:,j].quantile(q = 0.75)
            if((data.iloc[i,j] < q1 or data.iloc[i,j] > q2) and (i not in noneed)):
                    noneed.append(i)
    
    data3 = data.drop(axis = 1, index = noneed)
    data3.to_csv("data.csv", index = False)
    
    print("New data is saved to file 'data.csv'\nUse 'newFile' attribute of this package for accessing it directly'")

newFile = 'data.csv'

if (__name__ == "__main__"):
    removeOutlier(sys.argv[1])
    


    