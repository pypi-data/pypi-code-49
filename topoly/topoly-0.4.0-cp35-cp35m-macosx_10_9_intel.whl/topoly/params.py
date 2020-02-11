# -*- coding: utf-8 -*-
""" Topoly Parameters
This module contains common parameters for various functions used in Topoly
"""

class Closure:
    """
    Type of closure
    """
    CLOSED = 0
    """ (deterministic) direct segment between two endpoints """
    MASS_CENTER = 1
    """ (deterministic) segments added to two endpoints in the direction "going out of center of mass", and then connected by an arc on the big sphere"""
    TWO_POINTS = 2
    """ (random) each endpoint connected with different random point on the big sphere, and those added points connected by an arc on the big sphere"""
    ONE_POINT = 3
    """ (random) both endpoints connected with the same random point on the big sphere"""
    RAYS = 4
    """ (random) parallel segments added to two endpoints, and then connected by an arc on the big sphere; direction of added segments is random"""
    DIRECTION = 5
    """ (deterministic) the same as RAYS but the direction can be given"""


class ReduceMethod:
    """
    Reduction Method
    """
    KMT = 1
    """ KMT algorithm [ Koniaris K, Muthukumar M (1991) Self-entanglement in ring polymers, J. Chem. Phys. 95, 2873–2881 ]. This algorithm analyzes all triangles in a chain made by three consecutive amino acids, and removes the middle amino acid in case a given triangle is not intersected by any other segment of the chain. In effect, after a number of iterations, the initial chain is replaced by (much) shorter chain of the same topological type."""
    REIDEMEISTER = 2
    """ Simplification of chain (and number of crossings) by a sequence of Reidemeister moves"""
    EASY = 3
    #TODO: Nie wiem, co to za metoda, w chain_reduce() w manipulation.py nie jest uwzgledniona (Pawel ?)


class SurfacePlotFormat:
    VMD = 4
    JSMOL = 2
    MATHEMATICA = 1
    DONTPLOT = 0


class TopolyException(Exception):
    pass


class PlotFormat:
    PNG = 'png'
    SVG = 'svg'


class OutputFormat:
    """
    The output formats for the matrices.
    """
    KnotProt = 'knotprot'
    """ The matrix in the format used in KnotProt"""
    Dictionary = 'dict'
    """ The dictionary-like output"""


class PrecisionSurface:
    """
    Precision of computations of minimal surface spanned on the loop (high precision => time consuming computations)
    """
    HIGH = 0
    """ The highest precision, default for single structure """
    MEDIUM = 1
    """ Two lower precision levels, may be used when analyzing large structures, trajectories or other big sets of data"""
    LOW = 2


class DensitySurface:
    """
    Density of the triangulation of minimal surface spanned on the loop (high precision => time consuming computations)
    Default value: MEDIUM
    """
    HIGH = 2
    MEDIUM = 1
    LOW = 0

class Bridges:
    """
    The bridges types to be parsed from PDB file.
    """
    SSBOND = 'ssbond'
    ION = 'ion'
    COVALENT = 'covalent'
    ALL = 'all'


class OutputType:
    """
    The possible output types for find_loops, find_thetas, etc.
    """
    PDcode = 'pdcode'
    EMcode = 'emcode'
    XYZ = 'xyz'
    NXYZ = 'nxyz'
    PDB = 'pdb'
    Mathematica = 'math'
    MMCIF = 'mmcif'
    PSF = 'psf'