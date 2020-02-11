# SpectroscPy 0.0.0
# SpectroscPy is a script package developed by and containing contributions from

    # Karen Oda Hjorth Dundas
    # Magnus Ringholm
    # Yann Cornation
    # Benedicte Ofstad

# The package is released under a LGPL licence.
# For questions, please contact on karen.o.dundas@uit.no

from .parameters import*
import numpy as np
from math import exp
from sys import exit
from .ir import qi_prefactor2

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

    SI_polarizability_gradient = np.multiply(polarizability_gradients, \
                                             (hartree_to_coulomb**2*bohr_to_meter)/ \
                                             (hartree_to_joule*electron_mass))
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


def get_raman_headers(specifications):

    if ('Raman: CPG 45+4, a.u.' in specifications):
        intensities_caption = 'CPG 45+4 a.u.'
        format_string = '%20.11f'
    elif ('Raman: CPG 45+7, a.u.' in specifications):
        intensities_caption = 'CPG 45+7 a.u.'
        format_string = '%20.11f'
    # Default in Dalton
    elif ('Raman: PCPG 45+4, Å^4/amu' in specifications):
        intensities_caption = 'PCPG 45+4 Å^4/amu'
        format_string = '%20.11f'
    elif ('Raman: PCPG 45+7, Å^4/amu' in specifications):
        intensities_caption = 'PCPG 45+7 Å^4/amu'
        format_string = '%20.11f'
    elif ('Raman: SCS 45+4, SI arb units' in specifications):
        intensities_caption = 'SCS 45+4 SI arb units'
        format_string = '%20.10E'
    elif ('Raman: SCS 45+7, SI arb units' in specifications):
        intensities_caption = 'SCS 45+7 SI arb units'
        format_string = '%20.10E'
    else:
        print('\n')
        print('Error in get_vibrational_frequencies_and_intensities ')
        print('You forgot to specify the Raman specifications')
        exit()

    return intensities_caption, format_string


def requested_unit_incident_mode(specifications, au_incident_vibration_energy):

    incident_frequencies = au_incident_vibration_energy*hartree_to_joule/plancs_constant
    incident_recp_m_wn = au_incident_vibration_energy*hartree_to_joule/(plancs_constant*speed_of_light)
    incident_recp_cm_wn = incident_recp_m_wn*1.0e-2

    if ('Vib modes: 1/m' in specifications):
        incident_mode = incident_recp_m_wn
    elif ('Vib modes: 1/cm' in specifications):
        incident_mode = incident_recp_cm_wn
    elif ('Vib modes: 1/s' in specifications):
        incident_mode = incident_frequencies
    elif ('Vib modes: Eh' in specifications):
        incident_mode = au_incident_vibration_energy

    return incident_mode


def get_raman_intensities(specifications, au_incident_vibration_energy, au_polarizability_gradients, \
                          au_vibrational_energies, print_level, temperature):

    raman_au_cpg_45_4 = combined_polarizabilites(au_polarizability_gradients, '45+4')
    raman_au_cpg_45_7 = combined_polarizabilites(au_polarizability_gradients, '45+7')

    if (print_level > 2):
        print('\n')
        print('CPG: Combined polarizability gradients a.u., input energy. ', au_incident_vibration_energy)
        print('%4s %14s %28s' %('Mode', '45+4', '45+7'))
        for j in range(len(au_vibrational_energies)):
            print('%2d %27.22f %27.22f' %(j, raman_au_cpg_45_4[j], raman_au_cpg_45_7[j]))

    # PCPG: Pseudo combined polarizability gradients
    # Units: Å**4/amu
    raman_A4amu_pcpg_45_4 = np.multiply(raman_au_cpg_45_4, (bohr_to_meter*10**(10))**4* \
                                        one_twelfth_carbon/electron_mass)
    raman_A4amu_pcpg_45_7 = np.multiply(raman_au_cpg_45_7, (bohr_to_meter*10**(10))**4* \
                                        one_twelfth_carbon/electron_mass)

    if (print_level > 2):
        print('\n')
        print('Dalton-units.  They do not quite make sense, so use only for comparison.')
        print('PCPG: Pseudo combined polarizability gradients Å^4/amu, input energy. ', \
                au_incident_vibration_energy)
        print('%4s %14s %28s' %('Mode', '45+4', '45+7'))
        for j in range(len(au_vibrational_energies)):
            print('%2d %27.22f %27.22f' %(j, raman_A4amu_pcpg_45_4[j], raman_A4amu_pcpg_45_7[j]))

    # SCS: Absolute differential scattering cross section
    raman_SI_scs_45_4 = raman_scattering_cross_section(au_polarizability_gradients, \
                                                       au_incident_vibration_energy, \
                                                       au_vibrational_energies, '45+4', \
                                                       print_level,  temperature)

    raman_SI_scs_45_7 = raman_scattering_cross_section(au_polarizability_gradients, \
                                                       au_incident_vibration_energy, \
                                                       au_vibrational_energies, '45+7', \
                                                       print_level, temperature)

    if (print_level > 2):
        print('\n')
        print('SCS: Absolute differential scattering cross section SI arbitrary units, input energy. ', \
                au_incident_vibration_energy)
        print('%4s %14s %28s' %('Mode', '45+4', '45+7'))
        for j in range(len(au_vibrational_energies)):
            print('%2d %27.18E %27.18E' %(j, raman_SI_scs_45_4[j], raman_SI_scs_45_7[j]))

    if ('Raman: CPG 45+4, a.u.' in specifications):
        raman_intensities = raman_au_cpg_45_4
    elif ('Raman: CPG 45+7, a.u.' in specifications):
        raman_intensities = raman_au_cpg_45_7
    # Default in Dalton
    elif ('Raman: PCPG 45+4, Å^4/amu' in specifications):
        raman_intensities = raman_A4amu_pcpg_45_4
    elif ('Raman: PCPG 45+7, Å^4/amu' in specifications):
        raman_intensities = raman_A4amu_pcpg_45_7
    elif ('Raman: SCS 45+4, SI arb units' in specifications):
        raman_intensities = raman_SI_scs_45_4
    elif ('Raman: SCS 45+7, SI arb units' in specifications):
        raman_intensities = raman_SI_scs_45_7
    else:
        print('\n')
        print('Error in get_vibrational_frequencies_and_intensities ')
        print('You forgot to specify the Raman specifications')
        exit()

    return raman_intensities
