import pandas as pd
import numpy as np

def remove_outliers_z(incsv_filename, outcsv_filename,threshold=1.5):
    dataset = pd.read_csv(incsv_filename)	
    data = dataset.iloc[:,1:]  
    outliers= []
    for col in range(data.shape[1]):
        mean = np.mean(data.iloc[:,col])
        std = np.std(data.iloc[:,col])
        for row in range(data.shape[0]):
            z_score = ((data.iloc[row,col]) - mean)/std
			
            if abs(z_score) > threshold:
                if row not in outliers:
                    outliers.append(row)
     
    dataset = dataset.drop(outliers)
    dataset.to_csv(outcsv_filename, index=False)
    print('\n||Method z_score||')
    print ('\nThe no of rows removed:',len(data) - len(dataset))
    print('\nFollowing rows were removed: ',outliers)

def remove_outliers_iqr(incsv_filename,outcsv_filename,threshold=1.5):
    dataset=pd.read_csv(incsv_filename)
    data=dataset.iloc[:,1:]
    	
    outliers=[]
    for col in range(data.shape[1]):
        quar1,quar3=np.percentile(sorted(data.iloc[:,col]),[25,75])
        iqr=quar3-quar1
        lb= quar1-threshold*iqr
        ub= quar3+threshold*iqr
        for row in range(data.shape[0]):
            if data.iloc[row,col]<lb or data.iloc[row,col]>ub:
                if row not in outliers:
                    outliers.append(row)
                    
    dataset = dataset.drop(outliers)
    dataset.to_csv(outcsv_filename, index=False)
    print('\n||Method IQR||')
    print ('\nThe no of rows removed:',len(data) - len(dataset))
    print('\nFollowing rows were removed: ',outliers)