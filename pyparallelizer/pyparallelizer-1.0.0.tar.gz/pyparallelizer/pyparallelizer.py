import pandas as pd
import numpy as np
import itertools
from multiprocessing import  Pool, cpu_count 
from tqdm import tqdm, tqdm_notebook
try:
    tqdm_notebook.tqdm.pandas(desc="chunk process")
except:
    tqdm.pandas(desc="chunk process")



class Pyparallelizer:
    def __init__(self, n_cpu=-1):
        # Select all cores by default
        self.n_cores = self.select_cores(n_cpu)
    
    
    def select_cores(self, n_cpu):
        if n_cpu == -1:
            return cpu_count()
        elif n_cpu > 1:
            if n_cpu <= cpu_count():
                return n_cpu
            else:
                return cpu_count()
        else:
            raise ValueError('__init__: Number of cpu is not well define')
        

    def func(self, df, _args):
        column = _args[0]
        c_func = _args[1]
        col_apply_on = _args[2]
        if len(_args) > 3:
            func_args = _args[3:]
            df[column] = df[col_apply_on].progress_apply(lambda x: c_func(x, func_args), axis=1)
        else:
            df[column] = df[col_apply_on].progress_apply(c_func, axis=1)
        return df

    
    def func_processor(self, args):
        return self.func(*args)


    def parallelize_dataframe(self, df, func_processor=func_processor, **kwargs):
        try:
            if kwargs['output_column']:
                if isinstance(kwargs['output_column'],str):
                    column = kwargs['output_column']
                else:
                    return ValueError('parallelize_dataframe : Column name output is not well define.')
        except:
            column = 'pyparallelizer_col'
        try:
            col_apply_on = kwargs['input_columns']
        except:
            col_apply_on = list(df.columns)
        try:
            func_args = kwargs['func_args']
        except:
            func_args = []
        
        if func_args:
            _args = [column,kwargs['function_to_Apply'],col_apply_on] + func_args
        else:
            _args = [column,kwargs['function_to_Apply'],col_apply_on]

        if len(df) < self.n_cores:
            self.n_cores = len(df)
        df_split = np.array_split(df, self.n_cores)
        with Pool(self.n_cores) as pool:
            df = pd.concat(pool.map(self.func_processor, zip(df_split, itertools.repeat(_args))))
        return df
    