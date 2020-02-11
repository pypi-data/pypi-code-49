#!/usr/bin/python3
# -*- coding: utf-8 -*- 
from time import time

from topoly import import_coords, yamada, homfly, alexander, conway, \
    jones, yamada, blmho, kauffman_bracket, kauffman_polynomial, Closure, TopolyException
#file = 'data/1j85.pdb'
curve = 'data/2efv.xyz'
#file = 'data/2efv.cif'
#print(curve_xyz)
#print(curve)

#poly =  {'HOMFLY-PT: [[0] 0 -2 0 -1]|[0]|[0] 0 1': 0.49, 'HOMFLY-PT: [[1]]': 0.5, 'HOMFLY-PT: [-1 0 -2 0 [0]]|[0]|1 0 [0]': 0.005, 'HOMFLY-PT: [1 0 1 0 -1 0 [0]]|[0]|-1 0 1 0 [0]': 0.005}
#from topoly.invariants import find_matching_structure

#print(find_matching_structure(poly))

print('homfly : ', homfly(curve, matrix=False, closure=Closure.TWO_POINTS, tries=200, translate=True))
print('alex : ', alexander(curve, matrix=False, closure=Closure.TWO_POINTS, tries=200, translate=True))

