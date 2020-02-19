import pandas as pd
import sys

def rem_out(data):
    if data.shape[0] == 0:
        return print("Error! Empty Dataset")
    lb=list()
    ub=list()
    q=data.quantile([0.25,0.75],axis=0)
    r=data.shape[0]
    c=data.shape[1]
    for i in range(c):
        q1,q3=q.iloc[0,i],q.iloc[1,i]
        iqr=q3-q1
        l=q.iloc[0,i]-(1.5*iqr)
        u=q.iloc[1,i]+(1.5*iqr)
        lb.append(l)
        ub.append(u)
    out_row=list()
    for i in range(r):
        for j in range(c):
            if((data.iloc[i,j]<lb[j])or(data.iloc[i,j]>ub[j])):
                out_row.append(i)
                break
    newdata = data.drop(out_row)    
    print("Total outlier rows are: ",len(out_row))
    return newdata    

def main():
    if len(sys.argv)!=3:
        print("Incorrect input! Input Format: python outlier.py <inputFile> <outputFile>")
        exit(1)
    else:
        data=pd.read_csv(sys.argv[1])
        rem_out(data).to_csv(sys.argv[2], index=False)

if __name__ == "__main__":
    main()
        
