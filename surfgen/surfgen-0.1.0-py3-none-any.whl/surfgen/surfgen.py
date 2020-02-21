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

def slab_generator(bulk, miller_index, layers, vacuum, supercell):

    """
    This function can generate slab from the ASE bulk object

    Parameter:

    bulk:
        ASE Object. It is the bulk that we want to cut surface from

    miller_index:
        (3x1) tuple. It defines the miller index of the surface

    layers:
        Integer. It defines how many layers we want for the surface slab

    vacuum:
        Real. It defines the length of the vacuum layer

    supercell:
        (3x1) tuple or (3x3) np.array. It defines the supercell of our surface slab
        * (3x3) np.array is quite useful in generating surface like sqrt(3)*sqrt(3)

    Return:

        Atoms object, which is the slab that we want
    """

    # since in pymatgen, the layers we need is usually two time as ASE, so
    pmg_layers = layers * 2

    # convert ASE object (bulk) to pymatgen object
    bulk_pmg = AseAtomsAdaptor.get_structure(bulk)
    bulk_pmg = SpacegroupAnalyzer(bulk_pmg).get_conventional_standard_structure()

    # create miller_index surfaces (return a list of surfaces)
    slab_gen = SlabGenerator(bulk_pmg,
                             miller_index,
                             min_slab_size = pmg_layers,
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
        # print('1-3-2-4')
        # print(d12, d13, d14, d23, d24, d34)

        #2.5307351698666527 2.5307351698666536 3.5790000000000006 3.579 2.5307351698666536 5.658895872871316

        return True

    if (abs(d13 - d14) < 0.1) and (abs(d14 - d24) < 0.1) and (abs(d23 - d24) < 0.1) and (abs(np.sqrt(2)*d13 - d12) < 0.1) and (abs(np.sqrt(2)*d23 - d34) < 0.1):
        # print('1-4-3-2')
        # print(d12, d13, d14, d23, d24, d34)
        return True

    if (abs(d12 - d14) < 0.1) and (abs(d12 - d23) < 0.1) and (abs(d23 - d34) < 0.1) and (abs(np.sqrt(2)*d14 - d13) < 0.1) and (abs(np.sqrt(2)*d24 - d23) < 0.1):
        # print('1-2-4-3')
        # print(d12, d13, d14, d23, d24, d34)
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
        ads_sites[site] = [] # an empty list

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
                        ads_sites['hollow'].append(coord_hollow_site)
                        hcp_site_ensemble.append(name_hollow)

                    # check whether it can form a bridge site between central atom and item 1
                    tmp = np.sort(np.array([index_1, index_2]))
                    name_bridge = '1_' + str(tmp[0]) + '-2_' + str(tmp[1])

                    if not (name_bridge in bridge_site_ensemble):
                        coord_bridge_site = (coord_center_atom + coord_atom1) / 2 + height['bridge'] * norm_vector
                        ads_sites['bridge'].append(coord_bridge_site)
                        bridge_site_ensemble.append(name_bridge)

                    # check whether it can form a bridge site between central atom and item 2
                    tmp = np.sort(np.array([index_1, index_3]))
                    name_bridge = '1_' + str(tmp[0]) + '-2_' + str(tmp[1])

                    if not (name_bridge in bridge_site_ensemble):
                        coord_bridge_site = (coord_center_atom + coord_atom2) / 2 + height['bridge'] * norm_vector
                        ads_sites['bridge'].append(coord_bridge_site)
                        bridge_site_ensemble.append(name_bridge)

                    # check whether it can form a bridge site between item 1 and item 2
                    tmp = np.sort(np.array([index_2, index_3]))
                    name_bridge = '1_' + str(tmp[0]) + '-2_' + str(tmp[1])

                    if not (name_bridge in bridge_site_ensemble):
                        coord_bridge_site = (coord_center_atom + coord_atom2) / 2 + height['bridge'] * norm_vector
                        ads_sites['bridge'].append(coord_bridge_site)
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
                                ads_sites['four_fold'].append(coord_four_fold_site)
                                four_fold_site_ensemble.append(name_four_fold)

                            # construct bridge sites

                            d12 = np.linalg.norm(coord_center_atom - coord_atom1)
                            d13 = np.linalg.norm(coord_center_atom - coord_atom2)
                            d14 = np.linalg.norm(coord_center_atom - coord_atom3)
                            d23 = np.linalg.norm(coord_atom1 - coord_atom2)
                            d24 = np.linalg.norm(coord_atom1 - coord_atom3)
                            d34 = np.linalg.norm(coord_atom2 - coord_atom3)

                            print(d12, d13, d14, d23, d24, d34)

                            if (abs(d12 - bond_length) < 0.1):
                                tmp = np.sort(np.array([index_1, index_2]))
                                name_bridge = '1_' + str(tmp[0]) + '-2_' + str(tmp[1])

                                if not (name_bridge in bridge_site_ensemble):
                                    coord_bridge_site = (coord_center_atom + coord_atom1) / 2 + height['bridge'] * norm_vector
                                    ads_sites['bridge'].append(coord_bridge_site)
                                    bridge_site_ensemble.append(name_bridge)

                            if (abs(d13 - bond_length) < 0.1):
                                tmp = np.sort(np.array([index_1, index_3]))
                                name_bridge = '1_' + str(tmp[0]) + '-2_' + str(tmp[1])

                                if not (name_bridge in bridge_site_ensemble):
                                    coord_bridge_site = (coord_center_atom + coord_atom2) / 2 + height['bridge'] * norm_vector
                                    ads_sites['bridge'].append(coord_bridge_site)
                                    bridge_site_ensemble.append(name_bridge)

                            if (abs(d14 - bond_length) < 0.1):
                                tmp = np.sort(np.array([index_1, index_4]))
                                name_bridge = '1_' + str(tmp[0]) + '-2_' + str(tmp[1])

                                if not (name_bridge in bridge_site_ensemble):
                                    coord_bridge_site = (coord_center_atom + coord_atom3) / 2 + height['bridge'] * norm_vector
                                    ads_sites['bridge'].append(coord_bridge_site)
                                    bridge_site_ensemble.append(name_bridge)

                            if (abs(d23 - bond_length) < 0.1):
                                tmp = np.sort(np.array([index_2, index_3]))
                                name_bridge = '1_' + str(tmp[0]) + '-2_' + str(tmp[1])

                                if not (name_bridge in bridge_site_ensemble):
                                    coord_bridge_site = (coord_atom1 + coord_atom2) / 2 + height['bridge'] * norm_vector
                                    ads_sites['bridge'].append(coord_bridge_site)
                                    bridge_site_ensemble.append(name_bridge)

                            if (abs(d24 - bond_length) < 0.1):
                                tmp = np.sort(np.array([index_2, index_4]))
                                name_bridge = '1_' + str(tmp[0]) + '-2_' + str(tmp[1])

                                if not (name_bridge in bridge_site_ensemble):
                                    coord_bridge_site = (coord_atom1 + coord_atom3) / 2 + height['bridge'] * norm_vector
                                    ads_sites['bridge'].append(coord_bridge_site)
                                    bridge_site_ensemble.append(name_bridge)

                            if (abs(d34 - bond_length) < 0.1):
                                tmp = np.sort(np.array([index_3, index_4]))
                                name_bridge = '1_' + str(tmp[0]) + '-2_' + str(tmp[1])

                                if not (name_bridge in bridge_site_ensemble):
                                    coord_bridge_site = (coord_atom2 + coord_atom3) / 2 + height['bridge'] * norm_vector
                                    ads_sites['bridge'].append(coord_bridge_site)
                                    bridge_site_ensemble.append(name_bridge)

        if average(tmp_vec) != 0:
            norm_vec_average = average(tmp_vec) # get the averaged norm vector by using average function
            norm_vec_average = norm_vec_average / np.linalg.norm(norm_vec_average) # always normalize the vectors

            if not (int(i) in ontop_site_ensemble):
                ontop_site_ensemble.append(int(i))
                ads_sites['ontop'].append(coord_center_atom + height['ontop'] * norm_vec_average)
        else:
            pass

    return ads_sites

############################## Sample codes ##############################

# # test
# slab = slab_generator(Cu_bulk, (5, 3, 3), 4, 18.0, (2, 2, 1))
#
# bond_length = 2.53
#
# H = molecule('H')
# O = molecule('O')
# N = molecule('N')
#
# slab_trial = slab[0]
#
# surf_atoms = surf_atom_finder(slab_trial)
#
# # set constraints, and fix atoms
# c = FixAtoms([atom.index for atom in slab_trial if atom.index in surf_atoms])
# slab_trial.set_constraint(c)
#
# connector, conn_coordinates, outer_ite = connection_matrix(slab_trial, surf_atoms, bond_length)
#
# # print(connector)
# # print(conn_coordinates)
#
# ads_sites = find_all_ads_sites(slab_trial, connector, conn_coordinates, surf_atoms, bond_length)
#
# for site in ads_sites:
#     print('{} site has {} possible positions'.format(site, len(ads_sites[site])))
#     for coord in ads_sites[site]:
#         print('The location is: {}'.format(coord))
#
# for site in ads_sites['ontop']:
#     O.set_positions([[site[0], site[1], site[2]]])
#     slab_trial += O
#
# for site in ads_sites['bridge']:
#     H.set_positions([[site[0], site[1], site[2]]])
#     slab_trial += H
#
# for site in ads_sites['four_fold']:
#     N.set_positions([[site[0], site[1], site[2]]])
#     slab_trial += N
#
# view(slab_trial)
