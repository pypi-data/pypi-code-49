import numpy as np
import pandas as pd
import sys
def topsis_solution(argv):
    df=pd.read_csv(sys.argv[1]).values
    dfbaad=df
    df = df.astype(float)
    weights=list(map(float,sys.argv[2].split(",")))
    impacts=list(map(str,sys.argv[3].split(",")))
    (x,y)=df.shape

    summation=list()
    for j in range(0,y):
        temp=0
        for i in range(0,x):
            temp+=(df[i,j]**2)
        summation.append(float((temp)**(0.5)))
            
    for i in range(0,x):
        for j in range(0,y):
            df[i,j]=(df[i,j]/(summation[j]))*weights[j]
    
    
    vjplus=list()
    vjminus=list()
    for j in range(0,y):
        if impacts[j]=='-':
            vjplus.append(min(df[:,j]))
            vjminus.append(max(df[:,j]))
        elif impacts[j]=='+':
            vjplus.append(max(df[:,j]))
            vjminus.append(min(df[:,j]))
    
    siplus=list()
    siminus=list()
    temp1 = 0 
    temp2 = 0 
    
    for i in range(0,x):
        a = np.array(df[i,:])
        b = np.array(vjplus)
        c = np.array(vjminus)
        temp1= np.sum((a-b)**2)
        temp1= np.sqrt(temp1)
        temp2 = np.sum((a-c)**2)
        temp2 = np.sqrt(temp2)
        siplus.append(temp1)
        siminus.append(temp2)
        temp1 = 0 
        temp2 = 0
    
    
    pscore=list()
    for i in range(0,x):
        pscore.append(float(siminus[i]/(siplus[i]+siminus[i])))
    output = [0] * x
    for i, p in enumerate(sorted(range(x), key=lambda y: pscore[y])):
        output[p] = i+1

    output = np.array(output)
    dftemp=np.zeros(shape=(x,y+1))
    dftemp[:,:-1] = dfbaad
    dftemp[:,-1] = output
    dftemp = dftemp.astype(int)
    
    #df = np.concat(df,output)
    #print(dftemp)
    outdict={}
    outdict['values:']=[i+1 for i in range(0,x)]
    outdict["Performance Score:"]=pscore
    outdf=pd.DataFrame(outdict)
    print(outdf.head())


if __name__ == "__main__":
   topsis_solution(sys.argv[1:])