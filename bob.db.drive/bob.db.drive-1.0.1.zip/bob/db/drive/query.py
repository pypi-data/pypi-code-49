#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from PIL import Image
import json
from pathlib import Path
import pkg_resources
import itertools
from .models import Sample, FundusImage, GroundTruth, Mask


class FileList:
    """
    FileList object that loads the protocol as defined in a json file. 
    Provides a ``__getitem__`` interface. 
    """

    def __init__(self, db_json):
        with open(db_json,'r') as in_file:
            self._filelist = json.load(in_file)
    

    def __getitem__(self, key):
        # if no valid split is passed, return all paths of train and test 
        return self._filelist.get(key, (self._filelist['train']+self._filelist['test']))
    

class Database:
    """
    A low level database interface to be used with PyTorch or other deep learning frameworks. 

    Attributes
    ----------
    protocol : str
                protocol defining the train-test split.
    """
    
    def __init__(self, protocol = 'default'):
        self.protocol = protocol
        root = Path(pkg_resources.resource_filename(__name__, ''))
        db_json =  root.joinpath('drive_db_'+self.protocol+'.json')
        # initialize filelist
        self._filelist = FileList(db_json)


    @property    
    def paths(self):
        """
        Returns
        -------
        paths : list
                    list of all paths of all samples
        """
        return list(itertools.chain(*(self._filelist[None]) ))
    

    def _make_sample(self, img_path,gt_path,mask_path):
        """
        Make a single sample object

        Parameters
        ----------
        img_path : str
                    relative path to image
        gt_path  : str
                    relative path to ground truth
        mask     : str
                    relative path to mask

        Returns
        -------
        sample : Sample
        """

        img = FundusImage(img_path)
        gt = GroundTruth(gt_path)
        mask = Mask(mask_path)
        return Sample(img, gt, mask)


    def samples(self, split=None):
        """
        Given a split, returns a list of Sample objects.

        Parameters
        ----------
        split : str
                    'train', 'test' or None (returns all samples)

        Returns
        -------
        samples : list
                    list of Sample objects
        """

        samples = []
        for s in self._filelist[split]:
            sample_obj = self._make_sample(s[0], s[1], s[2])
            samples.append(sample_obj)
        return samples
            


