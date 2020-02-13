import pandas as pd
import numpy as np
import sys
class outlier:
	def read_file(self):
		try:
			return pd.read_csv(self.i_filename)
		except IOError:
			raise Exception("Filename not correct")

	def iqr(self):
		for column in self.data.columns:
			ds = self.data[column]
			ds = sorted(ds)
			q1,q3 = np.percentile(ds,[25,75])
			iqr_val = q3 - q1
			lb = int(q1 - (1.5*iqr_val))
			ub = int(q3 + (1.5*iqr_val))
			for i in self.data[column]:
				if(i not in range(lb,ub)):
					self.count=self.count+1
					self.data = self.data[self.data[column]!=i]
		return self.data,self.count

	def z_score(self):
		thr=3
		for column in self.data.columns:
			mean = np.mean(self.data[column])
			std = np.std(self.data[column])
			for i in self.data[column]:
				zscore = (i-mean)/std
				if(np.abs(zscore)>thr):
					self.count=self.count+1
					self.data = self.data[self.data[column]!=i]
		return self.data,self.count

	def calc(self):
		dataset = self.read_file()
		try:
			float(dataset.iloc[0][0])
			self.data = dataset
		except:
			self.data = pd.DataFrame(dataset.iloc[:,1:])
		self.count=0
		if(self.method == "z_score"):
			data,count = self.z_score()
		else:
			data,count = self.iqr()
		print("Number of Outliers:",count)
		data.to_csv(self.o_filename)

	def __init__(self,i_filename,o_filename,method="iqr"):
		self.i_filename=i_filename
		self.o_filename=o_filename
		self.method = method
		self.calc()

def main(i_filename,o_filename,method="iqr"):
	t = outlier(i_filename,o_filename,method)

if __name__ == '__main__':
	i_filename=sys.argv[1]
	o_filename=sys.argv[2]
	main(i_filename,o_filename)
