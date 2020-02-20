import sys
import numpy as np
import pandas as pd
import os
import csv
from sklearn.linear_model import LinearRegression

def helper():
	path_file = os.getcwd() + '/' + sys.argv[1]
	data = pd.read_csv(path_file)

	def f1(s):
		if s == "male":
			return 0
		elif s == "female":
			return 1
		else:
			return np.nan


	def f2(s):
		if s == "S":
			return 0
		elif s == "Q":
			return 1
		elif s == "C":
			return 2
		else:
			return np.nan


	data["Sex_numeric"] = data.Sex.apply(f1)
	data["Embarked_numeric"] = data.Embarked.apply(f2)
	del data["Sex"]
	del data["Embarked"]
	del data["Cabin"]
	del data["PassengerId"]
	del data["Ticket"]
	del data["Name"]




	data2 = data.copy()
	a = data2.isnull().sum()
	l = data2.isnull().sum()[a > 0].index#Null Columns
	nl = data2.isnull().sum()[a == 0].index#Non Null Columns

	selected_rows = data2.loc[:,"Age"].isnull() == False
	x_train = data2.loc[selected_rows, nl].values
	y_train = data2.loc[selected_rows, "Age"].values
	selected_rows = (selected_rows == False)#This is way of taking negation
	x_test = data2.loc[selected_rows, nl].values
	lr = LinearRegression()
	lr.fit(x_train, y_train)
	data2.loc[selected_rows, "Age"] = lr.predict(x_test)

	#print(data2.isnull().sum())

	a = data2.isnull().sum()
	l = data2.isnull().sum()[a > 0].index
	nl = data2.isnull().sum()[a == 0].index

	selected_rows = data2.loc[:, "Embarked_numeric"].isnull() == False
	x_train = data2.loc[selected_rows,nl].values
	y_train = data2.loc[selected_rows, "Embarked_numeric"].values
	selected_rows = (selected_rows == False)
	x_test = data2.loc[selected_rows, nl].values
	lr = LinearRegression()
	lr.fit(x_train, y_train)
	data2.loc[selected_rows,"Embarked_numeric"] = lr.predict(x_test)

	#Undo the operations
	def f11(s):
		if s == 0.0:
			return "male"
		else:
			return "female"

	def f22(s):
		if s == 0.0:
			return "S"
		elif s == 1.0:
			return "Q"
		else:
			return "C"

	data2["Sex"] = data2.Sex_numeric.apply(f11)
	data2["Embarked"] = data2.Embarked_numeric.apply(f22)
	del data2["Embarked_numeric"]
	del data2["Sex_numeric"]
	final_path = os.getcwd() + '/' + 'Missing.csv'
	data2.to_csv(final_path)

	return 1;


def main():
	if(len(sys.argv) != 2):
		print("Operation failed")
		return sys.exit(1)
	else:
		a = helper()
		if(a == 1):
			print("Task Complete")



