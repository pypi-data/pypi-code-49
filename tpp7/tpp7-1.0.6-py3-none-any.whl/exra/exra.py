
#importation du package numpy
import numpy as np

#Randomly extract Krand values from a vector and calculate the average of these values. Do it Ntimes times and return the vector of the averages

def extrac_random(data,Krand,Ntimes):

# find the dimension of data
    dim = np.size(data)
    
# create a vector me of Ntimes dimension
    me=np.zeros(Ntimes)

# For loop to fill the vector me
    for k in range(Ntimes):
# randomly draw Krand number between 1 and dim
        wh=np.random.randint(1,dim,Krand)

# extract the Krand values from data and calculate the average that is stored in me[k]       
        me[k]=np.mean(data[wh])
    return me
