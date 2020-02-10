import numpy as np


def topsis(a,weights,benefits):
    
    if(len(weights)!=np.size(a,1)):
        raise Exception('number of weights doesn\'t match number of columns')
    
    if(len(benefits)!=np.size(a,1)):
        raise Exception('number of benefits doesn\'t match number of columns')
    
        
    b = np.zeros([np.size(a,0),0])
    for column in a.T:
        t = np.sqrt(sum(np.square(column)))
        column = column/t
        b = np.column_stack((b,column))
    # b is normalized decision matrix
        
        
    
    # weighted normalized decision matrix
    c=b*weights
    
    v = np.zeros([2,0])
    #a.shape[1]= num of columns
    
    for i in range(c.shape[1]):
        M = max(c.T[i])
        m = min(c.T[i])
        if(benefits[i]=='+'):
            v=np.column_stack((v,[M,m]))
        else:        
            v=np.column_stack((v,[m,M]))
                          
    s = np.zeros([0,2])
    #s[0]= s+ , s[1]=s-
    for row in c:
        sp = np.sqrt(np.sum(np.square(row-v[0])))
        sn = np.sqrt(np.sum(np.square(row-v[1])))    
        s = np.row_stack((s,[sp,sn]))
    
    
    p = np.zeros(0)
    for row in s:
        pi = (row[1]/(row[0]+row[1]))
        p = np.append(p,pi)
        
        
    result = np.where(p == np.amax(p))
    return result[0]