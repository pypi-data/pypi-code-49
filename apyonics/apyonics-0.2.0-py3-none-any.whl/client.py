import warnings
import json
import time
import os

import requests
import pandas as pd
import numpy as np
from io import StringIO

# default url and api key
service_url='http://127.0.0.1:5000/'
api_key='nothing-special'

# if host_info.dat file found, take host info from it
homedir = os.path.expanduser('~')
hostfile = os.path.join(homedir,'.aionics_key')
if os.path.exists(hostfile):
    with open(hostfile,'r') as f:
        service_url = str(f.readline().strip())
        api_key = str(f.readline().strip())

class Client(object):

    def __init__(self,service_url=service_url,api_key=api_key):
        """Client initializer.

        Parameters
        ----------
        service_url : str
            Web URL pointing to your AIONICS service
        api_key : str
            API authorization key for your AIONICS service
        """
        super(Client,self).__init__()
        test_url = service_url+'test_connection'
        resp = requests.get(test_url, headers={'Api-Key':api_key})
        try:
            if resp.json()['response'] == 'connected to aionics service':
                self.service_url = service_url
                self.api_key = api_key
            else: 
                raise RuntimeError('unexpected response: {}'.format(resp.json()))
        except Exception as ex:
            raise RuntimeError('failed to connect to {} ({})'.format(service_url,ex))

    def compute_poscar_descriptors(self,poscar_dir,poscar_filenames=[]):
        """Compute descriptors from POSCAR files.

        Parameters
        ----------
        poscar_dir : str
            Path to directory containing POSCAR files on client's local filesystem
        poscar_filenames : list of str
            Filenames for POSCAR files in `poscar_dir`

        Returns
        -------
        resp : dict
            Dict containing computed descriptors or error report 
        """
        paths = {}
        files = {}
        for fn in poscar_filenames:
            paths[fn] = os.path.join(poscar_dir,fn)
            if not os.path.exists(paths[fn]):
                raise IOError('file path {} does not exist'.format(paths[fn]))
            files[fn] = open(paths[fn])
        resp = requests.post(
            self.service_url+'compute_poscar_descriptors',
            files=files,
            headers={'Api-Key':self.api_key}
            )
        return resp.json()

    def compute_cif_descriptors(self,cif_dir,cif_filenames=[]):
        """Compute descriptors from CIF files.

        Parameters
        ----------
        cif_dir : str
            Path to directory containing CIF files on client's local filesystem
        cif_filenames : list of str
            Filenames for CIF files in `cif_dir`

        Returns
        -------
        resp : dict
            Dict containing computed descriptors or error report 
        """
        paths = {}
        files = {}
        for fn in cif_filenames:
            paths[fn] = os.path.join(cif_dir,fn)
            if not os.path.exists(paths[fn]):
                raise IOError('file path {} does not exist'.format(paths[fn]))
            files[fn] = open(paths[fn])
        resp = requests.post(
            self.service_url+'compute_cif_descriptors',
            files=files,
            headers={'Api-Key':self.api_key})
        return resp.json()

    def run_fractional_cif_descriptors(self,cif_file,sample_size=100):
        """Compute descriptors from a CIF file with fractional occupancies.

        Parameters
        ----------
        cif_file : str
            Full path to a CIF file on client's local filesystem

        Returns
        -------
        resp : dict
            Dict containing featurization process id 
        """
        resp = requests.post(
            self.service_url+'compute_fractional_cif_descriptors',
            files={'cif':open(cif_file,'r')},
            params={'sample_size':sample_size},
            headers={'Api-Key':self.api_key})
        return resp.json()

    def sample_space_analysis(self,dspath_or_dsid,samples,input_keys):
        """Compute input space metrics for one or more samples relative to a dataset.

        Parameters
        ----------
        dspath_or_dsid : str or int
            Either a path to a csv file on the local filesystem (for using a local dataset),
            or an integer dataset index for the desired dataset (for using a saved dataset)
        samples : dict
            Dict of sample descriptors- keys are sample ids, 
            and values are dicts of sample descriptors. 
            The returned dict will have the same keys.
        input_keys : list
            List of input keys to be used in the analysis

        Returns
        -------
        resp : dict 
            Dict containing sample space metrics or error reports
        """
        if isinstance(dspath_or_dsid,int):
            resp = requests.post(
                self.service_url+'sample_space_analysis',
                params={'dataset_id':dspath_or_dsid,\
                        'samples':json.dumps(samples),\
                        'input_keys':json.dumps(input_keys)},
                headers={'Api-Key':self.api_key})
        elif isinstance(dspath_or_dsid,str):
            resp = requests.post(
                self.service_url+'sample_space_analysis',
                files={'dataset':open(dspath_or_dsid,'r')},
                params={'samples':json.dumps(samples),\
                        'input_keys':json.dumps(input_keys)},
                headers={'Api-Key':self.api_key}
                )
        result = resp.json()
        return result 


    def get_descriptors_by_mpid(self,mpid_or_mpids=[]):
        """Compute descriptors for one or more materials by Materials Project id. 

        Parameters
        ----------
        mpid_or_mpids : str or list of str 
            single mpid or list of mpids for the desired materials

        Returns
        -------
        resp : dict 
            If a single mpid was provided, the returned dict contains its descriptors.
            If a list of mpids was provided, the keys of the returned dict are the mpids, 
            and the values are dicts of descriptors or error reports
        """
        unpack = False
        mpids = mpid_or_mpids
        if not isinstance(mpid_or_mpids,list):
            mpids = [mpids]
            unpack = True
        resp = requests.get(
                self.service_url+'get_descriptors_by_mpid', 
                params={'mpids':json.dumps(mpids)},
                headers={'Api-Key':self.api_key})
        result = resp.json()
        if unpack:
            result = result[mpids[0]]
        return result 

    def get_dataset_index(self):
        """Get the dataset index from the server.

        Returns
        -------
        dataset_index : list
            List containing all valid dataset ids.
        """
        resp = requests.get(
            self.service_url+'get_dataset_index',
            headers={'Api-Key':self.api_key}
            )
        return resp.json()

    def get_model_index(self):
        """Get the model index from the server.

        Returns
        -------
        model_index : list
            List containing all valid model ids.
        """
        resp = requests.get(
            self.service_url+'get_model_index',
            headers={'Api-Key':self.api_key}
            )
        return resp.json()

    def get_process_index(self):
        """Get the process index from the server.

        Returns
        -------
        process_index : list
            List containing all valid process ids.
        """
        resp = requests.get(
            self.service_url+'get_process_index',
            headers={'Api-Key':self.api_key}
            )
        return resp.json()

    def upload_dataset(self,dataset_path):
        """Upload a new dataset to the server.

        Parameters
        ----------
        dataset_path : str
            Path to csv file containing the dataset on the local filesystem-
            the csv file should contain a column named 'id', 
            and this column should be valid as an index 
            (i.e. it should be unique for all samples in the dataset)

        Returns
        -------
        resp : dict
            Dict containing the new dataset's id or an error report
        """
        resp = requests.post(
            self.service_url+'save_dataset',
            files={'dataset':open(dataset_path)},
            headers={'Api-Key':self.api_key}
            )
        return resp.json()

    def get_dataset(self,dataset_id=0):
        """Get a saved dataset by its id.

        Returns either a dataset (as a pandas.DataFrame) if the query is successful,
        or an error report (as a dict) if the query fails.

        Parameters
        ----------
        dataset_id : int
            Integer index of the desired dataset

        Returns
        -------
        ds : pandas.DataFrame 
            DataFrame containing the dataset
        resp : dict
            Dict containing an error report 
        """
        resp = requests.get(
            self.service_url+'get_dataset',
            params={'dataset_id':dataset_id},
            headers={'Api-Key':self.api_key}
            )
        if 'error' in resp._content.decode():
            return resp.json()
        else:
            ds = pd.read_csv(StringIO(resp._content.decode()),index_col='id')
            return ds

    def get_descriptors_by_sample_id(self,dataset_id,sample_id_or_ids=[]):
        """Get the descriptors of samples from a saved dataset.

        Parameters
        ----------
        dataset_id : int
            Integer index of the desired dataset
        sample_id_or_ids : str or list of str
            Id or list of ids of the desired sample(s)

        Returns
        -------
        resp : dict
            If a single sample_id was provided, 
            the returned dict contains its descriptors.
            If a list of sample_ids was provided,
            the returned dict has sample_ids as keys, 
            and sample descriptors or error reports as values.
        """
        unpack = False
        sample_ids = sample_id_or_ids
        if not isinstance(sample_ids,list):
            sample_ids = [sample_ids]
            unpack = True
        resp = requests.get(
            self.service_url+'get_descriptors_by_sample_id', 
            params={'dataset_id':dataset_id,
            'sample_ids':json.dumps(sample_ids)},
            headers={'Api-Key':self.api_key}
            )
        result = resp.json()
        if unpack:
            result = result[sample_ids[0]]
        return result 

    def delete_dataset(self,dataset_id):
        """Delete a dataset.

        Deletes the dataset from the index 
        and wipes out all existing files associated with the dataset.
        This cannot be undone.

        Parameters
        ----------
        dataset_id : int
            Integer index of the dataset to delete

        Returns
        -------
        resp : dict
            Report of success or failure in deleting the dataset
        """
        resp = requests.get(
            self.service_url+'delete_dataset', 
            params={'dataset_id':dataset_id},
            headers={'Api-Key':self.api_key}
            )
        return resp.json()

    def run_logreg_combo_selection(self,dspath_or_dsid,min_feats,max_feats,input_keys,output_key,penalty='none',C=1.,n_folds=5):
        """Run combinatoric feature selection for a logistic regression model.

        Parameters
        ----------
        dspath_or_dsid : str or int
            Either a path to a csv file on the local filesystem (for using a local dataset),
            or an integer dataset index for the desired dataset (for using a saved dataset)
        min_feats : int
            Minimum number of features to investigate
        max_feats : int
            Maximum number of features to investigate
        input_keys : list
            Dataset columns to include as inputs (descriptors are selected from among these)
        output_key : str
            Column to use as the model output (must be a categorical column)
        penalty : str
            Penalty function for regularization ('none', 'l1', or 'l2')
        C : float
            Penalty term (high values of C effectively lead to lower regularization strength)
        n_folds : int
            Number of shuffle-split folds to use during cross-validation
            (provide any number larger than the dataset size to get leave-one-out cross-validation)

        Returns
        -------
        resp : dict
            Dict containing combinatoric selection process id 
        """
        if isinstance(dspath_or_dsid,int):
            resp = requests.get(
                self.service_url+'run_logreg_cfs_by_dsid',
                params={'dataset_id':dspath_or_dsid,
                        'min_feats':min_feats,'max_feats':max_feats,
                        'input_keys':json.dumps(input_keys),'output_key':output_key,
                        'penalty':penalty,'C':C,'n_folds':n_folds},
                headers={'Api-Key':self.api_key})
        elif isinstance(dspath_or_dsid,str):
            resp = requests.post(
                self.service_url+'run_logreg_cfs_from_data',
                files={'dataset':open(dspath_or_dsid)},
                params={'min_feats':min_feats,'max_feats':max_feats,
                        'input_keys':json.dumps(input_keys),'output_key':output_key,
                        'penalty':penalty,'C':C,'n_folds':n_folds},
                headers={'Api-Key':self.api_key})
        return resp.json()

    def train_logistic_regression(self,dspath_or_dsid,input_keys,output_key,penalty='none',C=1.,n_folds=5):
        """Train a logistic regression model.

        Parameters
        ----------
        dspath_or_dsid : str or int
            Either a path to a csv file on the local filesystem (for using a local dataset),
            or an integer dataset index for the desired dataset (for using a saved dataset)
        input_keys : list
            Dataset columns to include as inputs (descriptors are selected from among these)
        output_key : str
            Column to use as the model output (must be a categorical column)
        penalty : str
            Penalty function for regularization ('none', 'l1', or 'l2')
        C : float
            Penalty term (high values of C effectively lead to lower regularization strength)
        n_folds : int
            Number of shuffle-split folds to use during cross-validation
            (provide any number larger than the dataset size to get leave-one-out cross-validation)

        Returns
        -------
        resp : dict
            Dict containing new model id and training results, or error report
        """
        if isinstance(dspath_or_dsid,int):
            resp = requests.get(
                self.service_url+'train_logreg_from_dsid',
                params={'dataset_id':dspath_or_dsid,
                        'input_keys':json.dumps(input_keys),'output_key':output_key,
                        'penalty':penalty,'C':C,'n_folds':n_folds},
                headers={'Api-Key':self.api_key}
                )
        elif isinstance(dspath_or_dsid,str):
            resp = requests.post(
                self.service_url+'train_logreg_from_data',
                files={'dataset':open(dspath_or_dsid)},
                params={'input_keys':json.dumps(input_keys),'output_key':output_key,
                        'penalty':penalty,'C':C,'n_folds':n_folds},
                headers={'Api-Key':self.api_key}
                )
        return resp.json()

    def get_model_info(self,model_id):
        """Get information about a trained model.

        Parameters
        ----------
        model_id : int
            Integer id of the model to be queried.
    
        Returns
        -------
        resp : dict
            Dict containing model information
        """
        resp = requests.get(
            self.service_url+'get_model_info', 
            params={'model_id':model_id},
            headers={'Api-Key':self.api_key}
            )
        return resp.json()

    def delete_model(self,model_id):
        """Delete a model.

        Deletes the model from the index 
        and wipes out all existing files associated with the model.
        This cannot be undone.

        Parameters
        ----------
        model_id : int
            Integer id of the model to be deleted.

        Returns
        -------
        resp : dict
            Dict reporting success or failure in deleting the model.
        """
        resp = requests.get(
            self.service_url+'delete_model', 
            params={'model_id':model_id},
            headers={'Api-Key':self.api_key}
            )
        return resp.json()

    def apply_model(self,model_id,samples):
        """Apply a model to one or more samples by providing descriptors.

        Parameters
        ----------
        model_id : int
            Integer id of the model to be applied
        samples : dict 
            Dict of sample descriptors- keys are sample ids, 
            and values are dicts of sample descriptors. 
            The returned dict will have the same keys.

        Returns
        -------
        resp : dict
            Dict containing model results or error reports
        """
        resp = requests.get(
                self.service_url+'apply_model',
                params={'model_id':model_id,'samples':json.dumps(samples)},
                headers={'Api-Key':self.api_key}
                )
        result = resp.json()
        return result 

    #def predict_label(self,model_id,sample,label):
    #    """Apply a model to a sample to predict the likelihood of a given label. 
    #
    #    Parameters
    #    ----------
    #    model_id : int
    #    sample : dict
    #    label : object
    #
    #    Returns
    #    -------
    #    resp : dict
    #    """
    #    resp = requests.get(
    #            self.service_url+'predict_label',
    #            params={'model_id':model_id,'sample':json.dumps(sample),'label':label},
    #            headers={'Api-Key':self.api_key}
    #            )
    #    return resp.json()

    def apply_model_to_mpid(self,model_id,mpid_or_mpids):
        """Apply model to material(s) by providing the mpid(s) of the material(s).

        Parameters
        ----------
        model_id : int
            Integer id of the model to be applied
        mpid_or_mpids : str or list of str
            Materials Project id(s) of the material(s) to be evaluated

        Returns
        -------
        resp : dict or dict of dict
            Dict containing model results or error reports-
            if multiple mpids were provided, a dict of dicts is returned,
            with the mpids as keys and the results as values
        """
        unpack = False
        mpids = mpid_or_mpids 
        if not isinstance(mpids,list):
            mpids = [mpids]
            unpack = True
        resp = requests.get(
                self.service_url+'apply_model_to_mpid',
                params={'model_id':model_id,'mpids':json.dumps(mpids)},
                headers={'Api-Key':self.api_key}
                )
        result = resp.json()
        if unpack:
            if not 'error' in result: 
                result = result[mpids[0]]
        return result 

    def apply_model_to_samples(self,model_id,dataset_id,sample_id_or_ids):
        """Apply a model to a sample from a saved dataset.

        Parameters
        ----------
        model_id : int
            Integer id of the model ot be applied
        dataset_id : int
            Integer id of the dataset containing the sample of interest
        sample_id_or_ids : str or list of str
            Id or list of ids of the desired sample(s)

        Returns
        -------
        resp : dict
            If a single sample_id was provided, 
            the returned dict contains model results for that sample.
            If a list of sample_ids was provided,
            the returned dict has sample_ids as keys,
            and model results or error reports as values.
        """
        unpack = False
        sample_ids = sample_id_or_ids
        if not isinstance(sample_ids,list):
            sample_ids = [sample_ids]
            unpack = True
        resp = requests.get(
                self.service_url+'apply_model_to_sample',
                params={'model_id':model_id,'dataset_id':dataset_id,'sample_ids':json.dumps(sample_ids)},
                headers={'Api-Key':self.api_key}
                )
        result = resp.json()
        if unpack:
            if not 'error' in result: 
                result = result[sample_ids[0]]
        return result 

    def apply_model_to_poscar(self,model_id,poscar_dir,poscar_filenames):
        """Compute descriptors from a POSCAR file.

        Parameters
        ----------
        model_id : int
            Integer id of the model ot be applied
        poscar_dir : str
            Path to a directory containing POSCAR files on the local filesystem
        poscar_filenames : list of str
            Names of POSCAR files from the `poscar_dir` directory to be evaluated

        Returns
        -------
        resp : dict
            Dict containing model results or error reports,
            keyed by `poscar_filenames`
        """
        paths = {}
        files = {}
        for fn in poscar_filenames:
            paths[fn] = os.path.join(poscar_dir,fn)
            if not os.path.exists(paths[fn]):
                raise IOError('file path {} does not exist'.format(paths[fn]))
            files[fn] = open(paths[fn])
        resp = requests.post(
            self.service_url+'apply_model_to_poscar',
            params={'model_id':model_id},
            files=files,
            headers={'Api-Key':self.api_key}
            )
        return resp.json()

    def get_process_results(self,process_id,wait=False):
        """Fetch results or progress report of a long-running process 

        Parameters
        ----------
        process_id : int
            Integer id assigned to the feature selection process
            when it was initially launched
        wait : bool
            If True, the client will attempt to retrieve the result repeatedly,
            until the result is successfully returned.
            If False, the client may immediately return a report
            that expresses the progress of the feature selection.

        Returns
        -------
        resp : dict
            Dict containing progress report, results, or error report
        """
        first_iter = True
        while wait or first_iter:
            first_iter = False
            resp = requests.get(
                self.service_url+'get_results',
                params={'process_id':process_id},
                headers={'Api-Key':self.api_key}
                )
            resp = resp.json()
            if ('results' in resp) \
            and ('status' in resp['results']) \
            and (resp['results']['status']=='FINISHED'):
                wait = False
            elif wait:
                sleep_time = 1.
                if ('results' in resp):
                    sleep_time = resp['results']['est_time_remaining']*0.5
                if sleep_time < 1. or np.isinf(sleep_time): sleep_time = 1.
                time.sleep(sleep_time)
        return resp

    def get_logreg_combo_results(self,process_id,wait=False):
        """Same as get_process_results(), post-processed"""
        res_raw = self.get_process_results(process_id,wait)
        resp = res_raw.copy()
        if ('results' in resp):
            # if we have results, try to re-cast the keys as integers,
            # and re-cast performance metrics as floats
            all_result_keys = list(resp['results'].keys())
            for k in all_result_keys:
                try:
                    result = resp['results'][k]
                    result['best_f1'] = float(result['best_f1'])
                    result['best_precision'] = float(result['best_precision'])
                    result['best_accuracy'] = float(result['best_accuracy'])
                    result['best_recall'] = float(result['best_recall'])
                    resp['results'][int(k)] = result 
                    resp['results'].pop(k)
                except:
                    pass
        return resp

    def delete_results(self,process_id):
        """Delete results by providing the process_id

        Parameters
        ----------
        process_id : int
            Integer id assigned to the process
            when it was initially launched

        Returns
        -------
        resp : dict
            Dict containing a report of success or failure 
            in deleting the process results
        """
        resp = requests.get(
            self.service_url+'delete_results', 
            params={'process_id':process_id},
            headers={'Api-Key':self.api_key}
            )
        return resp.json()

