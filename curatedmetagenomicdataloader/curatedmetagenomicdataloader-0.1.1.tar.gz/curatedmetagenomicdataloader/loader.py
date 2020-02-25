import fireworks
from fireworks import Pipe, Message
from collections import defaultdict
import curatedmetagenomicdataloader
from caboodle import gcs
import functools
import pandas as pd
import numpy as np
import os
from os import environ as env
from io import BytesIO
import pickle
import logging
import torch
from itertools import count
from joblib import Parallel, delayed
import pickle
from tqdm import tqdm

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def get_row_ids(query, filters_dict, keys=['body_site', 'title', 'path'], filter_keys=['sampleID', 'title', 'body_site']):
    """
    args:
        query: str
            A SQL query that returns a table containing filepaths along with file ids (paper title)
        filters_dict: dict
            A dict of the form { label : q}, where the results of SQL query q will have label 'label'. 
        Additionally, the result
            of this query should have file_id as one of the columns.
    returns:
        Returns a dict mapping { filepaths : row ids }
    """
    conn = curatedmetagenomicdataloader.get_connection()
    curr = conn.cursor()
    # Execute query
    curr.execute(query)
    qf = pd.DataFrame(curr.fetchall(), columns=keys)
    # Execute filter queries
    curr.close()
    filters = pd.DataFrame(columns=filter_keys)
    for f in filters_dict.values():
        curr = conn.cursor()
        curr.execute(f)
        filters = filters.append(pd.DataFrame(curr.fetchall(), columns=filter_keys))
        curr.close()
    # Match columns
    conn.close()
    filters['path'] = ['' for _ in range(len(filters))]
    merged = pd.DataFrame(columns=['body_site', 'title', 'path', 'sampleID'])
    for _, row in qf.iterrows():
        matched = filters.loc[filters['title'] == row['title']]
        matched['path'] = row['path']
        matched['body_site'] = row['body_site']
        merged = merged.append(matched)

    row_ids = {path: [] for path in set(merged.path)}
    for _, row in merged.iterrows():
        row_ids[row['path']].append(row['sampleID'])

    return row_ids

def get_row_labels(query, filters_dict, keys=['body_site', 'title', 'path'], filter_keys=['sampleID', 'title', 'body_site']):
    """
    args:
        query: str,
            A SQL query that returns a table containing filepaths along with file ids (paper title)
        filters_dict: dict,
            A dict of the form { label : q}, where the results of SQL query q will have label 'label'. Additionally, the result
            of this query should have file_id as one of the columns.
    returns:
        Returns a dict mapping { labels : row_ids }
    """
    conn = curatedmetagenomicdataloader.get_connection()
    curr = conn.cursor()
    # Execute query
    curr.execute(query)
    qf = pd.DataFrame(curr.fetchall(), columns=keys)
    # Execute filter queries
    curr.close()
    labels_dict = {}
    for label, f in filters_dict.items():
        curr = conn.cursor()
        curr.execute(f)
        filters = pd.DataFrame(curr.fetchall(), columns=filter_keys)
        labels_dict[label] = filters['sampleID'].tolist()
        labels_dict['title'] = filters['title'].tolist()
        curr.close()

    return labels_dict

def get_file_labels(query, filters_dict, keys=['body_site', 'title', 'path'], filter_keys=['sampleID', 'title', 'body_site']):
    """
    args:
        query: str,
            A SQL query that returns a table containing filepaths along with file ids (paper title)
            filters_dict: A dict of the form { label : q}, where the results of SQL query q will have label 'label'. Additionally, the result
            of this query should have file_id as one of the columns.
    returns:
        Returns a dict mapping { filepaths : df }, where df is a DataFrame with columns row_id and labels
    """
    conn = curatedmetagenomicdataloader.get_connection()
    curr = conn.cursor()
    # Execute query
    curr.execute(query)
    qf = pd.DataFrame(curr.fetchall(), columns=keys)
    # Execute filter queries
    curr.close()
    label_df = pd.DataFrame(columns=filter_keys+['label'])
    for label, f in filters_dict.items():
        curr = conn.cursor()
        curr.execute(f)
        filters = pd.DataFrame(curr.fetchall(), columns=filter_keys)
        filters['label'] = label
        label_df = label_df.append(filters)
        curr.close()
    # Get body sites and paths associated with titles
    body_sites_dict = {row['path']: row[['body_site', 'title']] for _, row in qf.iterrows()}
    labels_dict = {}
    for path, row in body_sites_dict.items():
        matched = (label_df['title'] == row['title']) & (label_df['body_site'] == row['body_site']) # Get rows where title and body site match
        if sum(matched) > 0:
            extracted = label_df[matched]
            labels_dict[path] = extracted[['sampleID', 'title', 'body_site', 'label']]
    return labels_dict

def extract_row_ids(filepath, row_ids, columns=None):
    """
    args:
        filepath: str,
            Path to file.
        row_ids: list,
            The row_ids to search for in file.
        columns: list, default=None,
            Columns to extract from the file.
    returns:
        Extracts and returns rows matching a row id from a given file.
    """

    bucket = env.get("CMD_BUCKET") or 'curatedmetagenomicdatacsvs'
    bucket_path = env.get("CMD_FOLDER") or 'cmd_2_24_2020'
    csv_path = gcs.download_file_to_memory(bucket, os.path.join(bucket_path, filepath))
    df = pd.read_csv(csv_path, index_col=0).transpose() # HERE
    if columns is not None:
        df = df[df.columns.intersection(columns)]
    try:
        intersection = df.index.intersection(row_ids)
        return df.loc[row_ids]
    except:
        assert False

def interpolate(df, columns, fill_value =  0.):
    """
    Interpolates df so that it's columns are the same as the columns argument.
    If a column in df is present in columns, then it is retained.
    If a column in df is not present in columns, it is dropped.
    If a column in columns is not present in df, then that column is filled in with fill_value.
    """
    interp_df = pd.DataFrame(columns=columns, index=df.index).fillna(fill_value)
    columns_present = df.columns.intersection(columns)
    interp_df = interp_df.assign(**{c: value for c, value in df[columns_present].iteritems()}).fillna(0.0) # TODO: check this
    return interp_df

def parse_csv(labels_df, filepath, interpolate_columns, fill_value):

    df = extract_row_ids(filepath, labels_df['sampleID'].tolist(), columns=interpolate_columns)
    df = interpolate(df, interpolate_columns, fill_value=fill_value)
    labels_df.index = labels_df['sampleID']
    df['label'] = labels_df['label']
    matrix = np.array(df[interpolate_columns])
    message = Message({
        'label': df['label'],
        'title': labels_df['title'],
        'body_site': labels_df['body_site'],
        'SampleID': df.index,
    })
    df = None
    message['examples'] = torch.Tensor(matrix)
    answer = pickle.dumps(message)
    logging.info(filepath)
    return message

def generate_dataset(labels_dict, interpolate_columns, fill_value=0, num_cores=None):
    inputs = list(labels_dict.items())
    messages = []
    
    if num_cores is None:
        for filepath, labels_df in labels_dict.items():
            messages.append(
                parse_csv(
                    labels_df, filepath, interpolate_columns, fill_value
                )
            )
            logger.info(filepath)            
    else: # Use multicore
        i = 0
        batch_size = num_cores
        while i < len(inputs):
            batch = inputs[i:min(i+batch_size, len(inputs))]
            logging.info("Starting new batch at index {0}".format(i))
            messages.extend(
                Parallel(n_jobs=num_cores)(delayed(parse_csv)(
                    labels_df, filepath, interpolate_columns, fill_value
                    ) for filepath, labels_df in batch
                )
            )
            i = i + batch_size

    return fireworks.cat(messages)

def save_intermediate_file(intermediate_message, filename, bucket_name='microbiome_experiments'): #labels_dict, filename, interpolate_columns, fill_value=0, columns=None):
    """
    Extracts rows matching row ids in a dict of { filepaths : row'sample_id' ids } and saves to a new file,  which
    has a table index by row id and columns that correspond to the columns in the original files.

    Simultaneously saves another file that maps row id to labels.

    args:
        id_dict: Dict of the form { filepath : row_ids }
        labels_dict: Dict of the form { filepath : labels_df}
    """
    buffer = BytesIO() # TODO: Replace this with fireworks artifacts
    intermediate_message.save(buffer)
    logging.info("Uploading to bucket: interim")
    buffer.seek(0)
    gcs.upload_string(buffer.read(), bucket_name, os.path.join('interim', filename), verbose=True, replace=True)

characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','.',';',',','%','$','_','-']

def assign_file_name(query, filters_dict):

    everything = '_'.join([str(query)] + list(filters_dict.keys()) + list(filters_dict.values()))
    counts = count_characters(everything)
    pseudo_hash = ''.join(['%s%s' % (character, counts[character]) for character in characters])
    file_name = pseudo_hash + '.fireworks'

    return file_name

def count_characters(string):

    return {character: string.count(character) for character in characters}

@functools.lru_cache()
def get_unique_phenotypes(column):
    """ Returns all unique values of a phenotype from a chosen column in the 'phenotypes' table. """
    conn = curatedmetagenomicdataloader.get_connection()
    curr = conn.cursor()
    curr.execute("SELECT DISTINCT {0} FROM phenotypes;".format(column))
    fetched = curr.fetchall()
    result = []
    for f in fetched:
        if f[0]:
            result.extend(f[0].split(';'))
    result = list(set(result))
    return result

class LoaderPipe(Pipe):
    """
    Given a query and filter, either loads target file from disk or creates it and then loads it.
    """
    def __init__(self, input=None, interpolate_columns=None):
        super().__init__(input=None)
        self.interpolate_columns = interpolate_columns
        self.interpolate_set = set(self.interpolate_columns)
        self._current_index = 0

    def load(self, query, filters_dict, keys=None, columns=None, fill_value=0, num_cores=None, use_cache=True, bucket_name='microbiome_experiments'):
        """
        Loads from database and filesystem records corresponding to the provided query and filter dict.
        """
        # Check if file already exists
        # Try to download file from bucket into local path
        filename = assign_file_name(query, filters_dict)
        bucketpath = os.path.join('interim/{0}'.format(filename))

        try:
            assert use_cache
            logging.info("Downloading dataset from GCS")
            buffer = gcs.download_file_to_memory(bucket_name, bucketpath, buffer_type='binary')
        except:
            logging.info("Dataset not in bucket. Now creating dataset.")
            self._create_file(query, filters_dict, keys, fill_value, num_cores=num_cores)
            buffer = gcs.download_file_to_memory(bucket_name, bucketpath, buffer_type='binary')

        self.message = Message.load(buffer)

    def load_columns(self, query, filters_dict, columns, keys=None, fill_value=0, num_cores=None):
        """
        Loads from database and filesystem records corresponding to the provided query and filter dict
        but only returns the columns specified.
        """
        if keys is not None:
            labels_dict = get_file_labels(query, filters_dict, keys)
        else:
            labels_dict = get_file_labels(query, filters_dict)

        self.filtered_columns = list(set([c for c in columns if c in self.interpolate_set]))
        self.message = generate_dataset(labels_dict, self.filtered_columns, fill_value=fill_value, num_cores=num_cores)

    def _create_file(self, query, filters_dict, keys=None, fill_value=0, num_cores=None):

        if keys is not None:
            labels_dict = get_file_labels(query, filters_dict, keys)
        else:
            labels_dict = get_file_labels(query, filters_dict)

        filename = assign_file_name(query, filters_dict)
        intermediate_message = generate_dataset(labels_dict, self.interpolate_columns, fill_value=fill_value, num_cores=num_cores)
        save_intermediate_file(intermediate_message, filename) #labels_dict, filename, self.interpolate_columns, fill_value=fill_value)

    def __getitem__(self, index):

        return self.message[index]

    def __len__(self):

        return len(self.message)

    def __iter__(self):

        self._current_index = 0
        return self

    def __next__(self):

        if self._current_index >= len(self):
            raise StopIteration

        item = self.message[self._current_index]
        self._current_index += 1

        return item

def get_title(path):
    """ Returns the title of the paper as implied by the given filepath. """
    #units = path.replace('-','_').split('/') # NOTE: - must be replaced with _ because postgres does not support - in strings.
    units = path.split('/')
    for title in curatedmetagenomicdataloader.datasets:
        if title in units:
            return title

def load_annotations(paths):
    """
    Returns genomic annotations data from csvs stored in GCS and concatenates them together to have the same index or specified index.
    """

    """
        if annotation is 'metaphlan':
        reference_columns = all_columns_metaphlan()
        use_reference = True
        interpolator = lambda df: interpolate(df, reference_columns, fill_value = 0.)
    """
    columns = pd.Index([])
    bucket = env.get("CMD_BUCKET") or 'curatedmetagenomicdatacsvs'
    bucket_path = env.get("CMD_FOLDER") or 'cmd_2_24_2020'
    for path in paths:
        logging.info("Loading genomic annotations for {0}".format(path))
        csv_path = gcs.download_file_to_memory(bucket, os.path.join(bucket_path, path))
        df = pd.read_csv(csv_path, index_col=0).transpose()
        columns = columns.union(df.columns)

    return columns

def get_all_columns(annotation):
    conn = curatedmetagenomicdataloader.get_connection()
    curr = conn.cursor()
    keys = ['body_site', 'title', 'path']
    curr.execute("SELECT {0} FROM annotations where annotation = '{1}';".format(', '.join(keys), annotation))
    references = pd.DataFrame(curr.fetchall(), columns = keys)
    columns = load_annotations(references['path'])

    return columns

def get_columns(filename, annotation, use_cache, update_cache):

    if use_cache:
        try:
            columns = pickle.load(open(filename, 'rb'))['columns']
        except FileNotFoundError:
            columns = get_all_columns(annotation)
            if update_cache:
                pickle.dump({'columns': columns}, open(filename, 'wb'))
    else:
        columns = get_all_columns(annotation)
        if update_cache:
            pickle.dump({'columns': columns}, open(filename, 'wb'))

    return columns

def all_columns_functional(use_cache = True, update_cache = True):
    """ Returns all functional categories identified in the data set. """
    return get_columns('pathabundance_columns.pickle', 'pathabundance_relab', use_cache, update_cache)

def all_columns_metaphlan(use_cache = True, update_cache = True):
    """ Returns all metaphlan OTUs identified in the data set. """
    return get_columns('metaphlan_columns.pickle', 'metaphlan_bugs_list', use_cache, update_cache)

def all_columns_uniref(use_cache = True, update_cache = True):
    """ Returns all Uniref90 proteins identified in the data set. """
    return get_columns('uniref_columns.pickle', 'genefamilies_relab', use_cache, update_cache)
