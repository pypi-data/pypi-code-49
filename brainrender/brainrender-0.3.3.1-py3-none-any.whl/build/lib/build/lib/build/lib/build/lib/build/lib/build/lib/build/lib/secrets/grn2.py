import sys
sys.path.append('./')
from brainrender.scene import Scene
from brainrender.colors import colorMap
from allensdk.core.mouse_connectivity_cache import MouseConnectivityCache
import os 
import pandas as pd
import numpy as np
from vtkplotter import Text
from tqdm import tqdm


# # grab the StructureTree instance
mcc = MouseConnectivityCache(manifest_file='Data/ABA/MCC/manifest.json')
structure_tree = mcc.get_structure_tree()
GRN = structure_tree.get_structures_by_acronym(['SCm'])[0]

exps = mcc.get_experiments(cre=False, injection_structure_ids=[GRN['id']])


# exps_ids = [ e['id'] for e in exps ]
# structures = ['SCm', 'SCs', 'PAG', 'CUN', 'PPN']
# ctx_children = [structure_tree.get_structures_by_acronym([s])[0]['id'] for s in structures]
# ctx_children.extend(structure_tree.child_ids( [structure_tree.get_structures_by_acronym(['SCm'])[0]['id']] )[0])

# pm = mcc.get_projection_matrix(experiment_ids = exps_ids, 
#                                projection_structure_ids = ctx_children,
#                                hemisphere_ids= [2], # right hemisphere, ipsilateral
#                                parameter = 'projection_density')
# mtx = pm['matrix']


scene = Scene()

# txts = []
# for i, exp in enumerate(exps):
#     color = colorMap(mtx[0, i], name='Reds', vmin=0, vmax=np.max(mtx[0, :]))
#     xyz = [exp['injection_x'], exp['injection_y'], exp['injection_z']]
#     sphere = scene.add_sphere_at_point(xyz, color=color, alpha=.4)

#     t = Text(str(exp['id']), xyz, s=100, c="k")
#     txts.append(t)
#     scene.actors['others'].append(t)
# scene.plotter.show()
# for t in txts:
#     t.followCamera()


regions = ['GRN', 'PAG', 'SCm', 'SCs', 'RSP', 'MOs']
scene.add_brain_regions(regions, use_original_color= True, alpha=.4)

for reg in regions:
    scene.edit_actors([scene.actors['regions'][reg]], wireframe=True) 

from brainrender.Utils.parsers.streamlines import StreamlinesAPI
streamlines_api = StreamlinesAPI()
streamlines_files, data = streamlines_api.download_streamlines_for_region("RSP") 
scene.add_streamlines(data, colorby="RSP", show_injection_site=True, alpha=.2, radius=10)

txts = []
# for exp, color in tqdm(zip(["146078721", "175158132", "128001349", "126523066", "126646502"], ["skyblue", "lightskyblue", "lightsteelblue", "blackboard", 'sandybrown'])):
#     idx = [i for i,f in enumerate(streamlines_files) if exp in f][0]

#     xyz = [exps[idx]['injection_x'], exps[idx]['injection_y'], exps[idx]['injection_z']]
#     # sphere = scene.add_sphere_at_point(xyz, color=color, alpha=.4)
#     # t = Text(exp, xyz, s=150, c="k")
#     # txts.append(t)
#     # scene.actors['others'].append(t)

#     scene.add_streamlines(data[idx], color=color, show_injection_site=True, alpha=.2, radius=10)
# scene.plotter.show(interactive=False)

for t in txts:
    t.followCamera()

scene.render()
