import numpy as np

def main():
    import sys
    import pandas as pd
    if len(sys.argv)!=2:
        print("ERROR! WRONG NUMBER OF PARAMETERS")
        print("USAGES: remove-outlier <dataset>")
        print("EXAMPLE: remove-outlier data.csv")
        exit(1)

    dataset = pd.read_csv(sys.argv[1])             # importing the dataset
    new_dataset = remove_outlier(dataset)             
    new=pd.DataFrame(new_dataset)
    new.to_csv("output.csv",index=False)
    print("The number of rows removed are " + str(dataset.shape[0] - new_dataset.shape[0]))
    print("Successfully executed !!")

def outliers_iqr(col):
    quartile_1, quartile_3 = np.percentile(col, [25, 75])
    iqr = quartile_3 - quartile_1
    lower_bound = quartile_1 - (iqr * 1.5)
    upper_bound = quartile_3 + (iqr * 1.5)
    return np.where((col > upper_bound) | (col < lower_bound))

def remove_outliers(dataset):
    r,c = dataset.shape
    if c < 2 :
        return print("ERROR! data not in specifed format. Enter format as features, target.")
    data = dataset.iloc[:,:-1].values
    r,c = data.shape
    se=np.zeros([0])
    
    for i in range(c):
        if(dataset.dtypes[i] != 'object'):
            se = np.append(se,[outliers_iqr(data[:,i])])
    a = np.unique(se)
    dataset = dataset.drop(a)
    return dataset


if __name__ == "__main__":
    main()
    
'''  

import seaborn as sns
df = sns.load_dataset('iris')
 
# Make boxplot for one group only
r = sns.boxplot(data=df.ix[:,:])
r.get_figure().savefig('iris.png')


'''