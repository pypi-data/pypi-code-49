import sys
import logging
import pandas as pd 

if(sys.argv[1] is None):
    logging.error("Input datafile missing!!")
    sys.exit()

df=pd.read_csv(sys.argv[1]);
print("initially:");
print(df.isna().sum())

df=df.fillna(method='bfill');
df=df.fillna(method='ffill');

print("\nAfter using missing.py:")
print(df.isna().sum())
print("\nDataFrame:")
print(df.head());

df.to_csv(sys.argv[1][:-4]+"_not_null.csv",index=False);
print("\n new file stored as "+ sys.argv[1][:-4]+"_not_null.csv");


