import argparse
import pandas as pd
import numpy as np

def topsis(filename,weight,impact):

	w=np.array(weight)
	i=np.array(impact)

	data = pd.read_csv(filename+'.csv')
	data = data.values[:,1:]

	

	# Taking axis=0 to sum values along column
	normalizationFactor=np.sqrt(np.sum(data**2,axis=0,dtype=float),dtype=float)

	# Broadcasting operation to divide Xij with normalization factor
	
	normalizedData=(data/normalizationFactor)


	#Rounding normalized data values to 3 decimal places
	normalizedData=np.round(normalizedData.astype(np.float64),decimals=3)


	# Broadcasting operationn to multiply weight Xij with Wi
	
	wgtNormalizedData=normalizedData*w
	

	idealBest=[]
	idealWorst=[]

	for x in range(data.shape[1]):
	    if i[x]==1:
	        idealBest.append(max(wgtNormalizedData[:,x]))
	        idealWorst.append(min(wgtNormalizedData[:,x]))
	    if i[x]==0:
	        idealBest.append(min(wgtNormalizedData[:,x]))
	        idealWorst.append(max(wgtNormalizedData[:,x]))
	        


	distanceFromBest=np.sqrt(np.sum((wgtNormalizedData-idealBest)**2,axis=1,dtype=float),dtype=float)
	distanceFromBest=distanceFromBest.reshape(distanceFromBest.shape[0],-1)

	distanceFromWorst=np.sqrt(np.sum((wgtNormalizedData-idealWorst)**2,axis=1,dtype=float),dtype=float)
	distanceFromWorst=distanceFromWorst.reshape(distanceFromWorst.shape[0],-1)


	totalDistance=distanceFromBest+distanceFromWorst


	performance=distanceFromWorst/totalDistance


	order = performance.argsort(axis=0)

	ranks = order.argsort(axis=0)

	# Converting ranks to 1-d numpy array
	ranks=ranks.reshape(ranks.shape[0],)

	print("Item","Rank",sep="\t")
	for idx,x in enumerate(ranks):
	    print(idx+1,ranks.shape[0]-(x),sep="\t",end="\n")

def main():
	# create argument parser object 

	parser = argparse.ArgumentParser(description = "Weather Reporter") 
  
	parser.add_argument("-a", "--name", type = str, nargs = 1, 
	                    metavar = "name", default = None, help = "Name of csv file") 

	parser.add_argument("-b", "--weight", type = str, nargs = 1, 
	                    metavar = "weight", default = None, help = "Weights of attribute") 

	parser.add_argument("-c", "--impact", type = str, nargs = 1, 
	                    metavar = "impact", default = [1], help = "Impact of attribute") 

	# parse the arguments from standard input 
	args = parser.parse_args()

	filename=args.name
	weight=[int(w) for w in args.weight[0].split(',')]
	impact=[int(im) for im in args.impact[0].split(',')]
	topsis(filename[0],weight,impact)


if __name__ == "__main__":
	main()
