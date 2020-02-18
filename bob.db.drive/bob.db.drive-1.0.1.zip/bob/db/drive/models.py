from pathlib import Path
from PIL import Image
import bob.extension


class FundusImage:
    """
    Generic fundus image object.
    """

    def __init__(self, path):
        self.path = path


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


    def pil_image(self, datadir=bob.extension.rc['bob.db.drive.datadir']):
        """
        Returns
        -------
        img : :py:class:`PIL.Image.Image`
        """
        img = Image.open(str(Path(datadir).joinpath(self.path)))
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


    def pil_image(self, datadir=bob.extension.rc['bob.db.drive.datadir']):
        """
        Returns
        -------
        gt : :py:class:`PIL.Image.Image`
                mode = '1'
        """
        gt = Image.open(str(Path(datadir).joinpath(self.path)))
        gt = gt.convert(mode='1', dither=None)
        return gt


class Mask:
    """
    Generic mask object.
    """

    def __init__(self, path):
        self.path = path


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
                the mask image resolution in (W, H).
        """
        return self.pil_image().size


    def pil_image(self, datadir=bob.extension.rc['bob.db.drive.datadir']):
        """
        Returns
        -------
        mask : :py:class:`PIL.Image.Image`
                mode = '1'
        """
        mask = Image.open(str(Path(datadir).joinpath(self.path)))
        mask = mask.convert(mode='1', dither=None)
        return mask


class Sample:
    """
    Generic Sample object

    High level sample class that combines the objects 'FundusImage', 'GroundTruth' and 'Mask'. 
    Allows for access of the subclass, e.g. :

    .. testsetup:: *
        
        from bob.db.drive.models import *

    .. doctest::

        >>> img = FundusImage('path/to/some_img.file')
        >>> gt = GroundTruth('path/to/some_gt.file')
        >>> mask = Mask('path/to/some_mask.file')
        >>> mysample = Sample(img, gt, mask)
        >>> mysample.img.basename
        'some_img.file'
        >>> mysample.gt.basename
        'some_gt.file'
        >>> mysample.mask.basename
        'some_mask.file'
        >>> 

    Parameters
    ----------
    img  : FundusImage
    gt   : GroundTruth
    mask : Mask
    """
    
    def __init__(self, img, gt, mask):
        self.img = img
        self.gt = gt
        self.mask = mask
    
    
    @property
    def paths(self):
        """
        Returns
        --------
        paths : list
                 paths of image, ground truth and mask
        """
        return self.img.path, self.gt.path, self.mask.path
