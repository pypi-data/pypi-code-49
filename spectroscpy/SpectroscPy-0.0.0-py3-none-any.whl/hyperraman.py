# SpectroscPy 0.0.0
# SpectroscPy is a script package developed by and containing contributions from

    # Karen Oda Hjorth Dundas
    # Magnus Ringholm
    # Yann Cornation
    # Benedicte Ofstad

# The package is released under a LGPL licence.
# For questions, please contact on karen.o.dundas@uit.no

import numpy as np
from .parameters import*
from math import sqrt, pi
from .raman import get_exp_denominator

# Independent of units
def get_average_beta_aaa2(beta_grad):

    beta_aaa2 = np.zeros((len(beta_grad)))

    for i in range(len(beta_grad)):
        tmp = 0
        for j in range(3):
            tmp = tmp + beta_grad[i][j][j][j]**2

        beta_aaa2[i] = beta_aaa2[i] + (1/7)*tmp

        tmp = 0
        for j in range(3):
            for k in range(3):
                if (k != j):
                    beta_aaa = beta_grad[i][j][j][j]
                    beta_aab = beta_grad[i][j][j][k]
                    beta_abb = beta_grad[i][j][k][k]
                    beta_baa = beta_grad[i][k][j][j]
                    beta_bba = beta_grad[i][k][k][j]
                    tmp = tmp + 4*beta_aab**2 + 2*beta_aaa*beta_abb + 4*beta_baa*beta_aab + \
                                4*beta_aaa*beta_bba + beta_baa**2

        beta_aaa2[i] = beta_aaa2[i] + (1/35)*tmp

        tmp = 0
        for j in range(3):#a
            for k in range(3): #b
                if (k != j):
                    for l in range(3): # g
                        if (l != k):
                            beta_aab = beta_grad[i][j][j][k]
                            beta_abb = beta_grad[i][j][k][k]
                            beta_abg = beta_grad[i][j][k][l]
                            beta_baa = beta_grad[i][k][j][j]
                            beta_bag = beta_grad[i][k][j][l]
                            beta_bgg = beta_grad[i][k][l][l]
                            beta_ggb = beta_grad[i][l][l][k]

                            tmp = tmp + 4*beta_aab*beta_bgg + beta_baa*beta_bgg + \
                                        4*beta_aab*beta_ggb + 2*beta_abg**2 + 4*beta_abg*beta_bag

        beta_aaa2[i] = beta_aaa2[i] + (1/105)*tmp

    return beta_aaa2


# Independent of units
def get_average_beta_baa2(beta_grad):

    beta_baa2 = np.zeros((len(beta_grad)))

    for i in range(len(beta_grad)):
        tmp = 0
        for j in range(3):
            tmp = tmp + beta_grad[i][j][j][j]**2

        beta_baa2[i] = beta_baa2[i] + (1/35)*tmp

        tmp = 0
        for j in range(3): #a
            for k in range(3): #b
                if (k != j):
                    beta_aaa = beta_grad[i][j][j][j]
                    beta_aab = beta_grad[i][j][j][k]
                    beta_abb = beta_grad[i][j][k][k]
                    beta_baa = beta_grad[i][k][j][j]
                    beta_bba = beta_grad[i][k][k][j]

                    tmp = tmp + 4*beta_aaa*beta_abb + 8*beta_aab**2 - 6*beta_aaa*beta_bba + \
                                beta_abb**2 - 6*beta_aab*beta_baa

        beta_baa2[i] = beta_baa2[i] + (1/105)*tmp

        tmp = 0
        for j in range(3): #a
            for k in range(3): #b
                if (k != j):
                    for l in range(3):
                        if (l != k):
                            beta_aab = beta_grad[i][j][j][k]
                            beta_aag = beta_grad[i][j][j][l]
                            beta_abb = beta_grad[i][j][k][k]
                            beta_abg = beta_grad[i][j][k][l]
                            beta_agg = beta_grad[i][j][l][l]
                            beta_bag = beta_grad[i][k][j][l]
                            beta_bbg = beta_grad[i][k][k][l]
                            beta_bgg = beta_grad[i][k][l][l]

                            tmp = tmp + 3*beta_abb*beta_agg - 2*beta_aag*beta_bbg - \
                                        2*beta_aab*beta_bgg + 6*beta_abg**2 - 2*beta_abg*beta_bag

        beta_baa2[i] = beta_baa2[i] + (1/105)*tmp

    return beta_baa2


# Scattering cross section.  au in, SI out
def get_hyperraman_SI_scs(au_incident_e, au_vib_e, au_beta2, T):

    SI_beta2 = np.multiply(au_beta2, (hartree_to_coulomb**6*bohr_to_meter**4/ \
                           hartree_to_joule**4*electron_mass))

    SI_incident_wn = au_incident_e*hartree_to_joule/(plancs_constant*speed_of_light)
    SI_wn = np.multiply(au_vib_e, hartree_to_joule/(plancs_constant*speed_of_light))

    sigma = np.zeros(len(SI_beta2))

    exp_denom = get_exp_denominator(SI_wn, T)

    for i in range(len(sigma)):
        sigma[i] = (2*SI_incident_wn - SI_wn[i])**4*SI_beta2[i]/(SI_wn[i]*exp_denom[i])

    sigma = np.multiply(sigma, 2*pi**2*plancs_constant*speed_of_light**3)

    return sigma


def get_hyperraman_intensities(au_incident_vibration_energy, au_vibrational_energies, au_beta_gradients, \
                               T):

    beta_aaa2 = get_average_beta_aaa2(au_beta_gradients)
    beta_baa2 = get_average_beta_baa2(au_beta_gradients)

    sigma_vv = get_hyperraman_SI_scs(au_incident_vibration_energy, au_vibrational_energies, beta_aaa2, T)
    sigma_hv = get_hyperraman_SI_scs(au_incident_vibration_energy, au_vibrational_energies, beta_baa2, T)

    return sigma_vv, sigma_hv
