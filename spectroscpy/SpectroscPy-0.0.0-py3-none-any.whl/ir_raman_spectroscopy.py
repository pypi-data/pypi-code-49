# SpectroscPy v.3
# SpectroscPy is a script package developed by and containing contributions from

    # Karen Oda Hjorth Dundas
    # Magnus Ringholm
    # Yann Cornation
    # Benedicte Ofstad

# The package is released under a LGPL licence.
# For questions, please contact on karen.o.dundas@uit.no

# For this routine, KD would like to thank John Kendrick for helpful discussions regardin IR

# IR/Raman spectroscopy

from .parameters import*
import numpy as np
from math import exp, pi, sqrt
from sys import exit

# Independent of units
def summed_dip_grad_sq(dipole_gradient):

    red_dipole_strength = np.zeros((len(dipole_gradient)))

    for i in range(len(dipole_gradient)):
        for j in range(3):
            red_dipole_strength[i] = red_dipole_strength[i] + dipole_gradient[i][j]**2

    return red_dipole_strength


# Independent of units
def combined_polarizabilites(polarizability_gradients, combination_type):

    a2 = get_a2_term(polarizability_gradients)
    b2 = get_b2_term(polarizability_gradients)

    if ('45+7' in combination_type):
        a_factor = 45.0
        b_factor = 7.0
    elif ('45+4' in combination_type):
        a_factor = 45.0
        b_factor = 4.0
    else:
        print('\n')
        print('Error in combined_polarizabilites')
        print('No combination rule specified')
        exit()

    combo = np.zeros((len(polarizability_gradients)))
    for i in range(len(polarizability_gradients)):
        combo[i] = a_factor*a2[i] + b_factor*b2[i]

    return combo


# SI units
def raman_scattering_cross_section(polarizability_gradients, au_incident_energy, \
                                   au_vibrational_energies, combination_type, print_level, \
                                   temperature):

    SI_polarizability_gradient = np.multiply(polarizability_gradients, ((hartree_to_coulomb*hbar)/ \
                                                                        (hartree_to_joule))**2/ \
                                                                        ((one_twelfth_carbon)**(3/2)* \
                                                                          bohr_to_meter))
    a2 = get_a2_term(SI_polarizability_gradient)
    b2 = get_b2_term(SI_polarizability_gradient)

    if ('45+7' in combination_type):
        intensities_caption = 'Intensities 45 + 7'
    elif ('45+4' in combination_type):
        intensities_caption = 'Intensities 45 + 4'
    else:
        print('\n')
        print('Error in raman_scattering_cross_section')
        print('No combination rule specified')
        exit()

    cpg = combined_polarizabilites(SI_polarizability_gradient, combination_type)

    SI_wavenumbers = np.multiply(au_vibrational_energies, \
                                 (hartree_to_joule/(plancs_constant*speed_of_light)))
    SI_incident_wavenumbers = au_incident_energy*hartree_to_joule/(plancs_constant*speed_of_light)

    qi2 = qi_prefactor2(SI_wavenumbers)

    exp_denominator = get_exp_denominator(SI_wavenumbers, temperature)

    intensities = np.zeros((len(au_vibrational_energies)))

    for i in range(len(intensities)):
        intensities[i] = qi2[i]*exp_denominator[i]*(SI_incident_wavenumbers - \
                                                    SI_wavenumbers[i])**4*cpg[i]

    if (print_level > 3):
        print('\n')
        print('Raman SI values for input wavenumer ', SI_incident_wavenumbers)
        print('%4s %18s %13s %20s %20s' %('Mode', 'Wavenumbers', 'a**2', 'b**2 ', 'qi**2'))
        for i in range(len(SI_wavenumbers)):
            print('%2d %20.6f %20.10E %20.10E %20.10E' %(i, SI_wavenumbers[i], a2[i], b2[i], qi2[i]))
        print('\n')
        print('%4s %15s %25s' %('Mode', 'Boltzfac', intensities_caption))
        for i in range(len(SI_wavenumbers)):
            print('%2d %20.10E %20.10E' %(i, exp_denominator[i], intensities[i]))
        print('\n')

    return intensities


# SI units
def get_exp_denominator(wavenumbers, temperature):

    exp_denominator = np.zeros((len(wavenumbers)))

    if (temperature == 0):
        for i in range(len(exp_denominator)):
            exp_denominator[i] = 1
    else:
        factor = np.multiply(wavenumbers, (-plancs_constant*speed_of_light/ \
                                          (boltzmann_constant_SI*temperature)))

        for i in range(len(wavenumbers)):
            exp_denominator[i] = 1 - exp(factor[i])

    return exp_denominator


# SI units
def qi_prefactor2(wavenumbers):

    qi2 = np.zeros((len(wavenumbers)))

    prefactor = plancs_constant/(8*pi**2*speed_of_light)

    for i in range(len(wavenumbers)):
        qi2[i] = prefactor/wavenumbers[i]

    return qi2


# Unit independent
def get_b2_term(polarizability_gradients):

    b2 = np.zeros((len(polarizability_gradients)))

    for i in range(len(polarizability_gradients)):
        for j in range(3):
            for k in range(3):
                if (k != j):
                    b2[i] = b2[i] + 0.5*(polarizability_gradients[i][j][j] - \
                                         polarizability_gradients[i][k][k])**2 \
                                  + 3*(polarizability_gradients[i][j][k])**2

    b2 = 0.5*b2

    return b2


# Unit independent
def get_a2_term(polarizability_gradients):

    a2 = np.zeros((len(polarizability_gradients)))

    for i in range(len(polarizability_gradients)):
        for j in range(3):
            a2[i] = a2[i] + polarizability_gradients[i][j][j]

    a2 = a2/3

    a2 = a2**2

    return a2
