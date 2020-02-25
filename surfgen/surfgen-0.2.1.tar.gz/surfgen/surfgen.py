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
from matplotlib import pyplot as plt

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

def check_hollow(v1, v2, v3):

    """
    This function can determine whether three points can form a 3-fold hollow site or not

    Parameters:

    v1:
        (3x1) np.array. Coordinates of the first point

    v2:
        (3x1) np.array. Coordinates of the second point

    v3:
        (3x1) np.array. Coordinates of the third point

    Return:
        Boolean. True or False
    """

    d_12 = np.linalg.norm(v1-v2)

    d_23 = np.linalg.norm(v2-v3)

    d_13 = np.linalg.norm(v1-v3)

    if (abs(d_12 - d_23)) < 0.1 and (abs(d_12 - d_13) < 0.1) and (abs(d_13 - d_23) < 0.1):

        return True

    else:

        return False

def check_4fold(v1, v2, v3, v4):

    """
    This function is used to check whether the four atoms can form a square size or not

    Parameters:

    v1:
        (3x1) np.array. Coordinates of the first point

    v2:
        (3x1) np.array. Coordinates of the second point

    v3:
        (3x1) np.array. Coordinates of the third point

    v4:
        (3x1) np.array. Coordinates of the fourth point

    Return:
        Boolean. True or False
    """

    d12 = np.linalg.norm(v1 - v2) # from p1 to p2

    d13 = np.linalg.norm(v1 - v3) # from p1 to p3

    d14 = np.linalg.norm(v1 - v4) # from p1 to p4

    d23 = np.linalg.norm(v2 - v3) # from p2 to p3

    d24 = np.linalg.norm(v2 - v4) # from p2 to p4

    d34 = np.linalg.norm(v3 - v4) # from p3 to p4

    # if we choose any point then we set it to 1, then there are only three options in the other of diagnoal: 2, 3, 4.
    # Let's see it is 4, then the other diagonal is 2-3. So now we have "1-2", "2-4", "3-4", "1-3" as four sides, and we can check whether they have the same length.
    # The condition is really important !!!

    if (abs(d12 - d13) < 0.1) and (abs(d13 - d34) < 0.1) and (abs(d34 - d24) < 0.1) and (abs(np.sqrt(2)*d12 - d14) < 0.1) and (abs(np.sqrt(2)*d24 - d23) < 0.1):

        return True

    if (abs(d13 - d14) < 0.1) and (abs(d14 - d24) < 0.1) and (abs(d23 - d24) < 0.1) and (abs(np.sqrt(2)*d13 - d12) < 0.1) and (abs(np.sqrt(2)*d23 - d34) < 0.1):

        return True

    if (abs(d12 - d14) < 0.1) and (abs(d12 - d23) < 0.1) and (abs(d23 - d34) < 0.1) and (abs(np.sqrt(2)*d14 - d13) < 0.1) and (abs(np.sqrt(2)*d24 - d23) < 0.1):

        return True

    return False

def average(v):

    """
    This function can calculate the average of a list of vectors.

    Parameter:

    v:
        A list of (3x1) np.array. It contains several vectors

    Return:
        (3x1) tuple. The averaged vector.
    """

    n = len(v)

    if n == 0:

        return 0

    else:

        tot = [0, 0, 0]

        for i in v:

            if i[2] < 0:

                i = i * (-1)

            tot = tot + i

        return [tot[0]/n, tot[1]/n, tot[2]/n]

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

def find_connection_atoms(molecule, mol_index, distance_range = [0.5, 1.8]):

    """
    This function can find all the closest atoms respect to the adsorbed atom. We only need to use this function when **we only have one adsorbed atom**. If there are more than one adsorbed atoms, then we only need to find the furthest atom.

    Parameters:

    molecule:
        ASE Atoms Object. The molecule that we want to adsorb on the surface

    mol_index:
        Integer. The index of the adsorbed atom of molecules

    distange_range:
        List of Reals. Define the shortest and longest bond length in the molecule. Default is 0.5->1.8. [a,b]: a < b needed.

    Return:

    The function will retun a list of indexes in the molecule.
    """

    coord_mol_index = molecule[mol_index].position

    list_return = []

    for atom in molecule:

        if atom.index != mol_index:

            coord_atom = atom.position

            d = np.linalg.norm(coord_atom - coord_mol_index)

            if (d > distance_range[0]) and (d < distance_range[1]): # 0.5A - 2.0A is our first guess, could be larger, need to be validated.

                list_return.append(atom.index)

    return list_return

def check_above(site, molecule):

    """
    This function can check whether all atoms in molecule are above the adsorption site

    Parameters:

    site:
        Numpy Array. The adsorption site that we want

    molecule:
        Atoms Object. The adsorbates.
    """

    for atom in molecule:

        if atom.position[2] < site[2]:

            return False

    return True

def dist_molecule_surface(slab, first_layer, molecule):

    """
    This function can calculate the distance between the molecule and the slab

    Parameters:

    slab:
        Atoms Object. The surface slab that we are interested in

    first_layer:
        List of integers. The indexes of the first layer of slab

    molecule:
        Atoms Object. The adsorbates that we want

    Return:
        shortest distance between the slab and the molecule
    """

    distance = 100 # really large number

    for atom in molecule:

        for index in first_layer:

            coord_atom_molecule = atom.position

            coord_surface_atom = slab[index].position

            d = np.linalg.norm(coord_atom_molecule - coord_surface_atom)

            if (d < distance):
                distance = d

    return distance

def rotation_matrix_from_vectors(vec1, vec2):

    """

    Find the rotation matrix that aligns vec1 to vec2

    This function is taken from Peter's answer on stackoverflow:
    `Question Link <https://stackoverflow.com/questions/45142959/calculate-rotation-matrix-to-align-two-vectors-in-3d-space>`_

    Parameters:

    vec1:
        Numpy array. A 3d "source" vector

    vec2:
        Numpy array. A 3d "destination" vector

    Return:
        A transform matrix (3x3) which when applied to vec1, aligns it with vec2.

    """

    a, b = (vec1 / np.linalg.norm(vec1)).reshape(3), (vec2 / np.linalg.norm(vec2)).reshape(3)

    v = np.cross(a, b)

    c = np.dot(a, b)

    s = np.linalg.norm(v)

    kmat = np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])

    rotation_matrix = np.eye(3) + kmat + kmat.dot(kmat) * ((1 - c) / (s ** 2))

    return rotation_matrix

def check_hybridization(slab, first_layer, norm_vector, molecule, mol_index, hybridization):

    """
    This function can check whether the hybridization is confirmed or not

    Parameters:

    slab:
        Atoms Object. The slab that we want to study. It has to be the pure-surface.

    first_layer:
        List of Integers. The indexes of first layer of slab.

    molecule:
        Atoms Object. The molecule that we are interested in

    mol_index:
        Integer. Index of adsorbed atom

    hybridization:
        String. 'sp', 'sp2', 'sp3'

    Return:

    Atoms Object. With correct direction of hybridization
    """

    num_near_atoms = find_connection_atoms(molecule, mol_index)

    # We only need to adjust the hybridzation of molecule like "OH, OCH3", etc.
    if len(num_near_atoms) == 1:

        coord_mol_index = molecule[mol_index].position

        coord_near_atom = molecule[num_near_atoms[0]].position

        vector_molIndex_nearAtom = coord_near_atom - coord_mol_index

        cos_two_vector = np.dot(vector_molIndex_nearAtom, -norm_vector)/(np.linalg.norm(vector_molIndex_nearAtom) * np.linalg.norm(norm_vector)) # -> cosine of the angle

        # sometimes cos_two_vector can be larger than 1 (very exceptional case), we need to do something
        if cos_two_vector > 1:

            cos_two_vector = 2 - cos_two_vector

        elif cos_two_vector < -1:

            cos_two_vector = -2 - cos_two_vector

        angle = np.arccos(cos_two_vector) # if you really want the angle

        angle_degree = np.degrees(angle)

        # prevent too large angles
        if angle_degree > 180:

            angle_degree -= 180

        # check 'sp', 'sp2', 'sp3'

        if hybridization == 'sp': # the angle between slab_atom - mol_index - near_atom should be 180 degrees

            if abs(angle_degree - 180) < 5:

                return molecule

            else:

                norm_vector_length = np.linalg.norm(vector_molIndex_nearAtom) * norm_vector

                rotation_matrix = rotation_matrix_from_vectors(vector_molIndex_nearAtom, norm_vector_length)

                for atom in molecule:

                    if not(atom.index == mol_index):

                        atom.position = np.matmul(rotation_matrix, atom.position)

                return molecule

        if hybridization == 'sp2': # the angle between slab_atom - mol_index - near_atom should be 120 degrees

            if abs(angle_degree - 120) < 5:

                return molecule

            else:

                # Create localized coordinate system for the norm_vector

                x_origin = np.array([1, 0, 0])

                y_origin = np.array([0, 1, 0])

                z_origin = np.array([0, 0, 1])

                rotation_matrix_z_norm = rotation_matrix_from_vectors(z_origin, norm_vector)

                x_rotate = np.matmul(rotation_matrix_z_norm, x_origin)

                y_rotate = np.matmul(rotation_matrix_z_norm, y_origin)

                # start rotation

                molecule_original = copy.deepcopy(molecule) # original molecule

                for atom in molecule_original:

                    atom.position -= molecule[mol_index].position # let mol_index be (0, 0, 0)

                bond_y = np.linalg.norm(vector_molIndex_nearAtom) * np.cos(np.radians(60))

                bond_x = np.linalg.norm(vector_molIndex_nearAtom) * np.sin(np.radians(60))

                for theta in range(0, 360, 5):

                    # turn angle to radius
                    rad = np.radians(theta)

                    # copy molecule to its original point
                    molecule_check = copy.deepcopy(molecule_original)

                    coord_near_atom_sp2 =  bond_y * norm_vector + bond_x * np.cos(rad) * x_rotate + bond_x * np.sin(rad) * y_rotate

                    new_vector_molIndex_nearAtom = coord_near_atom_sp2

                    # rotate the original vector to the new vector
                    rotation_matrix_origin_new = rotation_matrix_from_vectors(vector_molIndex_nearAtom, new_vector_molIndex_nearAtom)

                    # rotate every atom in the molecule
                    for atom in molecule_check:

                        if atom.index != mol_index:

                            atom.position = np.matmul(rotation_matrix_origin_new, atom.position)

                    for atom in molecule_check:

                        atom.position += molecule[mol_index].position

                    d = dist_molecule_surface(slab, first_layer, molecule_check)

                    if d > 0.9:

                        return molecule_check

        if hybridization == 'sp3': # the angle between slab_atom - mol_index - near_atom should be 110 degrees

            if abs(angle_degree - 110) < 5:

                return molecule

            else:

                # Create localized coordinate system for the norm_vector

                x_origin = np.array([1, 0, 0])

                y_origin = np.array([0, 1, 0])

                z_origin = np.array([0, 0, 1])

                rotation_matrix_z_norm = rotation_matrix_from_vectors(z_origin, norm_vector)

                x_rotate = np.matmul(rotation_matrix_z_norm, x_origin)

                y_rotate = np.matmul(rotation_matrix_z_norm, y_origin)

                # start rotation

                molecule_original = copy.deepcopy(molecule) # original molecule

                for atom in molecule_original:

                    atom.position -= molecule[mol_index].position # let mol_index be (0, 0, 0)

                bond_y = np.linalg.norm(vector_molIndex_nearAtom) * np.cos(np.radians(60))

                bond_x = np.linalg.norm(vector_molIndex_nearAtom) * np.sin(np.radians(60))

                for theta in range(0, 360, 5):

                    # turn angle to radius
                    rad = np.radians(theta)

                    # copy molecule to its original point
                    molecule_check = copy.deepcopy(molecule_original)

                    coord_near_atom_sp2 =  bond_y * norm_vector + bond_x * np.cos(rad) * x_rotate + bond_x * np.sin(rad) * y_rotate

                    new_vector_molIndex_nearAtom = coord_near_atom_sp2

                    # rotate the original vector to the new vector
                    rotation_matrix_origin_new = rotation_matrix_from_vectors(vector_molIndex_nearAtom, new_vector_molIndex_nearAtom)

                    # rotate every atom in the molecule
                    for atom in molecule_check:

                        if atom.index != mol_index:

                            atom.position = np.matmul(rotation_matrix_origin_new, atom.position)

                    for atom in molecule_check:

                        atom.position += molecule[mol_index].position

                    d = dist_molecule_surface(slab, first_layer, molecule_check)

                    if d > 0.9:

                        return molecule_check

    else:
        return molecule

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

            atom = slab[int(atom_index)]

            if atom.position[2] < height:

                height = atom.position[2]

                lowest_index = int(atom_index)

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

def check_match(molecule, match_dict, threshold = 2):

    """
    This function can check whether the molecule and the adsorption site are matched

    Parameters:

    molecule:
        The molecule that

    match_dict:
        Dictionary that contains the match information of molecule and the adsorption sites.

    threshold:
        Real number. It shows how large the mismatch can be. The default number is 0.8

    Return:
        Boolean
    """

    for index1 in match_dict:

        for index2 in match_dict:

            if index1 != index2:

                coord_ads_site_1 = match_dict[index1]['location']

                coord_ads_site_2 = match_dict[index2]['location']

                coord_mol_index_1 = molecule[int(float(index1))].position

                coord_mol_index_2 = molecule[int(float(index2))].position

                d_ads_site = np.linalg.norm(coord_ads_site_1 - coord_ads_site_2)

                d_mol_index = np.linalg.norm(coord_mol_index_1 - coord_mol_index_2)

                if abs(d_ads_site - d_mol_index) > threshold:

                    return False

    return True

def find_keys(dict):

    """
    This function can find the keys for the dictionary

    Parameters:
        dict: The dictionary that we want the keys

    Return:
        List: list of keys in the dict
    """

    set = []

    for key in dict:

        set.append(key)

    return set

def matrix_multiple(matrix_list):

    """
    This function can help to return the multiplication of a series of matrixes.

    Parameters:

    matrix_list:
        The list of matrix that we want to multiply

    Return:
        Numpy array. The result that we want
    """

    # set the identity matrix as the same dimension as the input matrix
    return_matrix = np.identity(np.shape(matrix_list[0])[0])

    # start multiplication
    for matrix in matrix_list:

        return_matrix = np.matmul(return_matrix, matrix)

    return return_matrix

def rotation_along_two_points(p, p1, p2, theta):

    """
    This function can rotate a point (p) at an angle (theta) along a line generated by two point (p1, p2)

    Parameters:

    p:
        Numpy Array (3x1). The point that we want to rotate

    p1:
        Numpy Array (3x1). First point of the line

    p2:
        Numpy Array (3x1). Second point of the line

    theta:
        Real. Angle that we want to rotate (0 - 360 degree)

    Return:
        Numpy Array (3x1). The point from rotation.

    Reference:

        The algorithm of this function is copied from two sources:

        1. `https://robotics.stackexchange.com/questions/12782/how-rotate-a-point-around-an-arbitrary-line-in-3d`_

        2. `http://paulbourke.net/geometry/rotate/`_

        Many thanks to the authors
    """

    # change the angle to radian
    rad = np.radians(theta)

    # calculate the unit vector of p1 -> p2
    vector_p1_p2 = p2 - p1

    norm_vector_p1_p2 = vector_p1_p2 / np.linalg.norm(vector_p1_p2)

    # the parameter are copied from the answer
    a = norm_vector_p1_p2[0]

    b = norm_vector_p1_p2[1]

    c = norm_vector_p1_p2[2]

    d = np.sqrt(np.power(b, 2) + np.power(c, 2))

    x1 = p1[0]

    y1 = p1[1]

    z1 = p1[2]

    # construct all the matrix

    if d != 0:

        matrix_T = np.array([
                            [1, 0, 0, -x1],
                            [0, 1, 0, -y1],
                            [0, 0, 1, -z1],
                            [0, 0, 0, 1]
                            ])

        matrix_Rx = np.array([
                             [1, 0, 0, 0],
                             [0, c/d, -b/d, 0],
                             [0, b/d, c/d, 0],
                             [0, 0, 0, 1]
                             ])

        matrix_Ry = np.array([
                             [d, 0, -a, 0],
                             [0, 1, 0, 0],
                             [a, 0, d, 0],
                             [0, 0, 0, 1]
                             ])

        matrix_Rz = np.array([
                             [np.cos(rad), -np.sin(rad), 0, 0],
                             [np.sin(rad), np.cos(rad), 0, 0],
                             [0, 0, 1, 0],
                             [0, 0, 0, 1]
                             ])

        # create 4x1 vector for p
        p_4_1 = np.array([p[0], p[1], p[2], 1])

        # do the matrix inverse
        matrix_inv_T = np.linalg.inv(matrix_T)

        matrix_inv_Rx = np.linalg.inv(matrix_Rx)

        matrix_inv_Ry = np.linalg.inv(matrix_Ry)

        matrix_inv_Rz = np.linalg.inv(matrix_Rz)

        # multiple all matrixes
        matrix_mul = matrix_multiple([matrix_inv_T, matrix_inv_Rx, matrix_inv_Ry, matrix_Rz, matrix_Ry, matrix_Rx, matrix_T])

        # calculate the final point
        p_final = np.matmul(matrix_mul, p_4_1)

        # calcualte the return
        p_return = np.array([p_final[0], p_final[1], p_final[2]])

        return p_return

    else:

        matrix_T = np.array([
                    [1, 0, 0, -x1],
                    [0, 1, 0, -y1],
                    [0, 0, 1, -z1],
                    [0, 0, 0, 1]
                    ])

        matrix_Ry = np.array([
                     [d, 0, -a, 0],
                     [0, 1, 0, 0],
                     [a, 0, d, 0],
                     [0, 0, 0, 1]
                     ])

        matrix_Rz = np.array([
                             [np.cos(rad), -np.sin(rad), 0, 0],
                             [np.sin(rad), np.cos(rad), 0, 0],
                             [0, 0, 1, 0],
                             [0, 0, 0, 1]
                             ])

        # create 4x1 vector for p
        p_4_1 = np.array([p[0], p[1], p[2], 1])

        # do the matrix inverse
        matrix_inv_T = np.linalg.inv(matrix_T)

        matrix_inv_Ry = np.linalg.inv(matrix_Ry)

        matrix_inv_Rz = np.linalg.inv(matrix_Rz)

        # multiple all matrixes
        matrix_mul = matrix_multiple([matrix_inv_T, matrix_inv_Ry, matrix_Rz, matrix_Ry, matrix_T])

        # calculate the final point
        p_final = np.matmul(matrix_mul, p_4_1)

        # calcualte the return
        p_return = np.array([p_final[0], p_final[1], p_final[2]])

        return p_return

def find_center_molecule_adsSites(molecule, match_dict):

    """
    This function can help us find the center of molecule and the center of the adsorption sites

    Parameters:

    molecule:
        Atoms Object. The molecules we are interested in.

    match_dict:
        The matching dictionary of the molecule and the adsorption site

    Return:
        Four Numpy Arraies (3x1). Contains:

        * mol_center_location: the center of adsorbed atom in molecule

        * mol_center_norm_vector_normalized: the averaged normalized norm vector of all adsorbed atom in molecule

        * adsSite_center_location: the center of adsorption sites

        * adsSites_center_norm_vector_normalized: the averaged normalized norm vector of all adsorption sites
    """

    mol_coordinates_set = [] # set of all adsorbed atom location

    mol_norm_vector = [] # set of all norm vectors of atoms in molecule

    adsSites_coordinates_set = [] # set of the location of all adsorption sites

    adsSites_norm_vector = [] # set of the norm vectors of all adsorption sites

    for index in match_dict:

        mol_coordinates_set.append(molecule[int(float(index))].position)

        adsSites_coordinates_set.append(match_dict[index]['location'])

        adsSites_norm_vector.append(match_dict[index]['norm_vector'])

    adsSite_center_location = average(adsSites_coordinates_set) # center of the location of adsorption sites

    adsSites_center_norm_vector = average(adsSites_norm_vector) # norm vector of the adsorption sites

    adsSites_center_norm_vector_normalized = adsSites_center_norm_vector / np.linalg.norm(adsSites_center_norm_vector)

    mol_center_location = average(mol_coordinates_set) # center of the location of molecule

    for index1, site1 in enumerate(mol_coordinates_set):

        mol_norm_vector_tmp = [] # used to calculate the norm_vector of index1

        check_duplicity = [] # check the duplicity

        for index2, site2 in enumerate(mol_coordinates_set):

            if index1 != index2: # if they are not the same atoms

                for index3, site3 in enumerate(mol_coordinates_set):

                    if (index3 != index1) and (index3 != index2): # if index3 is not identical to both index1 and index2

                        # check whether the norm_vector is stored or not
                        tmp = np.sort(np.array([index1, index2, index3]))

                        name_string = '1_' + str(tmp[0]) + '-2_' + str(tmp[1]) + '-3_' + str(tmp[2])

                        if not(name_string in check_duplicity): # if the norm vector is not calculated

                            v1 = site2 - site1

                            v2 = site3 - site1

                            norm_vector = np.cross(v1, v2)

                            norm_vector_normalized = norm_vector / np.linalg.norm(norm_vector) # nomalized the norm_vector

                            check_duplicity.append(name_string)

                            mol_norm_vector_tmp.append(norm_vector_normalized)

        avg_norm_vector = average(mol_norm_vector_tmp)

        avg_norm_vector_normalized = avg_norm_vector / np.linalg.norm(avg_norm_vector) # normalized

        mol_norm_vector.append(avg_norm_vector_normalized)

    mol_center_norm_vector = average(mol_norm_vector)

    mol_center_norm_vector_normalized = mol_center_norm_vector / np.linalg.norm(mol_center_norm_vector)

    return np.array(mol_center_location), np.array(mol_center_norm_vector_normalized), np.array(adsSite_center_location), np.array(adsSites_center_norm_vector_normalized)

def check_distance(molecule, match_dict):

    """
    This function can calculate the distance between the molecule and the adsorption sites.

    Parameters:

    molecule:
        The molecule that we are interested in

    match_dict:
        The dictionary of the adsorbed information.

    Return:
        One real number. Shows the distance between molecule and adsorption sites.
    """

    location_mol_indexes = []

    location_ads_sites = []

    # extract all the information
    for index in match_dict:

        coord_mol_index = molecule[int(float(index))].position

        location_mol_indexes.append(coord_mol_index)

        location_ads_sites.append(match_dict[index]['location'])

    # start calculation
    d = 0

    for item, loc in enumerate(location_mol_indexes):

        loc_ads_site = location_ads_sites[item]

        d += np.linalg.norm(loc - loc_ads_site)

    return d

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

        Data Structure of match_dict:

            {
                '0': {
                    'location': location,
                    'norm_vector': norm_vector
                },
                '1': {
                    'location': location,
                    'norm_vector': norm_vector
                }
            }

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
