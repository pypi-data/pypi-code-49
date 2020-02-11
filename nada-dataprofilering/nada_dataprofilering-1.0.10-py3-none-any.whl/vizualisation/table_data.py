import pandas as pd


def make_table_data(df, threshold=10):
    df_sorted = df.sort_values('ANTALL', ascending=False)

    try:
        df_sorted['VERDI'] = df_sorted['VERDI'].apply(lambda x: x.strftime('%d-%m-%Y'))
    except AttributeError:
        pass

    if df_sorted.shape[0] > threshold:
        counts_list = list(df_sorted['ANTALL'].iloc[:threshold - 1])
        values_list = list(df_sorted['VERDI'].iloc[:threshold - 1])

        counts_list.append(df_sorted['ANTALL'].iloc[threshold - 1:].sum())
        values_list.append('Andre')
    else:
        counts_list = list(df_sorted['ANTALL'])
        values_list = list(df_sorted['VERDI'])

    return [[str(values_list[i]), str(counts_list[i])] for i in range(len(counts_list))]








