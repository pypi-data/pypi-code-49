import scipy.stats as stats
import numpy as np
import pandas as pd

def summarize(df,pvalues=False,std=True,count=True,quartiles=False):
    """
    Compute a summary for a dataframe of portfolios.

    Parameters
    ----------
    df: pandas.core.frame.DataFrame
        DataFrame with portfolio returns in each column.
    pvalues: bool
        Whether to report pvalues. 
    std: bool
        Whether to report the standard deviations of portfolio returns.
    count: bool
        Whether to report the return count for each portfolio.
    quartiles: bool
        Whether to report quartiles for returns.
  
    Returns
    -------
    output: pandas.core.frame.DataFrame
        Summary DataFrame including by default t-statistics testing that the mean returns for each portfolio are zero, 
        the count for each portfolio, the mean return for each portfolio, and the standard deviation for each 
        portfolio. 

    """
    s = df.describe().T
    s['tstat'] = s['mean']/(s['std']/np.sqrt(s['count'])) # t-statistic testing that the mean return is zero
    s['pval'] = stats.t.sf(np.abs(s['tstat']),s['count']-1)*2 # 2-sided p-value for the t-statistic
    retlst = ['mean','tstat']
    if std:
        retlst.insert(1,'std')
    if quartiles:
        retlst.insert(0,'max')
        retlst.insert(0,'75%')
        retlst.insert(0,'50%')
        retlst.insert(0,'25%')
        retlst.insert(0,'min')
    if count:
        retlst.insert(0,'count')
    if pvalues:
        retlst.append('pval')
    return s[retlst].T