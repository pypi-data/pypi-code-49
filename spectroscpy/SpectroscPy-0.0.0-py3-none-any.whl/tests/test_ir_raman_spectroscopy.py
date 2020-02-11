# SpectroscPy v.3
# SpectroscPy is a script package developed by and containing contributions from

    # Karen Oda Hjorth Dundas
    # Magnus Ringholm
    # Yann Cornation
    # Benedicte Ofstad

# The package is released under a LGPL licence.
# For questions, please contact on karen.o.dundas@uit.no

from spectroscpy import get_a2_term, get_b2_term, qi_prefactor2, get_exp_denominator, \
                        raman_scattering_cross_section, summed_dip_grad_sq, combined_polarizabilites
import pytest

dipole_gradient = [[-3.55354963e-03, -2.04896147e-03,  4.65337189e-04], \
                   [-1.33397762e-03,  2.30954121e-03, -1.03887613e-06], \
                   [ 5.38119485e-04, -9.34229818e-04,  5.72704375e-07], \
                   [ 2.05564469e-04,  1.21485607e-04,  5.08962422e-03], \
                   [ 4.87101901e-05, -8.45631492e-05,  7.73625610e-08], \
                   [ 4.34177615e-03, -7.53776354e-03,  4.54332159e-06]]

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

def test_summed_dip_grad_sq():

    ref_intensities = [1.7042496777884122e-05, 7.113477970612742e-06, 1.1623582609672795e-06, \
                       2.596129020443402e-05, 9.523614807165442e-09, 7.566891996343323e-05]

    intensities = summed_dip_grad_sq(dipole_gradient)

    assert len(intensities) == len(ref_intensities)

    for i in range(len(intensities)):
        assert intensities[i] == ref_intensities[i]


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

    ref_intensities = [1.7714893192600483e-66, 7.336994814227279e-66, 3.718420917697062e-66, \
                       9.62540362865901e-67, 6.450566579365853e-66, 2.0414635630050874e-65]

    intensities = raman_scattering_cross_section(au_polarizability_gradient, au_input_frequency, \
                                                 au_vibrational_energies, raman_type, 0, temperature)

    assert len(ref_intensities) == len(intensities)

    for i in range(len(intensities)):
        assert ref_intensities[i] == intensities[i]

    raman_type = ['45+4']

    ref_intensities = [1.01228065e-66, 5.92694813e-66, 2.13692088e-66, 5.50023065e-67, \
                       5.00245158e-66, 1.16663681e-65]

    intensities = raman_scattering_cross_section(au_polarizability_gradient, au_input_frequency, \
                                                 au_vibrational_energies, raman_type, 0, temperature)

    assert len(ref_intensities) == len(intensities)

    for i in range(len(intensities)):
        assert ref_intensities[i] == pytest.approx(intensities[i],1.0e-10)


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


def test_qi_prefactor2():

    ref_qi2 = [6.74771801518888e-50, 6.759831521216551e-50, 1.5713198216234565e-49, \
               1.761508693292537e-49, 1.882524956794339e-49, 1.5296631135732734e-48]

    qi2 = qi_prefactor2(wavenumbers)

    assert len(qi2) == len(ref_qi2)

    for i in range(len(qi2)):
        assert ref_qi2[i] == qi2[i]


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
