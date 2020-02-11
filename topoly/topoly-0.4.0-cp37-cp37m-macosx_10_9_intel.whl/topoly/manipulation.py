#!/usr/bin/python3
# -*- coding: utf-8 -*- 

"""
The module containing the functions to manipulate the results.
Includes transforming the codes, printing, importing, simplification, and plotting functions.

Pawel Dabrowski-Tumanski
p.dabrowski at cent.uw.edu.pl
27.06.2019
Refactoring by p.rubach at cent.uw.edu.pl
17.01.2020

Docs:
https://realpython.com/documenting-python-code/#docstring-types

The type used here: Google


Support in PyCharm:
https://www.jetbrains.com/help/pycharm/settings-tools-python-integrated-tools.html
- change default reStructuredText to Google

Docs will be published in: https://readthedocs.org/

"""


# TODO
# Dopisac w opisie potrzebne paczki (MatPlotLib) do rysowania?

import re
import ctypes

from .params import Closure, ReduceMethod, TopolyException, OutputType
from .plotting import Reader, KnotMap
from topoly.topoly_preprocess import *
from topoly.topoly_homfly import *
from .polynomial import polynomial
from Bio.PDB.MMCIF2Dict import MMCIF2Dict
from Bio.PDB.MMCIFParser import MMCIFParser
from Bio.PDB.PDBParser import PDBParser
from collections import Sequence
from itertools import chain, count

from .codes import PD

### Data manipulation
def prepare_data(curve):
    # we assume that each point is represented by its coordinates (list of three elements) exactly
    # TODO relax this condition
    file_list = []
    points = {}
    n = 0
    for k in range(len(curve)):
        arc = curve[k]
        for point in arc:
            if tuple(point) not in points.keys():
                n += 1
                points[tuple(point)] = n
        file_name = '_arc' + str(k)
        with open(file_name, 'w') as myfile:
            for point in arc:
                myfile.write(' '.join([str(points[tuple(point)])] + [str(x) for x in point]) + '\n')
        file_list.append(file_name)
    return file_list

#### Translating
# translating the codes
def coords2em(structure, yamada=False, closure=Closure.DIRECTION, tries=200):
    # translating the coordinates to the (generalized) EM code
    if yamada:
        code = find_link_yamada_code(structure)
    else:
        code = find_link_homfly_code(structure, closure=closure, uTRY=tries)
    code = code.decode('utf-8').strip()
    return code

def coords2chain(curve, beg=-1, end=-1):
    res = ''
    indices = []
    for atom in curve:
        res += ' '.join([str(x) for x in atom]) + '\n'
        indices.append(int(atom[0]))
    chain, unable = chain_read_from_string(res.encode('utf-8'))
    if beg not in indices:
        beg = min(indices)
    if end not in indices:
        end = max(indices)
    chain, res = cut_chain(chain, beg, end)
    return chain

def em2pd(code):
    # translates the extended EM code to PD code
    result = ''
    letters = 'abcd'
    intervals = []
    for cross in code.splitlines():
        if not cross:
            continue
        number, rest = re.sub('[-+V]', ' ', cross, count=1).split()
        typ = cross.strip(number)[0]
        code_tmp = []
        tmp = re.split(r'(\d+)', rest)[1:]
        for k in range(0, len(tmp), 2):
            end = tmp[k] + tmp[k + 1]
            if typ == 'V':
                start = number + 'V'
            else:
                start = number + letters[int(k / 2)]
            interval = sorted([start, end])
            if interval not in intervals:
                intervals.append(interval)
            code_tmp.append(str(intervals.index(interval)))
        if typ == '-':
            code_tmp = list(reversed(code_tmp))
        if typ == '+':
            code_tmp = [code_tmp[1], code_tmp[0], code_tmp[3], code_tmp[2]]
        result += re.sub('[-+]', 'X', typ) + '[' + ','.join(code_tmp) + '];'
    result = result[:-1]
    return result

def braid2pd(code):
    # translates the braid one dimensional representation to PD code
    # returns the PD code of the braid, number of strings and the indices of the outgoing arcs
    crossings = [float(x) for x in code.split()]
    strings = max([abs(int(n)) for n in crossings] + [int(str(x)[2:]) for x in crossings if abs(x) < 1]) + 1
    current = range(strings)
    code = ''
    for cross in crossings:
        new = max(current) + 1
        if cross <= -1:
            ind = int(cross)
            code += 'X[' + ','.join([str(current[abs(ind)]), str(new + 1), str(new), str(current[abs(ind)-1])]) + '];'
        elif cross >= 1:
            ind = int(cross)
            code += 'X[' + ','.join([str(current[abs(ind)-1]), str(current[abs(ind)]), str(new + 1), str(new)]) + '];'
        else:
            ind = int(str(abs(cross))[2:])
            code += 'V[' + ','.join([str(current[abs(ind) - 1]), str(current[abs(ind)])]) + '];'
            code += 'V[' + ','.join([str(new), str(new + 1)]) + '];'
        current[abs(ind)] = new + 1
        current[abs(ind) - 1] = new
        code = code[:-1]
    return code, strings, current


def pd2em(code):
    # translates the extended PD code to EM code
    return


def empoly(poly):
    p = polynomial()
    parts = poly.split('|')
    n = 0
    for k in range(len(parts)):
        part = parts[k]
        print(part)
    return p


def data2knotprot(data, beg, end):
    res = '# ' + str(beg) + ' ' + str(end) +' >90 >87 >84 >81 >78 >75 >72 >69 >66 >63 >60 >57 >54 >51 >48 >45 >42 >39 ' \
                                '>36 >33 >30 >27 >24 >21 >18 >15 >12 >9 >6 >3 >0 IN ' + str(beg) + ' ' + str(end) + '\n'
    for key in sorted(data.keys()):
        res_line = list(key) + [0 for _ in range(32)] + list(key)
        knot = data[key]
        for k in knot.keys():
            if k=='empty set':
                continue
            ind = 32-int(min(100*knot[k], 90)/3)
            if res_line[ind] == 0:
                res_line[ind] = k.replace('_', '')
            else:
                res_line[ind] += ';' + k.replace('_', '')
            res += ' '.join([str(_) for _ in res_line]) + '\n'
    return res

def data2string(matrix_result):
    result = ''
    for subchain in matrix_result.keys():
        line_res = str(subchain) + '|'
        if type(matrix_result[subchain]) is dict:
            for knot in matrix_result[subchain].keys():
                line_res += knot + ':' + str(matrix_result[subchain][knot]) + ';'
        result += line_res[:-1] + '\n'
    return result[:-1]


### Graph manipulation

def substitute_edge(graph, substitue='Virtual', debug=True):
    # substituting second edge type with another structure
    return

### Closing the chains or braids
def braid_close(code, strings, current, close_type='N'):
    # returns the PD code of the closed braid
    start = range(strings)
    if close_type == 'N':
        code += 'V[' + ','.join(str(x) for x in list(reversed(start))) + '];'
        code += 'V[' + ','.join(str(x) for x in current) + ']'
    elif close_type == 'D':
        for s in range(strings):
            code += 'V[' + ','.join([str(start[s]), str(current[s])]) + '];'
        code = code[:-1]
    elif close_type == 'V':
        code += 'V[' + ','.join(str(x) for x in current + list(reversed(start))) + ']'
    else:
        new = max(current) + 1
        code += 'V[' + ','.join(str(x) for x in list(reversed(start))) + ',' + str(new) + '];'
        code += 'V[' + ','.join(str(x) for x in current) + ',' + str(new) + ']'
    return code

def chain_close(chain_in, closure=Closure.TWO_POINTS, output_type='', direction=0):
    method = closure
    if method == Closure.MASS_CENTER:
        res, chain = close_chain_out(chain_in)
    elif method == Closure.ONE_POINT:
        res, chain = close_chain_1point(chain_in)
    elif method == Closure.TWO_POINTS:
        res, chain = close_chain_2points(chain_in)
    elif method == Closure.RAYS:
        res, chain = close_chain_1direction(chain_in)
    elif method == Closure.DIRECTION:
        res, chain = close_chain_1direction_no_random(chain_in, direction)
    elif method == Closure.CLOSED:
        res, chain = 0, chain_in
    else:
        raise TopolyException('Unknown closing method ' + method)
    return chain

#### Simplification
# simplification of the curves
def chain_reduce(curve, reduce_method=None, output_type=None, closed=True):
    method = reduce_method
    if not method:
        chain = chain_kmt(curve,closed)
        code = chain_reidemeister(chain)
        return code
    elif method == ReduceMethod.KMT:
        return chain_kmt(curve, closed)
    elif method == ReduceMethod.REIDEMEISTER:
        return chain_reidemeister(curve)
    else:
        raise TopolyException('Unknown reduction method ' + method)


def chain_kmt(curve, closed=True):
    return kmt_reduction(curve, closed)


def chain_reidemeister(code):
    return

#### Plotting
# plotting the results, e.g. the matrices
def plot_matrix(matrix, plot_ofile="KnotFingerPrintMap", plot_format="png", matrix_type="knot", palette=None,
                cutoff=0.48, debug=False):
    knotmap_data = Reader(matrix, cutoff=cutoff)
    unique_knots = knotmap_data.getUniqueKnots()
    knots_size = len(unique_knots)
    knotmap = KnotMap(patches=knots_size, protstart=knotmap_data.chainStart(), protlen=knotmap_data.chainEnd(),
                      rasterized=True, matrix_type=matrix_type)

    for e in unique_knots:
        d = knotmap_data.getKnot(e)
        knotmap.add_patch_new(d)
    knotmap.saveFilePng(plot_ofile + "." + plot_format)
    knotmap.close()
    return



### Structure validation

### Others
def depth(seq):
    for level in count():
        if not seq:
            return level
        seq = list(chain.from_iterable(s for s in seq if isinstance(s, Sequence)))

def check_cuda():
    """
    It's a port of https://gist.github.com/f0k/0d6431e3faa60bffc788f8b4daa029b1
    Author: Jan Schlüter
    """

    libnames = ('libcuda.so', 'libcuda.dylib', 'cuda.dll')
    CUDA_SUCCESS = 0
    for libname in libnames:
        try:
            cuda = ctypes.CDLL(libname)
        except OSError:
            return False
        else:
            break
    else:
        return False

    nGpus = ctypes.c_int()
    result = cuda.cuInit(0)
    if result != CUDA_SUCCESS:
        return False
    result = cuda.cuDeviceGetCount(ctypes.byref(nGpus))
    if result != CUDA_SUCCESS:
        return False
    return True


class DataParser:
    def __init__(self, data):
        self.data = data

    def check_close(self, arcs):
        # checking if the structure has any tail, i.e. the vertex of valency < 2
        ends = {}
        for arc in arcs:
            if arc[0] not in ends.keys():
                ends[arc[0]] = 0
            if arc[-1] not in ends.keys():
                ends[arc[-1]] = 0
            ends[arc[0]] += 1
            ends[arc[-1]] += 1
        for key in ends.keys():
            if ends[key] < 2:
                return False
        return True

    def prepareArcsFromBreaks(self, coordinates, breaks, bridges):
        # preparing the arcs including the information in breaks and bridges
        beg = min(list(coordinates.keys()))
        end = max(list(coordinates.keys()))
        bridging_atoms = [atom for bridge in bridges for atom in bridge]
        arcs = []
        arc = []
        for k in range(beg, end + 1):
            if k == beg or k == end or k not in breaks + bridging_atoms:
                arc.append(k)
            elif k != beg and k != end and k in bridging_atoms:
                arc.append(k)
                arcs.append(arc)
                arc = [k]
            else:
                arc.append(k)
                arcs.append(arc)
                arc = []
        arcs.append(arc)
        arcs += bridges
        return arcs

class PDcodeDataParser(DataParser):
    def read(self):
        data = {'coordinates': {},
                'emcode': '',
                'pdcode': re.sub('\n', ';', self.data),
                'arcs': [],
                'closed': True,
                'breaks': [],
                'bridges': []}
        return data

class EMcodeDataParser(DataParser):
    def read(self):
        data = {'coordinates': {},
                'emcode': re.sub('\n', ';', self.data),
                'pdcode': '',
                'closed': True,
                'arcs': [],
                'breaks': [],
                'bridges': []}
        return data


class ListDataParser(DataParser):
    def read(self, bridges, breaks):
        if depth(self.data) == 3 and len(self.data[0][0]) == 4:
            return self.readArcsFourDim(bridges, breaks)
        elif depth(self.data) == 3 and len(self.data[0][0]) == 3:
            return self.readArcsThreeDim(bridges, breaks)
        elif depth(self.data) == 2 and len(self.data[0]) == 4:
            return self.readChainFourDim(bridges, breaks)
        elif depth(self.data) == 2 and len(self.data[0]) == 3:
            return self.readChainThreeDim(bridges, breaks)
        else:
            raise TypeError('Unrecognized format of the coordinate list. The input is expected as arcs = list of atoms,'
                            ' or list of arcs. The atoms are expected as 3 or 4 element lists.')

    def readArcsFourDim(self, bridges, breaks):
        coordinates = {}
        arcs = []
        # TODO Najlepiej by bylo dodac warning jak ponizej:
        # if bridges or breaks:
        #     WARNING: "The structure is completely determined by the coordinates. Disregarding the additional information on bridges or breaks."
        for arc in self.data:
            arc_indices = []
            for atom in arc:
                try:
                    coordinates[int(atom[0])] = [float(x) for x in atom[1:]]
                    arc_indices.append(int(atom[0]))
                # TODO czy taka jest praktyka na wyjasnienie, skad moze pochodzic blad?
                except ValueError:
                    raise ValueError("The coordinates given in wrong format.")
            arcs.append(arc_indices)

        # preparing the data to return
        data = {'coordinates': coordinates,
                'emcode': '',
                'pdcode': '',
                'closed': super().check_close(arcs),
                'arcs': arcs,
                'breaks': [],
                'bridges': []}
        return data

    def readArcsThreeDim(self, bridges, breaks):
        indices = []
        coordinates = {}
        arcs = []
        # TODO Najlepiej by bylo dodac warning jak ponizej:
        # if bridges or breaks:
        #     WARNING: "The structure is completely determined by the coordinates. Disregarding the additional information on bridges or breaks."
        for arc in self.data:
            arc_indices = []
            for atom in arc:
                pointer = ' '.join(atom[1:])
                if pointer in indices:
                    ind = indices.index(pointer)
                else:
                    ind = len(indices)
                    indices.append(pointer)
                try:
                    coordinates[ind] = [float(x) for x in atom[1:]]
                    arc_indices.append(ind)
                # TODO czy taka jest praktyka na wyjasnienie, skad moze pochodzic blad?
                except ValueError:
                    raise ValueError("The coordinates given in wrong format.")
            arcs.append(arc_indices)

        # preparing the data to return
        data = {'coordinates': coordinates,
                'emcode': '',
                'pdcode': '',
                'closed': super().check_close(arcs),
                'arcs': arcs,
                'breaks': [],
                'bridges': []}
        return data

    def readChainFourDim(self, bridges, breaks):
        # reading the coordinates
        coordinates = {}
        for atom in self.data:
            try:
                coordinates[int(atom[0])] = [float(x) for x in atom[1:]]
            # TODO czy taka jest praktyka na wyjasnienie, skad moze pochodzic blad?
            except ValueError:
                raise ValueError("The coordinates given in wrong format.")

        arcs = self.prepareArcsFromBreaks(coordinates, breaks, bridges)

        # preparing the data to return
        data = {'coordinates': coordinates,
                'emcode': '',
                'pdcode': '',
                'closed': super().check_close(arcs),
                'arcs': arcs,
                'breaks': breaks,
                'bridges': bridges}
        return data

    def readChainThreeDim(self, bridges, breaks):
        # reading the coordinates
        coordinates = {}
        indices = []
        for atom in self.data:
            pointer = ' '.join(atom[1:])
            if pointer in indices:
                ind = indices.index(pointer)
            else:
                ind = len(indices)
                indices.append(pointer)
            try:
                coordinates[ind] = [float(x) for x in atom[1:]]
            # TODO czy taka jest praktyka na wyjasnienie, skad moze pochodzic blad?
            except ValueError:
                raise ValueError("The coordinates given in wrong format.")

        arcs = super().prepareArcsFromBreaks(coordinates, breaks, bridges)

        # preparing the data to return
        data = {'coordinates': coordinates,
                'emcode': '',
                'pdcode': '',
                'closed': super().check_close(arcs),
                'arcs': arcs,
                'breaks': breaks,
                'bridges': bridges}
        return data


class NxyzDataParser(DataParser):
    def read(self, breaks, bridges):
        coordinates = {}
        arcs = []
        arc = []
        for line in self.data.splitlines():
            if len(line) == 0:
                continue
            try:
                int(line.split()[0])
                first_int = True
            except ValueError:
                first_int = False
            if first_int:
                try:
                    coords = line.strip().split()
                    index = int(coords[0])
                    coordinates[index] = [float(x) for x in coords[1:]]
                    arc.append(index)
                # TODO czy taka jest praktyka na wyjasnienie, skad moze pochodzic blad?
                except ValueError:
                    raise ValueError("The coordinates given in wrong format.")
            else:
                if arc:
                    arcs.append(arc)
                    arc = []
            # TODO sprawdzic metode na kajdanusiach - Pawel D.

        if arcs and arc:
            arcs.append(arc)	
        elif not arcs and (breaks or bridges):
            arcs = super().prepareArcsFromBreaks(coordinates, breaks, bridges)
        elif not arcs and not breaks and not bridges:
            arcs = [arc]

        # preparing the data to return
        data = {'coordinates': coordinates,
                'emcode': '',
                'pdcode': '',
                'closed': super().check_close(arcs),
                'arcs': arcs,
                'breaks': breaks,
                'bridges': bridges}
        return data

    def print(self, arcs):
        result = ''
        for arc in arcs:
            for atom in arc:
                result += str(atom) + ' ' + ' '.join([str(_) for _ in self.data[atom]]) + '\n'
            result += 'X\n'
        return result[:-3]


class MathematicaDataParser(DataParser):
    def read(self):
        coordinates = {}
        arcs = []
        indices = []
        arc_coords = self.data.strip('"{}\n').split('}}","{{')
        for arc in arc_coords:
            arc_list = []
            atoms = arc.strip().split('}, {')
            for atom in atoms:
                pointer = atom.replace(',', '')
                if pointer in indices:
                    ind = indices.index(pointer)
                else:
                    ind = len(indices)
                    indices.append(pointer)
                arc_list.append(ind)
                coordinates[ind] = [float(_.replace('*^','E')) for _ in coords.split()]
            arcs.append(arc_list)
            # TODO sprawdzic jak bedzie dzialac na kajdanusiach - Pawel D.

        # preparing the data to return
        data = {'coordinates': coordinates,
                'emcode': '',
                'pdcode': '',
                'closed': super().check_close(arcs),
                'arcs': arcs,
                'breaks': [],
                'bridges': []}
        return data

    def print(self, arcs):
        result = ''
        for arc in arcs:
            result += '"{'
            for atom in arc:
                result += '{' + ', '.join([str(_) for _ in self.data[atom]]) + '}, '
            result = result[:-2] + '}",'
        return result[:-1]


class PdbDataParser(DataParser):
    def __init__(self, data, model=None, chain=None):
        self.data = data
        self.model = model
        self.chain = chain

    def select_chain(self, structure):
        if not self.model and len(structure.get_list())>0:
            model = structure.get_list()[0]
        elif structure.hasid(self.model):
            model = structure[self.model]
        else:
            raise TopolyException('Selected model: ' + str(self.model) + ' does not exist in file: ' + str(self.data))
        if not self.chain and len(model.get_list())>0:
            self.chain = model.get_list()[0].get_id()
            return model.get_list()[0]
        elif model.has_id(self.chain):
            return model[self.chain]
        else:
            raise TopolyException('Selected chain: ' + str(self.chain) + ' does not exist in file: ' + str(self.data) + ' in model: ' + str(model.getid()))

    def read(self):
        coordinates = {}
        bridges = []
        pdb_structure = PDBParser().get_structure('6i7s', self.data)
        chain = self.select_chain(pdb_structure)
        for residue in chain.get_list():
            if residue.has_id("CA") and residue.id[0].strip()=='':
                ca = residue["CA"]
                coordinates[residue.id[1]] = list(ca.get_coord())
        with open(self.data, 'r') as myfile:
            data = myfile.read()
            for line in data.splitlines():
                if line[0:6] == 'SSBOND':
                    if line[15:17].strip()==self.chain and line[29:31].strip()==self.chain:
                        bridges.append([int(line[17:21].strip()), int(line[31:35].strip())])
                else:
                    continue

        arcs = self.prepareArcsFromBreaks(coordinates, [], bridges)

        # preparing the data to return
        data = {'coordinates': coordinates,
                'emcode': '',
                'pdcode': '',
                'closed': super().check_close(arcs),
                'arcs': arcs,
                'breaks': [],
                'bridges': bridges}
        return data

    def print(self, arcs):
        result = ''
        for arc in arcs:
            for atom in arc:
                x, y, z = self.data[atom]
                result += "ATOM  {:>5d}  CA  ALA A{:>4d}    {:>8.3f}{:>8.3f}{:>8.3f}  1.00  1.00           C\n".format(
                          atom, atom, x, y, z)
        return result[:-1]


class MMCIFDataParser(PdbDataParser):
    def read(self):
        coordinates = {}
        bridges = []
        mmcif_dict = MMCIF2Dict(self.data)
        cif_structure = MMCIFParser().get_structure(mmcif_dict['_entry.id'][0], self.data)
        for residue in self.select_chain(cif_structure).get_list():
            if residue.has_id("CA") and residue.id[0].strip()=='':
                ca = residue["CA"]
                coordinates[residue.id[1]] = list(ca.get_coord())
        ssbond_conn = mmcif_dict.get('_struct_conn.conn_type_id')
        chain_1_conn = mmcif_dict.get('_struct_conn.ptnr1_auth_asym_id')
        chain_2_conn = mmcif_dict.get('_struct_conn.ptnr2_auth_asym_id')
        if ssbond_conn:
            for idx in [n for n, x in enumerate(ssbond_conn) if x=='disulf']:
                if chain_1_conn[idx].strip()==self.chain and chain_2_conn[idx].strip()==self.chain:
                    bridges.append([int(mmcif_dict['_struct_conn.ptnr1_auth_seq_id'][idx]), int(mmcif_dict['_struct_conn.ptnr2_auth_seq_id'][idx])])

        arcs = self.prepareArcsFromBreaks(coordinates, [], bridges)

        # preparing the data to return
        data = {'coordinates': coordinates,
                'emcode': '',
                'pdcode': '',
                'closed': super().check_close(arcs),
                'arcs': arcs,
                'breaks': [],
                'bridges': bridges}
        return data

    def print(self, arcs):
        result = ''
        for arc in arcs:
            for atom in arc:
                x, y, z = self.data[atom]
                result += "ATOM   {:<4d}C CA  . ALA A 1 {:<4d}? {:<8.3f}{:<8.3f}{:<8.3f}1.00  1.00 ? {:<4d}ALA A CA  " \
                          "1\n".format(atom, atom, x, y, z, atom)
        return result[:-1]


class PsfDataParser(DataParser):
    def read(self, breaks, bridges):
        coordinates = {}
        arcs = []
        # preparing the data to return
        data = {'coordinates': coordinates,
                'emcode': '',
                'pdcode': '',
                'closed': super().check_close(arcs),
                'arcs': arcs,
                'breaks': breaks,
                'bridges': bridges}
        return data

    def print(self, arcs):
        bond1, bond2 = None, None
        indexes = []
        bonds = []
        i = 0

        for arc in arcs:
            for atom in arc:
                bond2 = bond1
                bond1 = atom
                if bond1 and bond2:
                    bonds.append((bond2, bond1))
                if atom not in indexes:
                    indexes.append(atom)
            bond2 = bond1
            bond1 = None

        result = """\n                    PSF CMAP\n\n                        {:>4d}  !NATOM\n""".format(len(indexes))
        for index in indexes:
            result += ' {:>7d} A {:>7d}  GLY  CA  CA   0.000  1.000      0\n'.format(index, index)
        result += '\n    {:>4d} !NBOND: bonds\n'.format(len(bonds))
        for bond in bonds:
            i += 1
            result += ' {:>7d} {:>7d}'.format(bond[0], bond[1])
            if i % 4 == 0:
                result += '\n'
        return result


class XyzDataParser(DataParser):
    def read(self, breaks, bridges):
        coordinates = {}
        arcs = []
        indices = []
        arc = []
        for line in self.data.splitlines():
            if len(line) == 0:
                continue
            try:
                float(line.split()[0])
                first_float = True
            except ValueError:
                first_float = False
                # TODO Najlepiej by bylo dodac warning jak ponizej:
                # if bridges or breaks:
                #     WARNING: "The structure is completely determined by the input data. Disregarding the additional information on bridges or breaks."
            if first_float:
                if line.strip() in indices:
                    ind = indices.index(line.strip())
                else:
                    ind = len(indices)
                    indices.append(line.strip())
                try:
                    coordinates[ind] = [float(x) for x in line.strip().split()]
                    arc.append(ind)
                # TODO czy taka jest praktyka na wyjasnienie, skad moze pochodzic blad?
                except ValueError:
                    raise ValueError("The coordinates given in wrong format.")
            else:
                if arc:
                    arcs.append(arc)
                    arc = []
        if arc not in arcs:
            arcs.append(arc)
            # TODO sprawdzic metode na kajdanusiach - Pawel D.
        # preparing the data to return
        data = {'coordinates': coordinates,
                'emcode': '',
                'pdcode': '',
                'closed': super().check_close(arcs),
                'arcs': arcs,
                'breaks': breaks,
                'bridges': bridges}
        return data

    def print(self, arcs):
        result = ''
        for arc in arcs:
            for atom in arc:
                result += ' '.join([str(_) for _ in self.data[atom]]) + '\n'
            result += 'X\n'
        return result[:-3]


class DataParser:
    format_dict = {
        'xyz' : XyzDataParser,
        'nxyz': NxyzDataParser,
        'list': ListDataParser,
        'pdb': PdbDataParser,
        'cif': MMCIFDataParser,
        'mathematica': MathematicaDataParser,
        'pdcode': PDcodeDataParser,
        'emcode': EMcodeDataParser
    }
    @classmethod
    def list_formats(cls):
        return cls.format_dict.keys()

    @classmethod
    def read_format(cls, data, orig_input, chain, bridges, breaks, debug):
        if isinstance(data, list):
            if debug:
                print("Recognized format as list.")
            return ListDataParser(data).read(bridges, breaks)
        elif not isinstance(data, str):
            raise TypeError('Unknown type of input data. Expected string or list.')

        lines = data.split('\n')
        first_line = lines[0]
        characters = set(re.split("[^a-zA-Z]*", data)) - {'V', ''}
        if len(lines) >= 3 and len(lines[2]) > 0 and lines[2].startswith('_entry.id'):
            if debug:
                print("Recognized format as CIF file.")
            # TODO Najlepiej by bylo dodac warning jak ponizej:
            # if bridges or breaks:
            #     WARNING: "The structure is completely determined by the input data. Disregarding the additional information on bridges or breaks."
            return MMCIFDataParser(orig_input, chain=chain).read()
        elif first_line.startswith('HEADER') and 'ATOM' in data:
            if debug:
                print("Recognized format as PDB file.")
            # TODO Najlepiej by bylo dodac warning jak ponizej:
            # if bridges or breaks:
            #     WARNING: "The structure is completely determined by the input data. Disregarding the additional information on bridges or breaks."
            # TODO dodac wybor lancucha i modelu
            return PdbDataParser(orig_input, chain=chain).read()
        elif '{' in data:
            if debug:
                print("Recognized format as Mathematica file.")
            # TODO Najlepiej by bylo dodac warning jak ponizej:
            # if bridges or breaks:
            #     WARNING: "The structure is completely determined by the input data. Disregarding the additional information on bridges or breaks."
            return MathematicaDataParser(data).read()
        elif 'X[' in data or 'V[' in data:
            if debug:
                print("Recognized format as PD code.")
            return PDcodeDataParser(data).read()
        elif characters == {'a', 'b', 'c', 'd'} in data:
            if debug:
                print("Recognized format as EM code.")
            return EMcodeDataParser(data).read()
        elif len(first_line.split()) == 4 and first_line.split()[0].isdigit():
            return NxyzDataParser(data).read(breaks, bridges)
        else:
            return XyzDataParser(data).read(breaks, bridges)

    # TODO dodac wypisywanie PDB, PSF i MMCIF
    @classmethod
    def print_data(cls, coordinates, arcs, pdcode, emcode, output_type):
        if output_type == OutputType.PDcode:
            return pdcode
        elif output_type == OutputType.EMcode:
            return emcode
        elif output_type == OutputType.NXYZ:
            return NxyzDataParser(coordinates).print(arcs)
        elif output_type == OutputType.PDB:
            return PdbDataParser(coordinates).print(arcs)
        elif output_type == OutputType.Mathematica:
            return MathematicaDataParser(coordinates).print(arcs)
        elif output_type == OutputType.MMCIF:
            return MMCIFDataParser(coordinates).print(arcs)
        elif output_type == OutputType.PSF:
            return PsfDataParser(coordinates).print(arcs)
        else:
            return XyzDataParser(coordinates).print(arcs)
