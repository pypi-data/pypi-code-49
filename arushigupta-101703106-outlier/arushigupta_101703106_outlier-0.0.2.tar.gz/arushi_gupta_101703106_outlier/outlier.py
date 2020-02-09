import pandas as pd
import sys
class MyError(Exception): 
  
    # Constructor or Initializer 
    def __init__(self, value): 
        self.value = value 
  
    # __str__ is to print() the value 
    def __str__(self): 
        return(repr(self.value))

def outlier_remove(df,outfile):
	data_frame = df.copy()
	Q1 = data_frame.quantile(0.25)
	Q3 = data_frame.quantile(0.75)
	inter = Q3 - Q1
	# print(IQR)
	# (boston_df<(Q1 - 1.5 * IQR))|(boston_df > (Q3 + 1.5 * IQR))
	df_out = data_frame[~((data_frame < (Q1 - 1.5 * inter)) |(data_frame > (Q3 + 1.5 * inter))).any(axis=1)]
	print("Number of removed rows that have been removed are:",data_frame.shape[0]-df_out.shape[0])
	df_out.to_csv(outfile, index=False)
	# return df_out
try:
	dataset=pd.read_csv(sys.argv[1])
	newdata = sys.argv[2]
	if newdata[-4:]!='.csv':
		raise(MyError(2))
	df_out = outlier_remove(dataset,newdata)
except MyError:
	print('Your output file is not csv')
except OSError:
	print(sys.argv[1],"Enter correct file name with correct path")
	print("Correct format is: python outlier.py input_file.csv output_file.csv")
