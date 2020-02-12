# Implemented by Aayush Singla
    #.....Roll No. 101703013
    #.....Group : 3CO1 (Coe-1)
    #.....Project - 1 UCS633...............

import pandas as pd

def topsis(file_name, weight, impact):
    
    data = pd.read_csv(file_name).iloc[:,1:].values.tolist()
   
    abcd = [0]*(len(data[0]))
    
    for j in range(len(data[0])):
        for i in range(len(data)):
            abcd[j] = abcd[j] + (data[i][j])**2
        abcd[j] = (abcd[j])**(1/2)
    
    x = list()
    for i in range(len(data)):
        l = list()
        for j in range(len(data[0])):
            l.append(data[i][j]/abcd[j])
        x.append(l)
    
        
    cdef = list(map(int, weight.strip().split(',')))
    
    if len(cdef)!= len(data[0]):
        raise Exception("Length must be equal to the no of colns in the data.")
    
    for i in cdef:
        if i<0:
            raise Exception("must be +")
    
    
    cdef = list()
    
    for i in range(len(cdef)):
        cdef.append(cdef[i]/sum(cdef))
        
    xyzg = impact.strip().split(',')
    
    if len(cdef)!= len(data[0]):
        raise Exception("Length must be equal to the no of colns in the data.")
        
    for i in xyzg:
        if i not in ['+','-']:
            raise Exception("'+' or '-' signs only")
    
    for j in range(len(data[0])):
        for i in range(len(data)):
            x[i][j] = x[i][j] * cdef[j]
    
    
    jqty = list()
    tyui = list()
    
    def transpose(x):
        t = list()
        for j in range(len(x[0])):
            l = list()
            for i in range(len(x)):
                l.append(x[i][j])
            t.append(l)
        return t
               
    trapose = transpose(x)
    
    for i in range(len(trapose)):
        if xyzg[i] == '+':
            jqty.append(max(trapose[i]))
            tyui.append(min(trapose[i]))
        if xyzg[i] == '-':
            tyui.append(max(trapose[i]))
            jqty.append(min(trapose[i]))
    
    pppp = list()
    

    for i in range(len(x)):
        spp = 0
        smmm = 0
        for j in range(len(x[0])):
            spp = spp + (x[i][j] - jqty[j])**2
            smmm = smmm + (x[i][j] - tyui[j])**2
        spp = spp**0.5
        smmm = smmm**0.5
        pi = smmm/(smmm+spp)
        pppp.append(pi)

    ranks = sorted(list(range(1,len(pppp)+1)))
    pt = sorted(pppp,reverse = True)
    
    perform = list()
    
    for i in pppp:
        perform.append([i,ranks[pt.index(i)]])
    
    d = {'row_no':['Score', 'Rank']}
    for i in range(len(perform)):
        d[i] = perform[i]
    for k,v in d.items():
        print(k,v)

