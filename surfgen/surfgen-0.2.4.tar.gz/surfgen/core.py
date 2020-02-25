# ase
from ase.build import molecule, bulk
from ase.visualize import view
from ase.constraints import FixAtoms
from ase.io import read

# pymatgen
from pymatgen.io.ase import AseAtomsAdaptor
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from pymatgen.core.surface import SlabGenerator
from pymatgen.analysis.adsorption import AdsorbateSiteFinder

# python module
import copy
import numpy as np

# surfgen
from surfgen.util import *
from surfgen.math import *

############################## Here comes the Python code ##############################

def slab_generator(bulk, miller_index, slab_height, vacuum, supercell):

    """
    This function can generate slab from the ASE bulk object

    Parameter:

    bulk:
        ASE Object. It is the bulk that we want to cut surface from

    miller_index:
        (3x1) tuple. It defines the miller index of the surface

    slab_height:
        Real (in Angstrom). It defines how large your surface slab should be on z-direction

        .. note:: You need to try slab_height first to generate the desired slab that you want to have. A role of thumb is that usually 10.0 is large enough for the calculations.

    vacuum:
        Real (in Angstrom). It defines the length of the vacuum layer

    supercell:
        (3x1) tuple or (3x3) np.array. It defines the supercell of our surface slab

        * (3x3) np.array is quite useful in generating surface like sqrt(3)*sqrt(3)

    Return:
        Atoms object, which is the slab that we want
    """

    # convert ASE object (bulk) to pymatgen object
    bulk_pmg = AseAtomsAdaptor.get_structure(bulk)

    bulk_pmg = SpacegroupAnalyzer(bulk_pmg).get_conventional_standard_structure()

    # create miller_index surfaces (return a list of surfaces)
    slab_gen = SlabGenerator(bulk_pmg,
                             miller_index,
                             min_slab_size = slab_height,
                             min_vacuum_size = vacuum,
                             center_slab = True)

    # convert everything to ASE object
    ase_slabs = []

    for slab in slab_gen.get_slabs():

        ase_slabs.append(AseAtomsAdaptor.get_atoms(slab) * supercell)

    return ase_slabs

def surf_atom_finder(slab, upper_lower = 'upper'):

    """
    This function is used to get the surface atom

    Parameters:

    slab:
        the surface slab that you want, it must be clean surface (without adsorption)

    upper_lower:
        string, to state whether you want the upper layer or lower layer or both.

        e.g. 'upper', 'lower', 'both'. In default it is 'upper'

        * 'upper': return indexes of atoms on upper surface layer

        * 'lower': return indexes of atoms on lower surface layer

        * 'both': return both of the surface layers
    """

    # parameter in this function (this can be adjust)

    threshold = 2.4 # when the bug has 1 angstrom distance to the surface atom

    step = 0.5 # if the bug survives, the how much distance should it move

    # first I need to create a dense points of "bugs" that I want to put on the surface
    v1 = slab.get_cell()[0]

    v2 = slab.get_cell()[1]

    num_x = 5 * (int(np.linalg.norm(v1))+1)

    num_y = 5 * (int(np.linalg.norm(v2))+1)

    # get the highest and lowest surface slab
    highest_z_coord = np.max(slab.get_positions()[:, 2])

    lowest_z_coord = np.min(slab.get_positions()[:, 2])

    bugs_upper_layer = [] # bugs for upper layer

    bugs_lower_layer = [] # bugs for lower layer

    surf_atom_upper = [] # surface atom from upper layer

    surf_atom_lower = [] # surface atom from lower layer

    for i in range(1, num_x): # in here 1 means we don't want to be at the edge

        for j in range(1, num_y):

            v1_step = v1 / num_x * i

            v2_step = v2 / num_y * j

            bugs_upper_layer.append([v1_step[0] + v2_step[0], v1_step[1] + v2_step[1], highest_z_coord + 3])

            bugs_lower_layer.append([v1_step[0] + v2_step[0], v1_step[1] + v2_step[1], lowest_z_coord - 3])

    # now let the bugs do their thing

    if (upper_lower == 'upper') or (upper_lower == 'both'):

        # the upper layer
        while len(bugs_upper_layer):

            kill_list = [] # store all the bugs that are dead

            for item, bug in enumerate(bugs_upper_layer):

                # iterate all atoms in the slab
                for atom in slab:

                    if np.linalg.norm(bug - atom.position) <= threshold:

                        if not(bug in kill_list):

                            kill_list.append(bug)# kill the bug

                        if not(atom.index in surf_atom_upper):

                            surf_atom_upper.append(atom.index) # found one surface atom
                        else:

                            pass
                    else:

                        pass

            # clear the dead bugs
            for dead_bug in kill_list:

                bugs_upper_layer.remove(dead_bug)

            # if there are still survived bugs
            for bug in bugs_upper_layer:

                bug[2] -= step

    if (upper_lower == 'lower') or (upper_lower == 'both'):

    # the lower layer
        while len(bugs_lower_layer):

            kill_list = [] # store all the bugs that are dead

            for item, bug in enumerate(bugs_lower_layer):

                # iterate all atoms in the slab
                for atom in slab:

                    if np.linalg.norm(bug - atom.position) <= threshold:

                        if not(bug in kill_list):

                            kill_list.append(bug)# kill the bug

                        if not(atom.index in surf_atom_lower):

                            surf_atom_lower.append(atom.index) # found one surface atom
                        else:

                            pass
                    else:

                        pass

            # clear the dead bugs
            for dead_bug in kill_list:

                bugs_lower_layer.remove(dead_bug)

            # if there are still survived bugs
            for bug in bugs_lower_layer:

                bug[2] += step

    if upper_lower == 'upper':

        return surf_atom_upper

    if upper_lower == 'lower':

        return surf_atom_lower

    if upper_lower == 'both':

        return [surf_atom_upper, surf_atom_lower]

def connection_matrix(slab, surface_atoms, bond_length):

    """
    This function can help us determine the connection matrix in the slab, and it will return two things:

    1. The connection matrix (which contains the index information)

    2. All the coordinates (which contains all the information of coordinates)

    Parameters:

    slab:
        The slab that we need

    surface_atoms:
        all the indexes of atoms on the surface

    Return:
        Two dictionaries and one list.

        Two dictionaries are:

            * connector. It defines all the nearest neighbour of top surface layer atoms

            * conn_coordinates. It defines all the coordinates of the atoms above

        One list is:

            * outer_atom_index. It defines all the index of atoms on the outside of our slab.
    """

    # get the cell vector
    v1_sc = slab.get_cell()[0]

    v2_sc = slab.get_cell()[1]

    # get all atoms in first layer
    first_layer = []

    for atom in slab:

        if atom.index in surface_atoms:

            first_layer.append(atom)

    # create the periodic repetition of the first layer
    outer_layer = []

    movement_vector = []

    index_multiplier = {'[-1, 0]': 1,
                        '[1, 0]': 2,
                        '[0, -1]': 3,
                        '[0, 1]': 4,
                        '[-1, -1]': 5,
                        '[1, -1]': 6,
                        '[1, 1]': 7,
                        '[-1, 1]': 8}

    outer_atom_index = []

    for atom in slab:

        outer_layer.append(atom.position + (-1)*v1_sc + (0)*v2_sc) # (-1,0)

        movement_vector.append([-1, 0])

        outer_atom_index.append(atom.index + len(slab)*index_multiplier['[-1, 0]'])

        outer_layer.append(atom.position + (1)*v1_sc + (0)*v2_sc) # (1,0)

        movement_vector.append([1, 0])

        outer_atom_index.append(atom.index + len(slab)*index_multiplier['[1, 0]'])

        outer_layer.append(atom.position + (0)*v1_sc + (-1)*v2_sc) # (0, -1)

        movement_vector.append([0, -1])

        outer_atom_index.append(atom.index + len(slab)*index_multiplier['[0, -1]'])

        outer_layer.append(atom.position + (0)*v1_sc + (1)*v2_sc) # (0, 1)

        movement_vector.append([0, 1])

        outer_atom_index.append(atom.index + len(slab)*index_multiplier['[0, 1]'])

        outer_layer.append(atom.position + (-1)*v1_sc + (-1)*v2_sc) # (-1, -1)

        movement_vector.append([-1, -1])

        outer_atom_index.append(atom.index + len(slab)*index_multiplier['[-1, -1]'])

        outer_layer.append(atom.position + (1)*v1_sc + (-1)*v2_sc) # (1, -1)

        movement_vector.append([1, -1])

        outer_atom_index.append(atom.index + len(slab)*index_multiplier['[1, -1]'])

        outer_layer.append(atom.position + (1)*v1_sc + (1)*v2_sc) # (1, 1)

        movement_vector.append([1, 1])

        outer_atom_index.append(atom.index + len(slab)*index_multiplier['[1, 1]'])

        outer_layer.append(atom.position + (-1)*v1_sc + (1)*v2_sc) # (-1, 1)

        movement_vector.append([-1, 1])

        outer_atom_index.append(atom.index + len(slab)*index_multiplier['[-1, 1]'])

    # construct the connection network
    connector = {}

    conn_coordinates = {}

    for atom1 in first_layer:

        connector[str(atom1.index)] = []

        conn_coordinates[str(atom1.index)] = []

        for atom2 in slab:

            if (atom1.index != atom2.index):

                distance = np.linalg.norm(atom1.position - atom2.position)

                if abs(distance - bond_length) < 0.01:

                    connector[str(atom1.index)].append(atom2.index)

                    conn_coordinates[str(atom1.index)].append(atom2.position)

        # check the distance between atom1 and outer_layer
        for item, atom2 in enumerate(outer_layer):

            distance = np.linalg.norm(atom1.position - atom2)

            if abs(distance - bond_length) < 0.01:

                connector[str(atom1.index)].append(outer_atom_index[item])

                conn_coordinates[str(atom1.index)].append(atom2)

    return connector, conn_coordinates, outer_atom_index

def get_coordination_number(slab, surface_atoms, bond_length):

    """
    This function can help us determine the coordination number of the top layer of the surface.

    Parameters:

    slab:
        The slab that we need

    surface_atoms:
        all the indexes of atoms on the surface

    Return:
        A dictionary. {atom_index: coordination_number}
    """

    # get the cell vector
    v1_sc = slab.get_cell()[0]

    v2_sc = slab.get_cell()[1]

    # get all atoms in first layer
    first_layer = []

    for atom in slab:

        if atom.index in surface_atoms:

            first_layer.append(atom)

    # create the periodic repetition of the first layer
    outer_layer = []

    movement_vector = []

    index_multiplier = {'[-1, 0]': 1,
                        '[1, 0]': 2,
                        '[0, -1]': 3,
                        '[0, 1]': 4,
                        '[-1, -1]': 5,
                        '[1, -1]': 6,
                        '[1, 1]': 7,
                        '[-1, 1]': 8}

    outer_atom_index = []

    for atom in slab:

        outer_layer.append(atom.position + (-1)*v1_sc + (0)*v2_sc) # (-1,0)

        movement_vector.append([-1, 0])

        outer_atom_index.append(atom.index + len(slab)*index_multiplier['[-1, 0]'])

        outer_layer.append(atom.position + (1)*v1_sc + (0)*v2_sc) # (1,0)

        movement_vector.append([1, 0])

        outer_atom_index.append(atom.index + len(slab)*index_multiplier['[1, 0]'])

        outer_layer.append(atom.position + (0)*v1_sc + (-1)*v2_sc) # (0, -1)

        movement_vector.append([0, -1])

        outer_atom_index.append(atom.index + len(slab)*index_multiplier['[0, -1]'])

        outer_layer.append(atom.position + (0)*v1_sc + (1)*v2_sc) # (0, 1)

        movement_vector.append([0, 1])

        outer_atom_index.append(atom.index + len(slab)*index_multiplier['[0, 1]'])

        outer_layer.append(atom.position + (-1)*v1_sc + (-1)*v2_sc) # (-1, -1)

        movement_vector.append([-1, -1])

        outer_atom_index.append(atom.index + len(slab)*index_multiplier['[-1, -1]'])

        outer_layer.append(atom.position + (1)*v1_sc + (-1)*v2_sc) # (1, -1)

        movement_vector.append([1, -1])

        outer_atom_index.append(atom.index + len(slab)*index_multiplier['[1, -1]'])

        outer_layer.append(atom.position + (1)*v1_sc + (1)*v2_sc) # (1, 1)

        movement_vector.append([1, 1])

        outer_atom_index.append(atom.index + len(slab)*index_multiplier['[1, 1]'])

        outer_layer.append(atom.position + (-1)*v1_sc + (1)*v2_sc) # (-1, 1)

        movement_vector.append([-1, 1])

        outer_atom_index.append(atom.index + len(slab)*index_multiplier['[-1, 1]'])

    # construct the connection network
    connector = {}

    conn_coordinates = {}

    coord_number_top_layer = {}

    for atom1 in first_layer:

        connector[str(atom1.index)] = []

        conn_coordinates[str(atom1.index)] = []

        for atom2 in slab:

            if (atom1.index != atom2.index):

                distance = np.linalg.norm(atom1.position - atom2.position)

                if abs(distance - bond_length) < 0.01:

                    connector[str(atom1.index)].append(atom2.index)

                    conn_coordinates[str(atom1.index)].append(atom2.position)

                # check the distance between atom1 and outer_layer
        for item, atom2 in enumerate(outer_layer):

            distance = np.linalg.norm(atom1.position - atom2)

            if abs(distance - bond_length) < 0.01:

                connector[str(atom1.index)].append(outer_atom_index[item])

                conn_coordinates[str(atom1.index)].append(atom2)

    for atom in first_layer:

        coord_number_top_layer[str(atom.index)] = len(connector[str(atom.index)])

    return coord_number_top_layer

def find_all_ads_sites(slab, connector, conn_coordinates, surf_atoms, bond_length):

    """
    This function can help us generate all possible adsorption sites on a surface.

    Parameters:

    slab:
        slab that we want to find adsorption sites

    connector:
        the connection matrix of all atoms on top layer

    conn_coordiantes:
        coordinates of all atoms on top layer and its related atoms

    surf_atoms:
        index of all atoms on top layer

    bond_length:
        for determining the bridge site

    Return:
        a dictionary which contains informations for 'ontop', 'bridge', 'hollow' and 'four_fold' sites

        There are three pieces of information:

        * location: contains the location of adsorption sites

        * norm_vector: contains the norm_vector for each adsorption sites

        * label: contains the index of atoms that construct the adsorption sites
    """

    # type of sites and height of adsorption site
    sites = ['ontop', 'bridge', 'hollow', 'four_fold']

    height = {
        'ontop': 1.5,
        'bridge': 1.2,
        'hollow': 1,
        'four_fold': 1
    }

    # construct the adsorption sites using "sites" parameter
    ads_sites = {} # return a dictionary

    for site in sites:

        ads_sites[site] = {} # an empty dictionary which contains two things: (1) location (2) norm_vector
        ads_sites[site]['location'] = [] # empty list of "location"
        ads_sites[site]['norm_vector'] = [] # empty list of "norm_vector"
        ads_sites[site]['label'] = [] # which atoms form the adsorption site

    # three sets for storing all adsorption sites:

    ontop_site_ensemble = []

    bridge_site_ensemble = []

    hcp_site_ensemble = []

    four_fold_site_ensemble = []

    # start constructing all the ontop and hollow adsorption sites

    norm_vec_assemble = {} # dictionary which contains all the normalized vectors

    for i in connector:

        coord_center_atom = slab[int(i)].position

        norm_vec_assemble[i] = []

        tmp_vec = []

        # set the first index
        index_1 = int(i)

        for item1, coord_atom1 in enumerate(conn_coordinates[i]):

            # set the second index
            index_2 = connector[i][item1]

            for item2, coord_atom2 in enumerate(conn_coordinates[i]):

                index_3 = connector[i][item2]

                # check whether it can form a 3-fold hollow site
                if (index_1 in surf_atoms) and (index_2 in surf_atoms) and (index_3 in surf_atoms) and check_hollow(coord_center_atom, coord_atom1, coord_atom2):

                    vector1 = coord_atom1 - coord_center_atom

                    vector2 = coord_atom2 - coord_center_atom

                    norm_vector = np.cross(vector1, vector2)

                    if norm_vector[2] < 0:

                        norm_vector = norm_vector * (-1) # the norm vector always points outwards

                    norm_vector = norm_vector / np.linalg.norm(norm_vector) # the norm vector is normalized, means its length is 1

                    norm_vec_assemble[i].append(norm_vector)

                    tmp_vec.append(norm_vector)

                    # construct the hollow site
                    tmp = np.sort(np.array([index_1, index_2, index_3]))

                    name_hollow = '1_' + str(tmp[0]) + '-2_' + str(tmp[1]) + '-3_' + str(tmp[2])

                    if not (name_hollow in hcp_site_ensemble):
                        coord_hollow_site = (coord_center_atom + coord_atom1 + coord_atom2) / 3 + height['hollow'] * norm_vector

                        ads_sites['hollow']['location'].append(coord_hollow_site)

                        ads_sites['hollow']['norm_vector'].append(norm_vector)

                        ads_sites['hollow']['label'].append(str(tmp[0]) + '.' + str(tmp[1]) + '.' + str(tmp[2]))

                        hcp_site_ensemble.append(name_hollow)

                    # check whether it can form a bridge site between central atom and item 1
                    tmp = np.sort(np.array([index_1, index_2]))

                    name_bridge = '1_' + str(tmp[0]) + '-2_' + str(tmp[1])

                    if not (name_bridge in bridge_site_ensemble):
                        coord_bridge_site = (coord_center_atom + coord_atom1) / 2 + height['bridge'] * norm_vector

                        ads_sites['bridge']['location'].append(coord_bridge_site)

                        ads_sites['bridge']['norm_vector'].append(norm_vector)

                        ads_sites['bridge']['label'].append(str(tmp[0]) + '.' + str(tmp[1]))

                        bridge_site_ensemble.append(name_bridge)

                    # check whether it can form a bridge site between central atom and item 2
                    tmp = np.sort(np.array([index_1, index_3]))

                    name_bridge = '1_' + str(tmp[0]) + '-2_' + str(tmp[1])

                    if not (name_bridge in bridge_site_ensemble):

                        coord_bridge_site = (coord_center_atom + coord_atom2) / 2 + height['bridge'] * norm_vector

                        ads_sites['bridge']['location'].append(coord_bridge_site)

                        ads_sites['bridge']['norm_vector'].append(norm_vector)

                        ads_sites['bridge']['label'].append(str(tmp[0]) + '.' + str(tmp[1]))

                        bridge_site_ensemble.append(name_bridge)

                    # check whether it can form a bridge site between item 1 and item 2
                    tmp = np.sort(np.array([index_2, index_3]))

                    name_bridge = '1_' + str(tmp[0]) + '-2_' + str(tmp[1])

                    if not (name_bridge in bridge_site_ensemble):

                        coord_bridge_site = (coord_center_atom + coord_atom2) / 2 + height['bridge'] * norm_vector

                        ads_sites['bridge']['location'].append(coord_bridge_site)

                        ads_sites['bridge']['norm_vector'].append(norm_vector)

                        ads_sites['bridge']['label'].append(str(tmp[0]) + '.' + str(tmp[1]))

                        bridge_site_ensemble.append(name_bridge)

                else:
                # check whether it can form a 4-fold hollow site

                    conn_coordinates_3 = []

                    conn_coordinates_3.extend(conn_coordinates[i])

                    if str(index_2) in conn_coordinates:

                        conn_coordinates_3.extend(conn_coordinates[str(index_2)])

                    if str(index_3) in conn_coordinates:

                        conn_coordinates_3.extend(conn_coordinates[str(index_3)])

                    connector_3 = np.array([])

                    connector_3 = np.append(connector_3, connector[i])

                    if str(index_2) in connector:

                        connector_3 = np.append(connector_3, connector[str(index_2)])

                    if str(index_3) in connector:

                        connector_3 = np.append(connector_3, connector[str(index_3)])

                    for item3, coord_atom3 in enumerate(conn_coordinates_3):

                        index_4 = int(connector_3[item3])

                        if (index_1 in surf_atoms) and (index_2 in surf_atoms) and (index_3 in surf_atoms) and (index_4 in surf_atoms) and check_4fold(coord_center_atom, coord_atom1, coord_atom2, coord_atom3):

                            vector1 = coord_atom1 - coord_center_atom

                            vector2 = coord_atom2 - coord_center_atom

                            norm_vector = np.cross(vector1, vector2)

                            if norm_vector[2] < 0:

                                norm_vector = norm_vector * (-1) # the norm vector always points outwards

                            norm_vector = norm_vector / np.linalg.norm(norm_vector) # the norm vector is normalized, means its length is 1

                            norm_vec_assemble[i].append(norm_vector)

                            tmp_vec.append(norm_vector)

                            # construct 4-fold site
                            tmp = np.sort(np.array([index_1, index_2, index_3, index_4]))

                            name_four_fold = '1_' + str(tmp[0]) + '-2_' + str(tmp[1]) + '-3_' + str(tmp[2]) + '-4_' + str(tmp[3])

                            # check
                            if not (name_four_fold in four_fold_site_ensemble):

                                coord_four_fold_site = (coord_center_atom + coord_atom1 + coord_atom2 + coord_atom3) / 4 + height['four_fold'] * norm_vector

                                ads_sites['four_fold']['location'].append(coord_four_fold_site)

                                ads_sites['four_fold']['norm_vector'].append(norm_vector)

                                ads_sites['four_fold']['label'].append(str(tmp[0]) + '.' + str(tmp[1]) + '.' + str(tmp[2]) + '.' + str(tmp[3]))

                                four_fold_site_ensemble.append(name_four_fold)

                            # construct bridge sites

                            d12 = np.linalg.norm(coord_center_atom - coord_atom1)

                            d13 = np.linalg.norm(coord_center_atom - coord_atom2)

                            d14 = np.linalg.norm(coord_center_atom - coord_atom3)

                            d23 = np.linalg.norm(coord_atom1 - coord_atom2)

                            d24 = np.linalg.norm(coord_atom1 - coord_atom3)

                            d34 = np.linalg.norm(coord_atom2 - coord_atom3)

                            if (abs(d12 - bond_length) < 0.1):

                                tmp = np.sort(np.array([index_1, index_2]))

                                name_bridge = '1_' + str(tmp[0]) + '-2_' + str(tmp[1])

                                if not (name_bridge in bridge_site_ensemble):

                                    coord_bridge_site = (coord_center_atom + coord_atom1) / 2 + height['bridge'] * norm_vector

                                    ads_sites['bridge']['location'].append(coord_bridge_site)

                                    ads_sites['bridge']['norm_vector'].append(norm_vector)

                                    ads_sites['bridge']['label'].append(str(tmp[0]) + '.' + str(tmp[1]))

                                    bridge_site_ensemble.append(name_bridge)

                            if (abs(d13 - bond_length) < 0.1):

                                tmp = np.sort(np.array([index_1, index_3]))

                                name_bridge = '1_' + str(tmp[0]) + '-2_' + str(tmp[1])

                                if not (name_bridge in bridge_site_ensemble):

                                    coord_bridge_site = (coord_center_atom + coord_atom2) / 2 + height['bridge'] * norm_vector

                                    ads_sites['bridge']['location'].append(coord_bridge_site)

                                    ads_sites['bridge']['norm_vector'].append(norm_vector)

                                    ads_sites['bridge']['label'].append(str(tmp[0]) + '.' + str(tmp[1]))

                                    bridge_site_ensemble.append(name_bridge)

                            if (abs(d14 - bond_length) < 0.1):

                                tmp = np.sort(np.array([index_1, index_4]))

                                name_bridge = '1_' + str(tmp[0]) + '-2_' + str(tmp[1])

                                if not (name_bridge in bridge_site_ensemble):

                                    coord_bridge_site = (coord_center_atom + coord_atom3) / 2 + height['bridge'] * norm_vector

                                    ads_sites['bridge']['location'].append(coord_bridge_site)

                                    ads_sites['bridge']['norm_vector'].append(norm_vector)

                                    ads_sites['bridge']['label'].append(str(tmp[0]) + '.' + str(tmp[1]))

                                    bridge_site_ensemble.append(name_bridge)

                            if (abs(d23 - bond_length) < 0.1):

                                tmp = np.sort(np.array([index_2, index_3]))

                                name_bridge = '1_' + str(tmp[0]) + '-2_' + str(tmp[1])

                                if not (name_bridge in bridge_site_ensemble):

                                    coord_bridge_site = (coord_atom1 + coord_atom2) / 2 + height['bridge'] * norm_vector

                                    ads_sites['bridge']['location'].append(coord_bridge_site)

                                    ads_sites['bridge']['norm_vector'].append(norm_vector)

                                    ads_sites['bridge']['label'].append(str(tmp[0]) + '.' + str(tmp[1]))

                                    bridge_site_ensemble.append(name_bridge)

                            if (abs(d24 - bond_length) < 0.1):

                                tmp = np.sort(np.array([index_2, index_4]))

                                name_bridge = '1_' + str(tmp[0]) + '-2_' + str(tmp[1])

                                if not (name_bridge in bridge_site_ensemble):

                                    coord_bridge_site = (coord_atom1 + coord_atom3) / 2 + height['bridge'] * norm_vector

                                    ads_sites['bridge']['location'].append(coord_bridge_site)

                                    ads_sites['bridge']['norm_vector'].append(norm_vector)

                                    ads_sites['bridge']['label'].append(str(tmp[0]) + '.' + str(tmp[1]))

                                    bridge_site_ensemble.append(name_bridge)

                            if (abs(d34 - bond_length) < 0.1):

                                tmp = np.sort(np.array([index_3, index_4]))

                                name_bridge = '1_' + str(tmp[0]) + '-2_' + str(tmp[1])

                                if not (name_bridge in bridge_site_ensemble):

                                    coord_bridge_site = (coord_atom2 + coord_atom3) / 2 + height['bridge'] * norm_vector

                                    ads_sites['bridge']['location'].append(coord_bridge_site)

                                    ads_sites['bridge']['norm_vector'].append(norm_vector)

                                    ads_sites['bridge']['label'].append(str(tmp[0]) + '.' + str(tmp[1]))

                                    bridge_site_ensemble.append(name_bridge)

        if average(tmp_vec) != 0:

            norm_vec_average = average(tmp_vec) # get the averaged norm vector by using average function

            norm_vec_average = norm_vec_average / np.linalg.norm(norm_vec_average) # always normalize the vectors

            if not (int(i) in ontop_site_ensemble):

                ontop_site_ensemble.append(int(i))

                tmp[0] = int(i)

                ads_sites['ontop']['location'].append(coord_center_atom + height['ontop'] * norm_vec_average)

                ads_sites['ontop']['norm_vector'].append(norm_vec_average)

                ads_sites['ontop']['label'].append(str(tmp[0]))

        else:

            pass

    return ads_sites

def align_adsorbate_one_atom(slab, first_layer, site, norm_vector, label, molecule, mol_index, hybridization):

    """
    This function can align the molecule on particular site through norm_vector.

    Parameter:

    slab:
        Atoms Object. The slab that we want to study. It has to be the pure-surface.

    first_layer:
        List of integers. the index of atoms in first layer of slab.

    site:
        Numpy Array (3x1). The location of adsorption site.

    norm_vector:
        Numpy Array (3x1). The norm_vector of the adsorption site ('ontop', 'bridge', 'hollow', 'four_fold')

    label:
        List of Strings. The index of atoms that construct the adsorption site

    molecule:
        Atoms Object. The adsorbate

    mol_index:
        Integer. The index of adsorbed atoms

    hybridization:
        String. 'sp', 'sp2', 'sp3'. Different hybridzation means different bond length.

    Return:

        The Atoms object of the molecule that aligned with the norm_vector
    """

    index_near_atoms = find_connection_atoms(molecule, mol_index) # find the closest atoms

    num_near_atoms = len(index_near_atoms)

    height = 100 # find the lowest point

    for site_string in label:

        site_ensemble = site_string.split('.')

        for atom_index in site_ensemble:

            atom = slab[int(float(atom_index))]

            if atom.position[2] < height:

                height = atom.position[2]

                lowest_index = int(float(atom_index))

    site_lowest_surface_atom = slab[lowest_index].position # get the lowest point

    # if there are no near atoms, then we should just more it to the adsorption site
    if num_near_atoms == 0:

        move_vector = site - molecule[0].position

        molecule[0].position += move_vector

        return molecule

    # if there is one near atoms, then we should align it with the norm_vector
    if num_near_atoms == 1:

        # calculate the vector between adsorbed atom and its closest atom

        vector = molecule[index_near_atoms[0]].position - molecule[mol_index].position

        length_vector = np.linalg.norm(vector) # length of the bond

        vector_align_norm = norm_vector * length_vector

        rotation_matrix = rotation_matrix_from_vectors(vector, vector_align_norm) # calculate the rotation matrix

        for atom in molecule:

                atom.position = np.matmul(rotation_matrix, atom.position)

        move_vector = site - molecule[mol_index].position # move all atoms to the adsorption site

        for atom in molecule:

            atom.position += move_vector

        # check whether molecule is OK for the hybridization
        molecule = check_hybridization(slab, first_layer, norm_vector, molecule, mol_index, hybridization)

        if check_above(site_lowest_surface_atom, molecule):

            return molecule

        else:

            for atom in molecule:

                if atom.index != mol_index:

                    atom.position = atom.position + 2 * np.dot(molecule[mol_index].position - atom.position, norm_vector) / (np.power(np.linalg.norm(norm_vector),2)) * norm_vector

            return molecule

    # if there are two near atoms, then we should align the middle point with the norm_vector
    if num_near_atoms == 2:

        # get two coordinates of two nearest atoms
        coord_atom_1 = molecule[index_near_atoms[0]].position

        coord_atom_2 = molecule[index_near_atoms[1]].position

        coord_mol_index = molecule[mol_index].position

        # calculate the middle point of two atoms, then calculate the vector from mol_index to the middle point
        coord_middle_point = (coord_atom_1 + coord_atom_2) / 2

        vector_molIndex_middle = coord_middle_point - coord_mol_index

        # calculate the length, and set the norm_vector to the same length
        length_vector_molIndex_middle = np.linalg.norm(vector_molIndex_middle)

        vector_align_norm = length_vector_molIndex_middle * norm_vector

        # calcualte the rotation matrix
        rotation_matrix = rotation_matrix_from_vectors(vector_molIndex_middle, vector_align_norm)

        # rotate all atoms
        for atom in molecule:

                atom.position = np.matmul(rotation_matrix, atom.position)

        # move all atoms

        move_vector = site - molecule[mol_index].position # move all atoms to the adsorption site

        for atom in molecule:

            atom.position += move_vector

        if check_above(site_lowest_surface_atom, molecule):

            return molecule

        else:

            for atom in molecule:

                if atom.index != mol_index:

                    atom.position = atom.position + 2 * np.dot(molecule[mol_index].position - atom.position, norm_vector) / (np.power(np.linalg.norm(norm_vector),2)) * norm_vector

            return molecule

    # if there are three near atoms, then we should align the center point with the norm_vector
    if num_near_atoms == 3:

        # get two coordinates of two nearest atoms
        coord_atom_1 = molecule[index_near_atoms[0]].position

        coord_atom_2 = molecule[index_near_atoms[1]].position

        coord_atom_3 = molecule[index_near_atoms[2]].position

        coord_mol_index = molecule[mol_index].position

        # calculate the center point of three atoms, then calculate the vector from mol_index to the middle point
        coord_center_point = (coord_atom_1 + coord_atom_2 + coord_atom_3) / 3

        vector_molIndex_center = coord_center_point - coord_mol_index

        # calculate the length, and set the norm_vector to the same length
        length_vector_molIndex_center = np.linalg.norm(vector_molIndex_center)

        vector_align_norm = length_vector_molIndex_center * norm_vector

        # calcualte the rotation matrix
        rotation_matrix = rotation_matrix_from_vectors(vector_molIndex_center, vector_align_norm)

        # rotate all atoms
        for atom in molecule:

                atom.position = np.matmul(rotation_matrix, atom.position)

        # move all atoms

        move_vector = site - molecule[mol_index].position # move all atoms to the adsorption site

        for atom in molecule:

            atom.position += move_vector

        if check_above(site_lowest_surface_atom, molecule):

            return molecule

        else:

            for atom in molecule:

                if atom.index != mol_index:

                    atom.position = atom.position + 2 * np.dot(molecule[mol_index].position - atom.position, norm_vector) / (np.power(np.linalg.norm(norm_vector),2)) * norm_vector

            return molecule

    # if there are four near atoms, then we should align the center point with the norm_vector
    if num_near_atoms == 4:

        # get two coordinates of two nearest atoms
        coord_atom_1 = molecule[index_near_atoms[0]].position

        coord_atom_2 = molecule[index_near_atoms[1]].position

        coord_atom_3 = molecule[index_near_atoms[2]].position

        coord_atom_4 = molecule[index_near_atoms[3]].position

        coord_mol_index = molecule[mol_index].position

        # calculate the center point of three atoms, then calculate the vector from mol_index to the middle point
        coord_center_point = (coord_atom_1 + coord_atom_2 + coord_atom_3 + coord_atom_4) / 4

        vector_molIndex_center = coord_center_point - coord_mol_index

        # calculate the length, and set the norm_vector to the same length
        length_vector_molIndex_center = np.linalg.norm(vector_molIndex_center)

        vector_align_norm = length_vector_molIndex_center * norm_vector

        # calcualte the rotation matrix
        rotation_matrix = rotation_matrix_from_vectors(vector_molIndex_center, vector_align_norm)

        # rotate all atoms
        for atom in molecule:

                atom.position = np.matmul(rotation_matrix, atom.position)

        # move all atoms

        move_vector = site - molecule[mol_index].position # move all atoms to the adsorption site

        for atom in molecule:

            atom.position += move_vector

        if check_above(site_lowest_surface_atom, molecule):

            return molecule

        else:

            for atom in molecule:

                if atom.index != mol_index:

                    atom.position = atom.position + 2 * np.dot(molecule[mol_index].position - atom.position, norm_vector) / (np.power(np.linalg.norm(norm_vector),2)) * norm_vector

            return molecule

def align_adsorbate_multiple_atoms(slab, first_layer, molecule, match_dict):

    """
    This function can align adsorbate with multiple adsorption site on the surface with correct geometry.

    Parameter:

    slab:
        Atoms Object. The slab that we want to study. It has to be the pure-surface

    first_layer:
        List. Indexes of atoms on the first layer.

    molecule:
        Atoms Object. The adsorbate

    match_dict:
        Dictionary which contains the matching information between the molecule and the surface

        Data Structure of match_dict: match_dict = {'0': {'location': a, 'norm_vector': b}}

    Return:

        The Atoms object of the molecule that aligned with the norm_vector
    """

    # step1: check the match
    if check_match(molecule, match_dict): # if there is a change that the molecule can adsorb on the multi-site

        num_adsorption_site = len(match_dict.keys()) # get how many adsorption sites on the molecule, we need to distinguish between 2 and more

        if num_adsorption_site == 2:

            # get the coordinate of adsorption atom in molecule and adsorption site
            mol_index_set = find_keys(match_dict)

            coord_mol_index_1 = molecule[int(float(mol_index_set[0]))].position

            coord_mol_index_2 = molecule[int(float(mol_index_set[1]))].position

            coord_ads_site_1 = match_dict[mol_index_set[0]]['location'] # location of the adsorption site according to first atom in molecule

            coord_ads_site_2 = match_dict[mol_index_set[1]]['location']

            coord_middle_mol_index = (coord_mol_index_1 + coord_mol_index_2) / 2 # calculate the middle point of two atoms in molecule

            coord_middle_ads_site = (coord_ads_site_1 + coord_ads_site_2) / 2 # calculate the middle point of two adsorption sites

            move_vector = coord_middle_ads_site - coord_middle_mol_index # the vector that can help us move the molecule to its location

            # move all atoms to its initial location (for the rotation in next step)
            for atom in molecule:

                atom.position += move_vector

            # rotate mol1-mol2 parallel with ads_site_1-ads_site_2
            vector_mol_1_2 = molecule[int(float(mol_index_set[0]))].position - molecule[int(float(mol_index_set[1]))].position

            unit_vector_mol_1_2 = vector_mol_1_2 / np.linalg.norm(vector_mol_1_2)

            vector_ads_site_1_2 = coord_ads_site_2 - coord_ads_site_1

            unit_vector_ads_site_1_2 = vector_ads_site_1_2 / np.linalg.norm(vector_ads_site_1_2)

            matrix_rotation = rotation_matrix_from_vectors(unit_vector_mol_1_2, unit_vector_ads_site_1_2)

            # let the rotational point (middle point) as 0
            for atom in molecule:

                atom.position -= coord_middle_ads_site

                atom.position = np.matmul(matrix_rotation, atom.position)

                atom.position += coord_middle_ads_site

            # now the molecule is rightly aligned
            coord_mol_index_1 = molecule[int(float(mol_index_set[0]))].position # because the molcule is rotated, so the coordinates need to be changed

            coord_mol_index_2 = molecule[int(float(mol_index_set[1]))].position

            coord_middle = (coord_mol_index_1 + coord_mol_index_2) / 2

            # rotation the molecule in order to make it furthest away from the surface
            d_max = -1 # start with negative number

            return_molecule = copy.deepcopy(molecule)

            molecule_original = copy.deepcopy(molecule)

            for theta in range(0, 360, 1): # every 1 degree

                molecule = copy.deepcopy(molecule_original) # everytime the molecule has to be returned to the original point

                for atom in molecule:

                    atom.position = rotation_along_two_points(atom.position, coord_mol_index_1, coord_mol_index_2, theta)

                d = dist_molecule_surface(slab, first_layer, molecule)

                if d > d_max:

                    d_max = d

                    return_molecule = copy.deepcopy(molecule)

            return return_molecule

        elif num_adsorption_site > 2:

            # first find the center of the molecule and adsorption sites

            center_molecule_location, center_molecule_norm_vector, center_ads_location, center_ads_norm_vector = find_center_molecule_adsSites(molecule, match_dict)

            move_vector = center_ads_location - center_molecule_location

            # move the center of the atom to the center of the adsorption site
            for atom in molecule:

                atom.position += move_vector

            # after movement, calculate again

            center_molecule_location, center_molecule_norm_vector, center_ads_location, center_ads_norm_vector = find_center_molecule_adsSites(molecule, match_dict)

            rotation_matrix = rotation_matrix_from_vectors(center_molecule_norm_vector, center_ads_norm_vector)


            # refer all the atom's position to the center of adsorption site, prepare for the rotation
            for atom in molecule:

                atom.position -= center_ads_location

                atom.position = np.matmul(rotation_matrix, atom.position)

                atom.position += center_ads_location

            d_min = 1000 # maximum length

            return_molecule = copy.deepcopy(molecule)

            molecule_original = copy.deepcopy(molecule)

            for theta in range(0, 360, 1): # rotate 1 degree at one time

                molecule = copy.deepcopy(molecule_original)

                for atom in molecule:

                    atom.position = rotation_along_two_points(atom.position, center_ads_norm_vector, 2*center_ads_norm_vector, theta)

                d = check_distance(molecule, match_dict) # add all the distance together

                if d < d_min:

                    d_min = d

                    return_molecule = copy.deepcopy(molecule)

            return return_molecule

    else:

        print('sorry, the choice of adsorption site is really bad!')
