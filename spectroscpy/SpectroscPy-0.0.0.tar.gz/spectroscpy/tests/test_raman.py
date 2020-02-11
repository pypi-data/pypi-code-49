# SpectroscPy 0.0.0
# SpectroscPy is a script package developed by and containing contributions from

    # Karen Oda Hjorth Dundas
    # Magnus Ringholm
    # Yann Cornation
    # Benedicte Ofstad

# The package is released under a LGPL licence.
# For questions, please contact on karen.o.dundas@uit.no

from spectroscpy import get_a2_term, get_b2_term, get_exp_denominator, \
                        raman_scattering_cross_section, combined_polarizabilites, \
                        requested_unit_incident_mode
import pytest

# Global test-variables
au_polarizability_gradient = [[[ 6.24435728e-02, -3.63042281e-02,  2.14401949e-02], \
                               [-3.63042281e-02, -6.26361513e-02, -3.72962095e-02], \
                               [ 2.14401949e-02, -3.72962095e-02, -9.06369159e-06]], \
                              [[ 1.25458452e-01,  5.20423355e-02,  8.34157410e-02], \
                               [ 5.20423355e-02,  6.50703815e-02,  4.80299100e-02], \
                               [ 8.34157410e-02,  4.80299100e-02,  6.96537639e-02]], \
                              [[-2.37970681e-02, -7.93763435e-03,  4.05413246e-02], \
                               [-7.93763435e-03, -1.45319888e-02,  2.33876187e-02], \
                               [ 4.05413246e-02,  2.33876187e-02,  4.94476269e-02]], \
                              [[-1.59236762e-02,  9.24345862e-03,  1.14034737e-02], \
                               [ 9.24345862e-03,  1.58998007e-02, -1.98171323e-02], \
                               [ 1.14034737e-02, -1.98171323e-02,  2.33747801e-05]], \
                              [[ 4.60303578e-03,  4.14936993e-04,  7.97344578e-03], \
                               [ 4.14936993e-04,  4.13298957e-03,  4.64696392e-03], \
                               [ 7.97344578e-03,  4.64696392e-03,  9.41809158e-02]], \
                              [[-2.45703253e-02, -4.36328512e-02, -1.21236513e-02], \
                               [-4.36328512e-02,  2.60312669e-02, -7.01564880e-03], \
                               [-1.21236513e-02, -7.01564880e-03, -2.52655827e-03]]]

au_input_frequency = 0.1

au_vibrational_energies = [0.018901854754709915, 0.018867982944327566, 0.008117022651510061, \
                           0.007240633346545635, 0.006775176360266165, 0.0008338070305617636]

temperature = 298

wavenumbers = [414847.68302357, 414104.28285256, 178148.02217701, 158913.50380254, 148697.90566093,  \
               18299.94565116]

def test_combined_polarizabilites():

    combination_type = ['45+7']
    ref_cpg = [0.14867859, 0.61365425, 0.08134748, 0.01808905, 0.11121733, 0.05762326]

    cpg = combined_polarizabilites(au_polarizability_gradient, combination_type)

    assert len(ref_cpg) == len(cpg)

    for i in range(len(cpg)):
        assert ref_cpg[i] == pytest.approx(cpg[i], 1.0e-7)

    combination_type = ['45+4']
    ref_cpg = [0.08495928, 0.49572025, 0.04674918, 0.0103366,  0.08624968, 0.03293001]

    cpg = combined_polarizabilites(au_polarizability_gradient, combination_type)

    assert len(ref_cpg) == len(cpg)

    for i in range(len(cpg)):
        assert ref_cpg[i] == pytest.approx(cpg[i], 1.0e-7)


def test_raman_scattering_cross_section():

    raman_type = ['45+7']

    ref_intensities = [1.17795838e-26, 4.87876185e-26, 2.47257775e-26, 6.40044776e-27, \
                       4.28932811e-26, 1.35747875e-25]

    intensities = raman_scattering_cross_section(au_polarizability_gradient, au_input_frequency, \
                                                 au_vibrational_energies, raman_type, 0, temperature)

    assert len(ref_intensities) == len(intensities)

    for i in range(len(intensities)):
        assert ref_intensities[i] == pytest.approx(intensities[i], 1.0e-100)

    raman_type = ['45+4']

    ref_intensities = [6.73119763e-27, 3.94114609e-26, 1.42095344e-26, 3.65739872e-27, \
                       3.32639868e-26, 7.75759466e-26]

    intensities = raman_scattering_cross_section(au_polarizability_gradient, au_input_frequency, \
                                                 au_vibrational_energies, raman_type, 0, temperature)

    assert len(ref_intensities) == len(intensities)

    for i in range(len(intensities)):
        assert ref_intensities[i] == pytest.approx(intensities[i],1.0e-100)


def test_get_exp_denominator():

    ref_exp_denominator = [0.9999999979983836, 0.9999999979252363, 0.9998161124349669, \
                           0.9995345574831861, 0.9992377998978554, 0.5866835980974099]

    exp_denominator = get_exp_denominator(wavenumbers, temperature)

    assert len(ref_exp_denominator) == len(exp_denominator)

    for i in range(len(exp_denominator)):
        assert ref_exp_denominator[i] == exp_denominator[i]

    exp_denominator = get_exp_denominator(wavenumbers, 0)

    assert len(ref_exp_denominator) == len(exp_denominator)

    for i in range(len(exp_denominator)):
        assert 1 == exp_denominator[i]


def test_get_b2_term():

    ref_b2 = [0.021239769179061247, 0.03931133318988317, 0.011532766376159364, 0.0025841499253242495, \
              0.00832255012728591, 0.008231082946554976]

    b2 = get_b2_term(au_polarizability_gradient)

    assert len(ref_b2) == len(b2)

    for i in range(len(b2)):
        assert ref_b2[i] == b2[i]


def test_get_a2_term():

    ref_a2 = [4.517730381024186e-09, 0.00752166488775672, 1.3735844316100002e-05, \
              2.785782425059312e-14, 0.0011768774195191735, 1.2617098748687706e-07]

    a2 = get_a2_term(au_polarizability_gradient)

    assert len(ref_a2) == len(a2)

    for i in range(len(a2)):
        assert ref_a2[i] == a2[i]


def test_requested_unit_incident_mode():

    specifications = ['Vib modes: 1/m']
    ref_incident_mode = 2194746.0394200613

    incident_mode = requested_unit_incident_mode(specifications, au_input_frequency)

    assert ref_incident_mode == incident_mode

    specifications = ['Vib modes: 1/cm']
    ref_incident_mode = 21947.460394200614

    incident_mode = requested_unit_incident_mode(specifications, au_input_frequency)

    assert ref_incident_mode == incident_mode

    specifications = ['Vib modes: 1/s']
    ref_incident_mode = 657968309843505.0

    incident_mode = requested_unit_incident_mode(specifications, au_input_frequency)

    specifications = ['Vib modes: Eh']

    incident_mode = requested_unit_incident_mode(specifications, au_input_frequency)

    assert au_input_frequency == incident_mode
