####################################################################################################
# neuropythy/vision/labels.py
# Tools for deducing labels related to visual areas.
# By Noah C. Benson

import numpy                        as np
import numpy.linalg                 as npla
import nibabel.freesurfer.mghformat as fsmgh
import nibabel.freesurfer.io        as fsio
import pyrsistent                   as pyr
import os, sys, gzip, six, types, pimms

from .. import geometry       as geo
from .. import freesurfer     as nyfs
from .. import mri            as mri
from .. import io             as nyio
from ..util               import (zinv, library_path, is_tuple, is_list)
from ..registration       import (mesh_register, java_potential_term)
from ..java               import (to_java_doubles, to_java_ints)
from functools            import reduce

from .models import (RetinotopyModel, SchiraModel, RetinotopyMeshModel, RegisteredRetinotopyModel,
                     load_fmm_model, visual_area_names, visual_area_numbers)
# due to parameter name clash we import this one special:
from .models import visual_area_field_signs as global_visual_area_field_signs
from .retinotopy import *

def find_visual_areas(hemi, retinotopy=Ellipsis, mask=Ellipsis):
    '''
    find_visual_areas(hemi) yields a predicted set of vertex labels, one per vertex in hemi, that
      give the visual area labels in the given hemisphere.

    For mappings from visual area numbers (returned by this function) to visual area names, see
    neuropythy.vision.visual_area_names and neuropythy.vision.visual_area_numbers.
    
    The following options may be given:
      * retinotopy (default: Ellipsis) specifies the retinotopy data to use for the hemisphere;
        the argument may be a map from retinotopy_data or a valid argument to it. The default
        indicates that the result of calling retinotopy_data(hemi) is used.
      * mask (default: Ellipsis) specifies that the specific mask should be used; by default, the
        mask is made using the vertices kept in to_flatmap('occipital_pole', hemi, radius=pi/2.75).
      * visual_area (default: Ellipsis) specifies the visual area labels to use; the default
        indicates that the visual area property found in the retinotopy data should be used, if any.
        If None then no visual area splitting is done. This property is only important if 
        map_visual_areas is not False or None; otherwise it is ignored.
    '''
    from neuropythy.util import curry
    import neuropythy.optimize as op
    rdat = (retinotopy_data(hemi) if retinotopy is Ellipsis   else
            retinotopy            if pimms.is_map(retinotopy) else
            retinotopy_data(hemi, retinotopy))
    # figure out the mask
    if mask is Ellipsis: mask = geo.to_flatmap('occipital_pole', hemi, radius=np.pi/2.75).labels
    else:                mask = hemi.mask(mask, indices=True)
    # get the subtess on which we will operate::
    tess = hemi.tess.subtess(mask)
    # possible that the mask got further downsampled:
    mask = supermesh.tess.index(mesh.labels)
    rdat = {k:(v[mask] if len(v) > len(mask) else v) for (k,v) in six.iteritems(rdat)}
    xy = as_retinotopy(rdat, 'geographical')
    n = tess.vertex_count # number vertices
    
