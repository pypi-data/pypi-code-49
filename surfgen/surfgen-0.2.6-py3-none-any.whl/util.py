# python module
import copy
import numpy as np

# surfgen
from surfgen.math import *

############################## Here comes the Python code ##############################
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

    Return:
        Boolean. Shows whether the molecule is above the surface or not.
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
        Boolean. Check whether the molecule and the adsorption sites are matched.
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
