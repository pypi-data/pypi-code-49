import numpy as np

def topsis(d,w,t):
    d = np.array(d,dtype = float)
    n = d.shape[0]
    m = d.shape[1]
    for j in range(m):
        s=0
        for i in range(n):
            s+=d[i][j]*d[i][j]
        s = s**0.5
        for i in range(n):
            d[i][j]=float(d[i][j])/float(s)
    for j in range(m):
        for i in range(n):
            d[i][j]=d[i][j]*w[j]
    v1=[]
    v2=[]
    for j in range(m):
        if t[j]=='+':
            v1.append(max(d[:,j]))
            v2.append(min(d[:,j]))
        else:
            v1.append(min(d[:,j]))
            v2.append(max(d[:,j]))
    p1=[]
    p2=[]
    for i in range(n):
        s1=0
        s2=0
        for j in range(m):
            s1+=(d[i][j]-v1[j])*(d[i][j]-v1[j])
            s2+=(d[i][j]-v2[j])*(d[i][j]-v2[j])
        s1 = s1**0.5
        s2 = s2**0.5
        p1.append(s1)
        p2.append(s2)
    r = []
    for i in range(n):
        k = p2[i]/(p1[i]+p2[i])
        r.append(k)

    r = np.array(r)
    a = np.argsort(r)[::-1]
    return a+1

