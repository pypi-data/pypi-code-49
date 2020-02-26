""" Create dataset and dataloader in PyTorch """
import bz2
import logging
import os
import sys
from urllib.request import urlretrieve

import numpy as np
import torch.utils.data

_logger = logging.getLogger('mlbench')

FEATURES_FILE = "epsilon_train.dat"
LABELS_FILE = "epsilon_train.lab"
DATASET_URL = "ftp://largescale.ml.tu-berlin.de/largescale/epsilon"

N_SAMPLES = 500000
TRAIN_SIZE = 400000
N_FEATURES = 2000


class Epsilon(torch.utils.data.Dataset):
    """
    Epsilon Dataset Loader
    Loads and downloads raw Epsilon dataset.

    Args:
        root (str): Root folder for the dataset
        train (bool): Whether to get the train or validation set.
            Default: `True`
        download (bool): Whether to download the dataset if it's not present.
            Default: `False`
        seed (int): Random seed for train/val.
            Default: 42

    .. Epsilon data location:
        ftp://largescale.ml.tu-berlin.de/largescale/epsilon/

        two files are used `epsilon_train.dat` and `epsilon_train.lab.dat`
    """

    def __init__(self, root, train=True, download=False, seed=42):
        self.root = root

        self.features_file = os.path.join(self.root, FEATURES_FILE)
        self.labels_file = os.path.join(self.root, LABELS_FILE)
        if download:
            download_and_extract_dataset(root)
            print("tamer")
        assert file_exists(self.features_file), \
            "Feature file {} does not exist".format(self.features_file)
        assert file_exists(self.labels_file), \
            "Labels file {} does not exist".format(self.labels_file)

        # Now get all train indices (same every time due to seed)
        np.random.seed(seed)
        train_indices = np.random.choice(N_SAMPLES, TRAIN_SIZE)
        if train:
            self.indices = train_indices
        else:
            self.indices = [x for x in np.arange(N_SAMPLES)
                            if x not in train_indices]

        self.indices = sorted(self.indices)  # Sort (maybe not necessary)
        self.length = len(self.indices)

        self.features = self._read_file_lines(self.features_file)
        self.labels = self._read_file_lines(self.labels_file)

        assert self.features.shape[1] == N_FEATURES, \
            "Dataset does not have expected number of features"

    def __getitem__(self, item):
        feat, label = self.features[item], self.labels[item]
        return feat, label

    def __len__(self):
        return self.length

    def __repr__(self):
        return self.__class__.__name__ + ' (' + self.root + ')'

    def _read_file_lines(self, file):
        indices_set = set(self.indices)
        lines = []
        with open(file) as f:
            for i, line in enumerate(f):
                if i in indices_set:
                    lines += [float(x) for x in line.strip().split()]
                if len(lines) == len(indices_set):  # Stopping condition
                    break

        assert len(lines) == len(indices_set), \
            "Number of lines read different than required for {}".format(file)
        return np.vstack(lines)


def download_and_extract_dataset(destination_dir):
    """ Downloads the Epsilon dataset and extracts it at the corresponding dir

    Args:
        destination_dir (str): Destination dir
    """
    # Download file to destination (features and labels)
    features_file = os.path.join(destination_dir, FEATURES_FILE)
    labels_file = os.path.join(destination_dir, FEATURES_FILE)

    if not file_exists(features_file):
        _logger.info("Downloading and extracting Epsilon Dataset")

        progress_download(os.path.join(DATASET_URL, FEATURES_FILE) + ".bz2",
                          features_file + ".bz2")
        extract_bz2_file(features_file + ".bz2", features_file)
        os.remove(features_file + ".bz2")

    if not file_exists(labels_file):
        progress_download(os.path.join(DATASET_URL, LABELS_FILE) + ".bz2",
                          labels_file + ".bz2")

        extract_bz2_file(labels_file + ".bz2", labels_file)
        os.remove(labels_file + ".bz2")

    _logger.info("Download successful")


def extract_bz2_file(source, dest):
    """ Extracts a bz2 archive

    Args:
        source (str): Source file (must have .bz2 extension)
        dest (str): Destination file

    """
    assert source.endswith(".bz2"), "Extracting non bz2 archive"
    with open(source, 'rb') as s, open(dest, 'wb') as d:
        d.write(bz2.decompress(s.read()))


def progress_download(url, dest):
    """ Downloads a file from `url` to `dest` and shows progress

    Args:
        url (src): Url to retrieve file from
        dest (src): Destination file
    """

    def _progress(count, block_size, total_size):
        sys.stdout.write('\r>> Downloading %s %.1f%%' % (
            os.path.basename(dest),
            float(count * block_size) / float(total_size) * 100.0))
        sys.stdout.flush()
    print(url, dest)
    urlretrieve(url, dest, _progress)
    _logger.info("Downloaded {} to {}".format(url, dest))


def file_exists(file):
    """ Returns true if the given file exists in the file system

    Args:
        file (str): File full path

    Returns:
        (bool) True if the path exists and is a file
    """
    return os.path.exists(file) and os.path.isfile(file)
