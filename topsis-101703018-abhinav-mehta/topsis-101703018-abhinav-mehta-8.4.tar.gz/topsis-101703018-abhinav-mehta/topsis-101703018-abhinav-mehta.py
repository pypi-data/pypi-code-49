import numpy as np
import pandas as pd
import sys
import array as arr
from sklearn.preprocessing import LabelEncoder

def TOPSIS(dmatrix,w,imp):

    flag=0
    for i in w:
        if i<0:
            flag=1
    if flag or len(w)!=dmatrix.shape[1]: #Error handling
        return print("Invalid weights. Kindly run again.")
    
    for i in imp:
        if i!="+" and i!="-":
            flag=1    
    if flag or len(imp)!=dmatrix.shape[1]: #Error handling
        return print("Invalid impact arguments. Kindly run again.")
    
    r = dmatrix.shape[0]
    c = dmatrix.shape[1]
    if r<2 or c<1:
        return print("Dataset incorrect. Kindly use another dataset.")
    for j in range(c):
        colsum=sum(dmatrix[:,j]**2)
        nf=np.sqrt(colsum)              #Evaluation of normalization factor for every coloumn
        if nf==0:
            nf=0.000001
        dmatrix[:,j]=dmatrix[:,j]/nf    #Normalization of dataset
        dmatrix[:,j]=dmatrix[:,j]*w[j]  #Calculating weighted normalised data 

    wval=arr.array('f')
    bval=arr.array('f')
    #Evaluating ideal worst and ideal best values for every coloumn
    for j in range(c):
        if imp[j]=="-":
            wval.append(max(dmatrix[:,j]))
            bval.append(min(dmatrix[:,j]))
        else:
            wval.append(min(dmatrix[:,j]))
            bval.append(max(dmatrix[:,j]))
	
       
    pscore=np.zeros((1,r))     
    for i in range(r):
        sminus=sum((dmatrix[i,:c]-wval)**2)
        eucworst=np.sqrt(sminus) #Evaluating eucledian distance from ideal worst
        splus=sum((dmatrix[i,:c]-bval)**2)
        eucbest=np.sqrt(splus) #Evaluating eucledian distance from ideal best values
        totdistance=eucbest+eucworst
        if totdistance==0:
            totdistance=0.0001
        pscore[0,i]=(eucworst/(totdistance))
        
    psort=pscore.argsort()
    rank=psort.argsort()
    
    print("Model","Performance Score","Rank",sep="\t")
    for i in range(r):
	    print(i+1,pscore[0,i],rank.shape[1]-rank[0,i],sep="\t",end="\n")
        
        
def main():
    
    if len(sys.argv)!=4: #Error handling
        print("Incorrect command line arguments. Kindly run as per the format: python <Name_of_program> <dataset> <weights> <impacts>")
        exit(1)
    else:
        dmatrix=pd.read_csv(sys.argv[1]).values #Dataset import
        dmatrix=dmatrix[:,1:]
        w=[int(i) for i in sys.argv[2].split(',')] #Extracting weights array
        imp=sys.argv[3].split(',') #Extracting impacts array
        catval=dmatrix[:,-1]  
        label_encoder=LabelEncoder()
        catval=label_encoder.fit_transform(catval) #Encoding the categorical values
        dmatrix[:,-1]=catval                 
        
        TOPSIS(dmatrix,w,imp)

if __name__ == "__main__":
    main()