"""
A module for manipulating zmats.
"""

import os

import numpy as np

from qcelemental.periodic_table import periodictable
from rmgpy.molecule import Molecule

from zmats.exceptions import ConverterError
from zmats.zmats import (KEY_FROM_LEN,
                         get_all_neighbors,
                         get_atom_indices_from_zmat_parameter,
                         get_parameter_from_atom_indices,
                         xyz_to_zmat,
                         zmat_to_coords,
                         )


def check_zmat_dict(zmat: dict or str) -> dict:
    """
    Check that the zmat dictionary entered is valid.
    If it is a string, convert it.
    If it represents cartesian coordinates, convert it to internal coordinates.
    If a map isn't given, a trivial one will be added.

    Args:
        zmat (dict, str): The zmat dictionary.

    Raises:
        ConverterError: If ``zmat`` is of wrong type or is missing vars or coords.
    """
    zmat_dict = str_to_zmat(zmat) if isinstance(zmat, str) else zmat
    if not isinstance(zmat_dict, dict):
        raise ConverterError(f'Expected a dictionary, got {type(zmat_dict)}')
    if 'vars' not in list(zmat_dict.keys()):
        # this is probably a representation of cartesian coordinates, convert to zmat
        zmat_dict = zmat_from_xyz(xyz=check_xyz_dict(zmat_dict), consolidate=True)
    if 'symbols' not in list(zmat_dict.keys()):
        raise ConverterError(f'zmat dictionary is missing symbols. Got:\n{zmat_dict}')
    if 'coords' not in list(zmat_dict.keys()):
        raise ConverterError(f'zmat dictionary is missing coords. Got:\n{zmat_dict}')
    if len(zmat_dict['symbols']) != len(zmat_dict['coords']):
        raise ConverterError(f'Got {len(zmat_dict["symbols"])} symbols and {len(zmat_dict["coords"])} '
                             f'coordinates:\n{zmat_dict}')
    if 'map' not in list(zmat_dict.keys()):
        # add a trivial map
        zmat_dict['map'] = {i: i for i in range(len(zmat_dict['symbols']))}
    if len(zmat_dict['symbols']) != len(zmat_dict['map']):
        raise ConverterError(f'Got {len(zmat_dict["symbols"])} symbols and {len(zmat_dict["isotopes"])} '
                             f'isotopes:\n{zmat_dict}')
    for i, coord in enumerate(zmat_dict['coords']):
        for j, param in enumerate(coord):
            if param is not None:
                indices = get_atom_indices_from_zmat_parameter(param)
                if not any(i == index_tuple[0] for index_tuple in indices):
                    raise ConverterError(f'The {param} parameter in the zmat is ill-defined:\n{zmat_dict}')
            if (i == 0 or i == 1 and j in [1, 2] or i == 2 and j == 3) and param is not None:
                raise ConverterError(f'The zmat is ill-defined:\n{zmat_dict}')
    return zmat_dict


def check_xyz_dict(xyz: dict or str) -> dict:
    """
    Check that the xyz dictionary entered is valid.
    If it is a string, convert it.
    If it is a Z matrix, convert it to cartesian coordinates,
    If isotopes are not in xyz_dict, common values will be added.

    Args:
        xyz (dict or str): The xyz dictionary.

    Raises:
        ConverterError: If ``xyz`` is of wrong type or is missing symbols or coords.
    """
    xyz_dict = str_to_xyz(xyz) if isinstance(xyz, str) else xyz
    if not isinstance(xyz_dict, dict):
        raise ConverterError(f'Expected a dictionary, got {type(xyz_dict)}')
    if 'vars' in list(xyz_dict.keys()):
        # this is a zmat, convert to cartesian
        xyz_dict = zmat_to_xyz(zmat=xyz_dict, keep_dummy=False)
    if 'symbols' not in list(xyz_dict.keys()):
        raise ConverterError(f'XYZ dictionary is missing symbols. Got:\n{xyz_dict}')
    if 'coords' not in list(xyz_dict.keys()):
        raise ConverterError(f'XYZ dictionary is missing coords. Got:\n{xyz_dict}')
    if len(xyz_dict['symbols']) != len(xyz_dict['coords']):
        raise ConverterError(f'Got {len(xyz_dict["symbols"])} symbols and {len(xyz_dict["coords"])} '
                             f'coordinates:\n{xyz_dict}')
    if 'isotopes' not in list(xyz_dict.keys()):
        xyz_dict = xyz_from_data(coords=xyz_dict['coords'], symbols=xyz_dict['symbols'])
    if len(xyz_dict['symbols']) != len(xyz_dict['isotopes']):
        raise ConverterError(f'Got {len(xyz_dict["symbols"])} symbols and {len(xyz_dict["isotopes"])} '
                             f'isotopes:\n{xyz_dict}')
    return xyz_dict


def remove_dummies(xyz: dict or str) -> dict:
    """
    Remove dummy ('X') atoms from cartesian coordinates.

    Args:
        xyz (dict, str): The cartesian coordinate, either in a dict or str format.

    Returns:
        dict: The coordinates w/o dummy atoms.

    Raises:
        ConverterError: If ``xyz`` if of wrong type.
    """
    if isinstance(xyz, str):
        xyz = str_to_xyz(xyz)
    if not isinstance(xyz, dict):
        raise ConverterError(f'xyz must be a dictionary, got {type(xyz)}')
    symbols, isotopes, coords = list(), list(), list()
    for symbol, isotope, coord in zip(xyz['symbols'], xyz['isotopes'], xyz['coords']):
        if symbol != 'X':
            symbols.append(symbol)
            isotopes.append(isotope)
            coords.append(coord)
    return xyz_from_data(coords=coords, symbols=symbols, isotopes=isotopes)


def xyz_to_str(xyz_dict: dict,
               isotope_format: str = None,
               ) -> str:
    """
    Convert an ARC xyz dictionary format, e.g.::

        {'symbols': ('C', 'N', 'H', 'H', 'H', 'H'),
         'isotopes': (13, 14, 1, 1, 1, 1),
         'coords': ((0.6616514836, 0.4027481525, -0.4847382281),
                    (-0.6039793084, 0.6637270105, 0.0671637135),
                    (-1.4226865648, -0.4973210697, -0.2238712255),
                    (-0.4993010635, 0.6531020442, 1.0853092315),
                    (-2.2115796924, -0.4529256762, 0.4144516252),
                    (-1.8113671395, -0.3268900681, -1.1468957003))}

    to a string xyz format with optional Gaussian-style isotope specification, e.g.::

        C(Iso=13)    0.6616514836    0.4027481525   -0.4847382281
        N           -0.6039793084    0.6637270105    0.0671637135
        H           -1.4226865648   -0.4973210697   -0.2238712255
        H           -0.4993010635    0.6531020442    1.0853092315
        H           -2.2115796924   -0.4529256762    0.4144516252
        H           -1.8113671395   -0.3268900681   -1.1468957003

    Args:
        xyz_dict (dict): The ARC xyz format to be converted.
        isotope_format (str, optional): The format for specifying the isotope if it is not the most abundant one.
                                        By default, isotopes will not be specified. Currently the only supported
                                        option is 'gaussian'.

    Returns:
        str: The string xyz format.

    Raises:
        ConverterError: If input is not a dict or does not have all attributes.
    """
    xyz_dict = check_xyz_dict(xyz_dict)
    if xyz_dict is None:
        print('Got None for xyz_dict')
        return None
    recognized_isotope_formats = ['gaussian']
    if any([key not in list(xyz_dict.keys()) for key in ['symbols', 'isotopes', 'coords']]):
        raise ConverterError(f'Missing keys in the xyz dictionary. Expected to find "symbols", "isotopes", and '
                             f'"coords", but got {list(xyz_dict.keys())} in\n{xyz_dict}')
    if any([len(xyz_dict['isotopes']) != len(xyz_dict['symbols']),
            len(xyz_dict['coords']) != len(xyz_dict['symbols'])]):
        raise ConverterError(f'Got different lengths for "symbols", "isotopes", and "coords": '
                             f'{len(xyz_dict["symbols"])}, {len(xyz_dict["isotopes"])}, and {len(xyz_dict["coords"])}, '
                             f'respectively, in xyz:\n{xyz_dict}')
    if any([len(xyz_dict['coords'][i]) != 3 for i in range(len(xyz_dict['coords']))]):
        raise ConverterError(f'Expected 3 coordinates for each atom (x, y, and z), got:\n{xyz_dict}')
    xyz_list = list()
    for symbol, isotope, coord in zip(xyz_dict['symbols'], xyz_dict['isotopes'], xyz_dict['coords']):
        common_isotope = periodictable.to_A(symbol)
        if isotope_format is not None and common_isotope != isotope:
            # consider the isotope number
            if isotope_format == 'gaussian':
                element_with_isotope = '{0}(Iso={1})'.format(symbol, isotope)
                row = '{0:14}'.format(element_with_isotope)
            else:
                raise ConverterError(f'Recognized isotope formats for printing are {recognized_isotope_formats}, '
                                     f'got: {isotope_format}')
        else:
            # don't consider the isotope number
            row = f'{symbol:4}'
        row += '{0:14.8f}{1:14.8f}{2:14.8f}'.format(*coord)
        xyz_list.append(row)
    return '\n'.join(xyz_list)


def str_to_xyz(xyz_str: str) -> dict:
    """
    Convert a string xyz format to the ARC dict xyz style.
    Note: The ``xyz_str`` argument could also direct to a file path to parse the data from.
    The xyz string format may have optional Gaussian-style isotope specification, e.g.::

        C(Iso=13)    0.6616514836    0.4027481525   -0.4847382281
        N           -0.6039793084    0.6637270105    0.0671637135
        H           -1.4226865648   -0.4973210697   -0.2238712255
        H           -0.4993010635    0.6531020442    1.0853092315
        H           -2.2115796924   -0.4529256762    0.4144516252
        H           -1.8113671395   -0.3268900681   -1.1468957003

    which will also be parsed into the ARC xyz dictionary format, e.g.::

        {'symbols': ('C', 'N', 'H', 'H', 'H', 'H'),
         'isotopes': (13, 14, 1, 1, 1, 1),
         'coords': ((0.6616514836, 0.4027481525, -0.4847382281),
                    (-0.6039793084, 0.6637270105, 0.0671637135),
                    (-1.4226865648, -0.4973210697, -0.2238712255),
                    (-0.4993010635, 0.6531020442, 1.0853092315),
                    (-2.2115796924, -0.4529256762, 0.4144516252),
                    (-1.8113671395, -0.3268900681, -1.1468957003))}

    Args:
        xyz_str (str): The string xyz format to be converted.

    Returns:
        dict: The ARC xyz format.

    Raises:
        ConverterError: If xyz_str is not a string or does not have four space-separated entries per non empty line.
    """
    if not isinstance(xyz_str, str):
        raise ConverterError(f'Expected a string input, got {type(xyz_str)}')
    if os.path.isfile(xyz_str):
        from arc.parser import parse_xyz_from_file
        return parse_xyz_from_file(xyz_str)
    if len(xyz_str.splitlines()[0]) == 1:
        # this is a zmat
        return zmat_to_xyz(zmat=str_to_zmat(xyz_str), keep_dummy=False)
    xyz_dict = {'symbols': tuple(), 'isotopes': tuple(), 'coords': tuple()}
    if all([len(line.split()) == 6 for line in xyz_str.splitlines() if line.strip()]):
        # Convert Gaussian output format, e.g., "      1          8           0        3.132319    0.769111   -0.080869"
        # not considering isotopes in this method!
        for line in xyz_str.splitlines():
            if line.strip():
                splits = line.split()
                symbol = periodictable.to_E(int(splits[1]))
                coord = (float(splits[3]), float(splits[4]), float(splits[5]))
                xyz_dict['symbols'] += (symbol,)
                xyz_dict['isotopes'] += (periodictable.to_A(symbol),)
                xyz_dict['coords'] += (coord,)
    else:
        # this is a "regular" string xyz format, if it has isotope information it will be preserved
        for line in xyz_str.strip().splitlines():
            if line.strip():
                splits = line.split()
                if len(splits) != 4:
                    raise ConverterError('xyz_str has an incorrect format, expected 4 elements in each line, '
                                         'got "{0}" in:\n{1}'.format(line, xyz_str))
                symbol = splits[0]
                if '(iso=' in symbol.lower():
                    isotope = int(symbol.split('=')[1].strip(')'))
                    symbol = symbol.split('(')[0]
                else:
                    # no specific isotope is specified in str_xyz
                    isotope = periodictable.to_A(symbol)
                coord = (float(splits[1]), float(splits[2]), float(splits[3]))
                xyz_dict['symbols'] += (symbol,)
                xyz_dict['isotopes'] += (isotope,)
                xyz_dict['coords'] += (coord,)
    return xyz_dict


def standardize_xyz_string(xyz_str: str,
                           isotope_format: str = None,
                           ) -> str:
    """
    A helper function to correct xyz string format input (** string to string **).
    Usually empty lines are added by the user either in the beginning or the end,
    here we remove them along with other common issues.

    Args:
        xyz_str (str): The string xyz format, or a Gaussian output format.
        isotope_format (str, optional): The format for specifying the isotope if it is not the most abundant one.
                                        By default, isotopes will not be specified. Currently the only supported
                                        option is 'gaussian'.

    Returns:
        str: The string xyz format in standardized format.

    Raises:
        ConverterError: If ``xyz_str`` is of wrong type.
    """
    if not isinstance(xyz_str, str):
        raise ConverterError('Expected a string format, got {0}'.format(type(xyz_str)))
    xyz_dict = str_to_xyz(xyz_str)
    return xyz_to_str(xyz_dict=xyz_dict, isotope_format=isotope_format)


def xyz_from_data(coords: tuple or list,
                  numbers: tuple or list = None,
                  symbols: tuple or list = None,
                  isotopes: tuple or list = None,
                  ) -> dict:
    """
    Get the ARC xyz dictionary format from raw data.
    Either ``numbers`` or ``symbols`` must be specified.
    If ``isotopes`` isn't specified, the most common isotopes will be assumed for all elements.

    Args:
        coords (tuple, list): The xyz coordinates.
        numbers (tuple, list, optional): Element nuclear charge numbers.
        symbols (tuple, list, optional): Element symbols.
        isotopes (tuple, list, optional): Element isotope numbers.

    Returns:
        dict: The ARC dictionary xyz format.

    Raises:
        ConverterError: If neither ``numbers`` nor ``symbols`` are specified, if both are specified,
                        or if the input lengths aren't consistent.
    """
    if isinstance(coords, np.ndarray):
        coords = tuple(tuple(coord.tolist()) for coord in coords)
    elif isinstance(coords, list):
        coords = tuple(tuple(coord) for coord in coords)
    if numbers is not None and isinstance(numbers, np.ndarray):
        numbers = tuple(numbers.tolist())
    elif numbers is not None and isinstance(numbers, list):
        numbers = tuple(numbers)
    if symbols is not None and isinstance(symbols, list):
        symbols = tuple(symbols)
    if isotopes is not None and isinstance(isotopes, list):
        isotopes = tuple(isotopes)
    if not isinstance(coords, tuple):
        raise ConverterError('Expected coords to be a tuple, got {0} which is a {1}'.format(coords, type(coords)))
    if numbers is not None and not isinstance(numbers, tuple):
        raise ConverterError('Expected numbers to be a tuple, got {0} which is a {1}'.format(numbers, type(numbers)))
    if symbols is not None and not isinstance(symbols, tuple):
        raise ConverterError('Expected symbols to be a tuple, got {0} which is a {1}'.format(symbols, type(symbols)))
    if isotopes is not None and not isinstance(isotopes, tuple):
        raise ConverterError('Expected isotopes to be a tuple, got {0} which is a {1}'.format(isotopes, type(isotopes)))
    if numbers is None and symbols is None:
        raise ConverterError('Must set either "numbers" or "symbols". Got neither.')
    if numbers is not None and symbols is not None:
        raise ConverterError('Must set either "numbers" or "symbols". Got both.')
    if numbers is not None:
        symbols = tuple(periodictable.to_E(number) for number in numbers)
    if len(coords) != len(symbols):
        raise ConverterError(f'The length of the coordinates ({len(coords)}) is different than the length of the '
                             f'numbers/symbols ({len(symbols)}).')
    if isotopes is not None and len(coords) != len(isotopes):
        raise ConverterError(f'The length of the coordinates ({len(coords)}) is different than the length of isotopes '
                             f'({len(isotopes)}).')
    if isotopes is None:
        isotopes = tuple(periodictable.to_A(symbol) for symbol in symbols)
    xyz_dict = {'symbols': symbols, 'isotopes': isotopes, 'coords': coords}
    return xyz_dict


def zmat_from_xyz(xyz: dict or str,
                  mol: Molecule = None,
                  constraints: dict = None,
                  consolidate: bool = True,
                  consolidation_tols: dict = None,
                  ) -> dict:
    """
    Generate a Z matrix from xyz.

    Args:
        xyz (dict, str): The cartesian coordinate, either in a dict or str format.
        mol (Molecule, optional): The corresponding RMG Molecule with connectivity information.
        constraints (dict, optional): Accepted keys are:
                                      'R_atom', 'R_group', 'A_atom', 'A_group', 'D_atom', 'D_group', or 'D_groups'.
                                      'R', 'A', and 'D', constraining distances, angles, and dihedrals, respectively.
                                      Values are lists of atom indices (0-indexed) tuples.
                                      The atom indices order matters.
                                      Specifying '_atom' will cause only the last atom in the specified list values
                                      to translate/rotate if the corresponding zmat parameter is changed.
                                      Specifying '_group' will cause the entire group connected to the last atom
                                      to translate/rotate if the corresponding zmat parameter is changed.
                                      Specifying '_groups' (only valid for D) will cause the groups connected to
                                      the last two atoms to translate/rotate if the corresponding parameter is changed.
        consolidate (bool, optional): Whether to consolidate the zmat after generation, ``True`` to consolidate.
        consolidation_tols (dict, optional): Keys are 'R', 'A', 'D', values are floats representing absolute tolerance
                                             for consolidating almost equal internal coordinates.

    Returns:
        dict: The Z matrix.

    Raises:
        ConverterError: If ``xyz`` if of wrong type.
    """
    if isinstance(xyz, str):
        xyz = str_to_xyz(xyz)
    if not isinstance(xyz, dict):
        raise ConverterError(f'xyz must be a dictionary, got {type(xyz)}')
    xyz = remove_dummies(xyz)
    return xyz_to_zmat(xyz,
                       mol=mol,
                       constraints=constraints,
                       consolidate=consolidate,
                       consolidation_tols=consolidation_tols)


def zmat_to_xyz(zmat: dict,
                keep_dummy: bool = False,
                xyz_isotopes: dict = None,
                ) -> dict:
    """
    Generate the xyz dict coordinates from a zmat dict.
    Most common isotopes assumed, unless a reference xyz dict is given.

    Args:
        zmat (dict): The zmat.
        keep_dummy (bool): Whether to keep dummy atoms ('X'), ``True`` to keep, default is ``False``.
        xyz_isotopes (dict): A reference xyz dictionary to take isotope information from.
                             Must be ordered as the original mol/xyz used to create ``zmat``.

    Returns:
        dict: The xyz cartesian coordinates.
    """
    coords, symbols = zmat_to_coords(zmat, keep_dummy=keep_dummy)
    isotopes = xyz_isotopes['isotopes'] if xyz_isotopes is not None else None
    xyz_dict = translate_to_center_of_mass(xyz_from_data(coords=coords, symbols=symbols, isotopes=isotopes))
    return xyz_dict


def zmat_to_str(zmat: dict,
                zmat_format: str = 'gaussian',
                consolidate: bool = True,
                ) -> str:
    """
    Convert a zmat to a string format.

    Args:
        zmat (dict): The Z Matrix to convert.
        zmat_format (str, optional): The requested format to output (varies by ESS).
                                     Allowed values are: 'gaussian', 'qchem', 'molpro', 'orca', or 'psi4'.
                                     The default format is 'gaussian'.
        consolidate (bool): Whether to return a consolidated zmat (geometry optimization will be more efficient).

    Returns:
        str: The string representation of the zmat in the requested format.

    Raises:
        ConverterError: If ``zmat`` is of wrong type or missing keys, or if ``zmat_format`` is not recognized.
    """
    if not isinstance(zmat, dict):
        raise ConverterError(f'zmat has to be a dict, got: {type(zmat)}')
    if 'symbols' not in zmat or 'coords' not in zmat or 'vars' not in zmat:
        raise ConverterError(f'zmat must contain the "symbols", "coords", and "vars" keys, got: '
                             f'{list(zmat.keys())}.')
    if zmat_format == 'terachem':
        raise ConverterError('TeraChem does not accept a zmat as input (it has its own internal conversions).')
    if zmat_format not in ['gaussian', 'qchem', 'molpro', 'orca', 'psi4']:
        raise ConverterError(f'zmat_format must be either gaussian, qchem, molpro, orca, or psi4, got: {zmat_format}.')
    if zmat_format == 'orca':
        # replace dummy atom symbols
        symbols = list()
        for symbol in zmat['symbols']:
            symbols.append(symbol if symbol != 'X' else 'DA')
    else:
        symbols = zmat['symbols']
    if zmat_format == 'orca':
        # Redundant internal coordinates are automatically used by Orca,
        # parametarized internal coordinates are hence not supported
        consolidate = False
    separator = ',' if zmat_format in ['molpro'] else ''
    var_separator = '=' if zmat_format in ['gaussian', 'molpro', 'qchem', 'psi4'] else ' '
    zmat_str, variables_str, variables = '', '', list()
    type_indices = {'R': 1, 'A': 1, 'D': 1}  # consolidation counters
    variables_dict = dict()  # keys are coord (e.g., 'R_2|4_0|0'), values are vars (e.g., 'R1')
    for i, (symbol, coords) in enumerate(zip(symbols, zmat['coords'])):
        line = f'{symbol:>3}'
        for coord in coords:
            if coord is not None:
                index_tuples = get_atom_indices_from_zmat_parameter(coord)
                for indices in index_tuples:
                    if indices[0] == i:
                        break
                if consolidate:
                    if coord in list(variables_dict.keys()):
                        var_str = variables_dict[coord]
                    else:
                        var_type = coord[0]  # 'R', 'A', or 'D'
                        var_str = f'{var_type}{type_indices[var_type]}'
                        type_indices[var_type] += 1
                        variables_dict[coord] = var_str
                        variables.append(f'{var_str}{var_separator}{zmat["vars"][coord]:.4f}\n')
                    line += f'{separator}{indices[-1] + 1:8d}{separator}{var_str:>8}'  # convert to 1-indexed
                else:
                    line += f'{separator}{indices[-1] + 1:8d}{separator}{zmat["vars"][coord]:10.4f}'
        if zmat_format == 'orca' and consolidate:
            symbol, indices, coordinates = '', '', ''
            for j, entry in enumerate(line.split()):
                if j == 0:
                    symbol = entry + ' '
                elif j % 2 == 0:
                    coordinates += entry + ' '
                else:
                    indices += entry + ' '
            while len(indices.split()) < 3:
                indices += '0 '
            while len(coordinates.split()) < 3:
                coordinates += '0.0 '
            line = symbol + indices + coordinates[:-1]
        zmat_str += line + '\n'
    if zmat_format in ['gaussian']:
        variables_str = ''.join(sorted(variables))
        result = f'{zmat_str}Variables:\n{variables_str}' if consolidate else zmat_str
    elif zmat_format in ['qchem', 'psi4', 'orca']:
        variables_str = ''.join(sorted(variables))
        result = f'{zmat_str}\n{variables_str}' if consolidate else zmat_str
    elif zmat_format in ['molpro']:
        variables_str = ''.join(sorted(variables))
        result = f'{variables_str}\n{zmat_str}' if consolidate else zmat_str
    else:
        result = zmat_str + variables_str
    return result


def str_to_zmat(zmat_str: str) -> dict:
    """
    Convert a string Z Matrix format to the ARC dict zmat style.
    Note: The ``zmat_str`` argument could also direct to a file path to parse the data from.
    A typical zmat string format may look like this::

          C
          H       1      R1
          H       1      R1       2      A1
          H       1      R1       2      A1       3      D1
          H       1      R1       2      A1       3      D2
          A1=109.4712
          D1=120.0000
          D2=240.0000
          R1=1.0912

    The resulting zmat for the above example is::

        {'symbols': ('C', 'H', 'H', 'H', 'H'),
         'coords': ((None, None, None),
                    ('R_1_0', None, None),
                    ('R_2_1', 'A_2_1_0', None),
                    ('R_3_2', 'A_3_2_0', 'D_3_2_0_1'), ('R_4_3', 'A_4_3_0', 'D_4_3_0_2')),
         'vars': {'R_1_0': 1.0912, 'R_2_1': 1.782, 'A_2_1_0': 35.2644, 'R_3_2': 1.782, 'A_3_2_0': 35.2644,
                  'D_3_2_0_1': 120.0, 'R_4_3': 1.782, 'A_4_3_0': 35.2644, 'D_4_3_0_2': 240.0},
         'map': {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}}

    Args:
        zmat_str (str): The string zmat format to be converted.

    Returns:
        dict: The ARC zmat format.

    Raises:
        ConverterError: If zmat_str is not a string or does not have enough values per line.
    """
    if not isinstance(zmat_str, str):
        raise ConverterError(f'Expected a string input, got {type(zmat_str)}')
    if os.path.isfile(zmat_str):
        with open(zmat_str, 'r') as f:
            zmat_str = f.read()
    symbols, coords, variables = list(), list(), dict()
    coords_str = split_str_zmat(zmat_str)[0]
    index = 1
    for i, line in enumerate(coords_str.splitlines()):
        splits = line.split()
        if i == 1:
            # the atom index in this line must point to the first atom in the zmat,
            # deduce whether this zmat is in a 0-index or a 1-index format
            index = int(splits[1])
        if len(splits) not in (1, 3, 5, 7):
            raise ConverterError(f'Could not interpret the zmat line {line}')
        symbols.append(splits[0])
        r_key = f'R_{i}_{int(splits[1]) - index}' if len(splits) >= 3 else None  # convert to 0-index
        a_key = 'A' + r_key[1:] + f'_{int(splits[3]) - index}' if len(splits) >= 5 else None
        d_key = 'D' + a_key[1:] + f'_{int(splits[5]) - index}' if len(splits) == 7 else None
        coords.append((r_key, a_key, d_key))
        if r_key is not None:
            variables[r_key] = float(splits[2]) if is_str_float(splits[2]) \
                else get_zmat_str_var_value(zmat_str, splits[2])
        if a_key is not None:
            variables[a_key] = float(splits[4]) if is_str_float(splits[4]) \
                else get_zmat_str_var_value(zmat_str, splits[4])
        if d_key is not None:
            variables[d_key] = float(splits[6]) if is_str_float(splits[6]) \
                else get_zmat_str_var_value(zmat_str, splits[6])
    map_ = {i: i for i in range(len(symbols))}  # trivial map
    zmat_dict = {'symbols': tuple(symbols), 'coords': tuple(coords), 'vars': variables, 'map': map_}
    return zmat_dict


def split_str_zmat(zmat_str: str) -> tuple:
    """
    Split a string zmat into its coordinates and variables sections.

    Args:
        zmat_str (str): The zmat.

    Returns:
        tuple[str: The coords section,
              str: The variables section if it exists, else None,
             ]
    """
    coords, variables = list(), list()
    flag = False
    if 'variables' in zmat_str.lower():
        for line in zmat_str.splitlines():
            if 'variables' in line.lower():
                flag = True
                continue
            elif flag and line:
                variables.append(line)
            elif line:
                coords.append(line)
    else:
        splits = zmat_str.splitlines()
        if len(splits[0].split()) == len(splits[1].split()) and \
                (len(splits[0].split()) == 2 or (len(splits[0].split()) == 1 and len(splits[1]) != 1)):
            # this string starts with the variables section
            for line in splits:
                if flag and line:
                    coords.append(line)
                if not flag and len(line.split()) == len(splits[0].split()) and line:
                    variables.append(line)
                else:
                    flag = True
        elif len(splits[-1].split()) == len(splits[-2].split()) and len(splits[-1].split()) in [1, 2]:
            # this string starts with the coordinates section
            for line in splits:
                if flag and len(line.split()) == len(splits[-1].split()) and line:
                    variables.append(line)
                if not flag and line:
                    coords.append(line)
                else:
                    flag = True
    coords = '\n'.join(coords) if len(coords) else zmat_str
    variables = '\n'.join(variables) if len(variables) else None
    return coords, variables


def get_zmat_str_var_value(zmat_str: str,
                           var: str,
                           ) -> float:
    """
    Returns the value of a zmat variable from a string-represented zmat.

    Args:
        zmat_str (str): The string representation of the zmat.
        var (str): The variable to look for.

    Returns:
        float: The value corresponding to the ``var``.
    """
    for line in reversed(zmat_str.splitlines()):
        if var in line and len(line.split()) in [1, 2]:
            return float(line.replace('=', ' ').split()[-1])
    raise ConverterError(f'Could not find var "{var}" in zmat:\n{zmat_str}')


def get_zmat_param_value(coords: dict,
                         indices: list,
                         mol: Molecule,
                         ) -> float:
    """
    Generates a zmat similarly to modify_coords(),
    but instead of modifying it, only reports on the value of a requested parameter.

    Args:
        coords (dict): Either cartesian (xyz) or internal (zmat) coordinates.
        indices (list): The indices to change (0-indexed). Specifying a list of length 2, 3, or 4
                        will result in a length, angle, or a dihedral angle parameter, respectively.
        mol (Molecule, optional): The corresponding RMG molecule with the connectivity information.

    Returns:
        float: The parameter value in Angstrom or degrees.
    """
    modification_type = KEY_FROM_LEN[len(indices)] + '_' + 'atom'  # e.g., R_atom
    if 'map' in list(coords.keys()):
        # a zmat was given, we actually need xyz to recreate a specific zmat for the parameter modification.
        xyz = zmat_to_xyz(zmat=coords)
    else:
        # coords represents xyz
        xyz = coords

    constraints = {modification_type: [tuple(indices)]}
    zmat = xyz_to_zmat(xyz=xyz, mol=mol, consolidate=False, constraints=constraints)
    param = get_parameter_from_atom_indices(zmat, indices, xyz_indexed=True)
    if isinstance(param, str):
        return zmat["vars"][param]
    elif isinstance(param, list):
        return sum(zmat["vars"][par] for par in param)


def modify_coords(coords: dict,
                  indices: list,
                  new_value: float,
                  modification_type: str,
                  mol: Molecule = None,
                  ) -> dict:
    """
    Modify either a bond length, angle, or dihedral angle in the given coordinates.
    The coordinates input could either be cartesian (preferred) or internal (will be first converter to cartesian,
    then to internal back again since a specific zmat must be created).
    Internal coordinates will be used for the modification (using folding and unfolding).

    Specifying an 'atom' modification type will only translate/rotate the atom represented by the first index
    if the corresponding zmat parameter is changed.
    Specifying a 'group' modification type will cause the entire group connected to the first atom to translate/rotate
    if the corresponding zmat parameter is changed.
    Specifying a 'groups' modification type (only valid for dihedral angles) will cause the groups connected to
    the first two atoms to translate/rotate if the corresponding zmat parameter is changed.

    Args:
        coords (dict): Either cartesian (xyz) or internal (zmat) coordinates.
        indices (list): The indices to change (0-indexed). Specifying a list of length 2, 3, or 4
                        will result in changing a bond length, angle, or a dihedral angle, respectively.
        new_value (float): The new value to set (in Angstrom or degrees).
        modification_type (str): Either 'atom', 'group', or 'groups' ('groups' is only allowed for dihedral angles).
                                 Note that D 'groups' is a composite constraint, equivalent to calling D 'group'
                                 for each 1st neighboring  atom in a torsion top.
        mol (Molecule, optional): The corresponding RMG molecule with the connectivity information.
                                  Mandatory if the modification type is 'group' or 'groups'.

    Returns:
        dict: The respective cartesian (xyz) coordinates reflecting the desired modification.

    Raises:
        ConverterError: If a group/s modification type is requested but ``mol`` is ``None``,
                    or if a 'groups' modification type was specified for R or A.
    """
    if modification_type not in ['atom', 'group', 'groups']:
        raise ConverterError(f'Allowed modification types are atom, group, or groups, got: {modification_type}.')
    if mol is None and 'group' in modification_type:
        raise ConverterError(f'A molecule must be given for a {modification_type} modification type.')
    modification_type = KEY_FROM_LEN[len(indices)] + '_' + modification_type  # e.g., R_group
    if modification_type == 'groups' and modification_type[0] != 'D':
        raise ConverterError(f'The "groups" modification type is only supported for dihedrals (D), '
                         f'not for an {modification_type[0]} parameter.')
    if 'map' in list(coords.keys()):
        # a zmat was given, we actually need xyz to recreate a specific zmat for the parameter modification.
        xyz = zmat_to_xyz(zmat=coords)
    else:
        # coords represents xyz
        xyz = coords

    constraints_list = [tuple(indices)]
    if modification_type == 'D_groups':
        # this is a special constraint for which neighbor dihedrals must be considered as well.
        neighbors = get_all_neighbors(mol=mol, atom_index=indices[1])
        for neighbor in neighbors:
            if neighbor not in indices:
                constraints_list.append(tuple([neighbor] + indices[1:]))
        modification_type = 'D_group'

    new_xyz = xyz
    increment = None
    for constraint in constraints_list:
        constraint_dict = {modification_type: [constraint]}
        zmat = xyz_to_zmat(xyz=new_xyz, mol=mol, consolidate=False, constraints=constraint_dict)
        param = get_parameter_from_atom_indices(zmat, constraint, xyz_indexed=True)

        if modification_type == 'D_group' and increment is None:
            # determine the dihedral increment, will be used for all other D-group modifications
            increment = new_value - zmat["vars"][param]
        if isinstance(param, str):
            if increment is None:
                zmat['vars'][param] = new_value
            else:
                zmat['vars'][param] += increment
        elif isinstance(param, list):
            # the requested parameter represents an angle split by a dummy atom,
            # a list of the two corresponding parameters was be returned
            zmat['vars'][param[0]] = new_value - sum(zmat['vars'][par] for par in param[1:])
        new_xyz = zmat_to_xyz(zmat=zmat)
    return new_xyz


def translate_to_center_of_mass(xyz: dict) -> dict:
    """
    Translate coordinates to their center of mass.

    Args:
        xyz (dict): The 3D coordinates.

    Returns:
        dict: The translated coordinates.
    """
    # identify and remove dummy atoms for center of mass determination (but then do translate dummy atoms as well)
    dummies = list()
    for i, symbol in enumerate(xyz['symbols']):
        if symbol == 'X':
            dummies.append(i)
    no_dummies_xyz = {'symbols': [symbol for i, symbol in enumerate(xyz['symbols']) if i not in dummies],
                      'isotopes': [isotope for i, isotope in enumerate(xyz['isotopes']) if i not in dummies],
                      'coords': [coord for i, coord in enumerate(xyz['coords']) if i not in dummies]}
    cm_x, cm_y, cm_z = get_center_of_mass(no_dummies_xyz)
    x = [coord[0] - cm_x for coord in xyz['coords']]
    y = [coord[1] - cm_y for coord in xyz['coords']]
    z = [coord[2] - cm_z for coord in xyz['coords']]
    for i in range(len(x)):
        x[i] = x[i] if abs(x[i]) > 1e-10 else 0.0
        y[i] = y[i] if abs(y[i]) > 1e-10 else 0.0
        z[i] = z[i] if abs(z[i]) > 1e-10 else 0.0
    translated_coords = tuple((xi, yi, zi) for xi, yi, zi in zip(x, y, z))
    return xyz_from_data(coords=translated_coords, symbols=xyz['symbols'], isotopes=xyz['isotopes'])


def is_str_float(value: str) -> bool:
    """
    Check whether a string represents a number.

    Args:
        value (str): The string to check.

    Returns:
        bool: ``True`` if it does, ``False`` otherwise.
    """
    try:
        float(value)
        return True
    except ValueError:
        return False


def get_center_of_mass(xyz: dict) -> tuple:
    """
    Get the center of mass of xyz coordinates.
    Assumes arc.converter.standardize_xyz_string() was already called for xyz.
    Note that xyz from ESS output is usually already centered at the center of mass (to some precision).

    Args:
        xyz (dict): The xyz coordinates.

    Returns:
        tuple: The center of mass coordinates.
    """
    masses = [periodictable.to_mass(f'{symbol}{isotope}')
              for symbol, isotope in zip(xyz['symbols'], xyz['isotopes'])]
    cm_x, cm_y, cm_z = 0, 0, 0
    for coord, mass in zip(xyz['coords'], masses):
        cm_x += coord[0] * mass
        cm_y += coord[1] * mass
        cm_z += coord[2] * mass
    cm_x /= sum(masses)
    cm_y /= sum(masses)
    cm_z /= sum(masses)
    return cm_x, cm_y, cm_z
