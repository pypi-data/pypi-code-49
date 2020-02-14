# this file will have utility functions such as finding
# which columns are continuous and categorical


def _get_continuous_categorical_columns(feat):
    ''' 
    Finds out which columns are continuous and which
    are categorical in the given dataframe and 
    returns them as lists
    '''

    continuous_columns = []
    categorical_columns = []
    for col in feat.columns:
        if feat[col].dtype in [int, float]:
            if feat[col].unique().shape[0] / feat.shape[0] < 0.01:
                categorical_columns.append(col)
            else:
                continuous_columns.append(col)
        else:
            categorical_columns.append(col)

    return continuous_columns, categorical_columns
