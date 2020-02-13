import pandas as pd
import numpy as np
import sys

def z_score(feature_df,dataset_df):
    rows_removed=0
    threshold=3
    #skipping if the dataframe has cateogrical values
    if(feature_df.dtype=='object'):
        return (dataset_df,rows_removed)
    #creating a numpy array of feature dataframe
    feature_np=feature_df.values
    #finding mean of feature column
    mean=np.mean(feature_np)
    #finding standard deviation of feature column
    std=np.std(feature_np)
    #finding z score values of each of the training value in the column
    z_scr=abs((feature_np-mean)/std)
    #a loop for iterating over the rows of the numpy array
    for i in range(z_scr.shape[0]):
        if z_scr[i]>threshold:
            dataset_df.drop(i,inplace=True)
            rows_removed+=1
    dataset_df.reset_index(drop=True,inplace=True)
    return (dataset_df,rows_removed)

def features(filename):
    dataset=pd.read_csv(filename)
    tot_rows_removed=0
    cols=dataset.columns
    for i in cols:
            (dataset,temp)=z_score(dataset[i],dataset)
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

