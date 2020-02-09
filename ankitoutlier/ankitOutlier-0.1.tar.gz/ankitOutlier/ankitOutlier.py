import pandas as pd

def rem_out(data):
	df = data.copy()
	Q1 = df.quantile(0.25)
	Q3 = df.quantile(0.75)
	IQR = Q3 - Q1
	df_out = df[~((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]
	print("Number of rows removed is:",df.shape[0]-df_out.shape[0])
	return df_out
import sys

try:
	dataset=pd.read_csv(sys.argv[1])
	df_out = rem_out(dataset)
	# newdataset=sys.argv[2]
except OSError:
	print(sys.argv[1],"Enter correct file name with correct path")
except:
	flag_name = True
	print('Some error in entering name of csv file.')
	print("Correct format is: python ankitOutlier.py path_of\\input_file.csv path_of\\output_file.csv")
