import argparse
import pandas as pd
import numpy as np

def topsis(filename,w,i):

	

	data = pd.read_csv(filename+'.csv')
	data = data.values[:,1:]

	

	normalizationFactor=np.sqrt(np.sum(data**2,axis=0,dtype=float),dtype=float)

	normalizedData=(data/normalizationFactor)


	normalizedData=np.round(normalizedData.astype(np.float64),decimals=3)
	
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

	ranks=ranks.reshape(ranks.shape[0],)

	print("Item","Rank",sep="\t")
	for idx,x in enumerate(ranks):
	    print(idx+1,ranks.shape[0]-(x),sep="\t",end="\n")
        
   
def main():
	# create argument parser object
	parser = argparse.ArgumentParser(description = "Topsis Analysis")

	parser.add_argument("-n", "--name", type = str, nargs = 1,
	                    metavar = "name", default = None, help = "Name of csv file")

	parser.add_argument("-w", "--weight", type = str, nargs = 1,
	                    metavar = "weight", default = None, help = "Weights of attribute")

	parser.add_argument("-i", "--impact", type = str, nargs = 1,
	                    metavar = "impact", default = [1], help = "Impact of attribute")

	# parse the arguments from standard input
	args = parser.parse_args()

	filename=args.name
	weight=[float(w) for w in args.weight[0].split(',')]
	impact=[int(im) for im in args.impact[0].split(',')]
	topsis(filename[0],weight,impact)


if __name__ == "__main__":
	main()


