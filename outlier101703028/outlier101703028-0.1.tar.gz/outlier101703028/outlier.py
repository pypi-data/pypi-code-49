import numpy as np
import pandas as pd
import csv
import sys
    
def outlier_removal(input,output):
    try:
        input_file=pd.read_csv(input)
    except:
        print("Input file doesn't exist or path is wrong")
    else:
        col=len(input_file.iloc[0,:])
        row=len(input_file.iloc[:,0])
        outliers=[]
        for i in range(col):
            data=input_file.iloc[:,i]
            mean=np.mean(data)
            std=np.std(data)
            for x in data:
                z_score=(x-mean)/std
                if np.abs(z_score)>3:
                    outliers.append(x)
        count=0
        with open(output,'w') as output_file:
            writer=csv.writer(output_file)
            for i in range(row):
                data=input_file.iloc[i,:]
                for x in data:
                    if x in outliers:
                        count+=1
                        break
                else:
                    writer.writerow(data)
        print(f'{count} no of rows are removed')


if __name__=="__main__":
    outlier_removal(sys.argv[1],sys.argv[2])

    

    

