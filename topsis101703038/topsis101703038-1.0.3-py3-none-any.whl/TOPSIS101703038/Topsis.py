import numpy as np
import pandas as pd
import sys
import copy

def main(a,b,c):
    
    filename=a
    weights =b
    impacts =c
    
    dataset=pd.read_csv(filename).values
    #print(dataset)
    datamat=dataset[:,1:]

    weights = list(map(float ,weights.split(',')))
    impacts = list(map(str ,impacts.split(',')))
    
    r,c=(datamat.shape) 

    #weights=[1,1,1,1]
    #impacts=['-','+','+','+']
    
    if len(weights)!=c:
        print("Enter correct number of weights")
        sys.exit()

    if len(impacts)!=c:
        print("Enter correct number of impacts")
        sys.exit()
    
    for i in weights:
        if(i<0):
            print("Enter positive weights only")
            sys.exit()
        
        for i in impacts:
            if(i!='+' and  i!='-'):
                print("impacts can only be + or -")
                sys.exit()
        
    sum_weights=sum(weights)

    normalized_mat=np.zeros([r,c])

    for i in range(c):
        for j in range(r):
            d=np.sqrt(sum(datamat[:,i]**2))
            temp=datamat[j,i]/d
            #print(temp)
            normalized_mat[j,i]=temp*(weights[i]/sum_weights)
        
    vpositive=[]
    vnegative=[]

    for i in range(c):
        if impacts[i]=='+':
            vpositive.append(max(normalized_mat[:,i]))
            vnegative.append(min(normalized_mat[:,i]))
        
        else:
            vpositive.append(min(normalized_mat[:,i]))
            vnegative.append(max(normalized_mat[:,i]))
        
    spositive=[]
    snegative=[]

    for i in range(r):
        s=0
        for j in range(c):
            s=s+ (normalized_mat[i,j]-vpositive[j])**2
        
        spositive.append(np.sqrt(s))
    
    for i in range(r):
        s=0
        for j in range(c):
            s=s+ (normalized_mat[i,j]-vnegative[j])**2
        
        snegative.append(np.sqrt(s)) 
    
    prank=[]

    for i in range(r):
        prank.append(snegative[i]/(spositive[i]+snegative[i]))

    item=[]*r
    for i in range(r):
        item.append(dataset[i,0])    
    
    item=list(item)


    rank=[0]*r

    dupli=copy.deepcopy(prank)
    c=1

    for i in range(r):
        t=max(dupli)
        for j in range(r):
            if(dupli[j]==t):
                rank[j]=c
                c=c+1
                dupli[j]=0
                break
       
    rank=list(rank)

    out={'Item':item,'Perforamnce score':prank,'Rank':rank}

    output=pd.DataFrame(out)

    print(output)
def do_work():
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
    main(a,b,c)
if __name__=="__main__":
    do_work()



       
        
      



    
        
        
        
        
        
    
    
        
    
        

    





    