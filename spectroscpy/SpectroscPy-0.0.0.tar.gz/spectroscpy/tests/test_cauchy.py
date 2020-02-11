# SpectroscPy 0.0.0
# SpectroscPy is a script package developed by and containing contributions from

    # Karen Oda Hjorth Dundas
    # Magnus Ringholm
    # Yann Cornation
    # Benedicte Ofstad

# The package is released under a LGPL licence.
# For questions, please contact on karen.o.dundas@uit.no

from spectroscpy import get_interquartile_range, get_gamma, cauchy_lincomb, get_weighted_averages, \
                        get_set_of_weighted_averages, get_simple_averages
import pytest

def test_get_simple_averages():

    ref_y = [10.2,  2.6,  4.4,  2.0,   7.4]

    y = [[10, 3, 4, 2, 7], [11, 4, 5, 1, 8], [9, 2, 5, 1, 8], [10, 2, 5, 3, 6], [11, 2, 3, 3, 8]]

    avg_y = get_simple_averages(y)

    assert len(ref_y) == len(avg_y)

    for i in range(len(avg_y)):
        assert ref_y[i] == avg_y[i]

    ref_y = [10, 3, 4, 2, 7]
    y = [[10, 3, 4, 2, 7]]

    avg_y = get_simple_averages(y)

    assert len(ref_y) == len(avg_y)

    for i in range(len(avg_y)):
        assert ref_y[i] == avg_y[i]


def test_get_set_of_weighted_averages():

    ref_x = [1.12019608,  4.12923077,  6.23090909,  2.275,      10.01783784]
    ref_y = [10.2,  2.6,  4.4,  2.0,   7.4]

    x = [[1.15, 4, 6.1, 2.3, 9.8], [1.13, 4.15, 6.5, 2.4, 10], [1, 4.13, 6.11, 2.25, 10.1], \
         [1.1, 4.25, 6.2, 2.18, 10.05], [1.2, 4.16, 6.21, 2.32, 10.12]]
    y = [[10, 3, 4, 2, 7], [11, 4, 5, 1, 8], [9, 2, 5, 1, 8], [10, 2, 5, 3, 6], [11, 2, 3, 3, 8]]

    avg_x, avg_y = get_set_of_weighted_averages(x, y)

    assert len(ref_x) == len(avg_x) == len(avg_y)

    for i in range(len(avg_x)):
        assert ref_x[i] == pytest.approx(avg_x[i], 1.0e-8)
        assert ref_y[i] == pytest.approx(avg_y[i], 1.0e-10)

    ref_x = [1.15, 4, 6.1, 2.3, 9.8]
    ref_y = [10, 3, 4, 2, 7]

    x = [[1.15, 4, 6.1, 2.3, 9.8]]
    y = [[10, 3, 4, 2, 7]]

    avg_x, avg_y = get_set_of_weighted_averages(x, y)

    assert len(ref_x) == len(avg_x) == len(avg_y)

    for i in range(len(avg_x)):
        assert ref_x[i] == pytest.approx(avg_x[i], 1.0e-10)
        assert ref_y[i] == pytest.approx(avg_y[i], 1.0e-10)


def test_get_weighted_averages():

    ref_y = 10.2
    ref_x = 1.1201960784313725

    x = [1.15, 1.13, 1, 1.1, 1.2]
    y = [10, 11, 9, 10, 11]

    avg_x, avg_y = get_weighted_averages(x, y)

    assert ref_x == avg_x
    assert ref_y == avg_y


def test_get_interquartile_range():

    x = [1.15, 1.13, 1, 1.1, 1.2]

    ref_iqr = 0.0625*2

    iqr = get_interquartile_range(x)

    assert ref_iqr == pytest.approx(iqr, 1.0e-10)


def test_get_gamma():

    a = [[1.15, 4, 6.1, 2.3, 9.8], [1.13, 4.15, 6.5, 2.4, 10], [1, 4.13, 6.11, 2.25, 10.1], \
     [1.1, 4.25, 6.2, 2.18, 10.05], [1.2, 4.16, 6.21, 2.32, 10.12]]

    cauchy_type = 'WA'
    ref_gamma = [0.0625, 0.07  , 0.125 , 0.0725, 0.105 ]

    gamma = get_gamma(cauchy_type, a)

    assert len(ref_gamma) == len(gamma)

    for i in range(len(gamma)):
        assert ref_gamma[i] == pytest.approx(gamma[i], 1.0e-10)

    cauchy_type = 'WS'
    gamma = get_gamma(cauchy_type, a)

    assert len(ref_gamma) == len(gamma)
    for i in range(len(gamma)):
        assert ref_gamma[i] == pytest.approx(5*gamma[i], 1.0e-10)

    # GS
    cauchy_type = 0.01
    gamma = get_gamma(cauchy_type, a)

    assert 1 == len(gamma)
    assert 0.01 == gamma[0]


def test_cauchy_lincomb():

    x = [2.        , 2.12244898, 2.24489796, 2.36734694, 2.48979592, \
         2.6122449 , 2.73469388, 2.85714286, 3.        , 3.10204082, \
         3.2244898 , 3.34693878, 3.46938776, 3.59183673, 3.71428571, \
         3.83673469, 4.        , 4.08163265, 4.20408163, 4.32653061, \
         4.44897959, 4.57142857, 4.69387755, 4.81632653, 5.        , \
         5.06122449, 5.18367347, 5.30612245, 5.42857143, 5.55102041, \
         5.67346939, 5.79591837, 5.91836735, 6.04081633, 6.16326531, \
         6.28571429, 6.40816327, 6.53061224, 6.65306122, 6.7755102 , \
         6.89795918, 7.02040816, 7.14285714, 7.26530612, 7.3877551 , \
         7.51020408, 7.63265306, 7.75510204, 7.87755102, 8.        ]

    y = [ 1.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  9.,  0.,  0.,  0.,  0., \
          0.,  0.,  0., 10.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  8.,  0., \
          0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0., \
          0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0., 11.]

    gamma = [ 0.5,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  1.5,  0.,  0.,  0.,  0., \
              0.,  0.,  0., 0.5,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  2.5,  0., \
              0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0., \
              0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0., 1.]

    x_fit = [2.        , 2.12244898, 2.24489796, 2.36734694, 2.48979592, \
             2.6122449 , 2.73469388, 2.85714286, 2.97959184, 3.10204082, \
             3.2244898 , 3.34693878, 3.46938776, 3.59183673, 3.71428571, \
             3.83673469, 3.95918367, 4.08163265, 4.20408163, 4.32653061, \
             4.44897959, 4.57142857, 4.69387755, 4.81632653, 4.93877551, \
             5.06122449, 5.18367347, 5.30612245, 5.42857143, 5.55102041, \
             5.67346939, 5.79591837, 5.91836735, 6.04081633, 6.16326531, \
             6.28571429, 6.40816327, 6.53061224, 6.65306122, 6.7755102 , \
             6.89795918, 7.02040816, 7.14285714, 7.26530612, 7.3877551 , \
             7.51020408, 7.63265306, 7.75510204, 7.87755102, 8.        ]

    ref_y_fit = [ 2.84540055, 2.98167982, 3.07764205, 3.17073463, 3.28444522, 3.42567693, \
                  3.59451812, 3.79183583, 4.02344249, 4.30269408, 4.65245797, 5.10594493, \
                  5.70329046, 6.47474527, 7.39220499, 8.28165002, 8.78873367, 8.60373549, \
                  7.80176579, 6.75389522, 5.76649175, 4.95831734, 4.33348715, 3.85816717, \
                  3.49547865, 3.21560192, 2.99668213, 2.82332298, 2.68488588, 2.57413559, \
                  2.48626725, 2.41823339, 2.36828556, 2.33566519, 2.32039727, 2.32315328, \
                  2.34515669, 2.38810463, 2.45407423, 2.54536887, 2.66423898, 2.81238327, \
                  2.99011178, 3.19505925, 3.42044407, 3.65317288, 3.87265217, 4.05178043, \
                  4.16153299, 4.17889113]

    y_fit = cauchy_lincomb(x, y, gamma, x_fit)

    assert len(ref_y_fit) == len(y_fit)

    for i in range(len(y_fit)):
        assert ref_y_fit[i] == pytest.approx(y_fit[i], 1.0e-8)

    # Constant gamma
    gamma = [0.01]

    ref_y_fit = [3.18713932e+01, 2.61202266e-01, 1.17965269e-01, 1.11846817e-01,\
                 1.42424793e-01, 2.21099008e-01, 4.38427956e-01, 1.43247191e+00,\
                 5.55076845e+01, 2.77579122e+00, 6.31987216e-01, 3.25115485e-01,\
                 2.57032100e-01, 2.88614802e-01, 4.63984489e-01, 1.25238917e+00,\
                 1.80822327e+01, 4.76370771e+00, 8.25466559e-01, 3.73853860e-01,\
                 2.58620740e-01, 2.51079488e-01, 3.51173000e-01, 8.12894281e-01,\
                 6.66475598e+00, 6.65631383e+00, 7.86049219e-01, 3.00608287e-01,\
                 1.64585832e-01, 1.07565679e-01, 7.82101971e-02, 6.11533118e-02,\
                 5.04898551e-02, 4.35619248e-02, 3.90439395e-02, 3.62372005e-02,\
                 3.47777036e-02, 3.45089577e-02, 3.54329245e-02, 3.77097439e-02,\
                 4.17050730e-02, 4.81102336e-02, 5.82091266e-02, 7.44930023e-02,\
                 1.02222371e-01, 1.54029738e-01, 2.66800896e-01, 5.89814674e-01,\
                 2.32626217e+00, 3.50146928e+02]

    y_fit = cauchy_lincomb(x, y, gamma, x_fit)

    assert len(ref_y_fit) == len(y_fit)

    for i in range(len(y_fit)):
        assert ref_y_fit[i] == pytest.approx(y_fit[i], 1.0e-8)
