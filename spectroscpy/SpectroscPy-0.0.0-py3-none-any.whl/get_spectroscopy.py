# SpectroscPy 0.0.0
# SpectroscPy is a script package developed by and containing contributions from

    # Karen Oda Hjorth Dundas
    # Magnus Ringholm
    # Yann Cornation
    # Benedicte Ofstad

# The package is released under a LGPL licence.
# For questions, please contact on karen.o.dundas@uit.no

from .openrsp_tensor_reader import read_openrsp_tensor_file, rspProperty
from .vib_analysis import get_vib_harm_freqs_and_eigvecs
from .transform_nc_to_nm import transform_cartesian_to_normal, list_product_int

from .ir import get_ir_intensities
from .raman import get_raman_headers, get_raman_intensities, requested_unit_incident_mode
from .SpectroscPy_tools import check_spectroscopy_types_input
from .hyperraman import get_hyperraman_intensities

from .parameters import*
from sys import exit
import numpy as np
from math import sqrt, pi, log
import copy

def get_spectroscopy_sanity_checks(hess_index, cubic_index, quartic_index, dip_grad_index, \
                                   polariz_grad_index, hyper_polariz_grad_index, IR, Raman, \
                                   hyper_raman):
    if (hess_index == []):
        print('\n')
        print('Error in get_vibrational_frequencies_and_intensities')
        print('You forgot to calculate the hessian in your OpenRSP calculation')
        exit()
    if ((IR == True) and (dip_grad_index == [])):
        print('\n')
        print('Error in get_vibrational_frequencies_and_intensities')
        print('You asked for IR, but the dipole gradient was not calcuated in your OpenRSP calculation')
        exit()
    if ((Raman == True) and (polariz_grad_index == [])):
        print('\n')
        print('Error in get_vibrational_frequencies_and_intensities')
        print('You asked for Raman, but the polarizability gradient was not calcuated in your OpenRSP')
        print('calculation')
        exit()
    if ((hyper_raman == True) and (hyper_polariz_grad_index == [])):
        print('\n')
        print('Error in get_vibrational_frequencies_and_intensities')
        print('You asked for Hyper raman, but the hyper polarizability gradient was not calcuated in')
        print('your OpenRSP calculation')
        exit()


def which_spectroscopies_to_be_calculated(spectroscopy_types):

    IR = False
    Raman = False
    hyper_raman = False

    check_spectroscopy_types_input(spectroscopy_types)

    if ('IR' in spectroscopy_types):
        IR = True

    if ('Raman' in spectroscopy_types):
        Raman = True

    if ('Hyper Raman' in spectroscopy_types):
        hyper_raman = True

    return IR, Raman, hyper_raman


def get_spectroscopy_indices(redundant_properties, operator):

    spectroscopy_indices = []

    for i in range(len(redundant_properties)):

        if (redundant_properties[i].operator == operator):
            spectroscopy_indices.append(i)

    return spectroscopy_indices


def reduced_dims(mat_dims, remove_elms, rank_el):

    end_dims = []
    for i in range(len(mat_dims) - rank_el):
        end_dims.append(mat_dims[i] - remove_elms)

    for i in range(rank_el):
        end_dims.append(mat_dims[len(mat_dims) - rank_el + i])

    end_dims = tuple(end_dims)

    return end_dims


def getting_the_subblocks(larger_mat, remove_elms, out_mat, offset, rank_el):

    dims = np.shape(larger_mat)
    if (len(dims) - rank_el == 1):
        smaller_mat = larger_mat[0:(list(dims))[0] - remove_elms]
        smaller_mat = np.reshape(smaller_mat, list_product_int(np.shape(smaller_mat)))
        out_mat[offset:offset + len(smaller_mat)] = smaller_mat
        offset = offset + len(smaller_mat)

    else:
        for i in range(list(dims)[0] - remove_elms):
            offset = getting_the_subblocks(larger_mat[i], remove_elms, out_mat, offset, rank_el)
    return offset


def get_energy_derivatives(index, tensors, redundant_properties, rank_geo, rank_el, num_coordinates, \
                           vib_degrees_of_freedom, transformation_matrix):

    energy_derivatives = []

    for i in range(len(index)):
        temp = transform_cartesian_to_normal(tensors[index[i]], \
                                             redundant_properties[index[i]].components, rank_geo, \
                                             num_coordinates, vib_degrees_of_freedom, \
                                             transformation_matrix)

        end_dims = reduced_dims(np.shape(temp), num_coordinates - vib_degrees_of_freedom, rank_el)

        if (np.shape(temp) != end_dims):

            offset = 0
            vib_temp = np.zeros(list_product_int(end_dims))

            getting_the_subblocks(temp, num_coordinates - vib_degrees_of_freedom, vib_temp, offset, \
                                  rank_el)

            vib_temp = np.reshape(vib_temp, end_dims)
            energy_derivatives.append(vib_temp)

        else:
            energy_derivatives.append(temp)

    return energy_derivatives


def get_vibrational_frequencies_and_intensities(tensor_file, molecule_file, spectroscopy_types, \
                                                specifications, print_level, temperature, outproj):

    # For IR and Raman we need GG, GF, GFF

    IR, Raman, hyper_raman = which_spectroscopies_to_be_calculated(spectroscopy_types)

    redundant_properties, tensors = read_openrsp_tensor_file(tensor_file)
    hess_index = []
    cubic_index = []
    quartic_index = []
    dip_grad_index = []
    polariz_grad_index = []
    hyper_polariz_grad_index = []

    ## Find the property GG.  This is your hessian, to be done vib analysis on
    hess_index = get_spectroscopy_indices(redundant_properties, hess_operator)

    # Find the properties you are looking for
    if (IR == True):
        dip_grad_index = get_spectroscopy_indices(redundant_properties, dip_grad_operator)
    if (Raman == True):
        polariz_grad_index = get_spectroscopy_indices(redundant_properties, polariz_grad_operator)
    if (hyper_raman == True):
        hyper_polariz_grad_index = get_spectroscopy_indices(redundant_properties, \
                                                            hyper_polariz_grad_operator)

    get_spectroscopy_sanity_checks(hess_index, cubic_index, quartic_index, dip_grad_index, \
                                   polariz_grad_index, hyper_polariz_grad_index, IR, Raman, \
                                   hyper_raman)

    hess = tensors[hess_index[0]]

    # num_coordinates = 3N = total degrees of freedom
    au_vibrational_energies, transformation_matrix, num_coordinates = \
        get_vib_harm_freqs_and_eigvecs(molecule_file, hess, outproj, print_level)

    if (print_level > 0):
        print('\n')
        print('The harmonic frequencies have been calcuated from the molecular hessian')

    vibrational_frequencies = au_vibrational_energies*hartree_to_joule/plancs_constant
    recp_m_wavenumbers = au_vibrational_energies*hartree_to_joule/ \
                                 (plancs_constant*speed_of_light)
    recp_cm_wavenumbers = recp_m_wavenumbers*1.0e-2

    if ('Vib modes: 1/m' in specifications):
        vib_mode = recp_m_wavenumbers
    elif ('Vib modes: 1/cm' in specifications):
        vib_mode = recp_cm_wavenumbers
    elif ('Vib modes: 1/s' in specifications):
        vib_mode = vibrational_frequencies
    elif ('Vib modes: Eh' in specifications):
        vib_mode = au_vibrational_energies
    else:
        print('\n')
        print('Error in get_vibrational_frequencies_and_intensities')
        print('You forgot to specify the units for vibrational modes in specifications')
        exit()

    if (print_level > 1):
        print('\n')
        print('Vibrational modes')
        print('%4s %19s %17s %25s %22s' %('Mode', 'Energies a.u.', 'Frequencies 1/s', \
                                          'Wavenumbers 1/m', 'Wavenumbers 1/cm'))
        for i in range(len(au_vibrational_energies)):
            print('%2d %20.14f %20.3f %25.14f %25.14f' %(i, au_vibrational_energies[i], \
                   vibrational_frequencies[i],  recp_m_wavenumbers[i], recp_cm_wavenumbers[i]))

    # Use the info from the vib analysis to transfor all tensors to normal coordinates
    if (IR == True):
        dipole_gradient = get_energy_derivatives(dip_grad_index, tensors, redundant_properties, \
                                                 1, 1, num_coordinates, \
                                                 len(au_vibrational_energies), transformation_matrix)

        if (len(dipole_gradient) > 1):
            print('\n')
            print('Error in get_vibrational_frequencies_and_intensities')
            print('It doesnt make sense to have more than one configuration for the dipole gradient')
            print('Something is strange with your OpenRSP tensor file')
            exit()

        if (print_level > 1):
            print('\n')
            print('Dipole gradient a.u.')
            for i in range(len(dipole_gradient[0])):
                print('%2d' %(i), '\t'.join(['%24.18f' % val for val in dipole_gradient[0][i]]))

        ir_intensities, current_unit, header_format_string, format_string = \
            get_ir_intensities(specifications, dipole_gradient[0], print_level)


        if (print_level > 0):
            print('\n')
            print('IR intensities in', current_unit)
            print(header_format_string %('Mode', 'Wavenumbers', 'Intensities'))
            for i in range(len(au_vibrational_energies)):
                print(format_string %(i, vib_mode[i], ir_intensities[i]))

    else:
        ir_intensities = ['You did not ask for IR intensities']

    if (Raman == True):

        au_polarizability_gradients = get_energy_derivatives(polariz_grad_index, tensors, \
                                                             redundant_properties, 1, 2, \
                                                             num_coordinates, \
                                                             len(au_vibrational_energies), \
                                                             transformation_matrix)

        raman_intensities = []
        input_raman_modes = []

        for i in range(len(polariz_grad_index)):

            au_incident_vibration_energy = abs(redundant_properties[polariz_grad_index[i]].frequencies[2])

            if (print_level > 0):
                print('\n')
                print('Calculating new Raman configuration, input frequency (au): ', \
                      au_incident_vibration_energy)

            if ((i > 0) and (au_incident_vibration_energy == old_incident_energy)):
                if (print_level > 0):
                    print('This configuration has already been calcuated, skip to next')
            else:

                if (print_level > 1):
                    print('Polarizability gradient in atomic units')
                    print('%4s %12s %15s %22s' %('Mode', 'x', 'y', 'z'))
                    for j in range(len(au_polarizability_gradients[i])):
                        for k in range(len(au_polarizability_gradients[i][j])):
                            if (k == 0):
                                print('%2d %3s' %(j, 'x'), '\t'.join(['%16.10f' % val for val in \
                                      au_polarizability_gradients[i][j][k]]))
                            elif (k == 1):
                                print('%2s %3s' %(' ', 'y'), '\t'.join(['%16.10f' % val for val in \
                                      au_polarizability_gradients[i][j][k]]))
                            elif (k == 2):
                                print('%2s %3s' %(' ', 'z'), '\t'.join(['%16.10f' % val for val in \
                                      au_polarizability_gradients[i][j][k]]))

                incident = requested_unit_incident_mode(specifications, au_incident_vibration_energy)
                temp_raman_intensities = \
                    get_raman_intensities(specifications, au_incident_vibration_energy, \
                                          au_polarizability_gradients[i], au_vibrational_energies, \
                                          print_level, temperature)

                input_raman_modes.append(incident)
                raman_intensities.append(temp_raman_intensities)

                old_incident_energy = copy.deepcopy(au_incident_vibration_energy)

        if (print_level > 0):
            intensities_caption, format_string = get_raman_headers(specifications)

            print('\n')
            print('Raman intensities in', intensities_caption)
            print('%4s %14s %35s' %('Mode', 'Wavenumbers', 'Intensities'))
            print('%20s' %(' '), '\t'.join(['%9s %6.5E' % ('Input waven: ', val) for val in \
                  input_raman_modes]))
            for i in range(len(recp_m_wavenumbers)):
                print('%2d %16.6f' %(i, recp_m_wavenumbers[i]), '\t'.join([format_string % \
                      raman_intensities[j][i] for j in range(len(raman_intensities))]))

    else:
        raman_intensities = ['You did not ask for Raman intensities']
        input_raman_modes = ['You did not ask for Raman intensities']

    if (hyper_raman == True):

        # Has three input frequencies per configuration, where the first is the negative sum of the 
        # two other.  I assume that the input frequency we are looking for is the summed one
        au_hyper_polarizability_gradients = get_energy_derivatives(hyper_polariz_grad_index, tensors, \
                                                                   redundant_properties, 1, \
                                                                   3, num_coordinates, \
                                                                   len(au_vibrational_energies), \
                                                                   transformation_matrix)

        hyperraman_vv_intensities = []
        hyperraman_hv_intensities = []
        input_hyperraman_modes = []
        old_incident_energy = []

        for i in range(len(hyper_polariz_grad_index)):
            # FIX: unit considerations
            au_incident_vibration_energy = \
                abs(redundant_properties[hyper_polariz_grad_index[i]].frequencies[1])

            if (print_level > 0):
                print('\n')
                print('Calculating new hyperraman configuration, input frequency (au): ', \
                      au_incident_vibration_energy)

            if ((i > 0) and (au_incident_vibration_energy in old_incident_energy)):
                if (print_level > 0):
                    print('This configuration has already been calcuated, skip to next')
            else:

                incident = requested_unit_incident_mode(specifications, au_incident_vibration_energy)
                hyperraman_scs_SI_vv, hyperraman_scs_SI_hv = \
                    get_hyperraman_intensities(au_incident_vibration_energy, au_vibrational_energies, \
                    au_hyper_polarizability_gradients[i], temperature)

                input_hyperraman_modes.append(incident)
                hyperraman_vv_intensities.append(hyperraman_scs_SI_vv)
                hyperraman_hv_intensities.append(hyperraman_scs_SI_hv)

                old_incident_energy.append(au_incident_vibration_energy)

    else:
        hyperraman_vv_intensities = ['You did not ask for Hyper Raman intensities']
        hyperraman_hv_intensities = ['You did not ask for Hyper Raman intensities']
        input_hyperraman_modes = ['You did not ask for Hyper Raman intensities']

    return vib_mode, input_raman_modes, input_hyperraman_modes, ir_intensities, raman_intensities, \
           hyperraman_vv_intensities, hyperraman_hv_intensities
