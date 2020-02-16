
project(datafile,weights,impacts):
	import sys
	if (len(sys.argv)<4 ):
    		#print ("Try This: python topsis.py <InputDataFile> <Weights> <Impacts>")
    		#print ("Example: python topsis.py myData.csv 1,2,1,1 +,+,-,+ ")
    	sys.exit()


	datafile = sys.argv[1]
	weights = str(sys.argv[2])
	impacts = str(sys.argv[3])

	import pandas as pd
	try:
    		file = pd.read_csv(datafile)
   
	except FileNotFoundError:
    	#print("The file does not Exist")
    	sys.exit()
   
	import pandas as pd
	import math
	import numpy as np
	df = pd.read_csv(datafile)
	wts = weights.split(",")
	its = impacts.split(",")
	its=np.array(its)

	wts = [int(i) for i in wts]
	sumw=sum(wts)
	wts2 = []
	for i in wts:
    	wts2.append(wts[i]/sumw)
   
	if(len(df.columns)!=len(wts) or len(df.columns)!=len(its)):
    	#print("Error:Arguments are incorrect")
    	sys.exit()
	h=len(df.columns)
	df2=np.array(df)
	ideal_best=[]
	ideal_worst=[]
	for j in range(0,h):
            k = math.sqrt(sum(df2[:,j]*df2[:,j]))
            maxx = 0
            minn = 1
            for i in range(0,len(df.index)):
                df2[i,j] = (df2[i,j]/k)*wts2[j]
                if df2[i,j]>maxx:
                    maxx = df2[i,j]
                if df2[i,j]<minn:
                    minn = df2[i,j]
            if its[j] == "+":
                ideal_best.append(maxx)
                ideal_worst.append(minn)
            else:
                ideal_best.append(minn)
                ideal_worst.append(maxx)
	p = []
	for i in range(0,len(df.index)):
            a = math.sqrt(sum((df2[i]-ideal_worst)*(df2[i]-ideal_worst)))
            b = math.sqrt(sum((df2[i]-ideal_best)*(df2[i]-ideal_best)))
            lst = []
            lst.append(i)
            lst.append(a/(a+b))
            p.append(lst)
import sys

def main():
    print(sys.argv)
    weights=[float(i) for i in sys.argv[2].split(',')]
    datafile=pd.read_csv(sys.argv[1]).values
    impacts=sys.argv[3].split(',')
    topsis(datafile,weights,impacts)

if __name__=="__main__":
    main()
