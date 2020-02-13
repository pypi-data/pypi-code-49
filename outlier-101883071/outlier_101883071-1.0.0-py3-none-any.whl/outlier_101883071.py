"""
Created on Mon Feb 10 12:26:50 2020

@author:Yogesh
"""

mport pandas as pd
import numpy as np
import csv
import sys
def main():
    try:
        file=open(sys.argv[1],"rb")
        dataframe=pd.read_csv(file)

        df=dataframe.iloc[:,:].values
        rows,cols=df.shape
        count=0
        data=list(dataframe)

        for i in range(0,cols):
           
            lis=[]
            dis=[]
            for j in range(0,df.shape[0]):
                lis.append(df[j][i])
               
            lis.sort()
            q1,q3=np.percentile(lis,[25,75])
            print(q1,q3)
            iqr=q3-q1
            for j in range(0,df.shape[0]):
                if (df[j][i]<q1-iqr*1.5) or (df[j][i]>q3+iqr*1.5):
                    count=count+1
                    dis.append(j)
            df=np.delete(df,dis,axis=0)
       
       
        with open(sys.argv[2],'w',newline='') as output_file:
             writer = csv.writer(output_file, dialect='excel')
             writer.writerow(data)
             np.savetxt(output_file, df, delimiter=",")
        output_file.close()
        print(" number of rows deleted:",count)
       
    except:
        print("Error: check input and output files should be in same directory")
