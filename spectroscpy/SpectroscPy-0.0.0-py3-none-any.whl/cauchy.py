# SpectroscPy 0.0.0
# SpectroscPy is a script package developed by and containing contributions from

    # Karen Oda Hjorth Dundas
    # Magnus Ringholm
    # Yann Cornation
    # Benedicte Ofstad

# The package is released under a LGPL licence.
# For questions, please contact on karen.o.dundas@uit.no

# Module for prepping values for the Cauchy distribution/Lorentzian lineshape
from sys import exit
import numpy as np
from math import pi

def get_interquartile_range(x):

    x_range = len(x)

    if (x_range == 1):
        print('\n')
        print('Error in get_interquartile_range')
        print('It does not make sense to look the IQR for only one value.  Something is wrong')
        exit()

    if (x_range%2 == 0):
        n = int(x_range/2)
    elif(x_range%2 == 1):
        n = int((x_range - 1)/2)

    lower_x = []
    upper_x = []
    temp_x = []

    for i in range(x_range):
        temp_x.append(x[i])

    temp_x.sort()

    for i in range(n):
        lower_x.append(temp_x[i])
        upper_x.append(temp_x[x_range - i - 1])

    if (n%2 == 0):
        lower_median = (lower_x[int(n/2) - 1] + lower_x[int(n/2 + 1) - 1])/2
        upper_median = (upper_x[int(n/2) - 1] + upper_x[int(n/2 + 1) - 1])/2
    elif (n%2 == 1):
        lower_median = lower_x[int((n + 1)/2) - 1]
        upper_median = upper_x[int((n + 1)/2) - 1]

    iqr = upper_median - lower_median

    return iqr


# For description of the different plotting options, checkout my doc on the subject, or thesis after 
# 2020
# 1) Given gamma, all snapshots (GS).  This one has a value sent in instead of a keyword
# 2) Width based gamma, all snapshots (WS)
# 3) Width base gamma, averaged values (WA)
def get_gamma(cauchy_type, a):

    if (cauchy_type == 'WS' or cauchy_type == 'WA'):

        num_snapshots = len(a)
        num_peaks = len(a[0])
        gamma = np.zeros(num_peaks)

        for i in range(num_peaks):

            x = []
            for j in range(num_snapshots):
                x.append(a[j][i])

            gamma[i] = get_interquartile_range(x)

        if (cauchy_type == 'WS'):
            gamma = np.multiply(gamma, 1/(2*num_snapshots))
        elif (cauchy_type == 'WA'):
            gamma = np.multiply(gamma, 1/2)

    # GS
    else:
        gamma = [cauchy_type]

    return gamma


def cauchy_lincomb(x, y, gamma, x_fit):

    num_peaks = len(x)
    y_fit = np.zeros((len(x_fit)))

    if (len(gamma) == 1):

        gamma_constant = gamma[0]

        for i in range(len(x_fit)):
            for k in range(num_peaks):
                y_fit[i] = y_fit[i] + y[k]*gamma_constant/(pi*((x_fit[i] - x[k])**2 + \
                                                           gamma_constant**2))

    else:

        for i in range(len(x_fit)):
            for k in range(num_peaks):
                if (y[k] != 0.0):
                    y_fit[i] = y_fit[i] + y[k]*gamma[k]/(pi*((x_fit[i] - x[k])**2 + \
                                                              gamma[k]**2))


    return y_fit


def get_weighted_averages(x, y):

    avg_y = sum(y)/len(y)

    avg_x = 0
    for i in range(len(x)):
        avg_x = avg_x + x[i]*y[i]

    avg_x = avg_x/(avg_y*len(x))

    return avg_x, avg_y


# Requires x and y have the same shape
# Makes averages over all values of a specific column
def get_set_of_weighted_averages(x, y):

    row_x = len(x)
    col_x = len(x[0])

    avg_x = np.zeros(col_x)
    avg_y = np.zeros(col_x)

    if (col_x == 1):
        for i in range(row_x):
            avg_x[i] = copy.deepcopy(x[0][i])
            avg_y[i] = copy.deepcopy(y[0][i])

    else:
        for i in range(col_x):
            temp_x = []
            temp_y = []

            for j in range(row_x):
                temp_x.append(x[j][i])
                temp_y.append(y[j][i])

            avg_x[i], avg_y[i] = get_weighted_averages(temp_x, temp_y)

    return avg_x, avg_y

def get_simple_averages(x):

    row_x = len(x)
    col_x = len(x[0])

    avg_x = np.zeros(col_x)

    if (col_x == 1):
        for i in range(row_x):
            avg_x[i] = copy.deepcopy(x[0][i])

    else:
        for i in range(col_x):
            temp_x = []

            for j in range(row_x):
                temp_x.append(x[j][i])

            avg_x[i] = sum(temp_x)/row_x

    return avg_x
