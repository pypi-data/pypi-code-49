import pandas as pd
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

def outlier_removal_iqr(feature_df,dataset_df):
    #converting feature dataframe to numpy array
    rows_removed=0
    if(feature_df.dtype=='object'):
        return(dataset_df,rows_removed)
    feature_np=feature_df.values
    #sorting the array
    feature_np.sort()
    #calucalting the first quartile and the third quartile
    quartile1,quartile3=np.percentile(feature_np,[25,75])
    #finding IQR
    IQR=quartile3-quartile1
    #finding lower bound
    lower_bound=quartile1-(1.5*quartile1)
    #finding upper bound
    upper_bound=quartile3+(1.5*quartile3)
    for i in range(feature_np.shape[0]):
        if(feature_np[i]<lower_bound or feature_np[i]>upper_bound):
            dataset_df.drop(i,inplace=True)
            rows_removed+=1
    dataset_df.reset_index(drop=True,inplace=True)
    return(dataset_df,rows_removed)

def features(filename):
    dataset=pd.read_csv(filename)
    tot_rows_removed=0
    cols=dataset.columns
    for i in cols:
            (dataset,temp)=outlier_removal_iqr(dataset[i],dataset)
            tot_rows_removed+=temp
    return (dataset,tot_rows_removed)

def main():
    arguments=sys.argv[1:]
    if(len(arguments)!=1):
        print('Usage python output.py <InputDataFile.py>')
        sys.exit(1)
    filename=arguments[0]
    (mod_dataset,tot_rows_removed)=features(filename)
    mod_dataset.to_csv('new_'+filename,index=False)
    print(tot_rows_removed)

if __name__=='__main__':
    main()