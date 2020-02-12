import pandas as pd
   

def topsis(dataset,weights,maxmin):
    #importing libraries
    import numpy as np
    import math as m
    

    #dataset into float
    a=dataset.astype(dtype='float')
    

    #calculating no. of rows and no. of columns
    row_count=a.shape[0]
    col_count=a.shape[1]
    

    #normalizing matrix
    for j in range(0,col_count):
        s=0
        for i in range(0,row_count):
            s=s+a[i,j]*a[i,j]
        s=m.sqrt(s)
        for i in range(0,row_count):
            a[i,j]=a[i,j]/s
    

    #multiplying by weights
    for j in range(0,col_count):
        for i in range(0,row_count):
            a[i,j]=a[i,j]*weights[j]
    

    #calculating vj+ and vj-
    v_best=[]
    v_worst=[]
    for j in range(0,col_count):
        if(maxmin[j]=='+'):
            v_best.append(max(a[:,j]))
            v_worst.append(min(a[:,j]))
        elif(maxmin[j]=='-'):
            v_best.append(min(a[:,j]))
            v_worst.append(max(a[:,j]))
    

    #calculating si+ and si-
    s_best=[]
    s_worst=[]
    for i in range(0,row_count):
        t=0
        s=0
        for j in range(0,col_count):
            t=t+(a[i,j]-v_best[j])*(a[i,j]-v_best[j])
            s=s+(a[i,j]-v_worst[j])*(a[i,j]-v_worst[j])
        s_best.append(m.sqrt(t))
        s_worst.append(m.sqrt(s))
    

    #calculating topsis score
    pi=[]
    for i in range(0,row_count):
        pi.append(s_worst[i]/(s_worst[i]+s_best[i]))
    

    #copying pi
    pi_temp=pi.copy()
    

    #calculating rank
    rank=[]
    for i in range(0,row_count):
        rank.append(0);
    t=1;
    for i in range(0,row_count):
        d=pi_temp.index(max(pi_temp)) 
        pi_temp[d]=-1
        rank[d]=t
        t=t+1

    dataset=pd.DataFrame(dataset)
    dataset['performance score']=pi
    dataset['rank as per topsis']=rank
    print(dataset)
    return dataset

import sys 

def main():
    print(sys.argv)
    weights=[float(i) for i in sys.argv[2].split(',')]
    dataset=pd.read_csv(sys.argv[1]).values
    maxmin=sys.argv[3].split(',')
    topsis(dataset,weights,maxmin)
    

if __name__=="__main__":
     main()