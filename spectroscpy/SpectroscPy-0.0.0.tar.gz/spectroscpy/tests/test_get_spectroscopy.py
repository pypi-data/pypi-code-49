# SpectroscPy 0.0.0
# SpectroscPy is a script package developed by and containing contributions from

    # Karen Oda Hjorth Dundas
    # Magnus Ringholm
    # Yann Cornation
    # Benedicte Ofstad

# The package is released under a LGPL licence.
# For questions, please contact on karen.o.dundas@uit.no

# Test get_spectroscopy

from spectroscpy import which_spectroscopies_to_be_calculated, get_spectroscopy_indices, \
                        get_energy_derivatives, get_vibrational_frequencies_and_intensities, \
                        read_openrsp_tensor_file, rspProperty, reduced_dims, getting_the_subblocks
from spectroscpy.parameters import*
import pytest
import os
import numpy as np

num_coordinates = 12
vib_degrees_of_freedom = 6

transformation_matrix = [[-1.53222366e-02, -1.53669898e-02,  3.22981029e-03,  4.17339750e-03, \
                          -4.03628935e-04, \
                          -8.54362584e-04, -1.61101304e-03,  7.11046382e-04,  7.11046382e-04, -2.69284905e-03, \
                           3.66800068e-03, -3.29058085e-03], \
                         [-4.88454619e-04, -6.26091008e-04, -2.86856327e-04,  9.19391511e-04,  5.97284973e-04, \
                           1.58823725e-02,  7.38452498e-04, -1.27867893e-03, -1.27867893e-03,  5.88922522e-03, \
                          -9.41504666e-03,  1.13685751e-02], \
                         [-4.54192168e-03, -4.36068046e-03, -1.50488550e-02, -1.51582564e-02, -3.00715954e-03, \
                           3.65915247e-04,  1.59820255e-05, -9.02891936e-04, -9.02891936e-04, -2.12606041e-03, \
                          -9.12185034e-04,  7.08979866e-04], \
                         [-8.12088770e-03,  8.23711336e-03, -1.38024626e-03,  2.89722027e-03, -3.15677778e-04, \
                          -1.33095836e-02,  5.49364785e-03,  1.32649051e-03,  1.32649051e-03, -6.70530881e-04, \
                          -4.08694673e-03,  6.11322887e-03], \
                         [-1.30330778e-02,  1.29622284e-02, -2.92412439e-03,  3.13500942e-03,  6.51580289e-04, \
                           8.70769925e-03,  2.84197888e-03, -1.02092330e-03, -1.02092330e-03, -2.09321016e-03, \
                           4.32044798e-03, -5.86075083e-03], \
                         [-4.54112268e-03,  4.34618821e-03,  1.50507111e-02, -1.51597014e-02,  3.00626318e-03, \
                          -3.80756323e-04, -5.68500175e-03, -1.42660735e-03, -1.42660735e-03, -3.56032980e-04, \
                          -1.02787417e-03,  1.07596757e-03], \
                         [ 5.11949910e-04, -5.26040912e-04,  1.11679672e-03,  1.44609648e-04, -1.70604131e-04, \
                           9.86304207e-04,  1.21121509e-03, -1.52042468e-03, -1.52042468e-03, -4.17812568e-03, \
                           3.63473835e-03, -3.45181715e-03], \
                         [ 8.20763158e-04, -8.20829942e-04,  7.77635542e-04, -7.65522454e-04, -1.48224540e-04, \
                          -4.63682087e-04,  3.98948691e-03,  1.72597918e-04,  1.72597918e-04,  4.97545185e-04, \
                          -6.13731827e-04,  2.95535526e-04], \
                         [ 2.86187731e-04, -3.45501477e-04, -6.03883325e-04,  9.55520115e-04,  4.06140688e-03, \
                          -1.10939379e-04, -1.30743314e-03,  2.44103733e-04,  2.44103733e-04, -1.52164634e-03, \
                          -6.75471940e-04,  5.12251411e-04], \
                         [ 9.65179963e-04,  9.75287920e-04, -1.23333606e-03, -5.90122822e-04,  2.15926991e-04, \
                          -9.38468797e-05, -9.57684851e-04,  4.80562923e-04,  4.80562923e-04, -2.77223894e-03, \
                           3.30819645e-03, -2.87764630e-03], \
                         [ 3.12162608e-05,  4.35411808e-05, -5.75314576e-04,  5.10058350e-04,  6.95346793e-05, \
                          -1.08571590e-03, -2.49791511e-03, -4.24312198e-03, -4.24312198e-03,  1.23211573e-03, \
                          -2.40047149e-04, -5.97994640e-05], \
                         [ 2.86126606e-04,  3.46414621e-04,  6.03766372e-04,  9.54786739e-04, -4.06135040e-03, \
                           1.11874502e-04, -1.84475586e-03,  1.97047095e-04,  1.97047095e-04, -1.35446823e-03, \
                          -6.85897044e-04,  5.46328295e-04]]

ref_dipole_gradient = \
      [[[-3.55354959e-03, -2.04896144e-03,  4.65337226e-04],
       [-1.33397761e-03,  2.30954119e-03, -1.03887733e-06],
       [ 5.38119487e-04, -9.34229819e-04,  5.72701937e-07],
       [ 2.05564456e-04,  1.21485597e-04,  5.08962420e-03],
       [ 4.87101890e-05, -8.45631462e-05,  7.73668483e-08],
       [ 4.34177613e-03, -7.53776352e-03,  4.54332299e-06]]]

ref_polarizability_gradient = \
     [[[[ 6.04610202e-02, -3.51511055e-02,  2.05867010e-02],
        [-3.51511055e-02, -6.06465271e-02, -3.58100073e-02],
        [ 2.05867010e-02, -3.58100073e-02, -8.24129166e-06]],
       [[ 1.20853575e-01,  4.99878490e-02,  7.95877729e-02],
        [ 4.99878490e-02,  6.28477170e-02,  4.58251237e-02],
        [ 7.95877729e-02,  4.58251237e-02,  6.62798317e-02]],
       [[-2.34431047e-02, -7.82917443e-03,  4.02920687e-02],
        [-7.82917443e-03, -1.43042013e-02,  2.32435281e-02],
        [ 4.02920687e-02,  2.32435281e-02,  4.87524759e-02]],
       [[-1.55313827e-02,  9.01591539e-03,  1.14149851e-02],
        [ 9.01591539e-03,  1.55074857e-02, -1.98366345e-02],
        [ 1.14149851e-02, -1.98366345e-02,  2.34202541e-05]],
       [[ 4.39674438e-03,  4.92827640e-04,  7.19780552e-03],
        [ 4.92827640e-04,  3.83525060e-03,  4.19756005e-03],
        [ 7.19780552e-03,  4.19756005e-03,  8.94657717e-02]],
       [[-2.41613385e-02, -4.31408089e-02, -1.19041040e-02],
        [-4.31408089e-02,  2.58697434e-02, -6.88886076e-03],
        [-1.19041040e-02, -6.88886076e-03, -2.42915073e-03]]], 
       [[[ 6.04610200e-02, -3.51511054e-02,  2.05867014e-02],
        [-3.51511054e-02, -6.06465273e-02, -3.58100074e-02],
        [ 2.05867014e-02, -3.58100074e-02, -8.24116238e-06]],
       [[ 1.20853575e-01,  4.99878487e-02,  7.95877733e-02],
        [ 4.99878487e-02,  6.28477171e-02,  4.58251237e-02],
        [ 7.95877733e-02,  4.58251237e-02,  6.62798311e-02]],
       [[-2.34431046e-02, -7.82917446e-03,  4.02920685e-02],
        [-7.82917446e-03, -1.43042012e-02,  2.32435281e-02],
        [ 4.02920685e-02,  2.32435281e-02,  4.87524752e-02]],
       [[-1.55313822e-02,  9.01591527e-03,  1.14149849e-02],
        [ 9.01591527e-03,  1.55074855e-02, -1.98366344e-02],
        [ 1.14149849e-02, -1.98366344e-02,  2.34202945e-05]],
       [[ 4.39674437e-03,  4.92827626e-04,  7.19780546e-03],
        [ 4.92827626e-04,  3.83525056e-03,  4.19755994e-03],
        [ 7.19780546e-03,  4.19755994e-03,  8.94657709e-02]],
       [[-2.41613390e-02, -4.31408092e-02, -1.19041042e-02],
        [-4.31408092e-02,  2.58697431e-02, -6.88886095e-03],
        [-1.19041042e-02, -6.88886095e-03, -2.42915100e-03]]], 
       [[[ 6.24435726e-02, -3.63042282e-02,  2.14401945e-02],
        [-3.63042282e-02, -6.26361513e-02, -3.72962094e-02],
        [ 2.14401945e-02, -3.72962094e-02, -9.06377656e-06]],
       [[ 1.25458452e-01,  5.20423354e-02,  8.34157406e-02],
        [ 5.20423354e-02,  6.50703814e-02,  4.80299099e-02],
        [ 8.34157406e-02,  4.80299099e-02,  6.96537637e-02]],
       [[-2.37970681e-02, -7.93763434e-03,  4.05413248e-02],
        [-7.93763434e-03, -1.45319890e-02,  2.33876188e-02],
        [ 4.05413248e-02,  2.33876188e-02,  4.94476269e-02]],
       [[-1.59236762e-02,  9.24345865e-03,  1.14034738e-02],
        [ 9.24345865e-03,  1.58998009e-02, -1.98171324e-02],
        [ 1.14034738e-02, -1.98171324e-02,  2.33748102e-05]],
       [[ 4.60303582e-03,  4.14937046e-04,  7.97344582e-03],
        [ 4.14937046e-04,  4.13298957e-03,  4.64696407e-03],
        [ 7.97344582e-03,  4.64696407e-03,  9.41809158e-02]],
       [[-2.45703252e-02, -4.36328511e-02, -1.21236513e-02],
        [-4.36328511e-02,  2.60312669e-02, -7.01564868e-03],
        [-1.21236513e-02, -7.01564868e-03, -2.52655828e-03]]]]

ref_hyper_polarizability_gradient = \
   [[[[[ 0.17587778,  0.1214237 ,  0.08764675],
         [ 0.1214237 ,  0.05715179,  0.05813472],
         [ 0.08764675,  0.05813472,  0.11869238]],
        [[ 0.12073663,  0.05836342,  0.05814728],
         [ 0.05836342,  0.01349165,  0.02034769],
         [ 0.05814728,  0.02034769,  0.0683274 ]],
        [[ 0.08949794,  0.05549355,  0.12084899],
         [ 0.05549355,  0.02521763,  0.06959147],
         [ 0.12084899,  0.06959147,  0.09086193]]],
       [[[-0.04149689, -0.0020507664841713656, -0.01116578],
         [-0.0020507664841713656,  0.04832673,  0.004006105523379081],
         [-0.01116578,  0.004006105523379081,  0.020458075246416445]],
        [[-0.004209771173609765,  0.04709664481317306,  0.00873144669066752],
         [ 0.04709664481317306, -0.007923226252559392,  0.01092292449656617],
         [ 0.00873144669066752,  0.01092292449656617, -0.0350074 ]],
        [[-0.021367294719130257,  0.012261967604661726,  0.030426775150505916],
         [ 0.012261967604661726,  0.02108574280390427, -0.05242135],
         [ 0.030426775150505916, -0.05242135,  0.0012440929778656231]]],
       [[[ 0.03412447, -0.010090768115349858, -0.013081175990389961],
         [-0.010090768115349858, -0.0165402 ,  0.002712436142715228],
         [-0.013081175990389961,  0.002712436142715228, -0.0241171 ]],
        [[-0.00512432, -0.01367083,  0.01252866],
         [-0.01367083, -0.0255157 ,  0.01323414],
         [ 0.01252866,  0.01323414,  0.04212922]],
        [[-0.02267988,  0.0133447 ,  0.00397849],
         [ 0.0133447 ,  0.02291822, -0.00672098],
         [ 0.00397849, -0.00672098,  0.00244773]]],
       [[[-0.05680783, -0.03500606,  0.04772037],
         [-0.03500606, -0.01960747,  0.01488809],
         [ 0.04772037,  0.01488809,  0.12578315]],
        [[-0.0357841 , -0.01825808,  0.01488111],
         [-0.01825808, -0.00815919,  0.03052813],
         [ 0.01488111,  0.03052813,  0.07259695]],
        [[ 0.04357009,  0.01111845,  0.12415317],
         [ 0.01111845,  0.0307047 ,  0.07167396],
         [ 0.12415317,  0.07167396,  0.10158605]]],
       [[[ 0.00998428, -0.00389458,  0.01114878],
         [-0.00389458, -0.00297943, -0.00816592],
         [ 0.01114878, -0.00816592,  0.01372287]],
        [[-0.00227564, -0.0020425 , -0.00469732],
         [-0.0020425 , -0.00997192, -0.0111154 ],
         [-0.00469732, -0.0111154 , -0.02371718]],
        [[ 0.00842858, -0.00482389,  0.02074203],
         [-0.00482389, -0.00838164, -0.03594238],
         [ 0.02074203, -0.03594238,  0.00066928]]],
       [[[ 0.20734257, -0.06173008,  0.07437265],
         [-0.06173008, -0.06981042, -0.04407297],
         [ 0.07437265, -0.04407297,  0.0354464 ]],
        [[-0.05814701, -0.06776477, -0.04182602],
         [-0.06776477, -0.17969909, -0.07398054],
         [-0.04182602, -0.07398054, -0.06144632]],
        [[ 0.08397181, -0.04848373,  0.03428225],
         [-0.04848373, -0.08345295, -0.05937212],
         [ 0.03428225, -0.05937212, -0.00022920269966851883 ]]]], 
        [[[[ 0.15032497,  0.10886933,  0.07699703],
         [ 0.10886933,  0.04959019,  0.05005866],
         [ 0.07699703,  0.05005866,  0.10123878]],
        [[ 0.10886933,  0.04959019,  0.05005866],
         [ 0.04959019,  0.00639102,  0.01911525],
         [ 0.05005866,  0.01911525,  0.05830806]],
        [[ 0.07699703,  0.05005866,  0.10123878],
         [ 0.05005866,  0.01911525,  0.05830806],
         [ 0.10123878,  0.05830806,  0.07297953]]],
       [[[-0.02841494, -0.00516954, -0.01017341],
         [-0.00516954,  0.04020646,  0.00586081],
         [-0.01017341,  0.00586081,  0.02213489]],
        [[-0.00516954,  0.04020646,  0.00586081],
         [ 0.04020646, -0.01521534,  0.01004565],
         [ 0.00586081,  0.01004565, -0.03804587]],
        [[-0.01017341,  0.00586081,  0.02213489],
         [ 0.00586081,  0.01004565, -0.03804587],
         [ 0.02213489, -0.03804587,  0.0008717338493781023]]],
       [[[ 0.03993635, -0.00820047, -0.0179262 ],
         [-0.00820047, -0.02095479,  0.01048564],
         [-0.0179262 ,  0.01048564, -0.01141521]],
        [[-0.00820047, -0.02095479,  0.01048564],
         [-0.02095479, -0.0245979 ,  0.01810307],
         [ 0.01048564,  0.01810307,  0.01989428]],
        [[-0.0179262 ,  0.01048564, -0.01141521],
         [ 0.01048564,  0.01810307,  0.01989428],
         [-0.01141521,  0.01989428,  0.0014796063067753448]]],
       [[[-0.05381275, -0.03338372,  0.04564154],
         [-0.03338372, -0.01772252,  0.01130176],
         [ 0.04564154,  0.01130176,  0.11214544]],
        [[-0.03338372, -0.01772252,  0.01130176],
         [-0.01772252, -0.0077297 ,  0.03259076],
         [ 0.01130176,  0.03259076,  0.06473155]],
        [[ 0.04564154,  0.01130176,  0.11214544],
         [ 0.01130176,  0.03259076,  0.06473155],
         [ 0.11214544,  0.06473155,  0.09810841]]],
       [[[ 0.01011243, -0.0031187149510231295,  0.00933912],
         [-0.0031187149510231295, -0.00301255, -0.00537947],
         [ 0.00933912, -0.00537947,  0.01489873]],
        [[-0.0031187149510231295, -0.00301255, -0.00537947],
         [-0.00301255, -0.00925884, -0.00931122],
         [-0.00537947, -0.00931122, -0.02583531]],
        [[ 0.00933912, -0.00537947,  0.01489873],
         [-0.00537947, -0.00931122, -0.02583531],
         [ 0.01489873, -0.02583531,  0.0004224694615169236]]],
       [[[ 0.17437904, -0.05244226,  0.06356234],
         [-0.05244226, -0.05429012, -0.03677508],
         [ 0.06356234, -0.03677508,  0.02778907]],
        [[-0.05244226, -0.05429012, -0.03677508],
         [-0.05429012, -0.15579895, -0.06334062],
         [-0.03677508, -0.06334062, -0.04824893]],
        [[ 0.06356234, -0.03677508,  0.02778907],
         [-0.03677508, -0.06334062, -0.04824893],
         [ 0.02778907, -0.04824893, -0.00020926632642968992]]]], 
        [[[[ 0.17587778,  0.1214237 ,  0.08764675],
         [ 0.1214237 ,  0.05715179,  0.05813472],
         [ 0.08764675,  0.05813472,  0.11869238]],
        [[ 0.12073663,  0.05836342,  0.05814728],
         [ 0.05836342,  0.01349165,  0.02034769],
         [ 0.05814728,  0.02034769,  0.0683274 ]],
        [[ 0.08949794,  0.05549355,  0.12084899],
         [ 0.05549355,  0.02521763,  0.06959147],
         [ 0.12084899,  0.06959147,  0.09086193]]],
       [[[-0.04149689, -0.0020507664841713656, -0.01116578],
         [-0.0020507664841713656,  0.04832673,  0.004006105523379081],
         [-0.01116578,  0.004006105523379081,  0.020458075246416445]],
        [[-0.004209771173609765,  0.04709664481317306,  0.00873144669066752],
         [ 0.04709664481317306, -0.007923226252559392,  0.01092292449656617],
         [ 0.00873144669066752,  0.01092292449656617, -0.0350074 ]],
        [[-0.021367294719130257,  0.012261967604661726,  0.030426775150505916],
         [ 0.012261967604661726,  0.02108574280390427, -0.05242135],
         [ 0.030426775150505916, -0.05242135,  0.0012440929778656231]]],
       [[[ 0.03412447, -0.010090768115349858, -0.013081175990389961],
         [-0.010090768115349858, -0.0165402 ,  0.002712436142715228],
         [-0.013081175990389961,  0.002712436142715228, -0.0241171 ]],
        [[-0.00512432, -0.01367083,  0.01252866],
         [-0.01367083, -0.0255157 ,  0.01323414],
         [ 0.01252866,  0.01323414,  0.04212922]],
        [[-0.02267988,  0.0133447 ,  0.00397849],
         [ 0.0133447 ,  0.02291822, -0.00672098],
         [ 0.00397849, -0.00672098,  0.00244773]]],
       [[[-0.05680783, -0.03500606,  0.04772037],
         [-0.03500606, -0.01960747,  0.01488809],
         [ 0.04772037,  0.01488809,  0.12578315]],
        [[-0.0357841 , -0.01825808,  0.01488111],
         [-0.01825808, -0.00815919,  0.03052813],
         [ 0.01488111,  0.03052813,  0.07259695]],
        [[ 0.04357009,  0.01111845,  0.12415317],
         [ 0.01111845,  0.0307047 ,  0.07167396],
         [ 0.12415317,  0.07167396,  0.10158605]]],
       [[[ 0.00998428, -0.00389458,  0.01114878],
         [-0.00389458, -0.00297943, -0.00816592],
         [ 0.01114878, -0.00816592,  0.01372287]],
        [[-0.00227564, -0.0020425 , -0.00469732],
         [-0.0020425 , -0.00997192, -0.0111154 ],
         [-0.00469732, -0.0111154 , -0.02371718]],
        [[ 0.00842858, -0.00482389,  0.02074203],
         [-0.00482389, -0.00838164, -0.03594238],
         [ 0.02074203, -0.03594238,  0.00066928]]],
       [[[ 0.20734257, -0.06173008,  0.07437265],
         [-0.06173008, -0.06981042, -0.04407297],
         [ 0.07437265, -0.04407297,  0.0354464 ]],
        [[-0.05814701, -0.06776477, -0.04182602],
         [-0.06776477, -0.17969909, -0.07398054],
         [-0.04182602, -0.07398054, -0.06144632]],
        [[ 0.08397181, -0.04848373,  0.03428225],
         [-0.04848373, -0.08345295, -0.05937212],
         [ 0.03428225, -0.05937212, -0.00022920269966851883 ]]]]]

def test_get_vibrational_frequencies_and_intensities():

    data_dir = '{0}/'.format(os.path.dirname(__file__))
    tensor_file = data_dir + 'hf_H2O2.rsp_tensor'
    mol_file = data_dir + 'H2O2.mol'

    # IR SSDG a.u. and Raman SCS 45 + 7 SI
    spectroscopy_type = ['IR', 'Raman']
    specifications = ['Vib modes: 1/m', 'IR: SSDG, a.u.', 'Raman: SCS 45+7, SI arb units']

    ref_wavenumbers = [414847.6830235662, 414104.2828525629, 178148.02217701354, 158913.5038025385, \
                       148697.90566093015, 18299.94565115991]

    ref_input_wavenumers = [0.0, 2194746.0394200613]
    ref_hyperraman_freq = ['You did not ask for Hyper Raman intensities']

    ref_ir_intensities = [1.70424946e-05, 7.11347711e-06, 1.16235812e-06, 2.59612870e-05, \
                          9.52361364e-09, 7.56689106e-05]

    ref_raman_intensities = [[4.879651346429856e-69, 1.973451994999927e-68, 2.2210970132851823e-70, \
                              3.5094085168284385e-71, 1.620940819715544e-70, 9.964856453902808e-74], \
                             [1.7714893117801702e-66, 7.33699479385739e-66, 3.718420769767595e-66, \
                              9.62540320983724e-67, 6.450566292861606e-66, 2.0414633627821737e-65]]
    ref_hyperraman = ['You did not ask for Hyper Raman intensities']

    w, iw, ih, ii, ri, hvvi, hhvi = \
        get_vibrational_frequencies_and_intensities(tensor_file, mol_file, spectroscopy_type, \
                                                    specifications, 0, 298, True)

    assert len(ref_wavenumbers) == len(w) == len(ii) == len(ri[0])
    assert len(ref_input_wavenumers) == len(iw) == len(ri)

    for i in range(len(w)):
        assert ref_wavenumbers[i] == pytest.approx(w[i], 10e-9)
        assert ref_ir_intensities[i] == pytest.approx(ii[i], 10e3)

    for i in range(len(iw)):
        assert ref_input_wavenumers[i] == iw[i]

    for i in range(len(ri)):
        for j in range(len(ri[0])):
            assert ref_raman_intensities[i][j] == pytest.approx(ri[i][j], 10e-83)

    assert ih ==  ref_hyperraman_freq == ref_hyperraman

    # No outproj
    spectroscopy_type = ['IR']
    specifications = ['Vib modes: 1/m', 'IR: SSDG, a.u.']

    ref_wavenumbers = [(4.14848132e+05   +0.j), (4.14105192e+05   +0.j),
                       (1.78147036e+05   +0.j),         (1.58912905e+05   +0.j),
                       (1.48698110e+05   +0.j),         (1.83061036e+04   +0.j),
                       (4.66792909e+02   +0.j),         (2.28608186e+02   +0.j),
                       (3.76592066e+00   +0.j),         (1.78308846e+00   +0.j),
                       (2.00676340e-16   +3.27729334j), (6.82319818e-14+1114.31282585j)]

    ref_ir_intensities = [1.70425815e-05, 7.11360916e-06, 1.16243696e-06, 2.59611627e-05,
                          9.52928458e-09, 7.56686604e-05, 4.15214594e-06, 1.41336245e-09,
                          1.03022827e-14, 6.28763989e-14, 6.88801500e-14, 2.09588423e-05]


    w, iw, ih, ii, ri, hvvi, hhvi = \
        get_vibrational_frequencies_and_intensities(tensor_file, mol_file, spectroscopy_type, \
                                                    specifications, 0, 298, False)
    assert len(ref_wavenumbers) == len(w) == len(ii)

    for i in range(len(w)):
        assert ref_wavenumbers[i] == pytest.approx(w[i], 1.0e-8)
        assert ref_ir_intensities[i] == pytest.approx(ii[i], 1.0e-83)

    # No IR and Raman SCS 45 + 4 SI
    spectroscopy_type = ['Raman']
    specifications = ['Vib modes: 1/m', 'Raman: SCS 45+4, SI arb units']

    ref_ir_intensities = ['You did not ask for IR intensities']
    ref_raman_intensities = [[2.78837502e-69, 1.59599832e-68, 1.27642348e-70, 2.00537634e-71, \
                              1.25718780e-70, 5.69440074e-74], [1.01228064e-66, 5.92694812e-66, \
                              2.13692079e-66, 5.50023041e-67, 5.00245135e-66, 1.16663670e-65]]

    w, iw, ih, ii, ri, hvvi, hhvi = \
        get_vibrational_frequencies_and_intensities(tensor_file, mol_file, spectroscopy_type, \
                                                    specifications, 0, 298, True)

    for i in range(len(ri)):
        for j in range(len(ri[0])):
            assert ref_raman_intensities[i][j] == pytest.approx(ri[i][j], 1.0e-83)

    assert ref_ir_intensities == ii

    # No IR, Raman CPG 45+4, a.u.
    specifications = ['Vib modes: 1/m', 'Raman: CPG 45+4, a.u.']
    ref_raman_intensities = [[0.07930255, 0.45635755, 0.0458494 , 0.01015121, 0.07769959, \
                              0.03215856], [0.08495927, 0.49572019, 0.04674917, 0.0103366 , \
                              0.08624967, 0.03293001]]

    w, iw, ih, ii, ri, hvvi, hhvi = \
        get_vibrational_frequencies_and_intensities(tensor_file, mol_file, spectroscopy_type, \
                                                    specifications, 0, 298, True)

    for i in range(len(ri)):
        for j in range(len(ri[0])):
            assert ref_raman_intensities[i][j] == pytest.approx(ri[i][j], 1.0e-6)

    assert ref_ir_intensities == ii

    # No IR, Raman CPG 45+7, a.u.
    specifications = ['Vib modes: 1/m', 'Raman: CPG 45+7, a.u.']
    ref_raman_intensities = [[0.13877932, 0.56428613, 0.07978227, 0.01776461, 0.10018108, \
                              0.05627554], [0.14867857, 0.61365418, 0.08134747, 0.01808905, \
                              0.11121732, 0.05762325]]


    w, iw, ih, ii, ri, hvvi, hhvi = \
        get_vibrational_frequencies_and_intensities(tensor_file, mol_file, spectroscopy_type, \
                                                    specifications, 0, 298, True)

    for i in range(len(ri)):
        for j in range(len(ri[0])):
            assert ref_raman_intensities[i][j] == pytest.approx(ri[i][j], 1.0e-6)

    assert ref_ir_intensities == ii

    # No IR, Raman PCPG 45+4, Å^4/amu
    specifications = ['Vib modes: 1/m', 'Raman: PCPG 45+4, Å^4/amu']
    ref_raman_intensities = [[11.33579065, 65.23338327,  6.55387684,  1.45104975, 11.10665772, \
                              4.59686046], [12.14438241, 70.86002056,  6.68249426,  1.47755042, \
                              12.32883741, 4.70713297]]



    w, iw, ih, ii, ri, hvvi, hhvi = \
        get_vibrational_frequencies_and_intensities(tensor_file, mol_file, spectroscopy_type, \
                                                    specifications, 0, 298, True)

    for i in range(len(ri)):
        for j in range(len(ri[0])):
            assert ref_raman_intensities[i][j] == pytest.approx(ri[i][j], 1.0e-8)

    assert ref_ir_intensities == ii

    # No IR, Raman PCPG 45+7, Å^4/amu
    specifications = ['Vib modes: 1/m', 'Raman: PCPG 45+7, Å^4/amu']
    ref_raman_intensities = [[19.83761352, 80.66108141, 11.40436285,  2.53933706, 14.32024325, \
                              8.04422734], [21.25264742, 87.71792697, 11.6280985 ,  2.58571323, \
                              15.89780238, 8.236874  ]]



    w, iw, ih, ii, ri, hvvi, hhvi = \
        get_vibrational_frequencies_and_intensities(tensor_file, mol_file, spectroscopy_type, \
                                                    specifications, 0, 298, True)

    for i in range(len(ri)):
        for j in range(len(ri[0])):
            assert ref_raman_intensities[i][j] == pytest.approx(ri[i][j], 1.0e-8)

    assert ref_ir_intensities == ii

    # IR SSDG C²/kg, No Raman
    specifications = ['Vib modes: 1/m', 'IR: SSDG, C**2/kg']
    spectroscopy_type = ['IR']

    ref_ir_intensities = [4.80247329e-13, 2.00453540e-13, 3.27545582e-14, 7.31573576e-13, \
                          2.68369749e-16, 2.13230475e-12]

    ref_input_wavenumers = ['You did not ask for Raman intensities']
    ref_raman_intensities = ['You did not ask for Raman intensities']

    w, iw, ih, ii, ri, hvvi, hhvi = \
        get_vibrational_frequencies_and_intensities(tensor_file, mol_file, spectroscopy_type, \
                                                    specifications, 0, 298, True)

    assert len(ref_ir_intensities) == len(ii)

    for i in range(len(ii)):
        assert ref_ir_intensities[i] == pytest.approx(ii[i], 10e-9)

    assert ref_input_wavenumers == iw == ri

    # IR SSDG (D/Å)²/amu
    specifications = ['Vib modes: 1/m', 'IR: SSDG, D2A2/amu']
    spectroscopy_type = ['IR']

    ref_ir_intensities = [7.16729788e-01, 2.99160484e-01, 4.88834942e-02, 1.09181362e+00, \
                          4.00519861e-04, 3.18229012e+00]

    w, iw, ih, ii, ri, hvvi, hhvi = \
        get_vibrational_frequencies_and_intensities(tensor_file, mol_file, spectroscopy_type, \
                                                    specifications, 0, 298, True)

    assert len(ref_ir_intensities) == len(ii)

    for i in range(len(ii)):
        assert ref_ir_intensities[i] == pytest.approx(ii[i], 10e-9)

    # IR MDAC m²/(s*mol)
    specifications = ['Vib modes: 1/m', 'IR: MDAC, m**2/(s*mol)']
    spectroscopy_type = ['IR']

    ref_ir_intensities = [1.57631129e+15, 6.57946767e+14, 1.07509978e+14, 2.40123706e+15, \
                          8.80867500e+11, 6.99884379e+15]

    w, iw, ih, ii, ri, hvvi, hhvi = \
        get_vibrational_frequencies_and_intensities(tensor_file, mol_file, spectroscopy_type, \
                                                    specifications, 0, 298, True)

    assert len(ref_ir_intensities) == len(ii)

    for i in range(len(ii)):
        assert ref_ir_intensities[i] == pytest.approx(ii[i], 10e-9)

    # IR MDAC L/(cm*s*mol)
    specifications = ['Vib modes: 1/m', 'IR: MDAC, L/(cm*s*mol)']
    spectroscopy_type = ['IR']

    ref_ir_intensities = [1.57631129e+14, 6.57946767e+13, 1.07509978e+13, 2.40123706e+14, \
                          8.80867500e+10, 6.99884379e+14]

    w, iw, ih, ii, ri, hvvi, hhvi = \
        get_vibrational_frequencies_and_intensities(tensor_file, mol_file, spectroscopy_type, \
                                                    specifications, 0, 298, True)

    assert len(ref_ir_intensities) == len(ii)

    for i in range(len(ii)):
        assert ref_ir_intensities[i] == pytest.approx(ii[i], 10e-9)

    # IR NIMAC m/mol
    specifications = ['Vib modes: 1/m', 'IR: NIMAC, m/mol']
    spectroscopy_type = ['IR']

    ref_ir_intensities = [3.02861786e+04, 1.26413440e+04, 2.06562397e+03, 4.61357442e+04, \
                          1.69243922e+01, 1.34471049e+05]

    w, iw, ih, ii, ri, hvvi, hhvi = \
        get_vibrational_frequencies_and_intensities(tensor_file, mol_file, spectroscopy_type, \
                                                    specifications, 0, 298, True)

    assert len(ref_ir_intensities) == len(ii)

    for i in range(len(ii)):
        assert ref_ir_intensities[i] == pytest.approx(ii[i], 10e-9)

    # IR NIMAC km/mol
    specifications = ['Vib modes: 1/m', 'IR: NIMAC, km/mol']

    ref_ir_intensities = [3.02861786e+01, 1.26413440e+01, 2.06562397e+00, 4.61357442e+01, \
                          1.69243922e-02, 1.34471049e+02]

    w, iw, ih, ii, ri, hvvi, hhvi = \
        get_vibrational_frequencies_and_intensities(tensor_file, mol_file, spectroscopy_type, \
                                                    specifications, 0, 298, True)

    assert len(ref_ir_intensities) == len(ii)

    for i in range(len(ii)):
        assert ref_ir_intensities[i] == pytest.approx(ii[i], 10e-9)

    # hyperraman
    spectroscopy_type = ['Hyper Raman']

    ref_ih = [4389492.078840123, 0.0]
    ref_vv = [[9.85551833e-101, 3.35681974e-101, 1.06694277e-101, \
               5.46408614e-101, 1.24271719e-102, 4.79330164e-100], \
              [3.82565832e-106, 1.37469213e-106, 1.76919208e-108, \
               5.47227480e-108, 8.67017002e-110, 7.20503289e-111]]
    ref_hv = [[8.00059356e-102, 5.40734225e-102, 2.43932466e-102, \
               8.79663799e-102, 1.88164067e-103, 5.79703442e-101], \
              [3.04266736e-107, 2.43369330e-107, 3.50106218e-109, \
               8.84144861e-109, 9.51538090e-111, 8.58568255e-112]]

    w, iw, ih, ii, ri, hvvi, hhvi = \
        get_vibrational_frequencies_and_intensities(tensor_file, mol_file, spectroscopy_type, \
                                                    specifications, 0, 298, True)

    assert len(ref_ih) == len(ih) == len(hvvi) == len(hhvi)
    for i in range(len(ih)):
        assert ref_ih[i] == ih[i]
        assert len(ref_vv[i]) == len(hvvi[i]) == len(hhvi[i])

        for j in range(len(hvvi[0])):
            assert ref_vv[i][j] == pytest.approx(hvvi[i][j], 1.0e-200)
            assert ref_hv[i][j] == pytest.approx(hhvi[i][j], 1.0e-200)


def test_which_spectroscopies_to_be_calculated():

    spectroscopy_types = ['IR', 'Raman', 'Hyper Raman']

    IR, Raman, hyper_raman = which_spectroscopies_to_be_calculated(spectroscopy_types)

    assert IR == True
    assert Raman == True
    assert hyper_raman == True

    spectroscopy_types = ['IR', 'Raman']

    IR, Raman, hyper_raman = which_spectroscopies_to_be_calculated(spectroscopy_types)

    assert IR == True
    assert Raman == True
    assert hyper_raman == False

    spectroscopy_types = ['Raman', 'Hyper Raman']

    IR, Raman, hyper_raman = which_spectroscopies_to_be_calculated(spectroscopy_types)

    assert IR == False
    assert Raman == True
    assert hyper_raman == True

    spectroscopy_types = ['IR', 'Hyper Raman']

    IR, Raman, hyper_raman = which_spectroscopies_to_be_calculated(spectroscopy_types)

    assert IR == True
    assert Raman == False
    assert hyper_raman == True


def test_get_spectroscopy_indices():

    data_dir = '{0}/'.format(os.path.dirname(__file__))
    tensor_file = data_dir + 'hf_H2O2.rsp_tensor'

    redundant_properties, tensors = read_openrsp_tensor_file(tensor_file)

    ref_spectroscopy_indices = [9]

    spectroscopy_indices = get_spectroscopy_indices(redundant_properties, hess_operator)

    assert len(spectroscopy_indices) == len(ref_spectroscopy_indices)
    for i in range(len(spectroscopy_indices)):
        spectroscopy_indices[i] == ref_spectroscopy_indices[i]

    ref_spectroscopy_indices = [3]

    spectroscopy_indices = get_spectroscopy_indices(redundant_properties, dip_grad_operator)

    assert len(spectroscopy_indices) == len(ref_spectroscopy_indices)
    for i in range(len(spectroscopy_indices)):
        spectroscopy_indices[i] == ref_spectroscopy_indices[i]

    ref_spectroscopy_indices = [4, 5, 6]

    spectroscopy_indices = get_spectroscopy_indices(redundant_properties, polariz_grad_operator)

    assert len(spectroscopy_indices) == len(ref_spectroscopy_indices)
    for i in range(len(spectroscopy_indices)):
        spectroscopy_indices[i] == ref_spectroscopy_indices[i]

    data_dir = '{0}/'.format(os.path.dirname(__file__))
    tensor_file = data_dir + 'multifreq_H2O2.rsp_tensor'

    redundant_properties, tensors = read_openrsp_tensor_file(tensor_file)

    ref_spectroscopy_indices = [0, 1, 2]

    spectroscopy_indices = get_spectroscopy_indices(redundant_properties, hyper_polariz_grad_operator)

    assert len(spectroscopy_indices) == len(ref_spectroscopy_indices)
    for i in range(len(spectroscopy_indices)):
        spectroscopy_indices[i] == ref_spectroscopy_indices[i]


def test_reduced_dims():

    mat_dims = (12, 3)
    remove_elms = 6
    rank_el = 1
    ref_end_dims = (6, 3)

    end_dims = reduced_dims(mat_dims, remove_elms, rank_el)

    assert ref_end_dims == end_dims

    mat_dims = (12, 3, 3)
    rank_el = 2
    ref_end_dims = (6, 3, 3)

    end_dims = reduced_dims(mat_dims, remove_elms, rank_el)

    assert ref_end_dims == end_dims

    mat_dims = (12, 3)
    remove_elms = 5
    rank_el = 1
    ref_end_dims = (7, 3)

    end_dims = reduced_dims(mat_dims, remove_elms, rank_el)

    assert ref_end_dims == end_dims

    mat_dims = (12, 12, 3)
    remove_elms = 6
    ref_end_dims = (6, 6, 3)

    end_dims = reduced_dims(mat_dims, remove_elms, rank_el)

    assert ref_end_dims == end_dims

    mat_dims = (18, 18, 3)
    remove_elms = 6
    ref_end_dims = (12, 12, 3)

    end_dims = reduced_dims(mat_dims, remove_elms, rank_el)

    assert ref_end_dims == end_dims

    remove_elms = 0
    ref_end_dims = (18, 18, 3)

    end_dims = reduced_dims(mat_dims, remove_elms, rank_el)

    assert ref_end_dims == end_dims


def test_getting_the_subblocks():

    input_mat = \
        [[-3.55354959e-03, -2.04896144e-03,  4.65337226e-04], \
         [-1.33397761e-03,  2.30954119e-03, -1.03887733e-06], \
         [ 5.38119487e-04, -9.34229819e-04,  5.72701937e-07], \
         [ 2.05564456e-04,  1.21485597e-04,  5.08962420e-03], \
         [ 4.87101890e-05, -8.45631462e-05,  7.73668483e-08], \
         [ 4.34177613e-03, -7.53776352e-03,  4.54332299e-06], \
         [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00], \
         [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00], \
         [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00], \
         [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00], \
         [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00], \
         [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00]]

    remove_elms = 6
    out_mat = np.zeros(18)
    offset = 0
    rank_el = 1

    ref_out_mat = np.reshape(ref_dipole_gradient, (18))

    getting_the_subblocks(input_mat, remove_elms, out_mat, offset, rank_el)

    assert len(ref_out_mat) == len(out_mat)
    for i in range(len(out_mat)):
        assert ref_out_mat[i] == out_mat[i]

    input_mat = \
        [[[ 6.04610202e-02, -3.51511055e-02,  2.05867010e-02], \
          [-3.51511055e-02, -6.06465271e-02, -3.58100073e-02], \
          [ 2.05867010e-02, -3.58100073e-02, -8.24129166e-06]], \
         [[ 1.20853575e-01,  4.99878490e-02,  7.95877729e-02], \
          [ 4.99878490e-02,  6.28477170e-02,  4.58251237e-02], \
          [ 7.95877729e-02,  4.58251237e-02,  6.62798317e-02]], \
         [[-2.34431047e-02, -7.82917443e-03,  4.02920687e-02], \
          [-7.82917443e-03, -1.43042013e-02,  2.32435281e-02], \
          [ 4.02920687e-02,  2.32435281e-02,  4.87524759e-02]], \
         [[-1.55313827e-02,  9.01591539e-03,  1.14149851e-02], \
          [ 9.01591539e-03,  1.55074857e-02, -1.98366345e-02], \
          [ 1.14149851e-02, -1.98366345e-02,  2.34202541e-05]], \
         [[ 4.39674438e-03,  4.92827640e-04,  7.19780552e-03], \
          [ 4.92827640e-04,  3.83525060e-03,  4.19756005e-03], \
          [ 7.19780552e-03,  4.19756005e-03,  8.94657717e-02]], \
         [[-2.41613385e-02, -4.31408089e-02, -1.19041040e-02], \
          [-4.31408089e-02,  2.58697434e-02, -6.88886076e-03], \
          [-1.19041040e-02, -6.88886076e-03, -2.42915073e-03]], \
         [[ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00], \
          [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00], \
          [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00]], \
         [[ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00], \
          [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00], \
          [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00]], \
         [[ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00], \
          [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00], \
          [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00]], \
         [[ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00], \
          [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00], \
          [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00]], \
         [[ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00], \
          [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00], \
          [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00]], \
         [[ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00], \
          [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00], \
          [ 0.00000000e+00,  0.00000000e+00,  0.00000000e+00]]]

    out_mat = np.zeros(54)
    rank_el = 2

    ref_out_mat = np.reshape(ref_polarizability_gradient[0], (54))

    getting_the_subblocks(input_mat, remove_elms, out_mat, offset, rank_el)

    assert len(ref_out_mat) == len(out_mat)
    for i in range(len(out_mat)):
        assert ref_out_mat[i] == out_mat[i]


def test_get_energy_derivatives():

    data_dir = '{0}/'.format(os.path.dirname(__file__))
    tensor_file = data_dir + 'hf_anharm_H2O2.rsp_tensor'

    redundant_properties, tensors = read_openrsp_tensor_file(tensor_file)

    dip_grad_index = [0]

    dipole_gradient = get_energy_derivatives(dip_grad_index, tensors, redundant_properties, 1, \
                                             1, num_coordinates, vib_degrees_of_freedom, \
                                             transformation_matrix)

    assert len(ref_dipole_gradient) == len(dipole_gradient)
    for i in range(len(dipole_gradient)):
        assert len(ref_dipole_gradient[i]) == len(dipole_gradient[i])

        for j in range(len(dipole_gradient[0])):
            assert len(ref_dipole_gradient[i][j]) == len(dipole_gradient[i][j])

            for k in range(len(dipole_gradient[0][0])):
                assert ref_dipole_gradient[i][j][k] == pytest.approx(dipole_gradient[i][j][k], 1.0e-8)

    polariz_grad_index = [3, 4, 5]

    polarizability_gradient = get_energy_derivatives(polariz_grad_index, tensors, redundant_properties, \
                                                     1, 2, num_coordinates, vib_degrees_of_freedom, \
                                                     transformation_matrix)

    assert len(polarizability_gradient) == len(ref_polarizability_gradient)
    for i in range(len(polarizability_gradient)):
        assert len(polarizability_gradient[i]) == len(ref_polarizability_gradient[i])

        for j in range(len(polarizability_gradient[i])):
            assert len(polarizability_gradient[i][j]) == len(ref_polarizability_gradient[i][j])

            for k in range(len(polarizability_gradient[i][j])):
                assert len(polarizability_gradient[i][j][k]) == len(ref_polarizability_gradient[i][j][k])

                for l in range(len(polarizability_gradient[i][j][k])):
                    assert polarizability_gradient[i][j][k][l] == \
                           pytest.approx(ref_polarizability_gradient[i][j][k][l], 1.0e-8)

    data_dir = '{0}/'.format(os.path.dirname(__file__))
    tensor_file = data_dir + 'multifreq_H2O2.rsp_tensor'

    redundant_properties, tensors = read_openrsp_tensor_file(tensor_file)

    hyper_polariz_grad_index = [0, 1, 2]

    hyper_polarizability_gradients = get_energy_derivatives(hyper_polariz_grad_index, tensors, \
                                                            redundant_properties, 1, 3, \
                                                            num_coordinates, \
                                                            vib_degrees_of_freedom, \
                                                            transformation_matrix)

    assert len(ref_hyper_polarizability_gradient) == len(hyper_polarizability_gradients)
    for i in range(len(hyper_polarizability_gradients)):
        assert len(ref_hyper_polarizability_gradient[i]) == len(hyper_polarizability_gradients[i])

        for j in range(len(hyper_polarizability_gradients[0])):
            assert len(ref_hyper_polarizability_gradient[i][j]) == \
                   len(hyper_polarizability_gradients[i][j])

            for k in range(len(hyper_polarizability_gradients[0][0])):
                assert len(ref_hyper_polarizability_gradient[i][j][k]) == \
                       len(hyper_polarizability_gradients[i][j][k])

                for l in range(len(hyper_polarizability_gradients[0][0][0])):
                    assert len(ref_hyper_polarizability_gradient[i][j][k][l]) == \
                           len(hyper_polarizability_gradients[i][j][k][l])

                    for m in range(len(hyper_polarizability_gradients[0][0][0][0])):
                        assert ref_hyper_polarizability_gradient[i][j][k][l][m] == \
                               pytest.approx(hyper_polarizability_gradients[i][j][k][l][m], 1.0e-6)
