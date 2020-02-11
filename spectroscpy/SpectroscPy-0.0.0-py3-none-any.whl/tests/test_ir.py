# SpectroscPy 0.0.0
# SpectroscPy is a script package developed by and containing contributions from

    # Karen Oda Hjorth Dundas
    # Magnus Ringholm
    # Yann Cornation
    # Benedicte Ofstad

# The package is released under a LGPL licence.
# For questions, please contact on karen.o.dundas@uit.no

from spectroscpy import qi_prefactor2, summed_dip_grad_sq, get_ir_intensities
import pytest

dipole_gradient = [[-3.55354963e-03, -2.04896147e-03,  4.65337189e-04], \
                   [-1.33397762e-03,  2.30954121e-03, -1.03887613e-06], \
                   [ 5.38119485e-04, -9.34229818e-04,  5.72704375e-07], \
                   [ 2.05564469e-04,  1.21485607e-04,  5.08962422e-03], \
                   [ 4.87101901e-05, -8.45631492e-05,  7.73625610e-08], \
                   [ 4.34177615e-03, -7.53776354e-03,  4.54332159e-06]]



au_input_frequency = 0.1

au_vibrational_energies = [0.018901854754709915, 0.018867982944327566, 0.008117022651510061, \
                           0.007240633346545635, 0.006775176360266165, 0.0008338070305617636]

temperature = 298

wavenumbers = [414847.68302357, 414104.28285256, 178148.02217701, 158913.50380254, 148697.90566093,  \
               18299.94565116]

def test_summed_dip_grad_sq():

    ref_intensities = [1.7042496777884122e-05, 7.113477970612742e-06, 1.1623582609672795e-06, \
                       2.596129020443402e-05, 9.523614807165442e-09, 7.566891996343323e-05]

    intensities = summed_dip_grad_sq(dipole_gradient)

    assert len(intensities) == len(ref_intensities)

    for i in range(len(intensities)):
        assert intensities[i] == ref_intensities[i]


def test_qi_prefactor2():

    ref_qi2 = [6.74771801518888e-50, 6.759831521216551e-50, 1.5713198216234565e-49, \
               1.761508693292537e-49, 1.882524956794339e-49, 1.5296631135732734e-48]

    qi2 = qi_prefactor2(wavenumbers)

    assert len(qi2) == len(ref_qi2)

    for i in range(len(qi2)):
        assert ref_qi2[i] == qi2[i]


def test_get_ir_intensities():

    specifications = ['IR: SSDG, a.u.']
    print_level = 0

    ref_intensities = [1.70424968e-05, 7.11347797e-06, 1.16235826e-06, \
                       2.59612902e-05, 9.52361481e-09, 7.56689200e-05]


    ir_intensities, current_unit, header_format_string, format_string = \
        get_ir_intensities(specifications, dipole_gradient, print_level)

    assert len(ref_intensities) == len(ir_intensities)
    for i in range(len(ir_intensities)):
        assert ref_intensities[i] == pytest.approx(ir_intensities[i], 1.0e-83)

    assert 'SSDG, a.u.' == current_unit
    assert '%4s %15s %15s' == header_format_string
    assert '%2d %17.6f %22.17f' == format_string

    specifications = ['IR: SSDG, C**2/kg']

    ref_intensities = [4.80247389e-13, 2.00453564e-13, 3.27545622e-14, \
                       7.31573666e-13, 2.68369782e-16, 2.13230501e-12]

    ir_intensities, current_unit, header_format_string, format_string = \
        get_ir_intensities(specifications, dipole_gradient, print_level)

    assert len(ref_intensities) == len(ir_intensities)
    for i in range(len(ir_intensities)):
        assert ref_intensities[i] == pytest.approx(ir_intensities[i], 1.0e-83)

    assert 'SSDG, C**2/kg' == current_unit
    assert '%4s %15s %16s' == header_format_string
    assert '%2d %17.6f %25.20f' == format_string

    specifications = ['IR: SSDG, D2A2/amu']

    ref_intensities = [7.16729878e-01, 2.99160520e-01, 4.88835002e-02, \
                       1.09181375e+00, 4.00519910e-04, 3.18229051e+00]


    ir_intensities, current_unit, header_format_string, format_string = \
        get_ir_intensities(specifications, dipole_gradient, print_level)

    assert len(ref_intensities) == len(ir_intensities)
    for i in range(len(ir_intensities)):
        assert ref_intensities[i] == pytest.approx(ir_intensities[i], 1.0e-8)

    assert '(D/Å)**2/amu' == current_unit
    assert '%4s %15s %14s' == header_format_string
    assert '%2d %17.6f %15.10f' == format_string

    specifications = ['IR: MDAC, m**2/(s*mol)']

    ref_intensities = [1.57631148e+15, 6.57946846e+14, 1.07509991e+14, \
                       2.40123735e+15, 8.80867608e+11, 6.99884465e+15]

    ir_intensities, current_unit, header_format_string, format_string = \
        get_ir_intensities(specifications, dipole_gradient, print_level)

    assert len(ref_intensities) == len(ir_intensities)
    for i in range(len(ir_intensities)):
        assert ref_intensities[i] == pytest.approx(ir_intensities[i], 1.0e-8)

    assert 'MDAC, m**2/(s*mol)' == current_unit
    assert '%4s %15s %14s' == header_format_string
    assert '%2d %17.6f %20.1f' == format_string

    specifications = ['IR: MDAC, L/(cm*s*mol)']

    ref_intensities = [1.57631148e+14, 6.57946846e+13, 1.07509991e+13, \
                       2.40123735e+14, 8.80867608e+10, 6.99884465e+14]

    ir_intensities, current_unit, header_format_string, format_string = \
        get_ir_intensities(specifications, dipole_gradient, print_level)

    assert len(ref_intensities) == len(ir_intensities)
    for i in range(len(ir_intensities)):
        assert ref_intensities[i] == pytest.approx(ir_intensities[i], 1.0e-8)

    assert 'MDAC, L/(cm*s*mol)' == current_unit
    assert '%4s %15s %16s' == header_format_string
    assert '%2d %17.6f %20.1f' == format_string

    specifications = ['IR: NIMAC, m/mol']

    ref_intensities = [3.02861824e+04, 1.26413456e+04, 2.06562423e+03, \
                       4.61357499e+04, 1.69243943e+01, 1.34471066e+05]

    ir_intensities, current_unit, header_format_string, format_string = \
        get_ir_intensities(specifications, dipole_gradient, print_level)

    assert len(ref_intensities) == len(ir_intensities)
    for i in range(len(ir_intensities)):
        assert ref_intensities[i] == pytest.approx(ir_intensities[i], 1.0e-8)

    assert 'NIMAC, m/mol' == current_unit
    assert '%4s %15s %16s' == header_format_string
    assert '%2d %17.6f %17.8f' == format_string

    specifications = ['IR: NIMAC, km/mol']

    ref_intensities = [3.02861824e+01, 1.26413456e+01, 2.06562423e+00, \
                       4.61357499e+01, 1.69243943e-02, 1.34471066e+02]

    ir_intensities, current_unit, header_format_string, format_string = \
        get_ir_intensities(specifications, dipole_gradient, print_level)

    assert len(ref_intensities) == len(ir_intensities)
    for i in range(len(ir_intensities)):
        assert ref_intensities[i] == pytest.approx(ir_intensities[i], 1.0e-8)

    assert 'NIMAC, km/mol' == current_unit
    assert '%4s %15s %16s' == header_format_string
    assert '%2d %17.6f %17.10f' == format_string
