"""
Created on Sat Jan 15 12:26:50 2020

@author: Sunvir
"""

import pandas as pd
import math
import scipy.stats as ss
import sys
def main():
    try:
        file = open(sys.argv[1],'rb')
        ww =sys.argv[2]
        w=ww.split(",")
        w=list(map(int, w))
        f = sys.argv[3]
        f=f.split(",")
        sqr=[]
        nm=[]
        ds=pd.read_csv(file)
        target=ds.iloc[:,0]
        ds=ds.iloc[:,1:].values.astype('float64')
        rows=ds.shape[0]
        cols=ds.shape[1]
        
        for i in range(0,cols):
            sum1=0
            for j in range(0,rows):
                sum1=sum1+(ds[j][i]*ds[j][i])
            sum1=math.sqrt(sum1)
            sqr.append(sum1)
              
        sum2=0 
        for i in range(0,cols):
            sum2=sum2+w[i]
            
        for i in range(0,cols):
            w[i]=w[i] /sum2
        
        for i in range(0,cols):
            for j in range(0,rows):
                ds[j][i]=(ds[j][i]/sqr[i])*w[i]
        
        #f=['-','+','+','+']
        max1=[]
        min1=[]
        best=[]
        worst=[]
        for i in range(0,cols):
            max2=-1
            min2=10000;
            for j in range(0,rows):
                if(ds[j][i]>max2):
                    max2=ds[j][i]
                if(ds[j][i]<min2):
                    min2=ds[j][i]
            if(f[i]=='+'):
                best.append(max2)
                worst.append(min2)
            elif(f[i]=='-'):
                best.append(min2)
                worst.append(max2)
        
        sip=[]
        sin=[]
        for i in range(0,rows):
            sumsip=0
            sumsin=0
            for j in range(0,cols):
                sumsip=sumsip+(ds[i][j]-best[j])*(ds[i][j]-best[j])
                sumsin=sumsin+(ds[i][j]-worst[j])*(ds[i][j]-worst[j])
            sip.append(math.sqrt(sumsip))
            sin.append(math.sqrt(sumsin))
        p=[]
        for i in range(0,rows):
            p.append(sin[i]/(sip[i]+sin[i]))
        lst=(len(p)-ss.rankdata(p)+1)
        print("Rank of all Candidates:")
        print(lst)
        indexx=-1
        j=0
        for i in lst:
            if( i==1):
                indexx=j
                break
            j+=1
        print("Best Candidate:")
        print(target[indexx])
    except:
        if(len(sys.argv)!=4):
            print('ERROR: Please provide four arguments')
        elif(len(sys.argv[2])!=len(sys.argv[3])):
            print('ERROR: Unequal length of parameters')
        else:
            print('ERROR')

if __name__ == '__main__':
    main()
    
        
        
