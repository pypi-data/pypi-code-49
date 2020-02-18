import seaborn as sb
import pandas as pd
import numpy as np
import sys
class outliers:
    def __init__(self,reading_file,writing_file):
        
        file=pd.read_csv(reading_file,error_bad_lines=False)
        ddff=pd.DataFrame(file)
        di=dict()
        self.df=ddff
        shape=self.df.shape
        for i in range(shape[1]):
           # print(df[i])
            Q1 = self.df.iloc[:,i].quantile(0.25)
            Q3 = self.df.iloc[:,i].quantile(0.75)
            IQR = Q3 - Q1
            li=list();
            li.append((Q1 - 1.5 *IQR))
            li.append((Q3 + 1.5 * IQR))
            di[i]=li
        
        check=np.ones(shape[0])
        rows_to_be_removed=0;
        for i in range(shape[0]):
            for j in range(shape[1]):
                if (self.df.iloc[i,j] < di[j][0] or self.df.iloc[i,j] > di[j][1]):
                    check[i]=0
                    rows_to_be_removed+=1;
                    break
        print("No. of Rows Removed : " , rows_to_be_removed);                
        for i in range(shape[0]):
             if check[i]==0:
                 self.df.drop([i],inplace=True)
                 
        self.df.to_csv(writing_file) 



if( len (sys.argv)<3):
    print("ARGUMENTS NOT SUFFICIENT ");
    sys.exit(0);
    
reading_file=sys.argv[1];
writing_file=sys.argv[2];

outliers(reading_file,writing_file);
