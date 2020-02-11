# SpectroscPy 0.0.0
# SpectroscPy is a script package developed by and containing contributions from

    # Karen Oda Hjorth Dundas
    # Magnus Ringholm
    # Yann Cornation
    # Benedicte Ofstad

# The package is released under a LGPL licence.
# For questions, please contact on karen.o.dundas@uit.no

import numpy as np
from math import pi
import matplotlib.pyplot as plt
import copy
from .cauchy import get_gamma, get_weighted_averages, cauchy_lincomb, get_set_of_weighted_averages
from sys import exit

def get_sorted(x, y, gamma):

    new_x = np.copy(np.sort(x))
    temp_x = np.copy(new_x)
    exhange_value = 10*max(x)
    temp_old_x = np.copy(x)

    index_array = []
    for i in range(len(x)):
        for j in range(len(x)):
            if (temp_x[j] == temp_old_x[i] ):
                index_array.append(j)
                temp_old_x[i] = exhange_value
                temp_x[j] = -1*exhange_value

    new_y = np.zeros((len(x)))
    if (len(gamma) > 1):
        new_gamma = np.zeros((len(x)))

    for i in range(len(x)):
        new_y[index_array[i]] = y[i]
        if (len(gamma) > 1):
            new_gamma[index_array[i]] = gamma[i]

    if (len(gamma) == 1):
        new_gamma = []
        new_gamma.append(gamma[0])

    return new_x, new_y, new_gamma


# Expects arrays sorted based on wavenumbers
def get_zero_padded_intensities(wavenumbers, intensities, gamma, x_fit):

    padded_wavenumbers = np.append(x_fit[1:len(x_fit) - 1], wavenumbers)
    padded_intensities = np.append(np.zeros((len(x_fit) - 2)), intensities)

    if (len(gamma) > 1):
        padded_gamma = np.append(np.zeros((len(x_fit) - 2)), gamma)
    else:
        padded_gamma = []
        padded_gamma.append(gamma[0])

    sorted_padded_wavenumers, sorted_padded_intensities, sorted_padded_gamma = \
                 get_sorted(padded_wavenumbers, padded_intensities, padded_gamma)

    return sorted_padded_wavenumers, sorted_padded_intensities, sorted_padded_gamma


def get_x_fit(cauchy_type, wavenumbers, sorted_wavenumbers):

    num_snapshots = len(wavenumbers)
    num_vibrational_modes = len(wavenumbers[0])

    dist = (max(sorted_wavenumbers) - min(sorted_wavenumbers))/1.0e3

    if (num_snapshots == 1 or cauchy_type == 'WA'):
        min_dist = sorted_wavenumbers[1] - sorted_wavenumbers[0]

        for i in range(len(sorted_wavenumbers) - 1):
            if ((sorted_wavenumbers[i + 1] - sorted_wavenumbers[i]) < min_dist):
                min_dist = sorted_wavenumbers[i + 1] - sorted_wavenumbers[i]

        if (5*(max(sorted_wavenumbers) - min(sorted_wavenumbers))/min_dist > 1.0e3):
            print('get_x_fit: There are too many datapoints, so these will be reduced')
            print('This is done to avoid calculations taking impractically long')
            x_fit = np.linspace(min(sorted_wavenumbers) - 20*dist, max(sorted_wavenumbers) + 20*dist, \
                                1.04e3)
        else:
            x_fit = np.linspace(min(sorted_wavenumbers) - 20*dist, max(sorted_wavenumbers) + 20*dist, \
                                5*int((max(sorted_wavenumbers) - min(sorted_wavenumbers))/min_dist))

    else:

        x_fit = np.linspace(min(sorted_wavenumbers) - 20*dist, max(sorted_wavenumbers) + 20*dist, \
                                10*num_snapshots*num_vibrational_modes)

        # Find minimum for a specific mode
        for i in range(num_vibrational_modes):
            min_wavenumber = wavenumbers[0][i]
            max_wavenumber = wavenumbers[0][i]
            min_dist = abs(wavenumbers[1][i] - wavenumbers[0][i])

            for j in range(num_snapshots - 1):
                if (abs(wavenumbers[j + 1][i] - wavenumbers[j][i]) < min_dist):
                    min_dist = abs(wavenumbers[j + 1][i] - wavenumbers[j][i])
                if (wavenumbers[j][i] < min_wavenumber):
                    min_wavenumber = wavenumbers[j][i]
                if (wavenumbers[j][i] > max_wavenumber):
                    max_wavenumber = wavenumbers[j][i]

            x_fit = np.append(x_fit, np.linspace(min_wavenumber, max_wavenumber, \
                                                 5*int((max_wavenumber - min_wavenumber)/min_dist)))

        x_fit = np.sort(x_fit)

    return x_fit


# Both wavenumbers and intensities are 2D arrays, with first dim the number of snapshots, and then 
# each mode
# Ex. 1000 snapshots, with 6 vib modes each => 1000x6
# gamma is the broadening factor, or it's type.  Standard input would be 'Lorentz distribution'
# Ideally this routine should be tested, but the created arrays are impractically large.  All the 
# functions it is based on are however tested, so check against input values whether it makes 
# sense or not
def get_plot_values(cauchy_type, wavenumbers, intensities):

    num_peaks = len(wavenumbers)*len(wavenumbers[0])

    num_snapshots = len(wavenumbers)
    num_vibrational_modes = len(wavenumbers[0])

    check_num_peaks = 0

    min_wavenumber = wavenumbers[0][0]
    max_wavenumber = wavenumbers[0][0]

    gamma = get_gamma(cauchy_type, wavenumbers)

    avg_wavenumbers, avg_intensities = get_set_of_weighted_averages(wavenumbers, intensities)

    if (len(gamma) == 1):
        gamma_extended = [gamma[0]]
    elif (cauchy_type == 'WA'):
        gamma_extended = copy.deepcopy(gamma)
    elif (cauchy_type == 'WS'):
        gamma_extended = []

        for i in range(num_snapshots):
            for j in range(len(gamma)):
                gamma_extended.append(gamma[j])

    if (len(gamma) == 1 or cauchy_type == 'WS'):

        all_wavenumbers = np.zeros(num_peaks)
        all_intensities = np.zeros(num_peaks)

        k = 0
        for i in range(len(wavenumbers)):
            for j in range(len(wavenumbers[i])):
                check_num_peaks = check_num_peaks + 1
                all_wavenumbers[k] = copy.deepcopy(wavenumbers[i][j])
                all_intensities[k] = copy.deepcopy(intensities[i][j])
                k = k + 1

        if (num_peaks != check_num_peaks):
            print('\n')
            print('Error in get_plot_values')
            print('There are not the same vibrational modes in all the snapshots')
            exit()

    elif (cauchy_type == 'WA'):
        all_wavenumbers = np.zeros(num_vibrational_modes)
        all_intensities = np.zeros(num_vibrational_modes)

        for i in range(num_vibrational_modes):
            all_wavenumbers[i] = copy.deepcopy(avg_wavenumbers[i])
            all_intensities[i] = copy.deepcopy(avg_intensities[i])


    sorted_wavenumbers, sorted_intensities, sorted_gamma = get_sorted(all_wavenumbers, \
                                                                      all_intensities, gamma_extended)

    if (cauchy_type == 'WA'):
        x_fit = get_x_fit(cauchy_type, [avg_wavenumbers], sorted_wavenumbers)
    else:
        x_fit = get_x_fit(cauchy_type, wavenumbers, sorted_wavenumbers)

    padded_wavenumbers, padded_intensities, padded_gamma = \
                        get_zero_padded_intensities(sorted_wavenumbers, sorted_intensities, \
                                                    sorted_gamma, x_fit)

    if (cauchy_type == 'Discrete'):
        x_out = np.copy(padded_wavenumbers)
        y_out = np.copy(padded_intensities)
    else:
        y_fit = cauchy_lincomb(padded_wavenumbers, padded_intensities, padded_gamma, x_fit)
        x_out = np.copy(x_fit)
        y_out = np.copy(y_fit)

    return x_out, y_out, avg_wavenumbers, avg_intensities


# Not tested, but it doesn't really make sense to do so
def visualize_spectrum(cauchy_type, cauchy_prefactor, wavenumbers, intensities, mode_label, \
                       y_axis_label, legends, spectrum_file, spectral_boundaries, info):

    if (('IR NIMAC km/mol' in y_axis_label or 'IR NIMAC m/mol' in y_axis_label or \
         r'$A : \mathrm{m}\cdot \mathrm{mol}^{-1}$' in y_axis_label or \
         r'$A : \mathrm{km}\cdot \mathrm{mol}^{-1}$' in y_axis_label) and \
        cauchy_type != 'Discrete'):
        print('Remember that it doesnt make sense to plot Naperian integrated molar absorption')
        print('coefficients with a lineshape.  Therefore change cauchy_type to Discrete')
    if (('Raman: PCPG 45+4 Å^4*s/amu' in y_axis_label) or \
        (r'$\sigma_{45+4} : \mathrm{Å}^{4}\cdot\mathrm{s}\cdot\mathrm{amu}^{-1}$' in y_axis_label) or \
        ('Raman: PCPG 45+7 Å^4*s/amu' in y_axis_label) or \
        (r'$\sigma_{45+7} : \mathrm{Å}^{4}\cdot\mathrm{s}\cdot\mathrm{amu}^{-1}$' in y_axis_label)):
        print('Dalton-units.  They do not quite make sense, so use only for comparison.')


    line_type = ['r', 'b', 'g', 'c', 'm', 'y']
    if (len(intensities) > 6):
        print('Error in analysis')
        print('Add more line types')
        exit()

    if (len(intensities) == 1):

        x, y, avg_wavenumbers, avg_intensities = \
            get_plot_values(cauchy_type, wavenumbers, intensities[0])

        if (cauchy_type != 'Discrete'):
            y = np.multiply(y, cauchy_prefactor)

        f, ax1 = plt.subplots(figsize=(10,5))
        ax1.plot(x, y)

        ax1.set_xlabel(mode_label, fontsize=15)
        ax1.set_ylabel(y_axis_label[0], fontsize=15)

    elif (len(intensities) == 2 and not ('all one type' in info)):

        all_intensities = []

        for i in range(len(intensities)):
            x, y, avg_wavenumbers, avg_intensities = \
                   get_plot_values(cauchy_type, wavenumbers, intensities[i])

            all_intensities.append(y)

        if (cauchy_type != 'Discrete'):
            all_intensities = np.multiply(all_intensities, cauchy_prefactor)

        f, ax1 = plt.subplots(figsize=(10,5))
        l1 = ax1.plot(x, all_intensities[0], line_type[0])
        ax1.set_xlabel(mode_label, fontsize=15)

        ax1.set_ylabel(y_axis_label[0], fontsize=15)
        ax1.tick_params('y')

        ax2 = ax1.twinx()
        l2 = ax2.plot(x, all_intensities[1], line_type[1])

        ax2.set_ylabel(y_axis_label[1], fontsize=15)
        ax2.tick_params('y')

        f.legend([l1, l2], labels=legends, loc='upper center', bbox_to_anchor=(0.5, 0.9), fontsize=15)

    else:

        if ('all one type' in info):
            y_label = y_axis_label
        else:
            y_label = 'Arbitrary units'

        all_intensities = []
        for i in range(len(intensities)):
            x, y, avg_wavenumbers, avg_intensities = \
                get_plot_values(cauchy_type, wavenumbers, intensities[i])

            #max_y = max(y)
            #y = np.multiply(y, 1/max_y)
            all_intensities.append(y)

        if (cauchy_type != 'Discrete'):
            all_intensities = np.multiply(all_intensities, cauchy_prefactor)

        f, ax1 = plt.subplots(figsize=(10,5))
        for i in range(len(intensities)):
            ax1.plot(x, all_intensities[i], line_type[i], label=legends[i])

        legend = ax1.legend(loc='upper center', fontsize=15)

        ax1.set_xlabel(mode_label, fontsize=15)
        ax1.set_ylabel(y_label, fontsize=15)

    f.tight_layout()
    f.savefig(spectrum_file)

    if (spectral_boundaries != 'Keep all'):
        plt.xlim(spectral_boundaries[0], spectral_boundaries[1])
    plt.show()

    # Note that these are weighted averages
    return avg_wavenumbers, avg_intensities
