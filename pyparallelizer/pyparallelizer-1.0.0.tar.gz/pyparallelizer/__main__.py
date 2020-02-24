from pyparallelizer import Pyparallelizer
import pickle


def t(x):
    print(x.to_string())
    return x

def t_multi(x,args_list):
    print(args_list)
    print(x.to_string())
    return x

if "__name__" == "__main__":
    df = pd.read_pickle('flair_subset_corpus.pkl')
    df_parallelizer = Pyparallelizer(n_cpu=-1)
    df = df_parallelizer(df, function_to_Apply=t, output_column='output_col', input_columns=['goods','text'], func_args=[])