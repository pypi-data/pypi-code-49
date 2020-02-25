# %%
from allensdk.core.mouse_connectivity_cache import MouseConnectivityCache
import os 

# The manifest file is a simple JSON file that keeps track of all of
# the data that has already been downloaded onto the hard drives.
# If you supply a relative path, it is assumed to be relative to your
# current working directory.
mcc = MouseConnectivityCache(manifest_file='Data/ABA/MCC/manifest.json')

# %%
# pandas for nice tables
import pandas as pd

# grab the StructureTree instance
structure_tree = mcc.get_structure_tree()


# %%
from allensdk.api.queries.ontologies_api import OntologiesApi

oapi = OntologiesApi()

# get the ids of all the structure sets in the tree
structure_set_ids = structure_tree.get_structure_sets()


# %%
# From the above table, "Mouse Connectivity - Summary" has id 167587189
summary_structures = structure_tree.get_structures_by_set_id([167587189])
pd.DataFrame(summary_structures)

# %%
# fetch the experiments that have injections in the isocortex of cre-positive mice
GRN = structure_tree.get_structures_by_acronym(['GRN'])[0]
exps = mcc.get_experiments(cre=False, injection_structure_ids=[GRN['id']])

# print("%d cre cortical experiments" % len(exps))

# structure_unionizes = mcc.get_structure_unionizes([ e['id'] for e in exps ], 
#                                                   is_injection=False,
#                                                   structure_ids=[GRN['id']],
#                                                   include_descendants=True)

# print("%d VISp non-injection, cortical structure unionizes" % len(structure_unionizes))

# # %%
# dense_unionizes = structure_unionizes[ structure_unionizes.projection_density > .5 ]
# large_unionizes = dense_unionizes[ dense_unionizes.volume > .5 ]
# large_structures = pd.DataFrame(structure_tree.nodes(large_unionizes.structure_id))

# print("%d large, dense, cortical, non-injection unionizes, %d structures" % ( len(large_unionizes), len(large_structures) ))

# print(large_structures.name)

# large_unionizes

# %%
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline

exps_ids = [ e['id'] for e in exps ]
structures = ['SCm', 'SCs', 'PAG', 'CUN', 'PPN']
ctx_children = [structure_tree.get_structures_by_acronym([s])[0]['id'] for s in structures]
ctx_children.extend(structure_tree.child_ids( [structure_tree.get_structures_by_acronym(['SCm'])[0]['id']] )[0])

pm = mcc.get_projection_matrix(experiment_ids = exps_ids, 
                               projection_structure_ids = ctx_children,
                               hemisphere_ids= [2], # right hemisphere, ipsilateral
                               parameter = 'projection_density')

row_labels = pm['rows'] # these are just experiment ids
column_labels = [ c['label'] for c in pm['columns'] ] 
matrix = pm['matrix']

fig, ax = plt.subplots(figsize=(15,15))
heatmap = ax.pcolor(matrix, cmap=plt.cm.afmhot)

# put the major ticks at the middle of each cell
ax.set_xticks(np.arange(matrix.shape[1])+0.5, minor=False)
ax.set_yticks(np.arange(matrix.shape[0])+0.5, minor=False)

ax.set_xlim([0, matrix.shape[1]])
ax.set_ylim([0, matrix.shape[0]])          

# want a more natural, table-like display
ax.invert_yaxis()
ax.xaxis.tick_top()

ax.set_xticklabels(column_labels, minor=False)
ax.set_yticklabels(row_labels, minor=False)
plt.show()

# %%

# %%
# for i in structure_tree.child_ids( [structure_tree.get_structures_by_acronym(['SCm'])[0]['id']])[0]:
GRN = structure_tree.get_structures_by_acronym(['PPN'])[0]
print("\n\n", GRN['name'], '\n\n')
exps = mcc.get_experiments(cre=False, injection_structure_ids=[GRN['id']])
exps_ids = [ e['id'] for e in exps ]

structures = ['GRN', 'PAG', 'CUN', 'PPN']
ctx_children = [structure_tree.get_structures_by_acronym([s])[0]['id'] for s in structures]
ctx_children.extend(structure_tree.child_ids( [structure_tree.get_structures_by_acronym(['GRN'])[0]['id']] )[0])

pm = mcc.get_projection_matrix(experiment_ids = exps_ids, 
                            projection_structure_ids = ctx_children,
                            hemisphere_ids= [2], # right hemisphere, ipsilateral
                            parameter = 'projection_density')

row_labels = pm['rows'] # these are just experiment ids
column_labels = [ c['label'] for c in pm['columns'] ] 
matrix = pm['matrix']

fig, ax = plt.subplots(figsize=(8,8))
heatmap = ax.pcolor(matrix, cmap=plt.cm.afmhot)

# put the major ticks at the middle of each cell
_ = ax.set_xticks(np.arange(matrix.shape[1])+0.5, minor=False)
_ = ax.set_yticks(np.arange(matrix.shape[0])+0.5, minor=False)

_ = ax.set_xlim([0, matrix.shape[1]])
_ = ax.set_ylim([0, matrix.shape[0]])   
_ = ax.set(xlabel='Projection target', ylabel='Exp.ID')       

# want a more natural, table-like display
ax.invert_yaxis()
ax.xaxis.tick_top()

_ = ax.set_xticklabels(column_labels, minor=False)
_ = ax.set_yticklabels(row_labels, minor=False)



# %%
GRN = structure_tree.get_structures_by_acronym(['GRN'])[0]
print("\n\n", GRN['name'], '\n\n')
exps = mcc.get_experiments(cre=False, injection_structure_ids=[GRN['id']])
exps_ids = [ e['id'] for e in exps ]

structures = ['SCm', 'SCs',  'PAG', 'CUN', 'PPN', 'ZI']
sc_structs = ['SCop', 'SCs', 'SCsg', 'SCzo', 'SCiw', 'SCig', 'SCdw', 'SCdg']
ctx_children = [structure_tree.get_structures_by_acronym([s])[0]['id'] for s in sc_structs]
ctx_children.extend(structure_tree.child_ids( [structure_tree.get_structures_by_acronym(['GRN'])[0]['id']] )[0])

pm = mcc.get_projection_matrix(experiment_ids = exps_ids, 
                            projection_structure_ids = ctx_children,
                            hemisphere_ids= [2], # right hemisphere, ipsilateral
                            parameter = 'projection_density')

row_labels = pm['rows'] # these are just experiment ids
column_labels = [ c['label'] for c in pm['columns'] ] 
matrix = pm['matrix']

fig, ax = plt.subplots(figsize=(8,8))
heatmap = ax.pcolor(matrix, cmap=plt.cm.afmhot)

# put the major ticks at the middle of each cell
_ = ax.set_xticks(np.arange(matrix.shape[1])+0.5, minor=False)
_ = ax.set_yticks(np.arange(matrix.shape[0])+0.5, minor=False)

_ = ax.set_xlim([0, matrix.shape[1]])
_ = ax.set_ylim([0, matrix.shape[0]])   
_ = ax.set(xlabel='Projection target', ylabel='Exp.ID')       

# want a more natural, table-like display
ax.invert_yaxis()
ax.xaxis.tick_top()

_ = ax.set_xticklabels(column_labels, minor=False)
_ = ax.set_yticklabels(row_labels, minor=False)


# %%
