from pathlib import Path
from PIL import Image, ImageDraw
import bob.extension
import csv
import numpy as np


class FundusImage:
    """
    Generic fundus image object.
    """

    def __init__(self, path):
        self.path = path


    def _pad(self,img):
        """
        Pad the given PIL Image on the right side to account for image images/image_101.jpg with resolution of
        599x400 instead of 600x400 like all other images in the dataset.
        
        Parameters
        -----------
            img (PIL Image): Image to be padded.
        Returns
        -------
            PIL Image: Padded image.
        """
        img = np.asarray(img)
        img = np.pad(img, ((0, 0), (1, 0), (0, 0)), 'constant')        
        return Image.fromarray(img)


    @property
    def basename(self):
        """
        Returns the file name

        Returns
        -------
        name : str
        """
        return Path(self.path).name


    @property
    def size(self):
        """
        Returns
        -------
        size : tuple
                the fundus image resolution in (W, H).
        """
        return self.pil_image().size


    def pil_image(self, datadir=bob.extension.rc['bob.db.drionsdb.datadir']):
        """
        Returns
        -------
        img : :py:class:`PIL.Image.Image`
        """
        img = Image.open(str(Path(datadir).joinpath(self.path)))
        # account for database inconsistency and pad outlier fundus image with 1 pixel
        if img.size == (599,400):
            img = self._pad(img)
        return img

class GroundTruth:
    """
    Generic ground truth object.
    
    - Allows for thresholding in case there are multiple ground truth annotations in one bitmap
    - Allows for "on-the-fly" drawing of ground truth annotations with a specified size


    Parameters
    ----------
    path      : str
                    relative path to the file on disk
    threshold : float
                    in range [0,1] used to threshold ground-truth image data with multiple classes e.g. optic disc and cup
    drawsize  : tuple
                    size tuple in pillow (W, H) format. Used for cases where drawing of gt is required
    """

    def __init__(self, path, threshold=None, drawsize=None):
        self.path = path
        self.threshold = threshold
        self.drawsize = drawsize


    def _open_annot(self,file):
        """
        Reads a txt file with two columns: image_file_name , ground_truth_file_name.
        
        Returns
        -------
        file_list : list
        list containing two tuples. The first one contains image file names, the second the ground truth file names
        """
        with open(file,'r') as f:
            rows = csv.reader(f,delimiter=',',quoting=csv.QUOTE_NONNUMERIC)
            rows_tup = list(map(tuple,rows))
        return rows_tup


    @property
    def basename(self):
        """
        Returns the file name

        Returns
        -------
        name : str
        """
        return Path(self.path).name


    @property
    def size(self):
        """
        Retirms the ground truth image resolution in (W, H).

        Returns
        -------
        size : tuple
        """
        return self.pil_image().size


    def pil_image(self, datadir=bob.extension.rc['bob.db.drionsdb.datadir']):
        """
        Returns
        -------
        gt : :py:class:`PIL.Image.Image`
                mode = '1'
        """
        gttxt = self._open_annot(str(Path(datadir).joinpath(self.path)))
        # on the fly drawing
        gt = Image.new('1', self.drawsize)
        draw = ImageDraw.ImageDraw(gt)
        draw.polygon(gttxt,fill='white')
        del draw
        return gt


class Sample:
    """
    Generic Sample object

    High level sample class that combines the objects 'FundusImage' and 'GroundTruth'
    Allows for access of the subclass, e.g. :

    .. testsetup:: *
        
        from bob.db.drionsdb.models import *

    .. doctest::

        >>> img = FundusImage('path/to/some_img.file')
        >>> gt = GroundTruth('path/to/some_gt.file')
        >>> mysample = Sample(img, gt)
        >>> mysample.img.basename
        'some_img.file'
        >>> mysample.gt.basename
        'some_gt.file'
        >>> 

    Parameters
    ----------
    img  : FundusImage
    gt   : GroundTruth
    """
    
    def __init__(self, img, gt):
        self.img = img
        self.gt = gt
    
    
    @property
    def paths(self):
        """
        Returns
        --------
        paths : list
                 paths of image, ground truth
        """
        return self.img.path, self.gt.path
