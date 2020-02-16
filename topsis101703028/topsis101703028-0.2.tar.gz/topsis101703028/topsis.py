import numpy as np
"""n=int(input())
m=int(input())
a=[[int(input()) for x in range(m)] for y in range (n)]
w=[float(input()) for x in range(m)]
need=[int(input()) for x in range(m)]"""
def normalized_matrix(a):
    sum1=[]
    n1=len(a)
    m1=len(a[0])
    for i in range(m1):
        sum2=0
        for j in range(n1):
            sum2+=a[j][i]*a[j][i]
        sum1.append(sum2)
    for i in range(m1):
        for j in range(n1):
            a[j][i]=a[j][i]/sum1[j]
    return a
def weighted(a,w):
    n1=len(a)
    m1=len(a[0])
    for i in range(n1):
        for j in range(m1):
            a[i][j]=a[i][j]*w[j]
    return a
def ideal(a,req_class):
    n1=len(a)
    m1=len(a[0])
    vg=[]
    maxi=0
    mini=1e9
    for i in range(m1):
        for j in range(n1):
            if(req_class[i]==1):
                maxi=max(maxi,a[j][i])
            else:
                mini=min(mini,a[j][i])
        if(req_class[i]==1):
            vg.append(maxi)
        else:
            vg.append(mini)
    return vg
def negative_ideal(a,req_class):
    n1=len(a)
    m1=len(a[0])
    vg=[]
    maxi=0
    mini=1e9
    for i in range(m1):
        for j in range(n1):
            if(req_class[i]==0):
                maxi=max(maxi,a[j][i])
            else:
                mini=min(mini,a[j][i])
        if(req_class[i]==1):
            vg.append(mini)
        else:
            vg.append(maxi)
    return vg
def separation_positive(a,vg):
    n1=len(a)
    m1=len(a[0])
    sg=[]
    for i in range(n1):
        sum1=0
        for j in range(m1):
            sum1+=(vg[i]-a[i][j])**2
        sg.append(sum1**0.5)
    return sg

def separation_negative(a,vb):
    n1=len(a)
    m1=len(a[0])
    sb=[]
    for i in range(n1):
        sum1=0
        for j in range(m1):
            sum1+=(vb[i]-a[i][j])**2
        sb.append(sum1**0.5)
    return sb

def relative_closeness(sg,sb):
    n1=len(sg)
    p=[]
    for i in range(n1):
        p.append(sb[i]/(sg[i]+sb[i]))
    return p
def final_ranking(p):
    n1=len(p)
    k=p
    k.sort()
    dicti={}
    for i in range(0,n1):
        dicti[k[i]]=n1-i
    for j in range(n1):
        p[j]=dicti[p[j]]
    return p




def topsis(a,w,req_class):
    a=normalized_matrix(a)
    a=weighted(a,w)
    vg=ideal(a,req_class)
    vb=negative_ideal(a,req_class)
    sg=separation_positive(a,vg)
    sb=separation_negative(a,vb)
    p=relative_closeness(sg,sb)
    ranking=final_ranking(p)
    return ranking
