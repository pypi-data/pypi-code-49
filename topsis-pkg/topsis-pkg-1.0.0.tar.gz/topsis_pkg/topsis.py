import numpy as np
import pandas as pd
import sys

def topsis(data, weight, impact):
    """
    Returns the topsis ranks corresponding to input alternatives
    
    Parameters:
        data (numpy array): 2 dim array of shape (m, n), with m alternatives and n features
        weight (list): list of n elements corresponding to their weights
        impact (list): list of "+"/"-" corresponding to positive/negative impact
    
    Returns:
        ranks (numpy array): 2d array of shape (m, 1) with ranks corresponding to alternatives
    """
    
    m = data.shape[0]
    n = data.shape[1]
    rms = np.zeros((1, n), dtype = float)
    for i in range(m):
        for j in range(n):
            rms[0, j] += data[i, j]**2
    
    rms = np.sqrt(rms)
    norm_data = data/rms    #Division taking advantage of python broadcasting
    w = np.array(weight)
    w = w.reshape((1, n))
    w = w/np.sum(w)
    weighted_norm_data = norm_data * w      #Multiplication taking advantage of python broadcasting
    
    A_best = np.zeros((1, n), dtype = float)    #Ideally best values of all features
    A_worst = np.zeros((1, n), dtype = float)   #Ideally worst values of all features
    for i in range(n):
        if(impact[i]=="+"):
            A_best[0, i] = np.max(weighted_norm_data, axis = 0)[i]
            A_worst[0, i] = np.min(weighted_norm_data, axis = 0)[i]
        elif(impact[i]=="-"):
            A_best[0, i] = np.min(weighted_norm_data, axis = 0)[i]
            A_worst[0, i] = np.max(weighted_norm_data, axis = 0)[i]
        else:
            print("\nError! Invalid input corresponding to impact")
            return
    
    d_best = np.zeros((m ,1), dtype = float)    #To store distances of alternatives with ideally best behaviour
    d_worst = np.zeros((m, 1), dtype = float)   #To store distances of alternatives with ideally worst behaviour
    for i in range(m):
        tmp_b = 0
        tmp_w = 0
        for j in range(n):
            tmp_b += (A_best[0, j]-weighted_norm_data[i, j])**2
            tmp_w += (A_worst[0, j]-weighted_norm_data[i, j])**2
        d_best[i, 0] = tmp_b**0.5
        d_worst[i, 0] = tmp_w**0.5
    
    s = d_worst/(d_best+d_worst)
    arg_s = s.argsort(axis = 0)
    ranks = np.zeros((m, 1))
    for i in range(m):
        ranks[arg_s[i, 0], 0] = m-i

    return ranks

def main():
    file_name = sys.argv[1]
    weight = sys.argv[2]
    impact = sys.argv[3]
    
    data_df = pd.read_csv(file_name)
    data_arr = data_df.values
    weight_list = weight.split(',')
    weight_list_n = []
    
    for i in weight_list:
        weight_list_n.append(float(i))
        
    impact_list = impact.split(',')
    ranks = topsis(data_arr, weight_list_n, impact_list)
    print("The ranks of alternatives are:")
    print(ranks)
    best_alt_idx = np.argmin(ranks)
    print("The best is alternative corresponding to row", best_alt_idx+1)

if __name__ == "__main__":
    main()
