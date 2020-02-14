import numpy as np
import pandas as pd
import sys

def remove_outliers(filename_in, filename_out):
  dataset = pd.read_csv(filename_in)
  data = dataset.iloc[:,1:]
  (rows, cols) = data.shape
    
  outliers=[]

  for col in range(cols):
      q1,q3 = np.percentile(sorted(data.iloc[:,col]),[25,75])
      iqr = q3 - q1
      for row in range(rows):
          if data.iloc[row,col] < (q1 - 1.5 * iqr) or data.iloc[row,col] > (q3 + 1.5 * iqr):
              if row not in outliers:
                  outliers.append(row)
                  
  dataset = dataset.drop(outliers)
  dataset.to_csv(filename_out, index=False)
  print('\nCheck the modified dataset in out.csv file')
  print ('\nThe no of rows removed:',data.shape[0] - dataset.shape[0])


def main():
  filename_in = sys.argv[1]
  filename_out = sys.argv[2]
  remove_outliers(filename_in, filename_out)

if __name__=="__main__":
  main()