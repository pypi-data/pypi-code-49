from urllib3 import PoolManager
from urllib3 import Timeout
import json
import os
import tarfile
from .rest import simple_get
from .rest import simple_delete
from .rest import simple_post
from .rest import multipart_post
import numpy as np

__all__ = ['BoonException', 'NanoHandle']


############################
# BoonNano Python API v3 #
############################


class BoonException(Exception):
    def __init__(self, message):
        self.message = message


class NanoHandle:

    def __init__(self, license_id='default', license_file="~/.BoonLogic.license", timeout=120.0):
        """Primary handle for BoonNano Pod instances

        The is the primary handle to manage a nano pod instance

        Args:
            license_id (str): license identifier label found within the .BoonLogic.license configuration file
            license_file (str): path to .BoonLogic.license license file
            timeout (float): read timeout for http requests

        """
        self.license_file = license_file
        self.license_id = None
        self.api_key = None
        self.api_tenant = None
        self.instance = ''
        self.numeric_format = ''

        license_path = os.path.expanduser(license_file)

        if os.path.exists(license_path):
            try:
                with open(license_path, "r") as json_file:
                    file_data = json.load(json_file)
            except json.JSONDecodeError as e:
                raise BoonException(
                    "json formatting error in .BoonLogic.license file, {}, line: {}, col: {}".format(e.msg, e.lineno, e.colno))
        else:
            raise BoonException("file {} does not exist".format(license_path))

        # load the license block, environment gets precedence
        license_env = os.getenv('BOON_LICENSE_ID')
        if license_env:
            # license id was specified through environment
            if license_env in file_data:
                self.license_id = license_env
            else:
                raise BoonException("BOON_LICENSE_ID value of '{}' not found in .BoonLogic.license file".format(license_env))
        else:
            if license_id in file_data:
                self.license_id = license_id
            else:
                raise BoonException("license_id '{}' not found in .BoonLogic.license file".format(license_id))

        license_block = file_data[self.license_id]

        # load the api-key, environment gets precedence
        self.api_key = os.getenv('BOON_API_KEY')
        if not self.api_key:
            if 'api-key' not in license_block.keys():
                raise BoonException(
                    "'api-key' is missing from configuration, set via BOON_API_KEY or in ~/.BoonLogic.license file")
            self.api_key = license_block['api-key']

        # load the server, environment gets precedence
        self.server = os.getenv('BOON_SERVER')
        if not self.server:
            if 'server' not in license_block.keys():
                raise BoonException(
                    "'server' is missing from configuration, set via BOON_SERVER or in ~/.BoonLogic.license file")
            self.server = license_block['server']

        # load the tenant, environment gets precedence
        self.api_tenant = os.getenv('BOON_TENANT')
        if not self.api_tenant:
            if 'api-tenant' not in license_block.keys():
                raise BoonException(
                    "'api-tenant' is missing from configuration, set via BOON_TENANT or in ~/.BoonLogic.license file")
            self.api_tenant = license_block['api-tenant']

        # set up base url
        self.url = self.server + '/expert/v3/'
        if "http" not in self.server:
            self.url = "http://" + self.url

        # create pool manager
        timeout_inst = Timeout(connect=30.0, read=timeout)
        self.http = PoolManager(timeout=timeout_inst)

    def open_nano(self, instance_id):
        """Creates or attaches to a nano pod instance

        Args:
            instance_id (str): instance identifier to assign to new pod instance

        Returns:
            boolean: true if successful (instance is created or attached)

            str: None when result is true, error string when result=false

        """
        instance_cmd = self.url + 'nanoInstance/' + instance_id + '?api-tenant=' + self.api_tenant

        success, response = simple_post(self, instance_cmd)
        if not success:
            return False, response

        self.instance = instance_id
        return success, response

    def close_nano(self):
        """Closes the pod instance

        Returns:
            result (boolean):  true if successful (nano pod instance was closed)
            response (str): None when result is true, error string when result=false

        """
        close_cmd = self.url + 'nanoInstance/' + self.instance + '?api-tenant=' + self.api_tenant

        # delete instance
        result, response = simple_delete(self, close_cmd)
        if not result:
            return result, response

        self.http.clear()
        return result, None

    def nano_list(self):
        """returns list of nano instances allocated for a pod

        Returns:
            result (boolean):  true if successful (list was returned)
            response (str): json dictionary of pod instances when result=true, error string when result=false

        """

        # build command
        instance_cmd = self.url + 'nanoInstances' + '?api-tenant=' + self.api_tenant

        return simple_get(self, instance_cmd)

    def save_nano(self, filename):
        """serialize a nano pod instance and save to a local file

        Args:
            filename (str): path to local file where saved pod instance should be written

        Returns:
            result (boolean):  true if successful (pod instance was written)
            response (str): None when result is true, error string when result=false

        """

        # build command
        snapshot_cmd = self.url + 'snapshot/' + self.instance + '?api-tenant=' + self.api_tenant

        # serialize nano
        result, response = simple_get(self, snapshot_cmd)
        if not result:
            return result, response

        # at this point, the call succeeded, saves the result to a local file
        try:
            with open(filename, 'wb') as fp:
                fp.write(response)
        except Exception as e:
            return False, e

        return True, None

    def restore_nano(self, filename):
        """restore a nano pod instance from local file

        Args:
            filename (str): path to local file containing saved pod instance

        Returns:
            result (boolean):  true if successful (nano pod instance was restored)
            response (str): None when result is true, error string when result=false

        """

        # verify that input file is a valid nano file (gzip'd tar with Magic Number)
        try:
            with tarfile.open(filename, 'r:gz') as tp:
                with tp.extractfile('BoonNano/MagicNumber') as magic_fp:
                    magic_num = magic_fp.read()
                    if magic_num != b'\xef\xbe':
                        return False, 'file {} is not a Boon Logic nano-formatted file, bad magic number'.format(
                            filename)

        except KeyError:
            return False, 'file {} is not a Boon Logic nano-formatted file'.format(filename)

        with open(filename, 'rb') as fp:
            nano = fp.read()

        # build command
        snapshot_cmd = self.url + 'snapshot/' + self.instance + '?api-tenant=' + self.api_tenant

        fields = {'snapshot': (filename, nano)}

        result, response = multipart_post(self, snapshot_cmd, fields=fields)

        if not result:
            return result, response

        self.numeric_format = response['numericFormat']

        return True, response

    def configure_nano(self, feature_count=10, numeric_format="float32", min=1, max=10, weight=1, labels="",
                       percent_variation=0.05, streaming_window=1, accuracy=0.99, config=None):
        """returns the posted clustering configuration

         Args:
             feature_count (int): number of features per vector
             numeric_format (str): numeric type of data (one of "float32", "uint16", or "int16")
             min (float):
             max (float):
             weight (float):
             labels (list):
             percent_variation (float):
             streaming_window (integer):
             accuracy (float):
             config (dict):

         Returns:
             result (boolean): true if successful (configuration was successfully loaded into nano pod instance)
             response (dict or str): configuration dictionary when result is true, error string when result is false

         """

        # verify numeric_format
        if numeric_format not in ['float32', 'int16', 'uint16']:
            return False, 'numeric_format must be "float32", "int16", or "uint16"'

        # build command
        config_cmd = self.url + 'clusterConfig/' + self.instance + '?api-tenant=' + self.api_tenant
        if not config:
            new_config = generate_config(numeric_format, feature_count, min, max, weight, labels, percent_variation,
                                         streaming_window, accuracy)
        else:
            new_config = config

        body = json.dumps(new_config)

        result, response = simple_post(self, config_cmd, body=body)
        if result:
            self.numeric_format = new_config['numericFormat']

        return result, response

    def autotune_config(self, autotune_pv=True, autotune_range=True, by_feature=False, exclusions=None):
        """autotunes the percent variation, min and max for each feature

        Args:
            autotune_pv (boolean):
            autotune_range (boolean):
            by_feature (boolean):
            exclusions (boolean):

        Returns:
            result (boolean): true if successful (autotuning was completed)
            response (dict or str): configuration dictionary when result is true, error string when result is false

        """

        # build command
        config_cmd = self.url + 'autoTuneConfig/' + self.instance + '?api-tenant=' + self.api_tenant
        config_cmd += '&byFeature=' + str(by_feature).lower()
        config_cmd += '&autoTunePV=' + str(autotune_pv).lower()
        config_cmd += '&autoTuneRange=' + str(autotune_range).lower()
        if exclusions:
            config_cmd += '&exclusions=' + str(exclusions)[1:-1].replace(' ', '')

        # autotune parameters
        return simple_post(self, config_cmd)

    def get_config(self):
        """gets the configuration for this nano pod instance

        Returns:
            result (boolean): true if successful (configuration was found)
            response (dict or str): configuration dictionary when result is true, error string when result is false

        """
        config_cmd = self.url + 'clusterConfig/' + self.instance + '?api-tenant=' + self.api_tenant
        return simple_get(self, config_cmd)

    def load_file(self, file, file_type, gzip=False, metadata=None, append_data=False):
        """load nano data from a file

        Args:
            file (str): local path to data file
            file_type (str): file type specifier, must be either 'cvs' or 'raw'
            gzip (boolean): true if file is gzip'd, false if not gzip'd
            metadata (list): list of data labels to attach to data fields
            append_data (boolean): true if data should be appended to previous data, false if existing
                data should be truncated

        Returns:
            result (boolean): true if successful (file was successful loaded into nano pod instance)
            response (str): None when result is true, error string when result=false

        """

        # load the data file
        try:
            with open(file) as fp:
                file_data = fp.read()
        except FileNotFoundError as e:
            return False, e.strerror

        # verify file_type is set correctly
        if file_type not in ['csv', 'csv-c', 'raw', 'raw-n']:
            return False, 'file_type must be "csv", "csv-c", "raw" or "raw-n"'

        file_name = os.path.basename(file)

        if metadata:
            fields = {'data': (file_name, file_data),
                      'metadata': metadata.replace(',', '|').replace('{', '').replace('}', '').replace(' ', '')}
        else:
            fields = {'data': (file_name, file_data)}

        # build command
        dataset_cmd = self.url + 'data/' + self.instance + '?api-tenant=' + self.api_tenant
        dataset_cmd += '&fileType=' + file_type
        dataset_cmd += '&gzip=' + str(gzip).lower()
        dataset_cmd += '&appendData=' + str(append_data).lower()

        return multipart_post(self, dataset_cmd, fields=fields)

    def load_data(self, data, metadata=None, append_data=False):
        """load nano data from an existing numpy array or simple python list

        Args:
            data (np.ndarray or list): numpy array or list of data values
            metadata (list): list of data labels to attach to data fields
            append_data (boolean): true if data should be appended to previous data, false if existing
                data should be truncated

        Returns:
            result (boolean): true if successful (data was successful loaded into nano pod instance)
            response (str): None when result is true, error string when result=false

        """

        if not isinstance(data, np.ndarray):
            if self.numeric_format == 'int16':
                data = np.asarray(data, dtype=np.int16)
            elif self.numeric_format == 'float32':
                data = np.asarray(data, dtype=np.float32)
            elif self.numeric_format == 'uint16':
                data = np.asarray(data, dtype=np.uint16)

        if self.numeric_format == 'int16':
            data = data.astype(np.int16)
        elif self.numeric_format == 'float32':
            data = data.astype(np.float32)
        elif self.numeric_format == 'uint16':
            data = data.astype(np.uint16)
        data = data.tostring()
        file_name = 'dummy_filename.bin'
        file_type = 'raw'

        if metadata:
            fields = {'data': (file_name, data),
                      'metadata': metadata.replace(',', '|').replace('{', '').replace('}', '').replace(' ', '')}
        else:
            fields = {'data': (file_name, data)}

        # build command
        dataset_cmd = self.url + 'data/' + self.instance + '?api-tenant=' + self.api_tenant
        dataset_cmd += '&fileType=' + file_type
        dataset_cmd += '&appendData=' + str(append_data).lower()

        return multipart_post(self, dataset_cmd, fields=fields)

    def run_nano(self, results=None):
        """ clusters the data in the nano pod buffer and returns the specified results

        Args:
            results (str): comma separated list of result specifiers

                ID = cluster ID

                SI = smoothed anomaly index

                RI = raw anomaly index

                FI = frequency index

                DI = distance index

        Returns:
            result (boolean): true if successful (nano was successfully run)
            response (dict or str): dictionary of results when result is true, error message when result = false

        """

        results_str = ''
        if str(results) == 'All':
            results_str = 'ID,SI,RI,FI,DI'
        elif results:
            for result in results.split(','):
                if result not in ['ID', 'SI', 'RI', 'FI', 'DI']:
                    return False, 'unknown result "{}" found in results parameter'.format(result)
            results_str = results

        # build command
        nano_cmd = self.url + 'nanoRun/' + self.instance + '?api-tenant=' + self.api_tenant
        if results:
            nano_cmd += '&results=' + results_str

        return simple_post(self, nano_cmd)

    def get_version(self):
        """ results related to the bytes processed/in the buffer

        Returns:
            result (boolean): true if successful (version information was retrieved)
            response (dict or str): dictionary of results when result is true, error message when result = false

        """

        # build command (minus the v3 portion)
        version_cmd = self.url[:-3] + 'version' + '?api-tenant=' + self.api_tenant
        return simple_get(self, version_cmd)

    def get_buffer_status(self):
        """ results related to the bytes processed/in the buffer

        Returns:
            result (boolean): true if successful (nano was successfully run)
            response (dict or str): dictionary of results when result is true, error message when result = false

        """
        status_cmd = self.url + 'bufferStatus/' + self.instance + '?api-tenant=' + self.api_tenant
        return simple_get(self, status_cmd)

    def get_nano_results(self, results='All'):
        """ results per pattern

        Args:
            results (str): comma separated list of results

                ID: cluster ID

                SI: smoothed anomaly index

                RI: raw anomaly index

                FI: frequency index

                DI: distance index

                All: ID,SI,RI,FI,DI

        """
        # build results command
        if str(results) == 'All':
            results_str = 'ID,SI,RI,FI,DI'
        else:
            for result in results.split(','):
                if result not in ['ID', 'SI', 'RI', 'FI', 'DI']:
                    return False, 'unknown result "{}" found in results parameter'.format(result)
            results_str = results

        # build command
        results_cmd = self.url + 'nanoResults/' + self.instance + '?api-tenant=' + self.api_tenant
        results_cmd += '&results=' + results_str

        return simple_get(self, results_cmd)

    def get_nano_status(self, results='All'):
        """results in relation to each cluster/overall stats

        Args:
            results (str): comma separated list of results

                PCA = principal components (includes 0 cluster)

                clusterGrowth = indexes of each increase in cluster (includes 0 cluster)

                clusterSizes = number of patterns in each cluster (includes 0 cluster)

                anomalyIndexes = anomaly index (includes 0 cluster)

                frequencyIndexes = frequency index (includes 0 cluster)

                distanceIndexes = distance index (includes 0 cluster)

                patternMemory = base64 pattern memory (overall)

                totalInferences = total number of patterns clustered (overall)

                averageInferenceTime = time in milliseconds to cluster per
                    pattern (not available if uploading from serialized nano) (overall)

                numClusters = total number of clusters (includes 0 cluster) (overall)

        Returns:
            result (boolean): true if successful (nano was successfully run)
            response (dict or str): dictionary of results when result is true, error message when result = false

        """

        # build results command
        if str(results) == 'All':
            results_str = 'PCA,clusterGrowth,clusterSizes,anomalyIndexes,frequencyIndexes,' \
                          'distanceIndexes,totalInferences,numClusters'
        else:
            for result in results.split(','):
                if result not in ['PCA', 'clusterGrowth', 'clusterSizes', 'anomalyIndexes', 'frequencyIndexes',
                                  'distanceIndexes', 'totalInferences', 'numClusters', 'averageInferenceTime']:
                    return False, 'unknown result "{}" found in results parameter'.format(result)
            results_str = results

        # build command
        results_cmd = self.url + 'nanoStatus/' + self.instance + '?api-tenant=' + self.api_tenant
        results_cmd = results_cmd + '&results=' + results_str

        return simple_get(self, results_cmd)


###########
# PRIVATE #
###########


def generate_config(numeric_format, feature_count, minVal=1, maxVal=10, weight=1, labels=None,
                    percent_variation=0.05, streaming_window=1, accuracy=0.99):
    """generate a configuration for the given parameters

    A discrete configuration is specified as a list of minVal, maxVal, weights, and labels

    Args:
        feature_count (int): number of features per vector
        numeric_format (str): numeric type of data (one of "float32", "uint16", or "int16")
        minVal (list): the value that should be considered the minimum value for this feature. This
            can be set to a value larger than the actual min if you want to treat all value less
            than that as the same (for instance, to keep a noise spike from having undue influence
            in the clustering
        maxVal (list): corresponding maximum value
        weight (list): weight for this feature, if a list of 1 is specified, all weights are one
        labels (list):
        percent_variation (float):
        streaming_window (integer):
        accuracy (float):

    Returns:
        result (boolean): true if successful (configuration was successfully created)
        response (dict or str): configuration dictionary when result is true, error string when result is false

    """
    config = {}
    config['accuracy'] = accuracy
    temp_array = []
    for x in range(feature_count):
        temp_feature = {}
        # max
        if len([max]) == 1:
            temp_feature['maxVal'] = maxVal
        else:  # the max vals are given as a list
            temp_feature['maxVal'] = maxVal[x]
        # min
        if len([min]) == 1:
            temp_feature['minVal'] = minVal
        else:  # the min vals are given as a list
            temp_feature['minVal'] = minVal[x]
        # weights
        if len([weight]) == 1:
            temp_feature['weight'] = weight
        else:  # the weight vals are given as a list
            temp_feature['weight'] = weight[x]
        # labels
        if labels != "" and labels[x] != "":
            temp_feature['label'] = labels[x]
        temp_array.append(temp_feature)
    config['features'] = temp_array
    config['numericFormat'] = str(numeric_format)
    config['percentVariation'] = percent_variation
    config['streamingWindowSize'] = streaming_window

    return config

