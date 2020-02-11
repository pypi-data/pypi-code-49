#!/usr/bin/env python

import sys
from outliers_navkiran import remove_outliers_iqr,remove_outliers_z

def main():
    arguments = sys.argv[1:]
    assert len(arguments) >= 2 and len(arguments) <= 4, "Wrong number of arguments provided, need atleast two or exactly four (threshold as third arg, method(z_score or IQR) as fourth - both provided together)\n Example : outliers_navkiran_cli infile.csv outfile.csv 1.5 z_score"
    
    filename_in = arguments[0]
    filename_out = arguments[1]
    assert filename_in, "Input CSV filename must be provided"
    assert filename_out, "Output CSV filename must be provided"
    assert '.csv' in filename_in, "File extension must be .csv"
    assert '.csv' in filename_out, "File extension must be .csv"
    
    if (len(arguments)==4):
        threshold = float(arguments[2])
        method = arguments[3]
        assert method in ['z_score','IQR'],"Method should be either z_score or IQR"
        if (arguments[3]=='IQR'):
            remove_outliers_iqr(filename_in,filename_out,threshold)
        else:
            remove_outliers_z(filename_in, filename_out,threshold)
    else:
        threshold = 1.5
        remove_outliers_iqr(filename_in,filename_out,threshold)



	
