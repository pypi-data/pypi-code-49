import pandas as pd
import sys


input_file = sys.argv[1]
output_file = sys.argv[2]

def file(input_file):
    try:
        return pd.read_csv(input_file)
    except IOError:
        raise Exception("Data file doesn't exist\n")
        
def main(input_file,output_file):
    df = file(input_file)
    data = pd.DataFrame(df.iloc[:,:-1].values)
    q1=data.quantile(0.25)
    q3=data.quantile(0.75)
    iqr=q3-q1
    lis = []
    for col in data.columns:
        for row in range(len(data.index)):
            if(((data.iloc[row,col])<(q1[col]-1.5*iqr[col])) | ((data.iloc[row,col])>(q3[col]+1.5*iqr[col]))):
                lis.append(row)       
    for i in reversed(lis):
        df.drop(df.index[i],inplace = True)
    df.to_csv("out.csv",index=False)
    print("Total Number of rows deleted are",len(lis),".\n")
    
if __name__=='__main__':
    main(input_file,output_file)