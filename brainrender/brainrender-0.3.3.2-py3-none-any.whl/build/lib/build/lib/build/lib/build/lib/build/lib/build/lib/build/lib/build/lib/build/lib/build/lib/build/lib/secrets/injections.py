# from brainrender import *

import sys
sys.path.append('./')
from brainrender.scene import Scene
import pandas as pd
import os
from tqdm import tqdm
from brainrender.Utils.actors_funcs import edit_actor
from brainrender.colors import makePalette
import random
from vtkplotter.analysis import surfaceIntersection


def add_CoM(act, scene, color, **kwargs):
    """ Adds center of mass to the scene """
    com = act.centerOfMass()
    scene.add_sphere_at_point(com, color=color, **kwargs)

sc = ['SCdg', 'SCdw', 'SCig', 'SCiw', 'SCm', 'SCop', 'SCs', 'SCsg', 'SCzo']


scene = Scene(add_root=False)
fld = '/Users/federicoclaudi/Dropbox (UCL - SWC)/Rotation_vte/Anatomy/injections'
inj_files = [os.path.join(fld, f) for f in os.listdir(fld)]
inj_files = [f for f in inj_files if 'ch1' in f]

colors = makePalette('salmon', 'green', len(inj_files))

scene.add_brain_regions(['SCm'], use_original_color=True, wireframe=False, alpha=.2)
reg = scene.actors['regions']['SCm']
scene.add_brain_regions(['PAG', 'SCs'], use_original_color=True, wireframe=True, alpha=.1)

for fl, c in zip(inj_files, colors): 
    print("Adding: {}".format(fl))
    act = scene.add_from_file(fl, c=c, alpha=.6)
    edit_actor(act, smooth=False, line=False, line_kwargs=dict(lw=.25, c='blackboard'))


    add_CoM(act, scene, c)

    intersection = surfaceIntersection(act, reg)
    scene.add_vtkactor(intersection)



scene.render() 
