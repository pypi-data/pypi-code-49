import pandas as pd
import numpy as np
import datawig
import sys

def replace_missing_values(input_file, output_file):
    try:
        dataset = pd.read_csv(input_file)
    
    null_columns=dataset.columns[dataset.isnull().any()]
    filled_data=pd.DataFrame(0,index=np.arrange(len(dataset)),columns=null_columns)
    missing_value_count=list()
    
    for col in null_columns:
        null_cells=dataset[col].isnull()
        filled_cells=dataset[col].notnull()
        imputer=datawig.SimpleImputer(dataset.columns[dataset.columns!=col],col,'imputer_model') 
        imputer.fit(dataset[filled_cells])
        predicted=imputer.predict(dataset[null_cells])
        filled_data[col]=predicted[col+'_imputed']
        missing_value_count.append("Missing values replaced in "+ str(col) + " is "+ str(predicted.shape[0]))

    dataset = dataset.fillna(filled_data)
    dataset.to_csv(output_file)
    
    
    
    for i in missing_value_count:
        print("\n\n",i)

if __name__ == '__main__':
    print('EXPECTED ARGUMENTS TO BE IN ORDER : python <Program Name> <InputFile.csv> <OutputFile.csv>')
    if len(sys.argv) == 3:
        read_file = sys.argv[1]
        write_file = sys.argv[2]
        replace_missing_values(read_file, write_file)
    else:
        print("ERROR! WRONG NUMBER OF PARAMETERS")
        print("USAGES: $python <programName> <Input_File.csv> <Output_File.csv>")
        print('EXAMPLE: $python programName.py data.csv output.csv')