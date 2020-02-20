import numpy as np
import pandas as pd
import sys


def handle_missing(dataset):
    try:
        input_file=pd.read_csv(dataset,header=None)
    except:
        print("Input file is missing or wrong path")
    else:
        col=len(input_file.iloc[0,:])
        for i in range(col):
            mean_value=input_file[i].mean()
            input_file[i]=input_file[i].fillna(mean_value)
        input_file.to_csv("output.csv",index=False)
        print("Missing values are replaced")


if __name__=="__main__":
    handle_missing(sys.argv[1])
