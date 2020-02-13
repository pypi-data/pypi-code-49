import numpy as np
import pandas as pd
import math as ms


def topsis(df,impact,lst):    
    arr = np.array(df)
    for i in range(0,len(arr[0])):
        for j in range(0,len(arr)):
            arr[j][i] = arr[j][i] * lst[i]

    sum = []
    a = 0
    for i in range(len(arr[0])):
        a=0
        for j in range(len(arr)):   
            a = a + (arr[j][i]**2) 
        sum.append(ms.sqrt(a))

    for i in range(len(arr[0])):
        for j in range(len(arr)):
            arr[j][i] = arr[j][i] / sum[i]

    xmax = -1
    xmin = 1000

    Vplus = []
    Vminus = []

    for i in range(len(arr[0])):
        xmax = -1
        xmin = 1000
        for j in range(len(arr)):
            if(arr[j][i] > xmax):
                xmax = arr[j][i]
            elif(arr[j][i]< xmin):
                xmin = arr[j][i]
                if(impact[i] == '+'):
                    Vplus.append(xmax)
                    Vminus.append(xmin)
                elif(impact[i] == '-'):
                    Vplus.append(xmin)
                    Vminus.append(xmax)
    splus = []
    sminus = []
    euc_best = 0
    euc_worst = 0
    for i in range(len(arr)):
        euc_best = 0
        euc_worst = 0
        for j in range(len(arr[0])):
            euc_best = euc_best + (arr[i][j] - Vplus[j])**2
            euc_worst = euc_worst + (arr[i][j] - Vminus[j])**2
        splus.append(ms.sqrt(euc_best))
        sminus.append(ms.sqrt(euc_worst))
            
    performance = []
    
    for i in range(0,len(sminus)):
        performance.append((sminus[i])/(splus[i] + sminus[i]))
    r1=sorted(performance,reverse=True)
    rank=[(r1.index(v)+1) for v in performance]
    print(rank)

dataset = pd.read_csv('data.csv')

df = pd.DataFrame(dataset.iloc[:,1:])
arr1 = np.array(df)
lst = [] 

impact = []  

print("Enter the impacts")
for i in range(len(arr1[0])):
    im = (input())
    impact.append(im)

print("Enter the weights")   
for i in range(len(arr1[0])): 
    ele = int(input()) 
    lst.append(ele) 

topsis(df,impact,lst)