#! /usr/bin/env python

import pysiaf
from mirage.utils import siaf_interface

ra = 12.
dec = 12.
rotation = 0.
aperture = 'NRCA5_GRISM256_F444W'

siaf = pysiaf.Siaf('nircam')

roll, attitude_matrix, ffsize, subarray_bounds = siaf_interface.get_siaf_information(siaf,
                                                                                     aperture,
                                                                                     ra, dec,
                                                                                     rotation)
print(attitude_matrix)
print(roll)

loc_v2, loc_v3 = pysiaf.utils.rotations.getv2v3(attitude_matrix, ra, dec)

print(loc_v2, loc_v3)
print(siaf[aperture].V2Ref, siaf[aperture].V3Ref)

pixelx, pixely = siaf[aperture].tel_to_sci(loc_v2, loc_v3)
print(pixelx, pixely)
print(siaf[aperture].XSciRef, siaf[aperture].YSciRef)
