# SpectroscPy 0.0.0
# SpectroscPy is a script package developed by and containing contributions from

    # Karen Oda Hjorth Dundas
    # Magnus Ringholm
    # Yann Cornation
    # Benedicte Ofstad

# The package is released under a LGPL licence.
# For questions, please contact on karen.o.dundas@uit.no

# For this routine, KD would like to thank John Kendrick for helpful discussions regardin IR

from .parameters import*
import numpy as np
from math import exp, pi, sqrt, log
from sys import exit

# Independent of units
def summed_dip_grad_sq(dipole_gradient):

    red_dipole_strength = np.zeros((len(dipole_gradient)))

    for i in range(len(dipole_gradient)):
        for j in range(3):
            red_dipole_strength[i] = red_dipole_strength[i] + dipole_gradient[i][j]**2

    return red_dipole_strength


# SI units
def qi_prefactor2(wavenumbers):

    qi2 = np.zeros((len(wavenumbers)))

    prefactor = plancs_constant/(8*pi**2*speed_of_light)

    for i in range(len(wavenumbers)):
        qi2[i] = prefactor/wavenumbers[i]

    return qi2


def get_ir_intensities(specifications, dipole_gradient, print_level):

    # SSDG: summed and squared dipole au_polarizability_gradients
    # Units: a.u. or D^2 Å^-2 amu^-1
    # Reported as intensities many places, for instance in Dalton
    ir_au_ssdg = summed_dip_grad_sq(dipole_gradient)
    ir_SI_ssdg = np.multiply(ir_au_ssdg, hartree_to_coulomb**2/electron_mass)
    ir_DA_ssdg = np.multiply(ir_au_ssdg, \
                                 (hartree_to_coulomb*angstrom_to_meter)**2*one_twelfth_carbon/ \
                                 (electron_mass*debye_to_coulomb_meter**2))

    if (print_level > 2):
        print('\n')
        print('SSDG: summed and squared dipole gradients')
        print('%4s %14s %28s %29s' %('Mode', 'a.u', 'C**2/kg', '(D/Å)**2/amu'))
        for i in range(len(ir_au_ssdg)):
            print('%2d %27.22f %27.22f %27.22f' %(i, ir_au_ssdg[i], ir_SI_ssdg[i], ir_DA_ssdg[i]))

    ir_temp = np.multiply(ir_SI_ssdg, (avogadros_constant/(3*vacuum_permittivity*speed_of_light)))

    # MDAC: Molar decadic attenuated coefficient
    # Without lineshape, so the units that should be m^2/mol are actually m^2/s*mol
    ir_SI_mdac = np.multiply(ir_temp, (pi*6*log(10)))
    ir_Lcm_mdac = np.multiply(ir_SI_mdac, 0.1)

    if (print_level > 2):
        print('\n')
        print('MDAC: Molar decadic attenuated coefficient.  Without lineshape, so therefore the')
        print('extra s^-1 unit')
        print('%4s %16s %22s' %('Mode', 'm**2/(s*mol)', 'L/(cm*s*mol)'))
        for i in range(len(ir_SI_mdac)):
            print('%2d %22.4f %22.4f' %(i, ir_SI_mdac[i], ir_Lcm_mdac[i]))

    # NIMAC: Naperian integrated molar absorption coefficient
    ir_SI_nimac = np.multiply(ir_temp, 1/(4*speed_of_light))
    ir_kmmol_nimac = np.multiply(ir_SI_nimac, 10**(-3))

    if (print_level > 2):
        print('\n')
        print('NIMAC: Naperian integrated molar absorption coefficient')
        print('%4s %12s %22s' %('Mode', 'm/mol', 'km/mol'))
        for i in range(len(ir_SI_nimac)):
            print('%2d %24.13f %24.19f' %(i, ir_SI_nimac[i], ir_kmmol_nimac[i]))

    if ('IR: SSDG, a.u.' in specifications):
        ir_intensities = ir_au_ssdg
        current_unit = 'SSDG, a.u.'
        header_format_string = '%4s %15s %15s'
        format_string = '%2d %17.6f %22.17f'
    elif ('IR: SSDG, C**2/kg' in specifications):
        ir_intensities = ir_SI_ssdg
        current_unit = 'SSDG, C**2/kg'
        header_format_string = '%4s %15s %16s'
        format_string = '%2d %17.6f %25.20f'
    elif ('IR: SSDG, D2A2/amu' in specifications):
        ir_intensities = ir_DA_ssdg
        current_unit = '(D/Å)**2/amu'
        header_format_string = '%4s %15s %14s'
        format_string = '%2d %17.6f %15.10f'
    elif ('IR: MDAC, m**2/(s*mol)' in specifications):
        ir_intensities = ir_SI_mdac
        current_unit = 'MDAC, m**2/(s*mol)'
        header_format_string = '%4s %15s %14s'
        format_string = '%2d %17.6f %20.1f'
    elif ('IR: MDAC, L/(cm*s*mol)' in specifications):
        ir_intensities = ir_Lcm_mdac
        current_unit = 'MDAC, L/(cm*s*mol)'
        header_format_string = '%4s %15s %16s'
        format_string = '%2d %17.6f %20.1f'
    elif ('IR: NIMAC, m/mol' in specifications):
        ir_intensities = ir_SI_nimac
        current_unit = 'NIMAC, m/mol'
        header_format_string = '%4s %15s %16s'
        format_string = '%2d %17.6f %17.8f'
    elif ('IR: NIMAC, km/mol' in specifications):
        ir_intensities = ir_kmmol_nimac
        current_unit = 'NIMAC, km/mol'
        header_format_string = '%4s %15s %16s'
        format_string = '%2d %17.6f %17.10f'
    else:
        print('\n')
        print('You forgot to specify the IR units in specifications')
        exit()

    return ir_intensities, current_unit, header_format_string, format_string
