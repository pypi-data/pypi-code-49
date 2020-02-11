# SpectroscPy 0.0.0
# SpectroscPy is a script package developed by and containing contributions from

    # Karen Oda Hjorth Dundas
    # Magnus Ringholm
    # Yann Cornation
    # Benedicte Ofstad

# The package is released under a LGPL licence.
# For questions, please contact on karen.o.dundas@uit.no

# This module contains only one function, SpectroscPy_run, which is the startpoint for all the calculations

from .get_spectroscopy import get_vibrational_frequencies_and_intensities
from .plotting_module import visualize_spectrum
from .SpectroscPy_tools import check_spectroscopy_specifications_input, check_spectroscopy_types_input, \
                              check_command_input, check_cauchy_type, check_run_specification, \
                              get_mode_captions, get_ir_captions, get_raman_captions, \
                              get_cauchy_prefactor
from .cauchy import get_simple_averages
import numpy as np
from sys import exit

# File location MUST contain a backslash at the end
def SpectroscPy_run(run_specification, spectroscopy_types, spectroscopy_specifications, cauchy_type, \
                    names, spectral_boundaries, print_level, temperature):

    # run_specification is set up as follow
    # A) Is it at single or multiple snapshots? => 'Single snapshot', 'Multiple snapshots'
    # B) Do you want something plotted?  Then specify it by any combination of 'Plot IR',
    #    'Plot Raman separately', 'Plot IR and all Raman together', 'Plot Raman together',  
    #    'Plot IR and individual Raman together', 'Plot all Hyper Raman separately', 
    #    'Plot Hyper Raman VV and HV separately' or 'Plot all Hyper Raman together'.  Otherwise no plots will be created
    # C) 'FraME' or 'No FraME'
    # D) 'Outproj' or 'No outproj'
    # E) 'Symbolic labels' or nothing

    #run_specification = ['Single snapshot', ...]
    #run_specification = ['Multiple snapshots', ...]

    # spectroscopy_types specifies what spectroscopies we want, at least one of IR, Raman and Hyper Raman
    # spectroscopy_types = ['IR', 'Raman', 'Hyper Raman']

    # spectroscopy_specifications specifies the exant quantity we wish to calculuate and it's units.
    # Mandatory options IR: 'IR: SSDG, a.u.', 'IR: SSDG, C**2/kg', 'IR: SSDG, D2A2/amu', 
    # 'IR: MDAC, m**2/(s*mol)', 'IR: MDAC, L/(cm*s*mol)', 'IR: NIMAC, m/mol', 'IR: NIMAC, km/mol'
    #
    # Mandatory options Raman: 'Raman: CPG 45+4, a.u.', 'Raman: CPG 45+7, a.u.', 
    # 'Raman: PCPG 45+4, Å^4/amu', 'Raman: PCPG 45+7, Å^4/amu', 'Raman: SCS 45+4, SI arb units'
    # 'Raman: SCS 45+7, SI arb units'

    # cauchy_type specifies what type of Cauchy distribution you want, fixed gamma or width made from the
    # distribution of the snapshots.  The third option, width from snapshots and average values is not
    # available in this version.  For fixed gamma, insert 'GS' (this gives o.001*max(wavenumber)) or the
    # value that you wish.  For width determined gamma, insert 'WS'.  If single snapshot, you do not need 
    # to specify anything as fixed gamma is automatic, but you can specify a value if you wish.  Also, you
    # can choose not have a lineshape at all, through the keyword 'Discrete'

    # names contains the names and locations etc for the files.  Two different setups, either for single
    # or multiple snapshots
    # A) Single snapshot
    #    0) file location: folder where files are stored.  Must have backslash after
    #    1) rsp_tensor file
    #    2) mol file
    # B) Multiple snapshots
    #    0) file location: folder where files are stored
    #    1) start_snapshot: start number
    #    2) end_snapshot: end number
    #    3) dal name base
    #    4) mol name base
    #    5) json name base.  If FraME not used, write 'No FraME'

    # spectral_boundaries specifies the boundary of the x-axis.  If you wish to plot the whole spectrum, 
    # choose 'Keep all', otherwise specify [min_freq, max_freq]

    # print_level is a number, where 0 is default.
    # A higher number indicates a higher degree of prints, a negative number means less

    # T is temperature

    print('\n', '********************************************************************** \n')
    print('SpectroscPy is a script package developed by and containing contributions from ')
    print('    Karen Oda Hjorth Dundas')
    print('    Magnus Ringholm')
    print('    Yann Cornation')
    print('    Benedicte Ofstad')
    print('\n')
    print('The package is released under a LGPL licence')
    print('For questions, please contact on karen.o.dundas@uit.no')
    print('\n', '********************************************************************** \n')

    check_spectroscopy_types_input(spectroscopy_types)
    check_spectroscopy_specifications_input(spectroscopy_specifications)
    check_command_input(spectroscopy_types, run_specification)
    check_cauchy_type(cauchy_type, run_specification)
    check_run_specification(run_specification)

    print('Calculation')
    if ('Single snapshot' in run_specification):
        num_snapshots = 1
        print('For a single snapshot')
    elif ('Multiple snapshots' in run_specification):
        num_snapshots = names[2] - names[1] + 1
        print('For multiple snapshots:', num_snapshots)

    all_wavenumbers = []

    print('The following values will be determined')

    if ('Vib modes: 1/m' in spectroscopy_specifications):
        print('    Vibrational wavenumbers in 1/m')
    elif ('Vib modes: 1/cm' in spectroscopy_specifications):
        print('    Vibrational wavenumbers in 1/cm')
    elif ('Vib modes: 1/s' in spectroscopy_specifications):
        print('    Vibrational frequencies in 1/s')
    elif ('Vib modes: Eh' in spectroscopy_specifications):
        print('    Vibrational energies in hartree')
    else:
        print('\n')
        print('Error in SpectroscPy_run')
        print('You forgot to specify the units for vibrational modes in spectroscopy_specifications')
        exit()

    if ('IR' in spectroscopy_types):
        if ('IR: SSDG, a.u.' in spectroscopy_specifications):
            print('    Infrared SSDG (summed and squared dipole gradients) in a.u')
        elif ('IR: SSDG, C**2/kg' in spectroscopy_specifications):
            print('    Infrared SSDG (summed and squared dipole gradients) in C²/kg')
        elif ('IR: SSDG, D2A2/amu' in spectroscopy_specifications):
            print('    Infrared SSDG (summed and squared dipole gradients) in \
                   (D/Å)²/amu')
        elif ('IR: MDAC, m**2/(s*mol)' in spectroscopy_specifications):
            print('    Infrared MDAC (Molar decadic attenuated coefficient) in m²/mol, or w/o lineshape in m²/(s*mol)')
        elif ('IR: MDAC, L/(cm*s*mol)' in spectroscopy_specifications):
            print('    Infrared MDAC (Molar decadic attenuated coefficient in L/(cm*mol), or w/o lineshape in L/(cm*s*mol)')
        elif ('IR: NIMAC, m/mol' in spectroscopy_specifications):
            print('    Infrared NIMAC (Naperian integrated molar absorption coefficient) in m/mol')
        elif ('IR: NIMAC, km/mol' in spectroscopy_specifications):
            print('    Infrared NIMAC (Naperian integrated molar absorption coefficient) in km/mol')
        else:
            print('\n')
            print('Error in SpectroscPy_run')
            print('You forgot to specify the IR spectroscopy_specifications')
            exit()

        # Contains IR intensity for each snapshot => 2D
        all_ir_intensities = []

    if ('Raman' in spectroscopy_types):
        if ('Raman: CPG 45+4, a.u.' in spectroscopy_specifications):
            print('    Raman combined polarizability gradients, 45 + 4 combination rule, a.u')
        elif ('Raman: CPG 45+7, a.u.' in spectroscopy_specifications):
            print('    Raman combined polarizability gradients, 45 + 7 combination rule, a.u')
        elif ('Raman: PCPG 45+4, Å^4/amu' in spectroscopy_specifications):
            print('    Raman pseudo combined polarizability gradients, 45 + 4 combination rule, Å^4/amu')
        elif ('Raman: PCPG 45+7, Å^4/amu' in spectroscopy_specifications):
            print('    Raman pseudo combined polarizability gradients, 45 + 7 combination rule, Å^4/amu')
        elif ('Raman: SCS 45+4, SI arb units' in spectroscopy_specifications):
            print('    Absolute differential Raman scattering cross section, 45 + 4 combination rule, SI arbitrary units')
        elif ('Raman: SCS 45+7, SI arb units' in spectroscopy_specifications):
            print('    Absolute differential Raman scattering cross section, 45 + 7 combination rule, SI arbitrary units')
        else:
            print('\n')
            print('Error in SpectroscPy_run')
            print('You forgot to specify the Raman spectroscopy_specifications')
            exit()

        # Contains Raman intensities for each snapshot in each config => 3D
        all_raman_intensities = []

    if ('Hyper Raman' in spectroscopy_types):
        print('    Hyper Raman temp units')
        all_hyperraman_vv_intensities = []
        all_hyperraman_hv_intensities = []

    if ('Outproj' in run_specification):
        outproj = True
    elif ('No outproj'):
        outproj = False

    for i in range(num_snapshots):

        if (num_snapshots == 1):
            tensor_location = names[0] + names[1]
            mol_location = names[0] + names[2]
        else:

            if (print_level > 0):
                print('\n')
                print('Snapshot nr', i)

            if ('No FraME' in run_specification):
                tensor_file = names[3] + '_' + names[4] + '_' + str(i) + '.rsp_tensor'

            elif ('FraME' in run_specification):
                tensor_file = names[3] + '_' + names[4] + '_' + str(i) + '_' + names[5] + '_' + \
                              str(i) + '.rsp_tensor'

            molecule_file = names[4] + '_' + str(i) + '.mol'

            tensor_location = names[0] + tensor_file
            mol_location = names[0] + molecule_file

        # Note that raman intensities here contains all configurations.  These are to be considered as if
        # they were different properties, and therefore split up
        wavenumbers, input_raman_wavenumbers, input_hyperraman_modes, IR_intensities, raman_intensities, hyperraman_vv_intensities, hyperraman_hv_intensities = \
            get_vibrational_frequencies_and_intensities(tensor_location, mol_location, \
            spectroscopy_types, spectroscopy_specifications, print_level, temperature, outproj)

        all_wavenumbers.append(wavenumbers)

        if ('IR' in spectroscopy_types):
            all_ir_intensities.append(IR_intensities)

        if ('Raman' in spectroscopy_types):
            if (i == 0):
                num_raman_configs = len(raman_intensities)
                for i in range(num_raman_configs):
                    all_raman_intensities.append([])

            else:
                if (num_raman_configs != len(raman_intensities)):
                    print('NOT ALL rsp_tensors HAVE THE SAME AMOUNT OF GFF CONFIGS!! GO THROUGH YOUR')
                    print('.dal FILES AND CHECK THAT THEY ARE ALL IDENTICAL')

            # Reorganize to total array: num_raman_configs, num_snapshots, num_intensities
            for j in range(num_raman_configs):
                all_raman_intensities[j].append(raman_intensities[j])

        if ('Hyper Raman' in spectroscopy_types):
            if (i == 0):
                num_hyperraman_configs = len(input_hyperraman_modes)
                for i in range(num_hyperraman_configs):
                    all_hyperraman_vv_intensities.append([])
                    all_hyperraman_hv_intensities.append([])

            else:
                if (num_hyperraman_configs != len(hyperraman_vv_intensities)):
                    print('NOT ALL rsp_tensors HAVE THE SAME AMOUNT OF GFFF CONFIGS!! GO THROUGH YOUR')
                    print('.dal FILES AND CHECK THAT THEY ARE ALL IDENTICAL')

            # Reorganize to total array: num_hyperraman_configs, num_snapshots, num_intensities
            for j in range(num_hyperraman_configs):
                all_hyperraman_vv_intensities[j].append(hyperraman_vv_intensities[j])
                all_hyperraman_hv_intensities[j].append(hyperraman_hv_intensities[j])

    # AVERAGED VAULES PRINTING PART
    average_wavenumers = get_simple_averages(all_wavenumbers)
    if ('IR' in spectroscopy_types):
        average_ir_intensities = get_simple_averages(all_ir_intensities)
    if ('Raman' in spectroscopy_types):
        average_raman_intensities = np.zeros((num_raman_configs, len(wavenumbers)))
        for i in range(num_raman_configs):

            for j in range(num_snapshots):
                for k in range((len(wavenumbers))):

                    average_raman_intensities[i][k] = average_raman_intensities[i][k] + \
                                                      all_raman_intensities[i][j][k]

        average_raman_intensities = np.multiply(average_raman_intensities, 1/num_snapshots)

    if ('Hyper Raman' in spectroscopy_types):
        average_hyperraman_vv_intensities = np.zeros((num_hyperraman_configs, len(wavenumbers)))
        average_hyperraman_hv_intensities = np.zeros((num_hyperraman_configs, len(wavenumbers)))
        for i in range(num_hyperraman_configs):

            for j in range(num_snapshots):
                for k in range((len(wavenumbers))):
                    average_hyperraman_vv_intensities[i][k] = average_hyperraman_vv_intensities[i][k] + \
                                                              all_hyperraman_vv_intensities[i][j][k]
                    average_hyperraman_hv_intensities[i][k] = average_hyperraman_hv_intensities[i][k] + \
                                                              all_hyperraman_hv_intensities[i][j][k]

        average_hyperraman_vv_intensities = \
            np.multiply(average_hyperraman_vv_intensities, 1/num_snapshots)
        average_hyperraman_hv_intensities = \
            np.multiply(average_hyperraman_hv_intensities, 1/num_snapshots)

    # Set captions for graphs and tables
    mode_caption, latex_mode_caption, mode_header_sting, mode_format_string = \
        get_mode_captions(spectroscopy_specifications)

    if ('Symbolic labels' in run_specification):
        x_label = latex_mode_caption
    else:
        x_label = mode_caption

    if ('IR' in spectroscopy_types):
        IR_caption, IR_plot_caption, latex_ir_caption, header_format_string, format_string = \
            get_ir_captions(spectroscopy_specifications)

        if ('Symbolic labels' in run_specification):
            ir_y_label = latex_ir_caption
        else:
            ir_y_label = IR_plot_caption

    if ('Raman' in spectroscopy_types):
        raman_caption, raman_plot_caption, latex_raman_caption = \
            get_raman_captions(spectroscopy_specifications)

        if ('Symbolic labels' in run_specification):
            raman_y_label = latex_raman_caption
        else:
            raman_y_label = raman_plot_caption

    print('\n')
    print('********************************************************************************************')
    print('AVERAGE SPECTROSCOPIC DATA')
    if ('IR' in spectroscopy_types):
        print(('%4s' + mode_header_sting + header_format_string) %('Mode', mode_caption, IR_caption))
        for i in range(len(average_wavenumers)):
            print(('%2d' + mode_format_string + format_string) %(i, average_wavenumers[i], \
                   average_ir_intensities[i]))
        print('\n')

    if ('Raman' in spectroscopy_types):
        print(('%4s' + mode_header_sting + '%43s') %('Mode', mode_caption, raman_caption))
        print('%20s' %(' '), '\t'.join(['%9s %6.5E' % ('Input waven: ', val) for val in \
                                        input_raman_wavenumbers ]))
        for i in range(len(average_wavenumers)):
            print(('%2d' + mode_format_string) %(i, average_wavenumers[i]), '\t'.join(['%20.10E' % \
                      average_raman_intensities[j][i] for j in range(num_raman_configs)]))
        print('\n')

    if ('Hyper Raman' in spectroscopy_types):
        print(('%4s' + mode_header_sting + '%43s') %('Mode', mode_caption, 'VV Polarizes Hyper Raman'))
        print('%20s' %(' '), '\t'.join(['%9s %3.2E' % ('Input waven: ', val) for val in \
                                        input_hyperraman_modes]))
        for i in range(len(average_wavenumers)):
            print(('%2d' + mode_format_string) %(i, average_wavenumers[i]), '\t'.join(['%20.10E' % \
                    average_hyperraman_vv_intensities[j][i] for j in range(num_hyperraman_configs)]))

        print('\n')

        print(('%4s' + mode_header_sting + '%43s') %('Mode', mode_caption, 'HV Polarizes Hyper Raman'))
        print('%20s' %(' '), '\t'.join(['%9s %3.2E' % ('Input waven: ', val) for val in \
                                        input_hyperraman_modes]))
        for i in range(len(average_wavenumers)):
            print(('%2d' + mode_format_string) %(i, average_wavenumers[i]), '\t'.join(['%20.10E' % \
                   average_hyperraman_hv_intensities[j][i] for j in range(num_hyperraman_configs)]))
        print('\n')

    # PLOT
    plot_spectrum = False
    plot_commands = []
    for i in range(len(run_specification)):
        if ('Plot' in run_specification[i]):
            plot_spectrum = True
            plot_commands.append(run_specification[i])

    if (plot_spectrum):
        cauchy_prefactor = get_cauchy_prefactor(spectroscopy_specifications)

        if (cauchy_type == 'Discrete'):
            print('Only a stick spectrum of discrete peaks will be made')
            cauchy_type_or_value = cauchy_type
        elif (isinstance(cauchy_type, float) or isinstance(cauchy_type, int)):
            cauchy_type_or_value = float(cauchy_type)
            print('Fixed broadening factor, ', cauchy_type_or_value)
        elif (cauchy_type == 'WS'):
            cauchy_type_or_value = cauchy_type
            print('Width determined broadening factor')
        elif (cauchy_type == 'WA'):
            cauchy_type_or_value = cauchy_type
            print('Width determined broadening factor, but average values')
            print('\n')
            print('************************************************************')
            print('I do not know if this one works yet')
            print('************************************************************')
        else:
            cauchy_type_or_value = 0.001*max(all_wavenumbers[0])
            print('Fixed broadening factor, ', cauchy_type_or_value)


    for i in range(len(plot_commands)):
        if (('Plot IR' == plot_commands[i]) or \
            ('Plot IR and all Raman together' == plot_commands[i]) or \
            ('Plot Raman together' == plot_commands[i])):

            if ('Plot IR' == plot_commands[i]):
                print('IR spectrum')
                spectrum_file = names[0] + 'ir_spectrum.png'

                all_intensities = np.copy([all_ir_intensities])
                y_label = np.copy([ir_y_label])
                legends = 0
                plotting_info = []

            if (('Plot IR and all Raman together' == plot_commands[i]) or \
               ('Plot Raman together' == plot_commands[i])):

                legends = []

                if ('Plot IR and all Raman together' == plot_commands[i]):

                    print('IR and Raman spectrum')
                    print('Be aware that the graphs will be scaled')

                    plotting_info = []
                    if (num_raman_configs == 1):
                        # FIX this!! Should be the same as for IR and individual Raman together
                        y_label = []
                        y_label.append('IR')
                        y_label.append('Raman')
                    else:
                        y_label = []

                    all_intensities = []
                    max_ir = 0.0
                    for j in range(num_snapshots):
                        if (max(all_ir_intensities[j]) > max_ir):
                            max_ir = max(all_ir_intensities[j])

                    max_raman = 0.0
                    for j in range(num_raman_configs):
                        for k in range(num_snapshots):
                            if (max(all_raman_intensities[j][k]) > max_raman):
                                max_raman = max(all_raman_intensities[j][k])

                    all_intensities.append(np.multiply(all_ir_intensities, 1/max_ir))
                    for j in range(num_raman_configs):
                        all_intensities.append(np.multiply(all_raman_intensities[j], 1/max_raman))

                    legends.append('IR')

                    spectrum_file = names[0] + 'ir_raman_all_inp_spectrum.png'

                for j in range(num_raman_configs):
                    tmp_caption = 'Raman freq: ' + str(('%4.1E' %input_raman_wavenumbers[j]))
                    legends.append(tmp_caption)

                if ('Plot Raman together' == plot_commands[i]):
                    print('Raman spectrum')
                    print('Be aware that the graphs will be scaled')

                    spectrum_file = names[0] + 'raman_spectrum_all_inp.png'

                    all_intensities = np.copy(all_raman_intensities)
                    plotting_info = ['all one type']
                    y_label = raman_y_label


            avg_wavenumbers, avg_intensities = visualize_spectrum(cauchy_type_or_value, \
                                                                  cauchy_prefactor, \
                                                                  all_wavenumbers, \
                                                                  all_intensities, \
                                                                  x_label,  y_label, \
                                                                  legends, spectrum_file, \
                                                                  spectral_boundaries, plotting_info)


        if (('Plot IR and individual Raman together' == plot_commands[i]) or \
            ('Plot Raman separately' == plot_commands[i])):

            if ('Plot IR and individual Raman together' == plot_commands[i]):

                print('IR and individual Raman spectra')
                print('Be aware that the graphs will be scaled')

                name_base = names[0] + 'ir_raman_'

                max_ir = 0.0
                for j in range(num_snapshots):
                    if (max(all_ir_intensities[j]) > max_ir):
                        max_ir = max(all_ir_intensities[j])

            if ('Plot Raman separately' == plot_commands[i]):
                print('Individual Raman spectra')

                name_base = names[0] + 'raman_'

            for j in range(num_raman_configs):

                all_intensities = []
                y_label = []
                legends = []

                spectrum_file = name_base + str(('%4.1E' %input_raman_wavenumbers[j])) + '_spectrum.png'

                if ('Plot IR and individual Raman together' == plot_commands[i]):
                    max_raman = 0.0
                    for k in range(num_snapshots):
                        if (max(all_raman_intensities[j][k]) > max_raman):
                            max_raman = max(all_raman_intensities[j][k])

                    all_intensities.append(all_ir_intensities)
                    all_intensities.append(all_raman_intensities[j])

                    y_label.append(ir_y_label)
                    y_label.append(raman_y_label)

                    legends.append('IR')
                    legends.append('Raman')

                if ('Plot Raman separately' == plot_commands[i]):
                    print('Input wavenumber: ', input_raman_wavenumbers[j])

                    all_intensities.append(all_raman_intensities[j])
                    y_label.append(raman_y_label)
                    legends = 0

                plotting_info = []
                avg_wavenumbers, avg_intensities = visualize_spectrum(cauchy_type_or_value, \
                                                                      cauchy_prefactor, \
                                                                      all_wavenumbers, \
                                                                      all_intensities, \
                                                                      x_label,  y_label, \
                                                                      legends, spectrum_file, \
                                                                      spectral_boundaries, plotting_info)

        if ('Plot all Hyper Raman separately' == plot_commands[i]):

            for j in range(num_hyperraman_configs):
                tmp_y_label = 'Hyper Raman VV freq. ' + str(('%4.1E' %input_hyperraman_modes[j]))
                tmp_name = 'hyperraman_vv_freq_' + str(('%4.1E' %input_hyperraman_modes[j])) + '.svg'

                avg_wavenumbers, avg_intensities = \
                    visualize_spectrum(cauchy_type_or_value, cauchy_prefactor, all_wavenumbers, \
                                       [all_hyperraman_vv_intensities[j]], x_label, [tmp_y_label], [], \
                                       tmp_name, spectral_boundaries, [])

                tmp_y_label = 'Hyper Raman HV freq. ' + str(('%4.1E' %input_hyperraman_modes[j]))
                tmp_name = 'hyperraman_hv_freq_' + str(('%4.1E' %input_hyperraman_modes[j])) + '.svg'

                avg_wavenumbers, avg_intensities = \
                    visualize_spectrum(cauchy_type_or_value, cauchy_prefactor, all_wavenumbers, \
                                       [all_hyperraman_hv_intensities[j]], x_label, [tmp_y_label], [], \
                                       tmp_name, spectral_boundaries, [])

        if ('Plot Hyper Raman VV and HV separately' == plot_commands[i]):
            legends = []
            for j in range(num_hyperraman_configs):
                tmp_legend = 'Hyper Raman freq: ' + str(('%4.1E' %input_hyperraman_modes[j]))
                legends.append(tmp_legend)

            avg_wavenumbers, avg_intensities = \
                visualize_spectrum(cauchy_type_or_value, cauchy_prefactor, all_wavenumbers, \
                                   all_hyperraman_vv_intensities, x_label, \
                                   ['VV polarized hyperraman', ''], legends, 'vv_hyperraman.svg', \
                                   spectral_boundaries, [])

            avg_wavenumbers, avg_intensities = \
                visualize_spectrum(cauchy_type_or_value, cauchy_prefactor, all_wavenumbers, \
                                   all_hyperraman_hv_intensities, x_label, \
                                   ['HV polarized hyperraman', ''], legends, 'hv_hyperraman.svg', \
                                   spectral_boundaries, [])

        if ('Plot all Hyper Raman together' == plot_commands[i]):
            legends = []
            all_hyperraman_intensities = []
            for j in range(num_hyperraman_configs):
                tmp_legend = 'VV Hyper Raman freq: ' + str(('%4.1E' %input_hyperraman_modes[j]))
                legends.append(tmp_legend)
                tmp_legend = 'HV Hyper Raman freq: ' + str(('%4.1E' %input_hyperraman_modes[j]))
                legends.append(tmp_legend)

                all_hyperraman_intensities.append(all_hyperraman_vv_intensities[j])
                all_hyperraman_intensities.append(all_hyperraman_hv_intensities[j])

            avg_wavenumbers, avg_intensities = \
                visualize_spectrum(cauchy_type_or_value, cauchy_prefactor, all_wavenumbers, \
                                   all_hyperraman_intensities, x_label, 'Hyper Raman', \
                                   legends, 'all_hyperraman.svg', spectral_boundaries, ['all one type'])
