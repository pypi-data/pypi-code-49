# -*- coding: utf-8 -*-
from Bio.PDB import *
from atom_type import atom_type
import numpy as np
import sys
import os
import random
from itertools import combinations
from scipy.stats import mannwhitneyu
from scipy.stats import chi2_contingency
from numpy import linalg as LA
import warnings
import gzip
import shutil
import glob
import pickle
from multiprocessing import Process, JoinableQueue, Queue
import matplotlib as mpl
mpl.use('pdf')
import matplotlib.pyplot as plt
from collections import OrderedDict
from scipy.spatial import cKDTree

plt.rc('font', family='sans-serif', serif='Arial')
plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=14)
plt.rc('axes', labelsize=18)
plt.rc('axes', titlesize=18)
# we get all coordinates, b-factors, structure resolution and

AAs= set('ALA,ARG,ASN,ASP,CYS,GLN,GLU,GLY,HIS,ILE,LEU,LYS,MET,PHE,PRO,SER,THR,TRP,TYR,VAL'.split(','))
atom_names = [i.strip() for i in 'C   ,  CA  ,  CB  ,  CD  ,  CD1 ,  CD2 ,  CE  ,  CE1 ,  CE2 ,  CE3 ,  CG  ,  CG1 ,  CG2 ,  CH2 ,  CZ  ,  CZ2 ,  CZ3 ,  H   ,  HA  ,  HB  ,  HC  ,  HD1 ,  HD2 ,  HE  ,  HE1 ,  HE2 ,  HE3 ,  HG  ,  HG1 ,  HH  ,  HH2 ,  HO  ,  HOC ,  HZ  ,  HZ2 ,  HZ3 ,  N   ,  ND1 ,  ND2 ,  NE  ,  NE1 ,  NE2 ,  NH1 ,  NH2 ,  NZ  ,  O   ,  OC  ,  OD1 ,  OD2 ,  OE1 ,  OE2 ,  OG  ,  OG1 ,  OH  ,  SD  ,  SG  , 1H   , 1HA  , 1HB  , 1HD  , 1HD1 , 1HD2 , 1HE  , 1HE2 , 1HG  , 1HG1 , 1HG2 , 1HH1 , 1HH2 , 1HZ  , 2H   , 2HA  , 2HB  , 2HD  , 2HD1 , 2HD2 , 2HE  , 2HE2 , 2HG  , 2HG1 , 2HG2 , 2HH1 , 2HH2 , 2HZ  , 3HB  , 3HD1 , 3HD2 , 3HE  , 3HG1 , 3HG2 , 3HZ'.split(',')]
metals = 'ZN,CA,PO4,MG,MN,FE,CO,NA,K'.split(',')
valid_atoms = set(atom_names+metals +['P']) - {'PO4'}
pdbs = glob.glob('*.pdb')


def worker_task():
    while True:
        pdb = task_queue.get()
        if pdb is None:
            task_queue.task_done()
            break
        readPDB(pdb)
        task_queue.task_done()

def random_unit_vector():
    '''
    This generates a random unit vector
    '''
    generated=False
    while not generated:
        a = np.array([random.uniform(-1,1),random.uniform(-1,1),random.uniform(-1,1)])
        if sum(a*a) > 0 and sum(a*a) <= 1.0:
            generated=True
    return a/np.sqrt(sum(a*a))

def print_nonwaters_as_pdb(non_waters, waters, filename):
    #print ('number of non_waters is %s and number of waters is %s' % (len(non_waters), len(waters)))
    handle = open('%s_predicted_waters.pdb' % filename.split('.')[0], 'w')
    beginning =  'ATOM  61942  NA   NA C 989    '
    if non_waters:
        for non_water in non_waters:
            line = beginning+("%8.3f" % non_water[0])+("%8.3f" % non_water[1])+("%8.3f" % non_water[2]) +'  1.00  0.00'
            handle.write("%s\n" % line)
    beginning2 =  'HETATM%s O   HOH W0000    '
    if waters:
        for i in range(len(waters)):
            water=waters[i]
            line = (beginning2 % (100001+i))+("%8.3f" % water[0])+("%8.3f" % water[1])+("%8.3f" % water[2]) +'  1.00  0.00'
            handle.write("%s\n" % line)
    handle.close()


def read_surface(file_, atoms=None, print_inflated_mesh = False):
    '''
    This function reads in the coordinates defined by EDTSurf (run with option -f 20)
    '''
    handle = open(file_)
    scan_num_vertex = True
    scan_end_header = True
    counter=0
    coordinates = []
    for line in handle:
        if scan_num_vertex:
            if 'element vertex' in line:
                num_vertex = int(line.strip().split()[-1])
                scan_num_vertex = False
        if scan_end_header:
            if 'end_header' in line:
                counter=1
                scan_end_header=False
                continue
        if counter:
            parts = line.strip().split()
            assert('.' in parts[0])
            coordinates.append(map(float, parts[:3]))
            if counter==num_vertex:
                assert (len(coordinates)==num_vertex)
                coordinates = np.array(coordinates)
                handle.close()
                break
            counter+=1
    #if onion: legacy
    grid_sizes = []
    first_layer=-1.8
    first_layer2 = 0.0
    last_layer=5.8
    last_layer2=1.0
    for i in range(100):
        grid_sizes.append(sorted(LA.norm(coordinates- coordinates[random.choice(range(len(coordinates)))], axis=1))[1])
    grid_size = np.max(grid_sizes)
    if atoms is None:
        data, atoms = readPDB('%s.pdb' % (file_.split('.')[0]), pickle_=False, generate_nonwaters=False, return_atoms=True)
    else:
        data = {} # pass on empty data - this is when read surface is called from read_pdb
    atom_list = atoms.keys()
    atom_vectors = np.array(atom_list)
    proteins_centre = np.array([i.get_array() for i in atom_vectors]).mean(0)
    print ('Grid size is %s' % grid_size)
    num_layers_forward = int((last_layer-last_layer2)/grid_size) # we are seaching between 1.0 and 7.5A away
    num_layers_backward = int(-(first_layer-first_layer2)/grid_size)
    print ('Num onion layers is %s' % (num_layers_backward+num_layers_forward))
    print ('Num vertices is %s' % ((num_layers_backward+num_layers_forward)*num_vertex))
    coordinates_ = coordinates-proteins_centre # now the centre is at 0.0
    coordinates = [coordinates]
    mean_norm = np.mean(LA.norm(coordinates_, axis=1))
    scale_tick = grid_size/mean_norm
    print ('Scale tick size is %s' % scale_tick)
    start_forward = int(last_layer2/(mean_norm*scale_tick))
    start_backward = int(first_layer2/(mean_norm*scale_tick))
    coordinates = []
    for i in range(start_backward,num_layers_backward+start_backward):
        coordinates.append((1-(i)*scale_tick)*coordinates_+proteins_centre) # scale each layer and translate back to original position
    coordinates = coordinates[::-1]
    for i in range(start_forward, num_layers_forward+start_forward):
        coordinates.append((1+(i)*scale_tick)*coordinates_+proteins_centre) # scale each layer and translate back to original position
    for i in range(len(coordinates)):
        if print_inflated_mesh:
            handle = open(file_)
            handle2 = open("inflated_%s_%s.ply" % (file_.split('.')[0],i), "w")
            scan_num_vertex = True
            scan_end_header = True
            counter=0
            for line in handle:
                if scan_num_vertex:
                    if 'element vertex' in line:
                        num_vertex = int(line.strip().split()[-1])
                        scan_num_vertex = False
                if scan_end_header:
                    if 'end_header' in line:
                        handle2.write(line)
                        counter=1
                        scan_end_header=False
                        continue
                if counter:
                    handle2.write('%s %s\n' % (' '.join(map(str, coordinates[i][counter-1])),'255 255 255'))
                    counter+=1
                    if counter==num_vertex:
                        counter=False
                else:
                    handle2.write(line)
            handle.close()
            handle2.close()
    coordinates = np.array(coordinates)
    return coordinates, data, atoms

def parse_waters(atoms, waters, print_nonwaters=False, generate_nonwaters = True, nonwater_positions = None, all_nonwaters = False):
    # ensure that at least one atom is no firther than 5A from each water
    # we don't actually use the voxels
    '''
    print_nonwaters - for printing nonwater positions in PDB
    generate_nonwaters - flag specifying whether any (random or mesh) nonwaters are to be generated
    nonwater_positions - positions from the 'onion' mesh
    all_nonwaters - use all nonwaters from mesh, specifies the name for non-water pickled files
    Waters - key is original water position
    then we have vector from atom, atom type, presence in pocket voxel

    For each water, create random positions
    First find the geometric centre of the protein
    Then find atom on the protein's surface along a randomly generated vector
    Randomly choose a non-water position within 5A from this position and ensure that no real water is found closer than 2.5A from this position
    Run this function a desired number of times to get more negative data
    Alternatively, we can generate non-water positions by randomly selecting water molecules and choosing positions a random vector away (idea for the future)
    '''
    atom_list = atoms.keys() # list of atom vectors
    atom_vectors = np.array([i.get_array() for i in atom_list])
    non_waters = OrderedDict()
    waters_rejected=[] # if there are no atoms closer than 5A to the water, we reject that water molecule
    num_waters = len(waters)
    for water in waters:
        distances = atom_vectors-water.get_array()
        norms = LA.norm(atom_vectors-water.get_array(), axis=1)
        neighbor_norms = norms < 7.5
        neighbor_norms2 = norms < 4.6 # this just introduces a closer threshold to only include better examples
        if sum(neighbor_norms2)>3:
            counter_=0
            for i in neighbor_norms:
                if i:
                    if 'vectors' not in waters[water]:
                        waters[water]['vectors'] = [(Vector(distances[counter_]), atoms[atom_list[counter_]])]
                    else:
                        waters[water]['vectors'].append((Vector(distances[counter_]), atoms[atom_list[counter_]]))
                counter_+=1
        if len(waters[water])==0:
            waters_rejected.append(water)
    water_array = np.array([i.get_array() for i in waters.keys()])
    if generate_nonwaters:
        print ('generating non_waters')
        assert (nonwater_positions is not None)
        num_to_generate=len(waters)-len(waters_rejected)
        if all_nonwaters: # this is to use nonwaters from EDTSurf
            # check how many have already been generated previously
            already_generated = glob.glob('%s_[0-9].pickle' % (all_nonwaters))+glob.glob('%s_[0-9][0-9].pickle' % (all_nonwaters))
            if already_generated:
                already_generated = sorted([int(i.split('_')[-1].split('.')[0]) for i in already_generated])[-1]
                print("Already generated layers %s" % already_generated)
            else:
                already_generated=0
            num_to_generate = len(nonwater_positions)*len(nonwater_positions[0])
            total_to_generate = num_to_generate
            num_to_generate = num_to_generate-len(nonwater_positions[0])*already_generated
            print ("Number left to generate %s" % num_to_generate)
            counter = len(nonwater_positions[0])*already_generated
        very_far = False
        while num_to_generate>0:
            generated=False
            while not generated:
                if not all_nonwaters:
                    # generate the water away from the voxel
                    random1=-1
                    while random1 <0 or random1>=len(nonwater_positions):
                        random1 = np.random.normal(loc=len(nonwater_positions)/2.0, scale=np.sqrt(1.5*len(nonwater_positions)))
                    random1 = int(random1)
                    random2 = random.randint(0, len(nonwater_positions[0])-1)
                    nonwater_position = nonwater_positions[random1][random2]
                    # generate non_water and make sure water is not already presnet there...
                    if not very_far:
                        while min(LA.norm(water_array-nonwater_position, axis=1).tolist()) < 1.4 : # double check that water  is not already present here
                            random1=-1
                            while random1 <0 or random1>=len(nonwater_positions):
                                random1 = np.random.normal(loc=len(nonwater_positions)/3, scale=np.sqrt(1.5*len(nonwater_positions)))
                            random1 = int(random1)
                            random2 = random.randint(0,len(nonwater_positions[0])-1)
                            nonwater_position = nonwater_positions[random1][random2]
                    else:
                        while min(LA.norm(water_array-nonwater_position, axis=1).tolist()) < 1.4 or min(LA.norm(atom_vectors-nonwater_position, axis=1).tolist()) >= 7.5: # double check that water  is not already present here
                            random1=-1
                            while random1 <0 or random1>=len(nonwater_positions):
                                random1 = np.random.normal(loc=len(nonwater_positions)/3, scale=np.sqrt(1.5*len(nonwater_positions)))
                            random1 = int(random1)
                            random2 = random.randint(0,len(nonwater_positions[0])-1)
                            nonwater_position = nonwater_positions[random1][random2]
                    nonwater_position_ = Vector(nonwater_position)
                    non_waters[nonwater_position_] = {}
                else:
                	#add code that checks that non-waters are already generates so that code continues later... (fix the 4uis & 1g6v runs)
                    nonwater_position = nonwater_positions[counter/len(nonwater_positions[0])][counter % len(nonwater_positions[0])] # the purpose of this is to add all nonwater-positions generated by EDTSurf
                    counter+=1
                    nonwater_position_ = Vector(nonwater_position)
                    non_waters[nonwater_position_] = {}
                distances = atom_vectors-nonwater_position
                norms = LA.norm(atom_vectors-nonwater_position, axis=1)
                neighbor_norms = norms < 7.5
                counter_=0
                for i in neighbor_norms:
                    if i or ((all_nonwaters or not very_far) and not np.max(neighbor_norms)): # the purpose of this or is to add at least one vector for nonwater even if too far - when dealing with EDTSurf mesh
                        if 'vectors' not in non_waters[nonwater_position_]:
                            if not i: # this is when all are greater (or equal) 7.5
                                non_waters[nonwater_position_]['vectors'] = [(Vector(distances[norms.tolist().index(np.min(norms))]), atoms[atom_list[norms.tolist().index(np.min(norms))]])]
                                very_far=True
                            else:
                                non_waters[nonwater_position_]['vectors'] = [(Vector(distances[counter_]), atoms[atom_list[counter_]])]
                        else:
                            non_waters[nonwater_position_]['vectors'].append((Vector(distances[counter_]), atoms[atom_list[counter_]]))
                    counter_+=1
                    if very_far and 'vectors' in non_waters[nonwater_position_] and len(non_waters[nonwater_position_]['vectors'])==50:
                        break
                if nonwater_position_ in non_waters:
                    generated=True
                    num_to_generate-=1
                    if not all_nonwaters:
                        print ('non_water generated, no. interacting atoms is %s' % len(non_waters[nonwater_position_]['vectors']))
                    if all_nonwaters and (total_to_generate-num_to_generate) % len(nonwater_positions[0])==0:
                        data = {'waters':waters, 'non_waters':non_waters}
                        pickle.dump(data, open('%s_%s.pickle' % (all_nonwaters, (total_to_generate-num_to_generate)/len(nonwater_positions[0])), 'wb'), protocol=pickle.HIGHEST_PROTOCOL)
                        non_waters = OrderedDict() # after dumping file I empty non_water dict in order to save memory
    print ("%s out of %s waters rejected" % (len(waters_rejected),len(waters)))
    for water in waters_rejected:
        del waters[water]
    if print_nonwaters:
        print_nonwaters_as_pdb(non_waters,waters, print_nonwaters)
    else:
        print ('print nonwaters set to false')
    return waters, non_waters, len(waters_rejected), len(waters_rejected)+num_waters


def readPDB(filename, print_nonwaters=False, pickle_=True, generate_nonwaters=True, return_atoms = False):
    """
    Returns atom coordinates & water data
    """
    data = {}
    handle = open(filename)
    resolution=0
    r_factor=0
    solvent_content =  0
    for line in handle:
        parts = line.strip().split()
        if len(parts) >=4  and parts[0]=='REMARK' and parts[1]=='2' and parts[2]=='RESOLUTION.':
            try:
                resolution=float(parts[3])
            except:
                continue
        elif len(parts) >=6  and parts[0]=='REMARK' and parts[1]=='3' and parts[2]=='R' and parts[3]=='VALUE' and parts[4]=='(WORKING' and 'SET' in parts[5]:
            try:
                r_factor = float(parts[-1])
            except:
                continue
        elif len(parts) >=5  and parts[0]=='REMARK' and parts[1]=='280' and parts[2]=='SOLVENT' and parts[3]=='CONTENT,' and parts[4]=='VS':
            try:
                solvent_content = float(parts[-1])
            except:
                continue
    handle.close()
    print('Reading %s PDB file, resolution: %s, R-factor: %s, solvent per-cent: %s' % (filename.split('/')[-1].split('.')[0],resolution, r_factor, solvent_content) )
    handle.close()
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        atoms = {}
        waters = {}
        p=PDBParser()
        structure=p.get_structure('name', filename)
        for model in structure:
            for chain in model:
                for residue in chain:
                    if residue.resname in AAs or residue.resname in metals:
                        for atom in residue.child_dict.keys():
                            if atom in valid_atoms:
                                if residue.resname in AAs:
                                    atoms[residue[atom].get_vector()] = (atom,residue.resname, residue[atom].get_bfactor())
                                elif residue.resname in metals:
                                    atoms[residue[atom].get_vector()] = (atom,None, residue[atom].get_bfactor())
                    elif residue.resname=='HOH': # TODO: add reading of metal ions
                        if residue['O'].get_occupancy()==1.0:
                            waters[residue['O'].get_vector()] = {}
        if generate_nonwaters:
            try:
                coordinates, data, atoms = read_surface("%s.ply" % filename.split('.')[0], atoms=atoms)
            except:
                os.system('./EDTSurf -i %s -o %s -f 20 -h 2' % (filename, filename.split('.')[0]))
                coordinates, data, atoms = read_surface("%s.ply" % filename.split('.')[0], atoms=atoms)
            waters, non_waters, waters_rejected, total_waters = parse_waters(atoms, waters, print_nonwaters=print_nonwaters, generate_nonwaters=generate_nonwaters,nonwater_positions =coordinates)
        else:
            waters, non_waters, waters_rejected, total_waters = parse_waters(atoms, waters, print_nonwaters=print_nonwaters, generate_nonwaters=generate_nonwaters)
        data = {'waters':waters, 'non_waters':non_waters, 'waters_rejected':waters_rejected, 'total_waters':total_waters, 'resolution': resolution, 'r_factor':r_factor, 'solvent_content':solvent_content}
        if pickle_:
            pickle.dump(data, open('%s.pickle' % filename.split('.')[0], "wb"), protocol=pickle.HIGHEST_PROTOCOL)
        if return_atoms:
            return data, atoms
        else:
            return data



def process_waters(waters, vectors, b_values, num_atoms_to_consider=50,output_original_coordinates= False):
    '''
    This runs preprocessing on (non)waters and reurns data in format usable as input in the ML model
    '''
    if output_original_coordinates:
        original_cooridinates = []
    for water in waters:
        if output_original_coordinates:
            original_cooridinates.append(water)
        temp = np.zeros([num_atoms_to_consider,3])
        temp2 = np.ones([num_atoms_to_consider,30]) # since 1 is a 'bad' beta factor
        water_vectors = [i[0].__pow__(1.0/7.5) for i in waters[water]['vectors']] # normalized such that they are between 0 and 1
        water_vector_norms = [i.norm() for i in water_vectors]
        if np.max(water_vector_norms) >1.0:
            vectors.append(temp)
            b_values.append(np.zeros([num_atoms_to_consider,30]))
            continue
        closest_ids = sorted(range(len(water_vector_norms)), key=lambda k: water_vector_norms[k])
        atoms = [i[1][0] for i in waters[water]['vectors']]
        resids = [i[1][1] for i in waters[water]['vectors']]
        #betas = [np.log10(1+i[1][2])/2.7 for i in waters[water]['vectors']] # this was the original normalization
        betas = [np.log10(1+i[1][2]) for i in waters[water]['vectors']]
        if np.max(betas)==np.min(betas):
            betas = [0]*len(betas)
        else:
            betas = [(i-np.min(betas))/(np.max(betas)-np.min(betas)) for i in betas]
        ### dtete this betas = [np.log10(1+i[1][2])/max([np.log10(1+j[1][2]) for j in waters[water]['vectors']]) for i in waters[water]['vectors']] # per protein normalization
        angles = np.zeros([len(water_vectors), len(water_vectors)])
        if len(water_vectors) >1:
            for comb in combinations(range(len(water_vectors)),2):
                angles[comb[0], comb[1]] = water_vectors[comb[0]].angle(water_vectors[comb[1]])
                angles[comb[1], comb[0]] = water_vectors[comb[0]].angle(water_vectors[comb[1]])
            e1 = water_vectors[closest_ids[0]].normalized() # closest atom, then largest angle to closest
            id_of_partner = list(angles[closest_ids[0]]).index(max(angles[closest_ids[0]]))
            e2 = water_vectors[id_of_partner]-e1.__pow__(e1.__mul__(water_vectors[id_of_partner]))
            e2.normalize()
            e3= e1.__pow__(e2)
            m = np.array([e3[:], e2[:], e1[:]]) # normalization rotation-matrix
            done_waters= set([closest_ids[0], id_of_partner])
            index = atom_type(atoms[id_of_partner], resids[id_of_partner])#atom_names.index(atoms[id_of_partner])# this is correct
            normalized_coordinates = water_vectors[id_of_partner].left_multiply(m)[:]
            temp2[1,index] = betas[id_of_partner] # append beta factor
            temp[1,:] = normalized_coordinates
            if len(done_waters) < len(water_vectors):
                for id_ in closest_ids[1:]:
                    if len(done_waters) == num_atoms_to_consider:
                        break
                    if id_ in done_waters:
                        continue
                    else:
                        done_waters.add(id_)
                        index = atom_type(atoms[id_], resids[id_])#atom_names.index(atoms[id_])# this is correct
                        normalized_coordinates = water_vectors[id_].left_multiply(m)[:] # normalize coordinates
                        temp2[len(done_waters)-1,index] = betas[id_] # append beta factor
                        temp[len(done_waters)-1,:] = normalized_coordinates
                        if len(done_waters) < len(water_vectors) and len(done_waters) < num_atoms_to_consider:
                            ids_of_partners = sorted(range(len(angles[id_])), key=lambda k: angles[id_][k])
                            for id__ in ids_of_partners:
                                if id__ in done_waters:
                                    id_of_partner2 = id__
                                    break
                            done_waters.add(id_of_partner2)
                            index = atom_type(atoms[id_of_partner2], resids[id_of_partner2])#atom_names.index(atoms[id_of_partner2])# this is correct
                            normalized_coordinates = water_vectors[id_of_partner2].left_multiply(m)[:] # normalize coordinates
                            temp2[len(done_waters)-1,index] = betas[id_of_partner2] # append beta factor
                            temp[len(done_waters)-1,:] = normalized_coordinates
        else:
            e1 = water_vectors[closest_ids[0]].normalized()
            partner = Vector(3*random_unit_vector())
            e2 = partner-e1.__pow__(e1.__mul__(partner))
            e2.normalize()
            e3= e1.__pow__(e2)
            m = np.array([e3[:], e2[:], e1[:]]) # normalization rotation-matrix
        #at the end add first atom regardless whether we have one atom or more...
        index = atom_type(atoms[closest_ids[0]], resids[closest_ids[0]])#atom_names.index(atoms[closest_ids[0]])# this is correct
        normalized_coordinates = water_vectors[closest_ids[0]].left_multiply(m)[:] # normalize coordinates
        temp2[0,index] = betas[closest_ids[0]] # append beta factor
        temp[0,:] = normalized_coordinates
        vectors.append(temp)
        b_values.append(np.ones([num_atoms_to_consider,30]) -temp2)
    if output_original_coordinates:
        return vectors, b_values, original_cooridinates
    else:
        return vectors, b_values












