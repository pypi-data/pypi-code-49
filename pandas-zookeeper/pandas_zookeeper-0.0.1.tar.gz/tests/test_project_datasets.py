import os
import numpy as np
import pandas as pd
from pandas_zookeeper import main
import shapely


def run_df(df, name_conv):
    # demonstrate column simplification
    cols_orig = list(df)
    df.zookeeper.simplify_columns()
    print('Column mapping:')
    for col_1, col_2 in zip(cols_orig, list(df)):
        print('    %s: %s' % (col_1, col_2))
    # demonstrate memory usage reduction
    dtypes_orig = df.dtypes.to_dict().copy()
    len_orig = len(df)
    df = df.zookeeper.reduce_memory_usage(print_reduction=True)
    print('%i rows dropped' % (len_orig - len(df)))
    dtypes_end = df.dtypes.to_dict()
    print('Column conversions:')
    cols_unchanged = []
    for key, val in dtypes_end.items():
        if str(dtypes_orig[key]) != str(val):
            print('    %s: %s to %s' % (key, str(dtypes_orig[key]), str(val)))
        else:
            cols_unchanged.append(key)
    print('Columns that were not converted:')
    for col in cols_unchanged:
        print('    %s: %s' % (col, str(dtypes_orig[col])))
    cols_dropped = np.setdiff1d(list(dtypes_orig.keys()), list(dtypes_end.keys()))
    print('%i columns dropped:' % len(cols_dropped))
    for col in cols_dropped:
        print('    %s' % col)
    df.to_pickle(os.path.join(os.getcwd(), name_conv))


if __name__ == '__main__':
    # Daryl's file to test:
    file = r'C:\Users\ssmit\Integral Engineering Dropbox\Projects\M033 - SoCal DIMP Risk Metric Review\Engineering\2019-11-20 - Big Model\files\mainstable_20m.pkl'
    df = pd.read_pickle(file)
    run_df(df, 'test_01_converted.pkl')

    # Thomas's file to test:
    file = r'C:\Users\ssmit\Integral Engineering Dropbox\Public Data\PHMSA Pipeline Incident Data Set\Incidents\accident_hazardous_liquid_jan2010_present\accident_hazardous_liquid_jan2010_present.csv'
    df = pd.read_csv(file)
    run_df(df, 'test_02_converted.pkl')