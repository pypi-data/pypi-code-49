'''
 utils for loading dataset
'''


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import json
import threading
import os
import subprocess
import sys
import glob
import tqdm
from  sys import stderr
import requests
import warnings
import numpy as np
from tqdm import tqdm
import gzip
import tarfile
import zipfile
import shutil
import hashlib
import glob
import six
from scipy.io import loadmat

from six.moves.urllib.error import HTTPError
from six.moves.urllib.error import URLError
from six.moves.urllib.request import urlopen
try:
    from urllib.request import urlretrieve
except ImportError:
    from six.moves.urllib.request import urlretrieve



def ensure_dir(dirpath):
    if not os.path.exists(dirpath): os.makedirs(dirpath)

def ensure_parent_dir(childpath):
    ensure_dir(os.path.dirname(childpath))


class TqdmProgress(tqdm):
    """Provides `update_to(n)` which uses `tqdm.update(delta_n)`."""

    def update_to(self, b=1, bsize=1, tsize=None):
        """
        b  : int, optional
            Number of blocks transferred so far [default: 1].
        bsize  : int, optional
            Size of each block (in tqdm units) [default: 1].
        tsize  : int, optional
            Total size (in tqdm units). If [default: None] remains unchanged.
        """
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)  # will also set self.n = b * bsize

def calculate_md5(fpath, chunk_size=1024 * 1024):
    md5 = hashlib.md5()
    with open(fpath, 'rb') as f:
        for chunk in iter(lambda: f.read(chunk_size), b''):
            md5.update(chunk)
    return md5.hexdigest()


def check_md5(fpath, md5, **kwargs):
    return md5 == calculate_md5(fpath, **kwargs)


def check_integrity(fpath, md5=None):
    if not os.path.isfile(fpath):
        return False
    if md5 is None:
        return True
    return check_md5(fpath, md5)

def _write_h(dirname,is_downloaded=False,is_extracted=False):
    _h_path = os.path.join(dirname, 'status.json')
    _h = {
        'is_downloaded': is_downloaded,
        'is_extracted': is_extracted
    }
    try:
        with open(_h_path, 'w') as f:
            f.write(json.dumps(_h, indent=4))
    except IOError:
        # Except permission denied.
        pass
def _read_h(dirname):
    _h = {}
    _h_path = os.path.join(dirname, 'status.json')
    if os.path.exists(_h_path):
        try:
            with open(_h_path) as f:
                _h = json.load(f)
        except ValueError:
            _h = {}
    return _h

def download_file(src, dirname, filename, desc=''):
    _h = _read_h(dirname)
    if os.path.exists(os.path.join(dirname, filename)) and _h != {} and _h.get('is_downloaded', False) == True:
        print('archive file is already existing, donnot need download again.')
    else:
        if os.path.exists(os.path.join(dirname, filename)):
            os.remove(os.path.join(dirname, filename))
        error_msg = 'URL fetch failure on {}: {} -- {}'
        try:
            try:
                with TqdmProgress(unit='B', unit_scale=True,  leave=True,miniters=10, desc=desc) as t:  # all optional kwargs
                    urlretrieve(src, filename=os.path.join(dirname, filename), reporthook=t.update_to, data=None)
                    _write_h(dirname, True, False)
            except HTTPError as e:
                _write_h(dirname, False, False)
                raise Exception(error_msg.format(src, os.path.join(dirname, filename), e.code, e.__str__()))

            except URLError as e:
                _write_h(dirname, False, False)
                raise Exception(error_msg.format(src, os.path.join(dirname, filename), e.errno, e.reason))
            except (Exception, KeyboardInterrupt) as e:
                _write_h(dirname, False, False)
                if os.path.exists(os.path.join(dirname, filename)):
                    os.remove(os.path.join(dirname, filename))
        except:
            _write_h(dirname, False, False)
            raise



def download_file_from_google_drive(file_id, dirname, filename=None, md5=None):
    """Download a Google Drive file from  and place it in root.

    Args:
        file_id (str): id of file to be downloaded
        root (str): Directory to place downloaded file in
        filename (str, optional): Name to save the file under. If None, use the id of the file.
        md5 (str, optional): MD5 checksum of the download. If None, do not check
    """
    # Based on https://stackoverflow.com/questions/38511444/python-download-files-from-google-drive-using-url
    import requests
    url = "https://docs.google.com/uc?export=download"

    if not filename:
        filename = file_id
    fpath = os.path.join(dirname, filename)
    _h=_read_h(dirname)
    # if os.path.exists(os.path.join(dirname, filename)):
    #     print('archive file is already existing, donnot need download again.')
    if os.path.exists(os.path.join(dirname, filename)) and _h!={} and  _h.get('is_downloaded', False)==True:
        print('archive file is already existing, donnot need download again.')
    else:
        with TqdmProgress(unit='B', unit_scale=True, miniters=10, desc='') as t:  # all optional kwargs
            session = requests.Session()
            response = session.get(url, params={'id': file_id}, stream=True)
            token = _get_confirm_token(response)

            if token:
                params = {'id': file_id, 'confirm': token}
                response = session.get(url, params=params, stream=True)

            _save_response_content(response, fpath)
            _write_h(dirname,True,False)


def _get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None


def _save_response_content(response, destination, chunk_size=32768):
    with open(destination, "wb") as f:
        pbar = tqdm(total=None)
        progress = 0
        for chunk in response.iter_content(chunk_size):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                progress += len(chunk)
                pbar.update(progress - pbar.n)
        pbar.close()


def extract_archive(file_path, path='.', archive_format='auto'):
  """Extracts an archive if it matches tar, tar.gz, tar.bz, or zip formats.

  Arguments:
      file_path: path to the archive file
      path: path to extract the archive file
      archive_format: Archive format to try for extracting the file.
          Options are 'auto', 'tar', 'zip', and None.
          'tar' includes tar, tar.gz, and tar.bz files.
          The default 'auto' is ['tar', 'zip'].
          None or an empty list will return no matches found.

  Returns:
      True if a match was found and an archive extraction was completed,
      False otherwise.
  """
  _h = _read_h(path)
  if _h != {} and _h.get('is_extracted', False) == True:
      print('extraction is finished, donnot need extract again.')
      return True
  if archive_format is None:
    return False
  if archive_format == 'auto':
    archive_format = ['tar', 'zip']
  if isinstance(archive_format, six.string_types):
    archive_format = [archive_format]

  is_match_fn = tarfile.is_tarfile
  open_fn = tarfile.open
  for archive_type in archive_format:
    if archive_type == 'tar':
      open_fn = tarfile.open
      is_match_fn = tarfile.is_tarfile
    if archive_type == 'zip':
      open_fn = zipfile.ZipFile
      is_match_fn = zipfile.is_zipfile

    if is_match_fn(file_path):
      with open_fn(file_path) as archive:
        try:
          if os.path.exists(os.path.join(path,file_path.split('\\')[-1].strip().split('.')[0])) and os.path.isdir(path):
              print('extracted folder is already existing, donnot need extract again.')
          else:
            archive.extractall(path)
            _write_h(path, True, True)
        except (tarfile.TarError, RuntimeError, KeyboardInterrupt):
            _write_h(path, False, False)
            if os.path.exists(path):
                if os.path.isfile(path):
                    os.remove(path)
                else:
                    shutil.rmtree(path)
            raise
        return True
    else:
        _write_h(path, False, False)
  return False


def unpickle(file):
    import _pickle as pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

def open_pickle(fpath, data_key='data', label_key='labels'):
    d = unpickle(fpath)
    d_decoded = {}
    for k, v in d.items():
        d_decoded[k.decode('utf8')] = v
    d = d_decoded
    data = d[data_key]
    labels = d[label_key]
    return data, labels


def check_image(image, imagepath):
    if not os.path.exists(imagepath): return False
    with open(imagepath, 'rb') as fin:
        return (hashlib.md5(fin.read()).hexdigest() == image['md5'])




def read_mat(mat_path):
    mat = loadmat(mat_path)
    return mat

