
# [[file:~/Research/CFEDemands/Files/input_files.org][No\ heading:1]]

# Tangled on Tue Feb 25 14:12:20 2020
import numpy as np
import pandas as pd
from collections import defaultdict

def construct_df(VARS,INDICES):
    """ 
    Compile data on a collection of variables from one or more Stata =dta= files into a single pandas DataFrame.

    Ethan Ligon                                              February 2020
    """

    def construct_column(df,Mapping):
        try:
            return df[Mapping]
        except KeyError:
            return df.apply(eval(Mapping),axis=1)

    def read_and_index(fn,indices):
        df = pd.read_stata(fn).rename(columns=dict(map(reversed, indices.items())))
        df['t'] = indices['t']
        for index in indices.keys(): # Cast to simplest type (int or str)
            try:
                df[index] = df[index].astype(int)
            except ValueError:
                df[index] = df[index].astype(str)
        df.set_index(list(indices.keys()),inplace=True)
        return df

    DFs = defaultdict(list)
    file_groups = INDICES.groupby('File')
    for group in VARS.groupby(['t','File']):
        fn = group[0][1]
        mydf = read_and_index(group[0][1],INDICES.loc[fn].to_dict())
        d = {}
        for v in group[1].itertuples():
            d[v.Output] = construct_column(mydf,v.Mapping)
            try:
                idx,op = eval(v.Grouping)
                groups = d[v.Output].groupby([idx,'t'])
                if op == sum:
                    d[v.Output] = groups.sum()
                else:
                    d[v.Output] = groups.apply(op)
            except (ValueError,TypeError): pass

        DFs[group[0][0]].append(pd.DataFrame(d))

    by_year = []
    for t in DFs.keys():
        df_for_year = pd.concat(DFs[t],join='inner',axis=1)
        assert not any(df_for_year.columns.duplicated()), "Duplicate output columns not allowed; t=%s." % t
        by_year.append(df_for_year)
    
    df = pd.concat(by_year,axis=0)
    return df

# No\ heading:1 ends here
