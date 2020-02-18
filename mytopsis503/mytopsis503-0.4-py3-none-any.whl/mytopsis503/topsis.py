import numpy as np
import pandas as pd 
import sys 
def topsis(data,weight,impact):
	nmat =[]
	for i in data:
		col_data = data[i]
		sum1 = 0 
		for j in col_data:
			sum1 = sum1+(j*j)
		sum1 = np.sqrt(sum1)
		nmat.append(sum1)
	norm_data = data/nmat 
	norm_data = norm_data*weight
	best_val = [] 
	worst_val = []
	for i in norm_data:
		col_data = norm_data[i] 
		best_val.append(col_data.max())
		worst_val.append(col_data.min())
	norm_data = norm_data.transpose()
	euc_dist_max = []
	euc_dist_min = []
	p = 0
	for i in norm_data:
		col_data = norm_data[i]
		sum1 = 0 
		sum2 = 0 
		for j in col_data:
			if(impact[p]=='+'):
				sum1 = sum1 + (j-best_val[p])*(j-best_val[p])
				sum2 = sum2 + (j-worst_val[p])*(j-worst_val[p])
			else:
				sum1 = sum1 + (j-worst_val[p])*(j-worst_val[p])
				sum2 = sum2 + (j-best_val[p])*(j-best_val[p])
			p+=1
		sum1 = np.sqrt(sum1)
		sum2 = np.sqrt(sum2)
		euc_dist_max.append(sum1)
		euc_dist_min.append(sum2)
		p=0
			
	a = np.array(euc_dist_max)
	b = np.array(euc_dist_min)
	c = a+b
	performance_score = (euc_dist_min)/(c)
	return performance_score
def do_work():
	args = sys.argv
	args = args[1:]
	data = pd.read_csv(args[0])
	w = args[1].split(',')
	w1 = []
	for c in w:
		c = int(c)
		w1.append(c)
	
	i = args[2].split(',')
	fin_ans = topsis(data,w1,i)
	print(f"{data}\t")
	index  = 0 
	max1 = fin_ans[0]
	p = 1 
	for i in fin_ans:
		if max1 < i:
			max1 = i 
			index = p
		p+=1
	p = 0 	
	print("Model Num\tPerformance Score")
	for i in fin_ans:
		print(f"{p}\t\t{i}") 
	print("Best Model : Performance Score")
	print(f"{index} : {max1}")
if __name__ == "__main__":	
	do_work()