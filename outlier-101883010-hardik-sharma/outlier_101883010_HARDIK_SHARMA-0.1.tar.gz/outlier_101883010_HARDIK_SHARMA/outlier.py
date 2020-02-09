# CREATED BY 
#------------

# HARDIK SHARMA
# 101883010
# COE5

import numpy as np

def outlier_removal(dataset):    
    data=np.genfromtxt(dataset,delimiter=',')
    da=np.array(data,dtype = int)
    #print(da)
    #print(type(da))
    s=da.shape
    #print(s)
    r=s[0]
    c=s[1]
    
    dd=da
    dd=np.sort(dd,axis=0,kind='mergesort')
    #print(dd)
    
    li=[]
    lq1=[]  #stores quartile 1 of each column
    lq3=[]  #stores quartile 3 of each column
    liqr=[] #stores inter-quartile range of each column
    llb=[]  #stores lower bound value of each column
    lub=[]  #stores upper bound value of each column
    
    for i in range(0,c):
        li=dd[:,i]
        q1=np.percentile(li,25)
        q3=np.percentile(li,75)
        lq1.append(q1)
        lq3.append(q3)
        iqr=q3-q1
        liqr.append(iqr)
        lb=q1-(1.5*iqr)
        llb.append(lb)
        ub=q3+(1.5*iqr)
        lub.append(ub)
    
    w=[] #list to store which rows to be deleted

    for i in range(0,c):
        for j in range(0,r):
            if(da[j][i]<llb[i] or da[j][i]>lub[i]):
                w.append(j)
                r=r-1

    
    dn=da
    dn=np.delete(dn,w,0)
    
    
    return dn,len(w),w  #returns the new matrix,the no of rows deleted, indexs of rows deleted   
