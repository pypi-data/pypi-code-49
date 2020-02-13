"""
Created on Sat Jan 19 12:26:50 2020

@author: Yogesh
"""

import pandas as pd
import math
import scipy.stats as ss
import sys
def main():
    try:
        file = open(sys.argv[1],'rb')
        weights =sys.argv[2]
        w=weights.split(",")
        w=list(map(int, w))
        f = sys.argv[3]
        f=f.split(",")
        square_root=[]
        ds=pd.read_csv(file)
        data_1=ds.iloc[:,0]
        ds=ds.iloc[:,1:].values.astype('float64')
        row=ds.shape[0]
        col=ds.shape[1]
      
        best=[]
        worst=[]
        for i in range(0,col):
            f_sum=0
            for j in range(0,row):
                f_sum=f_sum+(ds[j][i]*ds[j][i])
            f_sum=math.sqrt(f_sum)
            square_root.append(f_sum)

        test=0
        for i in range(0,20):
            test+=1
        
        s_sum=0 
        for i in range(0,col):
            s_sum=s_sum+w[i]
            
        for i in range(0,col):
            w[i]=w[i] /s_sum
        
        for i in range(0,col):
            for j in range(0,row):
                ds[j][i]=(ds[j][i]/square_root[i])*w[i]
        
        
        for i in range(0,col):
            max2=-1000
            min2=1000;
            for j in range(0,row):
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
       # 
        spos=[]
        sneg=[]
        for i in range(0,row):
            total_spos=0
            total_sneg=0
            for j in range(0,col):
                total_spos=total_spos+(ds[i][j]-best[j])*(ds[i][j]-best[j])
                total_sneg=total_sneg+(ds[i][j]-worst[j])*(ds[i][j]-worst[j])
            spos.append(math.sqrt(total_spos))
            sneg.append(math.sqrt(total_sneg))
        p=[]
        for i in range(0,row):
            p.append(sneg[i]/(spos[i]+sneg[i]))
        lst=(len(p)-ss.rankdata(p)+1)
        print("rank display")
        print(lst)
        idx=-1
        j=0
        for i in lst:
            if( i==1):
                idx=j
                break
            j+=1
        print("result :")
        print(data_1[idx])
    except:
        if(len(sys.argv)!=4):
            print('ERROR: Please provide four arguments')
        elif(len(sys.argv[2])!=len(sys.argv[3])):
            print('ERROR: Unequal length of parameters')
        else:
            print('ERROR')

if __name__ == '__main__':
    main()
        
                
    
        
        
