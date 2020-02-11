# SpectroscPy 0.0.0
# SpectroscPy is a script package developed by and containing contributions from

    # Karen Oda Hjorth Dundas
    # Magnus Ringholm
    # Yann Cornation
    # Benedicte Ofstad

# The package is released under a LGPL licence.
# For questions, please contact on karen.o.dundas@uit.no

from math import sqrt

# Conversion factors
hartree_to_coulomb     = 1.60217656535e-19
bohr_to_meter          = 5.29177210922e-11
hartree_to_joule       = 4.3597441775e-18

# Constants
vacuum_permittivity    = 8.854187817e-12
hbar                   = 1.054571726e-34
avogadros_constant     = 6.02214075862e23
plancs_constant        = 6.62607015e-34
speed_of_light         = 299792458
boltzmann_constant_SI  = 1.38064852e-23

# mass of one electron in kg, or in other words conversion factor from au to kg
electron_mass = 9.1093829140e-31
# (1/12)th of the mass of a carbon atom in kg, or in other words conversion from amu to kg
one_twelfth_carbon = 1.66053904020e-27

#DALTON
debye_to_coulomb_meter = 10**(-21)/speed_of_light
angstrom_to_meter      = 1.0e-10

fermi_threshold  = 200.0
martin_threshold = 1.0

hess_operator = ['GEO', 'GEO']
dip_grad_operator = ['GEO', 'EL']
polariz_grad_operator = ['GEO', 'EL', 'EL']
hyper_polariz_grad_operator = ['GEO', 'EL', 'EL', 'EL']

