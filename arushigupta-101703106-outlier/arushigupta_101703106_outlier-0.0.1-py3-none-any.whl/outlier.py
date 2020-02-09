import pandas as pd
import sys
def outlier_remove(df):
	data_frame = df.copy()
	Q1 = data_frame.quantile(0.25)
	Q3 = data_frame.quantile(0.75)
	inter = Q3 - Q1
	# print(IQR)
	# (boston_df<(Q1 - 1.5 * IQR))|(boston_df > (Q3 + 1.5 * IQR))
	df_out = data_frame[~((data_frame < (Q1 - 1.5 * inter)) |(data_frame > (Q3 + 1.5 * inter))).any(axis=1)]
	print("Number of removed rows that have been removed are:",data_frame.shape[0]-df_out.shape[0])
	return df_out
try:
	dataset=pd.read_csv(sys.argv[1])
	df_out = outlier_remove(dataset)
except OSError:
	print(sys.argv[1],"Enter correct file name with correct path")
	print("Correct format is: python outlier.py input_file.csv output_file.csv")
