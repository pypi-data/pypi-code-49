#!/usr/bin/env python3
# encoding: utf-8

"""
A module for manipulating vectors
"""

import math
import numpy as np

from zmats.exceptions import VectorsError


def get_angle(v1: list,
              v2: list,
              units: str = 'degs',
              ) -> float:
    """
    Calculate the angle between two vectors.

    Args:
         v1 (list): Vector 1.
         v2 (list): Vector 2.
         units (str, optional): The desired units, either 'rads' for radians, or 'degs' for degrees.

    Returns:
        float: The angle between ``v1`` and ``v2`` in the desired units.

    Raises:
        ZMatError: If ``v1`` and ``v2`` are of different lengths.
    """
    if len(v1) != len(v2):
        raise VectorsError(f'v1 and v2 must be the same length, got {len(v1)} and {len(v2)}.')
    v1_u, v2_u = unit_vector(v1), unit_vector(v2)
    conversion = 180 / math.pi if 'degs' in units else 1
    return float(np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0)) * conversion)


def get_dihedral(v1: list,
                 v2: list,
                 v3: list,
                 units: str = 'degs',
                 ) -> float:
    """
    Calculate the dihedral angle between three vectors.
    ``v2`` connects between ``v1`` and ``v3``.
    Inspired by ASE Atoms.get_dihedral().

    Args:
         v1 (list): Vector 1.
         v2 (list): Vector 2.
         v3 (list): Vector 3.
         units (str, optional): The desired units, either 'rads' for radians, or 'degs' for degrees.

    Returns:
        float: The dihedral angle between ``v1`` and ``v2`` in the desired units.

    Raises:
        ZMatError: If either ``v1`` or ``v2`` have lengths different than three.
    """
    if len(v1) != 3 or len(v2) != 3 or len(v3) != 3:
        raise VectorsError(f'v1, v2, and v3 must have a length of three, got {len(v1)}, {len(v2)}, and {len(v3)}.')
    v1, v2, v3 = np.array(v1, np.float64), np.array(v2, np.float64), np.array(v3, np.float64)
    v2_x_v1 = np.cross(v2, v1)
    v2_x_v1 /= float(np.linalg.norm(v2_x_v1))
    v3_x_v2 = np.cross(v3, v2)
    v3_x_v2 /= np.linalg.norm(v3_x_v2)
    dihedral = np.arccos(np.clip(np.vdot(v2_x_v1, v3_x_v2), -1, 1))
    if np.vdot(v2_x_v1, v3) > 0:
        dihedral = 2 * np.pi - dihedral
    if np.isnan(dihedral):
        raise VectorsError('Could not calculate a dihedral angle')
    conversion = 180 / math.pi if 'degs' in units else 1
    return float(dihedral * conversion)


def calculate_distance(coords: list or tuple,
                       atoms: list,
                       index: int = 0,
                       ) -> float:
    """
    Calculate a distance.

    Args:
        coords (list, tuple): The array-format or tuple-format coordinates.
        atoms (list): The 2 atoms to calculate defining the vector for which the length will be calculated.
        index (int, optional): Whether ``atoms`` is 0-indexed or 1-indexed (accepted values are 0 or 1).

    Returns:
        float: The distance in the coords units.

    Raises:
        ZMatError: If ``index`` is out of range, or ``atoms`` is of wrong length or has repeating indices.
        TypeError: If ``coords`` is of wrong type.
    """
    if isinstance(coords, dict) and 'coords' in coords:
        coords = coords['coords']
    if not isinstance(coords, (list, tuple)):
        raise TypeError(f'coords must be a list or a tuple, got\n{coords}\nwhich is a {type(coords)}')
    if index not in [0, 1]:
        raise VectorsError(f'index must be either 0 or 1, got {index}')
    if len(atoms) != 2:
        raise VectorsError(f'distance atom list must be of length two, got {len(atoms)}')
    if len(set(atoms)) < 2:
        raise VectorsError(f'some atoms are repetitive: {atoms}')
    new_atoms = list()
    for atom in atoms:
        if isinstance(atom, str) and 'X' in atom:
            new_atoms.append(int(atom[1:]))
        else:
            new_atoms.append(atom)
    if not all([isinstance(a, int) for a in new_atoms]):
        raise VectorsError(f'all entries in atoms must be integers, got: {new_atoms} ({[type(a) for a in new_atoms]})')
    new_atoms = [a - index for a in new_atoms]  # convert 1-index to 0-index
    coords = np.asarray(coords, dtype=np.float32)
    vector = coords[new_atoms[1]] - coords[new_atoms[0]]
    return get_vector_length(vector)


def calculate_angle(coords: list or tuple,
                    atoms: list,
                    index: int = 0,
                    units: str = 'degs',
                    ) -> float:
    """
    Calculate an angle.

    Args:
        coords (list, tuple): The array-format or tuple-format coordinates.
        atoms (list): The 3 atoms defining the angle.
        index (int, optional): Whether ``atoms`` is 0-indexed or 1-indexed (values are 0 or 1).
        units (str, optional): The desired units, either 'rads' for radians, or 'degs' for degrees.

    Returns:
        float: The angle.

    Raises:
        VectorsError: If ``index`` is out of range, or ``atoms`` is of wrong length or has repeating indices.
        TypeError: If ``coords`` is of wrong type.
    """
    if isinstance(coords, dict) and 'coords' in coords:
        coords = coords['coords']
    if not isinstance(coords, (list, tuple)):
        raise TypeError(f'coords must be a list or a tuple, got\n{coords}\nwhich is a {type(coords)}')
    if index not in [0, 1]:
        raise VectorsError(f'index must be either 0 or 1, got {index}')
    if len(atoms) != 3:
        raise VectorsError(f'angle atom list must be of length three, got {len(atoms)}')
    if len(set(atoms)) < 3:
        raise VectorsError(f'some atoms are repetitive: {atoms}')
    new_atoms = list()
    for atom in atoms:
        if isinstance(atom, str) and 'X' in atom:
            new_atoms.append(int(atom[1:]))
        else:
            new_atoms.append(atom)
    if not all([isinstance(a, int) for a in new_atoms]):
        raise VectorsError(f'all entries in atoms must be integers, got: {new_atoms} ({[type(a) for a in new_atoms]})')
    new_atoms = [a - index for a in new_atoms]  # convert 1-index to 0-index
    coords = np.asarray(coords, dtype=np.float32)
    v1 = coords[new_atoms[1]] - coords[new_atoms[0]]
    v2 = coords[new_atoms[1]] - coords[new_atoms[2]]
    return get_angle(v1, v2, units=units)


def calculate_dihedral_angle(coords: list or tuple,
                             torsion: list,
                             index=0,
                             units: str = 'degs',
                             ) -> float:
    """
    Calculate a dihedral angle.

    Args:
        coords (list, tuple): The array-format or tuple-format coordinates.
        torsion (list): The 4 atoms defining the dihedral angle.
        index (int, optional): Whether ``torsion`` is 0-indexed or 1-indexed (values are 0 or 1).
        units (str, optional): The desired units, either 'rads' for radians, or 'degs' for degrees.

    Returns:
        float: The dihedral angle in a 0-360 degrees range.

    Raises:
        VectorsError: If ``index`` is out of range, or ``torsion`` is of wrong length or has repeating indices.
        TypeError: If ``coords`` is of wrong type.
    """
    if isinstance(coords, dict) and 'coords' in coords:
        coords = coords['coords']
    if not isinstance(coords, (list, tuple)):
        raise TypeError(f'coords must be a list or a tuple, got\n{coords}\nwhich is a {type(coords)}')
    if index not in [0, 1]:
        raise VectorsError(f'index must be either 0 or 1, got {index}')
    if len(torsion) != 4:
        raise VectorsError(f'torsion atom list must be of length four, got {len(torsion)}')
    if len(set(torsion)) < 4:
        raise VectorsError(f'some indices in the given torsion are repetitive: {torsion}')
    new_torsion = list()
    for atom in torsion:
        if isinstance(atom, str) and 'X' in atom:
            new_torsion.append(int(atom[1:]))
        else:
            new_torsion.append(atom)
    if not all([isinstance(t, int) for t in new_torsion]):
        raise VectorsError(f'all entries in torsion must be integers, got: {new_torsion} '
                           f'({[type(t) for t in new_torsion]})')
    new_torsion = [t - index for t in new_torsion]  # convert 1-index to 0-index if needed
    coords = np.asarray(coords, dtype=np.float32)
    v1 = coords[new_torsion[1]] - coords[new_torsion[0]]
    v2 = coords[new_torsion[2]] - coords[new_torsion[1]]
    v3 = coords[new_torsion[3]] - coords[new_torsion[2]]
    return get_dihedral(v1, v2, v3, units=units)


def unit_vector(vector: list) -> list:
    """
    Calculate a unit vector in the same direction as the input vector.

    Args:
        vector (list): The input vector.

    Returns:
        list: The unit vector.
    """
    length = get_vector_length(vector)
    return [vi / length for vi in vector]


def get_vector_length(v: list) -> float:
    """
    Get the length of an ND vector

    Args:
        v (list): The vector.

    Returns:
        float: The vector's length.
    """
    return float(np.dot(v, v) ** 0.5)
