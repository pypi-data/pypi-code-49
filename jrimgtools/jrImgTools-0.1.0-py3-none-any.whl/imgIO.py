# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 15:43:39 2020

@author: Jerry
"""
import numpy as np
import SimpleITK as sitk
def safeLoadMedicalImg(filename):
    """Load single image file of common medical image types
    

    Parameters
    ----------
    filename : TYPE
        DESCRIPTION.

    Raises
    ------
    ValueError
        DESCRIPTION.

    Returns
    -------
    img : TYPE
        DESCRIPTION.

    """
    
    img = sitk.GetArrayFromImage(sitk.ReadImage(filename))
    if np.ndim(img) != 3:
        raise ValueError(f'Unsupported image dim {np.ndim(img)} (with shape {img.shape})')
    
    # Strangely, [80, 70, 50] image become [50, 80, 70]!
    # i.e. [H, W, N] => [N, H, W]
    img = np.moveaxis(img, 0, 2)
    
    #sliceDim = 2 if sliceDim == -1 else sliceDim
    #img = np.moveaxis(img, sliceDim, -1)
    return img