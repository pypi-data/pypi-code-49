import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from .client import *

def add_to_dataset(ds,sample_or_samples):
    """Add a sample to a dataset.

    Parameters
    ----------
    ds : pandas.DataFrame
        Dataset to be augmented
    sample : dict or list of dict
        Sample(s) to add to the dataset- 
        every sample must have a value for each column in the dataset

    Returns
    -------
    new_ds : pandas.DataFrame
        The input dataset with the new sample(s) included
    """
    ds_cols = list(ds.columns)
    samples = sample_or_samples
    if not isinstance(samples,list):
        samples = [samples]
    for sample in samples:
        samp_cols = sample.keys()
        for col in samp_cols:
            if not col in ds_cols:
                sample.pop(col)
        samp_cols = sample.keys()
        for col in ds_cols:
            if not col in samp_cols:
                raise KeyError('sample does not contain an entry for {}'.format(col))
        new_ds = ds.append(sample,ignore_index=True,verify_integrity=True)
    return new_ds

def save_dataset(ds,filepath):
    """Save a dataset to a local file.

    Parameters
    ----------
    ds : pandas.DataFrame
        Dataset to be saved
    filepath : str
        Path to a local csv file where the dataset should be saved
    """
    ds.to_csv(filepath,index_label='id')

def get_binary_classification_results(results,label_to_evaluate):
    """Unpack classification results to yield binary results wrt a given label.

    Parameters
    ----------
    results : object
        Return value of an apply_model() function call.
    label_to_evaluate : object
        The returned result will be True if the model result
        is equal to `label_to_evaluate`, else False.
        The returned likelihoods will refer to the likelihood
        of the model result to be equal to `label_to_evaluate`.

    Returns
    -------
    results : object 
        The same as the input, with results repackaged,
        such that the result is binary wrt `label_to_evaluate`,
        and only the likelihood for `label_to_evaluate` is retained
    """
    if isinstance(results,list):
        binres = []
        for res in results:
            binres.append(_unpack_cl_result(res,label_to_evaluate))
    elif isinstance(results,dict):
        binres = {} 
        for k,res in results.items():
            binres[k] = _unpack_cl_result(res,label_to_evaluate)
    else:
        binres = _unpack_cl_result(results,label_to_evaluate)
    return binres

def _unpack_cl_result(cl_result,label):
    if not label in cl_result['classes']:
        raise ValueError('label {} is not a valid model output ({})'.format(label,cl_result['classes']))
    label_result = bool(cl_result['result']==label)
    label_idx = cl_result['classes'].index(label)
    label_likelihood = cl_result['probability'][0][label_idx]
    label_log_likelihood = cl_result['log_probability'][0][label_idx]
    binres = dict(result=label_result,likelihood=label_likelihood,log_likelihood=label_log_likelihood) 
    return binres
    
def plot_logreg_cfs(results,file_path=None,show=False):
    """Plot the results of logistic regression combinatoric feature selection

    Parameters
    ----------
    results : dict
        Dict of results, for example, client.get_process_results(0)['results']
    file_path : str 
        If provided, figure is printed to this path 
    show : bool
        Determines whether or not the figure should be displayed

    Returns
    -------
    fig : matplotlib.figure.Figure
        matplotlib Figure object containing the rendered plot
    """
    fig = plt.figure()
    n_feats_list = []
    for k in results.keys():
        try: 
            n_feats_list.append(int(k))
        except:
            pass
    n_feats = np.sort(np.array(n_feats_list))
    f1 = [results[nf]['best_f1'] for nf in n_feats]
    prec = [results[nf]['best_precision'] for nf in n_feats]
    rec = [results[nf]['best_recall'] for nf in n_feats]
    acc = [results[nf]['best_accuracy'] for nf in n_feats]
    plt.plot(n_feats,f1)
    plt.plot(n_feats,prec)
    plt.plot(n_feats,rec)
    plt.plot(n_feats,acc)
    plt.legend(['f1','precision','recall','accuracy'])
    plt.title('best performance metrics over all combinations')
    plt.xlabel('number of features')
    plt.ylabel('performance metrics')
    if file_path: plt.savefig(file_path)
    if show: plt.show()
    return fig

