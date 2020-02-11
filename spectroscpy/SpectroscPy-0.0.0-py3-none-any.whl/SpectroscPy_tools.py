# SpectroscPy 0.0.0
# SpectroscPy is a script package developed by and containing contributions from

    # Karen Oda Hjorth Dundas
    # Magnus Ringholm
    # Yann Cornation
    # Benedicte Ofstad

# The package is released under a LGPL licence.
# For questions, please contact on karen.o.dundas@uit.no

# Used to check validity of inputs, and also to make sense of the inputs
from sys import exit
from math import pi
from .parameters import speed_of_light, plancs_constant, hartree_to_joule

def check_spectroscopy_specifications_input(spectroscopy_specifications):

    ir_counter = 0
    raman_counter = 0

    if ('IR: SSDG, a.u.' in spectroscopy_specifications):
        ir_counter = ir_counter + 1
    elif ('IR: SSDG, C**2/kg' in spectroscopy_specifications):
        ir_counter = ir_counter + 1
    elif ('IR: SSDG, D2A2/amu' in spectroscopy_specifications):
        ir_counter = ir_counter + 1
    elif ('IR: MDAC, m**2/(s*mol)' in spectroscopy_specifications):
        ir_counter = ir_counter + 1
    elif ('IR: MDAC, L/(cm*s*mol)' in spectroscopy_specifications):
        ir_counter = ir_counter + 1
    elif ('IR: NIMAC, m/mol' in spectroscopy_specifications):
        ir_counter = ir_counter + 1
    elif ('IR: NIMAC, km/mol' in spectroscopy_specifications):
        ir_counter = ir_counter + 1

    if ('Raman: 45+7' in spectroscopy_specifications):
        raman_counter = raman_counter + 1
    elif ('Raman: 45+4' in spectroscopy_specifications):
        raman_counter = raman_counter + 1

    if (ir_counter > 1):
        print('\n')
        print('**********************************************************************************')
        print('MORE THAN ONE IR UNIT CHOSEN')
        print('We only calculate for one unit at a time.  Please remove all but one option from')
        print('spectroscopy_specifications')
        print('If you are uncertain how to do this check out the documentation or the top description')
        print('in SpectroscPy_wrapper.py')
        print('**********************************************************************************')
        exit()
    elif (raman_counter > 1):
        print('\n')
        print('**********************************************************************************')
        print('MORE THAN ONE RAMAN COMBINATION TYP CHOSEN')
        print('We only calculate for one Raman combination at a time.  Please remove all but one')
        print('option from spectroscopy_specifications')
        print('If you are uncertain how to do this check out the documentation or the top description')
        print('in SpectroscPy_wrapper.py')
        print('**********************************************************************************')
        exit()

def check_spectroscopy_types_input(spectroscopy_types):
    if (spectroscopy_types == []):
        print('\n')
        print('**********************************************************************************')
        print('NO SPECTROSCOPIES SPECIFIED')
        print('Specify IR or Raman in spectroscopy_types')
        print('If you are uncertain how to do this check out README or the top description in')
        print('SpectroscPy_wrapper.py')
        print('**********************************************************************************')
        exit()


def check_command_input(spectroscopy_types, run_specification):
    if (not 'IR' in spectroscopy_types and 'Plot IR' in run_specification):
        print('\n')
        print('**********************************************************************************')
        print('ILLEGAL VALUE/PLOT REQUEST')
        print('You have not requested to calculate IR values, but to still to plot them.  This doesnt')
        print('make sense.  Please choose to calculate IR before you plot the values')
        print('**********************************************************************************')
        exit()

    if ((not 'Raman' in spectroscopy_types and 'Plot Raman separately' in run_specification) or \
        (not 'Raman' in spectroscopy_types and 'Plot Raman together' in run_specification)):
        print('\n')
        print('**********************************************************************************')
        print('ILLEGAL VALUE/PLOT REQUEST')
        print('You have not requested to calculate Raman values, but to still to plot them.  This')
        print('doesnt make sense.  Please choose to calculate Raman before you plot the values')
        print('**********************************************************************************')
        exit()

    if (((not 'IR' in spectroscopy_types) or (not 'Raman' in spectroscopy_types)) and \
        ('Plot IR and individual Raman together' in run_specification)):
        print('\n')
        print('**********************************************************************************')
        print('ILLEGAL VALUE/PLOT REQUEST')
        print('You have not requested to calculate IR and Raman values, but to still to plot them.')
        print('This doesnt make sense.  Please choose to calculate IR and Raman before you plot the')
        print('values')
        print('**********************************************************************************')
        exit()

    if (((not 'IR' in spectroscopy_types) or (not 'Raman' in spectroscopy_types)) and \
        ('Plot IR and all Raman together' in run_specification)):
        print('\n')
        print('**********************************************************************************')
        print('ILLEGAL VALUE/PLOT REQUEST')
        print('You have not requested to calculate IR and Raman values, but to still to plot them.')
        print('This doesnt make sense.  Please choose to calculate IR and Raman before you plot the')
        print('values')
        print('**********************************************************************************')
        exit()


def check_cauchy_type(cauchy_type, run_specification):

    if (('Single snapshot' in run_specification) and (cauchy_type == 'WS' or cauchy_type == 'WA')):
        print('\n')
        print('**********************************************************************************')
        print('ILLEGAL cauchy_type REQUEST')
        print('It does not make sense to use the width determined gamma for a single snapshot.')
        print('Choose your desiered cauchy_type or leave cauchy_type input blank for default')
        print('0.001*max(wavenumber) value for cauchy_type')
        print('**********************************************************************************')
        exit()

    if (cauchy_type == 'WA'):
        print('**********************************************************************************')
        print('\n')
        print('The WA option for cauchy_type is not yet debugged.  Please choose one of the other')
        print('options available.')
        print('**********************************************************************************')
        exit()


def check_run_specification(run_specification):

    if ((not 'Single snapshot' in run_specification) and (not 'Multiple snapshots' in \
         run_specification)):
        print('\n')
        print('**********************************************************************************')
        print('Error in check_run_specification')
        print('You must specify if this calculation is for a single or multiple snapshots')
        print('If you are uncertain how to do this check out the documentation or the top description')
        print('in SpectroscPy_wrapper.py')
        exit()

    if ((not 'FraME' in run_specification) and (not 'No FraME' in run_specification)):
        print('\n')
        print('**********************************************************************************')
        print('Error in check_run_specification')
        print('You must specify if this calculation should use FraME or not')
        print('If you are uncertain how to do this check out the documentation or the top description')
        print('in SpectroscPy_wrapper.py')
        exit()

    if ((not 'Outproj' in run_specification) and (not 'No outproj' in run_specification)):
        print('\n')
        print('**********************************************************************************')
        print('Error in check_run_specification')
        print('You must specify if rotional and translational modes should be projected out or not')
        print('If you are uncertain how to do this check out the documentation or the top description')
        print('in SpectroscPy_wrapper.py')
        exit()


def get_mode_captions(spectroscopy_specifications):

    if ('Vib modes: 1/m' in spectroscopy_specifications):
        mode_caption = 'Wavenumber 1/m'
        latex_mode_caption = r'$\bar{v}: \mathrm{m}^{-1}$'
        mode_header_sting = '%18s'
        mode_format_string = '%19.6f'
    elif ('Vib modes: 1/cm' in spectroscopy_specifications):
        mode_caption = 'Wavenumber 1/cm'
        latex_mode_caption = r'$\bar{v}: \mathrm{cm}^{-1}$'
        mode_header_sting = '%18s'
        mode_format_string = '%19.6f'
    elif ('Vib modes: 1/s' in spectroscopy_specifications):
        mode_caption = 'Frequency 1/s'
        latex_mode_caption = r'$v: \mathrm{s}^{-1}$'
        mode_header_sting = '%17s'
        mode_format_string = '%20.9E'
    elif ('Vib modes: Eh' in spectroscopy_specifications):
        mode_caption = 'Vib energy Eh'
        latex_mode_caption = r'$E: \mathrm{E}_h$'
        mode_header_sting = '%17s'
        mode_format_string = '%20.9E'
    else:
        print('\n')
        print('Error in get_mode_captions')
        print('You forgot to specify the units for vibrational modes in spectroscopy_specifications')
        exit()

    return mode_caption, latex_mode_caption, mode_header_sting, mode_format_string


def get_ir_captions(spectroscopy_specifications):

    if ('IR: SSDG, a.u.' in spectroscopy_specifications):
        IR_caption = 'IR SSDG a.u'
        IR_plot_caption = IR_caption
        latex_ir_caption = r'$\bar{\mu}_g : a.u.$'
        header_format_string = ' %15s'
        format_string = '%20.10E'
    elif ('IR: SSDG, C**2/kg' in spectroscopy_specifications):
        IR_caption = 'IR SSDG C²/kg'
        IR_plot_caption = IR_caption
        latex_ir_caption = r'$\bar{\mu}_g : \mathrm{C}^2\cdot \mathrm{kg}^{-1}$'
        header_format_string = '%16s'
        format_string = '%20.10E'
    elif ('IR: SSDG, D2A2/amu' in spectroscopy_specifications):
        IR_caption = 'IR SSDG (D/Å)²/amu'
        IR_plot_caption = IR_caption
        latex_ir_caption = r'$\bar{\mu}_g : (\mathrm{D}/\mathrm{Å})^2\cdot \mathrm{amu}^{-1}$'
        header_format_string = '%20s'
        format_string = '%17.10f'
    elif ('IR: MDAC, m**2/(s*mol)' in spectroscopy_specifications):
        IR_caption = 'IR MDAC m²/(s*mol)'
        IR_plot_caption = 'IR MDAC m²/mol'
        latex_ir_caption = r'$\varepsilon : \mathrm{m}^2\cdot \mathrm{mol}^{-1}$'
        header_format_string = '%22s'
        format_string = '%20.10E'
    elif ('IR: MDAC, L/(cm*s*mol)' in spectroscopy_specifications):
        IR_caption = 'IR MDAC L/(s*cm*mol)'
        IR_plot_caption = 'IR MDAC L/(cm*mol)'
        latex_ir_caption = r'$\varepsilon : \mathrm{L}\cdot \mathrm{cm}^{-1}\mathrm{mol}^{-1}$'
        header_format_string = '%24s'
        format_string = '%22.10E'
    elif ('IR: NIMAC, m/mol' in spectroscopy_specifications):
        IR_caption = 'IR NIMAC m/mol'
        IR_plot_caption = IR_caption
        latex_ir_caption = r'$A : \mathrm{m}\cdot \mathrm{mol}^{-1}$'
        header_format_string = '%16s'
        format_string = '%17.8f'
    elif ('IR: NIMAC, km/mol' in spectroscopy_specifications):
        IR_caption = 'IR NIMAC km/mol'
        IR_plot_caption = IR_caption
        latex_ir_caption = r'$A : \mathrm{km}\cdot \mathrm{mol}^{-1}$'
        header_format_string = '%18s'
        format_string = '%17.10f'
    else:
        print('\n')
        print('Error in get_ir_captions')
        print('You forgot to specify the IR spectroscopy_specifications')
        exit()

    return IR_caption, IR_plot_caption, latex_ir_caption, header_format_string, format_string


def get_raman_captions(spectroscopy_specifications):

    if ('Raman: CPG 45+4, a.u.' in spectroscopy_specifications):
        raman_caption = 'Raman: CPG 45+4 a.u.'
        raman_plot_caption = raman_caption
        latex_raman_caption = r'$\bar{\alpha}_{g, 45+4} : a.u.$'
    elif ('Raman: CPG 45+7, a.u.' in spectroscopy_specifications):
        raman_caption = 'Raman: CPG 45+7 a.u.'
        raman_plot_caption = raman_caption
        latex_raman_caption = r'$\bar{\alpha}_{g, 45+7} : a.u.$'
    # Default in Dalton, but quite artificial
    elif ('Raman: PCPG 45+4, Å^4/amu' in spectroscopy_specifications):
        raman_caption = 'Raman: PCPG 45+4 Å^4/amu'
        raman_plot_caption = 'Raman: PCPG 45+4 Å^4*s/amu'
        latex_raman_caption = r'$\sigma_{45+4}^{\prime} : \mathrm{Å}^{4}\cdot\mathrm{s}\cdot\mathrm{amu}^{-1}$'
    elif ('Raman: PCPG 45+7, Å^4/amu' in spectroscopy_specifications):
        raman_caption = 'Raman: PCPG 45+7 Å^4/amu'
        raman_plot_caption = 'Raman: PCPG 45+7 Å^4*s/amu'
        latex_raman_caption = r'$\sigma_{45+7}^{\prime} : \mathrm{Å}^{4}\cdot\mathrm{s}\cdot\mathrm{amu}^{-1}$'
    elif ('Raman: SCS 45+4, SI arb units' in spectroscopy_specifications):
        raman_caption = 'Raman: SCS 45+4 C^4*s^2/(J*m^2*kg)'
        raman_plot_caption = 'Raman: SCS 45+4 C^4*s^3/(J*m^2*kg)'
        latex_raman_caption = r'$\sigma_{45+4}^{\prime} : \mathrm{C}^{4}\cdot\mathrm{s}^3\cdot\mathrm{J}^{-1}\cdot\mathrm{m}^{-2}\cdot\mathrm{kg}^{-1}$'
    elif ('Raman: SCS 45+7, SI arb units' in spectroscopy_specifications):
        raman_caption = 'Raman: SCS 45+7 C^4*s^2/(J*m^2*kg)'
        raman_plot_caption = 'Raman: SCS 45+7 C^4*s^3/(J*m^2*kg)'
        latex_raman_caption = r'$\sigma_{45+7}^{\prime} : \mathrm{C}^{4}\cdot\mathrm{s}^3\cdot\mathrm{J}^{-1}\cdot\mathrm{m}^{-2}\cdot\mathrm{kg}^{-1}$'
    else:
        print('\n')
        print('Error in get_raman_captions')
        print('You forgot to specify the Raman spectroscopy_specifications')
        exit()

    return raman_caption, raman_plot_caption, latex_raman_caption


def get_cauchy_prefactor(spectroscopy_specifications):

    if ('Vib modes: 1/m' in spectroscopy_specifications):
        cauchy_prefactor = 1/(2*pi*speed_of_light)
    elif ('Vib modes: 1/cm' in spectroscopy_specifications):
        cauchy_prefactor = 1/(2*pi*speed_of_light)*100
    elif ('Vib modes: 1/s' in spectroscopy_specifications):
        cauchy_prefactor = 1/(2*pi)
    elif ('Vib modes: Eh' in spectroscopy_specifications):
        cauchy_prefactor = plancs_constant*hartree_to_joule/(2*pi)
    else:
        print('\n')
        print('Error in get_cauchy_prefactor')
        print('You forgot to specify the units for vibrational modes in spectroscopy_specifications')
        exit()

    return cauchy_prefactor
