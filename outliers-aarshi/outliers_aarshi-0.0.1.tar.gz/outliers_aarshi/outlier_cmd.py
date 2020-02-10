
import pandas as pd
class err1(Exception): 
  
    # Constructor or Initializer 
    def __init__(self, value): 
        self.value = value 
  
    # __str__ is to print() the value 
    def __str__(self): 
        return(repr(self.value))
def rem_out(data):
	df = data.copy()
	Q1 = df.quantile(0.25)
	Q3 = df.quantile(0.75)
	IQR = Q3 - Q1
	# print(IQR)

	# (boston_df<(Q1 - 1.5 * IQR))|(boston_df > (Q3 + 1.5 * IQR))

	df_out = df[~((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]
	print("Number of removed rows is:",df.shape[0]-df_out.shape[0])
	# return df_out
	df_out.to_csv(newdata,index=False)
	# boston_df_out.shape
import sys

try:
	dataset=pd.read_csv(sys.argv[1])
	newdataset=sys.argv[2]
	if newdata[-4:]!='.csv':
		raise err1('error')
	rem_out(dataset)
except err1:
	print('The output file you entered is not in csv format')
except OSError:
	print(sys.argv[1],"Enter correct file name with correct path\n")
	# print('Some error in entering name of csv file.')
	print("Correct format is: python otlier.py path_of\\input_file.csv path_of\\output_file.csv")
