import numpy as np
import sys
import math

def topsis(data,w,impact):
    d = np.array(data,dtype = float)
#     print(d)
    s = d.shape
    c = s[1]
    r = s[0]
    vjplus = []
    vjminus = []
    splus = []
    sminus = []
#     print(s)
    for i in range(c):
        sum1 = 0
        for j in range(r):
            sum1 += d[j][i]**2
        sum1 = math.sqrt(sum1)
#         print(sum1)
        ma = 0
        mi =1 
        for j in range(r):
            d[j][i] = (d[j][i]/sum1)*w[i]
            if d[j][i] > ma:
                ma = d[j][i]
            if d[j][i] < mi:
                mi = d[j][i]
#         print(d)
        vjplus.append(ma)
        vjminus.append(mi)
#         print(vjplus)
#         print(vjminus)
    for i in range(c):
        if impact[i] == '-':
            vjplus[i],vjminus[i] = vjminus[i],vjplus[i]
    for i in range(r):
        v = 0
        u = 0
        for j in range(c):
            v += (d[i][j] - vjplus[j])**2
            u += (d[i][j] - vjminus[j])**2
        splus.append(math.sqrt(v))
        sminus.append(math.sqrt(u))
#     print(sminus)
#     print(splus)
    p = []
    for i in range(len(splus)):
        p.append(sminus[i]/(sminus[i]+splus[i]))
#     print(p)
    n = np.array(p)
    a = np.argsort(p)[::-1]
    return a+1,n
#If you want to take file input from cmd line:

# name = sys.argv[1]

#Input a CSV file

# a = np.genfromtxt(name,delimiter=',')

# GIVING A NP ARRAY DIRECTLY
# a = [[250,16,12,5],[200,16,8,3],[300,32,16,4],[275,32,8,4],[225,16,16,2]]

# # WEIGHTS OF EACH COLUMN
# w = [0.25,0.25,0.25,0.25]

# #IMPACT OF EACH COLUMN
# impact = ['-','+','+','+']

# r,n = topsis(a,w,impact)
# print("Rank Row is:",r)