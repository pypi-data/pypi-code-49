# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 22:53:02 2020

@author: PHULL
"""

import numpy as np
import pandas as pd
import argparse
import sys

def print_and_save(df,destfile):
         
    
    pd.DataFrame(df).to_csv(destfile,index=False,header=False)
    
    try:
        open(destfile, 'r')
       
    except IOError:
       print ("There was an error writing to", destfile)
       print ("Save unsuccessful!")
       sys.exit(0)
       
    print(f'Save successful!\nCheck {destfile} for results')

def outlier_removerfn(sourcefile,destfile="sans_outliers.csv",invalid_cols=[]):
    
    
    try:
        x=pd.read_csv(sourcefile).values
       
    except IOError:
       print ("There was an error reading", sourcefile)
       sys.exit(0)
 
    #x = pd.DataFrame(boston.data).values
    valid_cols=[i for i in range(np.size(x,1)) if i not in invalid_cols]
    
    if len(valid_cols)==0:
        print("Error:No features left to consider!")
        sys.exit(0)
        
    xnew=x[:,valid_cols]

    features=np.size(xnew,1)
    records=np.size(xnew,0)
    
    minval=[]
    maxval=[]
    row_with_outlier=[]
    
    for i in range(0,features):
        
        f=sorted(xnew[:,i])
    
        q1,q3=np.quantile(f,[0.25,0.75])
        #print(f'q1={q1}, q3={q3}')
        #print(m)
        iqr=q3-q1
        #print('iqr=',iqr)
        minval.append(q1-(1.5*iqr))
        maxval.append(q3+(1.5*iqr))
        #print(f'lb={minv}, ub={maxv}')
       
        for j in range(records):
            if xnew[j,i]<minval[i] or xnew[j,i]>maxval[i]:
                if j not in row_with_outlier:
                    row_with_outlier.append(j)
    
    if(len(row_with_outlier)==0):
        print("No outliers found.")
        
    else:  
        try:
            x=np.delete(x,row_with_outlier,0)
            
        except UnboundLocalError:
            print("Removal of record(s) failed!")
            sys.exit(0)
            
        print(f'Removed {len(row_with_outlier)} row(s) successfully.')
        
        print_and_save(x,destfile)     
   


def main():  
    
    parser = argparse.ArgumentParser(prog ='outlier_remover')
    parser.add_argument("InputDataFile", help="Enter the name of input CSV file with .csv extention",type=str)
    parser.add_argument("-o","--OutputDataFile", nargs=1, help="Enter the name of output CSV file with .csv extention" ,type=str)
    parser.add_argument("-c","--ColumnsToSkip", nargs=1, help="Enter the columns to be left out of analysis",type=str)
    args = parser.parse_args()
    

    sourcefile = args.InputDataFile 
    
    if args.OutputDataFile:
        destfile= args.OutputDataFile[0]
    else:
        destfile=sourcefile.rsplit('.', 1)[0]+"_sansOutliers.csv"
     
    #print(type(args.OutputDataFile)) 
    
    if args.ColumnsToSkip:
        
        try:
            cols_to_skip = np.array((args.ColumnsToSkip[0].replace(" ", "")).split(','),dtype=int)
  
        except ValueError:
            print ("Incorrect value(s) in columns vector")
            sys.exit()
          
    else:
        cols_to_skip=[]

    
    outlier_removerfn(sourcefile,destfile,cols_to_skip)



#driver code
if __name__=="__main__":
    main()        