from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import sys

class missing:
	def read_file(self):
		try:
			return pd.read_csv(self.i_filename)
		except IOError:
			raise Exception("Check filename!!")

	def mean_replace(self):
		col = []
		for column in self.dataset.columns:
			try:
				self.dataset[column].fillna(self.dataset[column].mean(),inplace = True)
			except:
				col.append(column)
		data1 = self.dataset.dropna()
		for column in col:
			try:
				y_train = data1[column]
				x_train = data1.drop(columns = col)
				model = KNeighborsClassifier()
				model.fit(x_train,y_train)
				x_predict = self.dataset[self.dataset[column].isnull()].drop(columns=col)
				y_predict = model.predict(x_predict)
				print("Replaced categorical values: ",y_predict)
				l = 0
				for i in x_predict.index:
					self.dataset.loc[i,column] = y_predict[l]
					l = l + 1
			except:
				pass
		return self.dataset

	def calc(self):
		self.dataset = self.read_file()
		if (self.method == 'replace'):
			data = self.mean_replace()
			print("Missing values replaced!!")
		else:
			data = self.dataset.dropna()
			print("Missing columns removed!!")
		data.to_csv(self.o_filename)
		print("File saved as: ",self.o_filename)

	def __init__(self,i_filename,o_filename,method):
		self.i_filename = i_filename
		self.o_filename = o_filename
		self.method = method
		self.calc()

def main(i_filename,o_filename,method='replace'):
	t = missing(i_filename,o_filename,method)

if __name__ == '__main__':
	i_filename = sys.argv[1]
	o_filename = sys.argv[2]
	method = sys.argv[3]
	main(i_filename,o_filename,method)