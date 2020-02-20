import pandas as pd
import sys


def main():
    if(len(sys.argv)<2):
        print("use command 'python <package name> <input.csv>'")
        sys.exit(0)
    input_csv = sys.argv[1]
    try:
        data = pd.read_csv(input_csv)
    except OSError:
        print('ERROR in opening', input_csv)
        sys.exit(0)
        
   
    missing_values = ["n/a", "na", "--","nan","NaN"]
    df = pd.read_csv(input_csv, na_values = missing_values)
    print("Number of Missing values in differnt columns: ")
    print(df.isnull().sum())
    df = df.fillna(df.mean())
    print("Number of Missing values in differnt columns after processing: ")
    print(df.isnull().sum())
    df.to_csv("output_missing.csv",index=False)
    print("A file with name 'output_missing' is also saved in your current working directory")
    print(df)
    return df;
if __name__ == '__main__':
    main()
        
                
    
        
        



