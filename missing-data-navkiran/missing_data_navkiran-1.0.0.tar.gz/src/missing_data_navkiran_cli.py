#!/usr/bin/env python

import sys
import numpy as np
import pandas as pd
from missing_data_navkiran import dropval,filler,impute

def main():
    arguments = sys.argv[1:]
    assert len(arguments) >= 2 and len(arguments) <= 4, "Wrong number of arguments provided, need atleast two or exactly four, third being method to handle NaN, fourth being the required parameter for that method"
    filename_in = arguments[0]
    filename_out = arguments[1]
    assert filename_in, "Input CSV filename must be provided"
    assert filename_out, "Output CSV filename must be provided"
    assert '.csv' in filename_in, "File extension must be .csv"
    assert '.csv' in filename_out, "File extension must be .csv"
    input_df = pd.read_csv(filename_in)
    if len(arguments) == 2:
        output = dropval(input_df)
        
    elif len(arguments) == 4:
        req_arg = int(arguments[3])
        if arguments[2] == 'DROP':
            output = dropval(input_df,along = req_arg)
        elif arguments[2] == 'FILL':
            output = filler(input_df,argument = req_arg)
        elif arguments[2] == 'IMPUTE':
            output = impute(input_df,argument = req_arg)
        else:
            print('Invalid arguments provided')
    else:
        print('Invalid number of arguments provided - need to be either 2 or exactly 4')
    
    output.to_csv(filename_out,index=False)