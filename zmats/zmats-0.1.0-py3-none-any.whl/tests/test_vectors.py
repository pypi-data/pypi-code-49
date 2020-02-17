"""
Unit and regression test for the zmats package.
"""

import math
import unittest

import zmats.converter as converter
import zmats.vectors as vectors
from zmats.exceptions import VectorsError


class TestZMat(unittest.TestCase):
    """
    Contains unit tests for the ARCSpecies class
    """
    @classmethod
    def setUpClass(cls):
        """
        A method that is run before all unit tests in this class.
        """
        cls.maxDiff = None

    def test_get_angle(self):
        """Test calculating the angle between two vectors"""
        v1 = [-1.45707856 + 0.02416711, -0.94104506 - 0.17703194, -0.20275830 - 0.08644641]
        v2 = [-0.03480906 + 0.02416711, 1.11948179 - 0.17703194, -0.82988874 - 0.08644641]
        theta = vectors.get_angle(v1, v2, 'rads')
        self.assertAlmostEqual(theta, 1.8962295, 5)
        self.assertAlmostEqual(theta * 180 / math.pi, 108.6459, 3)

        v1, v2 = [1, 0, 0], [0, 1, 0]
        theta_rads = vectors.get_angle(v1, v2, 'rads')
        theta_degs = vectors.get_angle(v1, v2, units='degs')
        self.assertEqual(theta_degs / theta_rads, 180 / math.pi)
        self.assertAlmostEqual(theta_rads, 1.5707963)

        v1, v2 = [1, 0, 0], [1, 0, 0]
        theta = vectors.get_angle(v1, v2, 'rads')
        self.assertAlmostEqual(theta, 0)

        v1, v2 = [1, 0, 0], [-1, 0, 0]
        theta = vectors.get_angle(v1, v2, 'rads')
        self.assertAlmostEqual(theta, math.pi)

    def test_get_dihedral(self):
        """Test calculating a dihedral angle from vectors"""
        v1, v2, v3 = [1., 1., 0.], [0., 1., 1.], [1., 0., 1.]  # test floats
        dihedral = vectors.get_dihedral(v1, v2, v3, units='degs')
        self.assertAlmostEqual(dihedral, 109.4712206)

        v1, v2, v3 = [1, 1, 0], [0, 1, 1], [1, 0, 1]  # test integers
        dihedral = vectors.get_dihedral(v1, v2, v3, units='degs')
        self.assertAlmostEqual(dihedral, 109.4712206)

        v1, v2, v3 = [1, 1, 0], [0, 1, 1], [1, 0, 1]
        dihedral = vectors.get_dihedral(v1, v2, v3, units='rads')
        self.assertAlmostEqual(dihedral, 1.91063323)
        self.assertAlmostEqual(dihedral * 180 / math.pi, 109.4712206)

        v1, v2, v3 = [0, 0, 0], [0, 0, 0], [0, 0, 0]
        with self.assertRaises(VectorsError):
            vectors.get_dihedral(v1, v2, v3, units='degs')

        v1, v2, v3 = [1, 0, 0], [0, 1, 0], [0, 0, 1]
        dihedral = vectors.get_dihedral(v1, v2, v3, units='degs')
        self.assertEqual(dihedral, 90.0)

    def test_calculate_distance(self):
        """Test calculating a distance between two atoms"""
        propene = converter.str_to_xyz("""C       1.22905000   -0.16449200    0.00000000
    C      -0.13529200    0.45314000    0.00000000
    C      -1.27957200   -0.21983000    0.00000000
    H       1.17363000   -1.25551200    0.00000000
    H       1.79909600    0.15138400    0.87934300
    H       1.79909600    0.15138400   -0.87934300
    H      -0.16831500    1.54137600    0.00000000
    H      -2.23664600    0.28960500    0.00000000
    H      -1.29848800   -1.30626200    0.00000000""")
        distance = vectors.calculate_distance(coords=propene['coords'], atoms=[1, 4], index=1)
        self.assertAlmostEqual(distance, 1.092426698)
        distance = vectors.calculate_distance(coords=propene['coords'], atoms=[1, 2], index=1)
        self.assertAlmostEqual(distance, 1.49763087)
        distance = vectors.calculate_distance(coords=propene['coords'], atoms=[2, 3], index=1)
        self.assertAlmostEqual(distance, 1.32750337)

    def test_calculate_angle(self):
        """Test calculating an angle from xyz coordinates"""
        co2 = converter.str_to_xyz("""O      -1.40465894   -0.03095532    0.00000000
C      -0.00000000    0.00000004    0.00000000
O       1.40465895    0.03095528    0.00000000""")
        angle = vectors.calculate_angle(coords=co2['coords'], atoms=[0, 1, 2], index=0, units='degs')
        self.assertEqual(angle, 180.0)
        angle = vectors.calculate_angle(coords=co2['coords'], atoms=[1, 2, 3], index=1, units='degs')
        self.assertEqual(angle, 180.0)
        angle = vectors.calculate_angle(coords=co2['coords'], atoms=[0, 1, 2], index=0, units='rads')
        self.assertEqual(angle, math.pi)
        with self.assertRaises(VectorsError):
            angle = vectors.calculate_angle(coords=co2['coords'], atoms=[1, 2, 1], index=1, units='degs')

        fake_co2 = converter.str_to_xyz("""O      -1.40465894   -0.03095532    0.00000000
C      -0.00000000    0.00000004    0.00000000
O      -1.40465894   -0.03095532    0.00000000""")
        angle = vectors.calculate_angle(coords=fake_co2['coords'], atoms=[0, 1, 2], index=0, units='degs')
        self.assertEqual(angle, 0.0)

        propene = converter.str_to_xyz("""C       1.22905000   -0.16449200    0.00000000
    C      -0.13529200    0.45314000    0.00000000
    C      -1.27957200   -0.21983000    0.00000000
    H       1.17363000   -1.25551200    0.00000000
    H       1.79909600    0.15138400    0.87934300
    H       1.79909600    0.15138400   -0.87934300
    H      -0.16831500    1.54137600    0.00000000
    H      -2.23664600    0.28960500    0.00000000
    H      -1.29848800   -1.30626200    0.00000000""")
        angle = vectors.calculate_angle(coords=propene['coords'], atoms=[8, 3, 9], index=1, units='degs')
        self.assertAlmostEqual(angle, 117.02817, 4)
        angle = vectors.calculate_angle(coords=propene['coords'], atoms=[9, 3, 8], index=1, units='degs')
        self.assertAlmostEqual(angle, 117.02817, 4)
        angle = vectors.calculate_angle(coords=propene['coords'], atoms=[1, 2, 3], index=1, units='degs')
        self.assertAlmostEqual(angle, 125.18344, 4)
        angle = vectors.calculate_angle(coords=propene['coords'], atoms=[5, 1, 2], index=1, units='degs')
        self.assertAlmostEqual(angle, 110.82078, 4)

    def test_calculate_dihedral_angle(self):
        """Test calculating a dihedral angle from xyz coordinates"""
        propene = converter.str_to_xyz("""C       1.22905000   -0.16449200    0.00000000
    C      -0.13529200    0.45314000    0.00000000
    C      -1.27957200   -0.21983000    0.00000000
    H       1.17363000   -1.25551200    0.00000000
    H       1.79909600    0.15138400    0.87934300
    H       1.79909600    0.15138400   -0.87934300
    H      -0.16831500    1.54137600    0.00000000
    H      -2.23664600    0.28960500    0.00000000
    H      -1.29848800   -1.30626200    0.00000000""")
        hydrazine = converter.str_to_xyz("""N       0.70683700   -0.07371000   -0.21400700
    N      -0.70683700    0.07371000   -0.21400700
    H       1.11984200    0.81113900   -0.47587600
    H       1.07456200   -0.35127300    0.68988300
    H      -1.11984200   -0.81113900   -0.47587600
    H      -1.07456200    0.35127300    0.68988300""")
        cj_11974 = converter.str_to_xyz("""C 	5.675	2.182	1.81
    O 	4.408	1.923	1.256
    C 	4.269	0.813	0.479
    C 	5.303	-0.068	0.178
    C 	5.056	-1.172	-0.639
    C 	3.794	-1.414	-1.169
    C 	2.77	-0.511	-0.851
    C 	2.977	0.59	-0.032
    C 	1.872	1.556	0.318
    N 	0.557	1.029	-0.009
    C 	-0.537	1.879	0.448
    C 	-0.535	3.231	-0.298
    C 	-1.831	3.983	0.033
    C 	-3.003	3.199	-0.61
    N 	-2.577	1.854	-0.99
    C 	-1.64	1.962	-2.111
    C 	-0.501	2.962	-1.805
    C 	-1.939	1.236	0.178
    C 	-1.971	-0.305	0.069
    C 	-3.385	-0.794	-0.209
    C 	-4.336	-0.893	0.81
    C 	-5.631	-1.324	0.539
    C 	-5.997	-1.673	-0.759
    C 	-5.056	-1.584	-1.781
    C 	-3.764	-1.147	-1.505
    C 	-1.375	-1.024	1.269
    C 	-1.405	-0.508	2.569
    C 	-0.871	-1.226	3.638
    C 	-0.296	-2.475	3.429
    C 	-0.259	-3.003	2.14
    C 	-0.794	-2.285	1.078
    C 	3.533	-2.614	-2.056
    C 	2.521	-3.574	-1.424
    C 	3.087	-2.199	-3.461
    H 	5.569	3.097	2.395
    H 	6.433	2.338	1.031
    H 	6.003	1.368	2.47
    H 	6.302	0.091	0.57
    H 	5.874	-1.854	-0.864
    H 	1.772	-0.654	-1.257
    H 	1.963	1.832	1.384
    H 	2.033	2.489	-0.239
    H 	0.469	0.13	0.461
    H 	-0.445	2.089	1.532
    H 	0.328	3.83	0.012
    H 	-1.953	4.059	1.122
    H 	-1.779	5.008	-0.352
    H 	-3.365	3.702	-1.515
    H 	-3.856	3.118	0.074
    H 	-1.226	0.969	-2.31
    H 	-2.211	2.259	-2.999
    H 	-0.639	3.906	-2.348
    H 	0.466	2.546	-2.105
    H 	-2.586	1.501	1.025
    H 	-1.36	-0.582	-0.799
    H 	-4.057	-0.647	1.831
    H 	-6.355	-1.396	1.347
    H 	-7.006	-2.015	-0.97
    H 	-5.329	-1.854	-2.798
    H 	-3.038	-1.07	-2.311
    H 	-1.843	0.468	2.759
    H 	-0.904	-0.802	4.638
    H 	0.125	-3.032	4.262
    H 	0.189	-3.977	1.961
    H 	-0.772	-2.708	0.075
    H 	4.484	-3.155	-2.156
    H 	1.543	-3.093	-1.308
    H 	2.383	-4.464	-2.049
    H 	2.851	-3.899	-0.431
    H 	3.826	-1.542	-3.932
    H 	2.134	-1.659	-3.429
    H 	2.951	-3.078	-4.102""")

        dihedral0 = vectors.calculate_dihedral_angle(coords=propene['coords'], torsion=[9, 3, 2, 7], index=1)
        dihedral1 = vectors.calculate_dihedral_angle(coords=propene['coords'], torsion=[5, 1, 2, 7], index=1)
        self.assertAlmostEqual(dihedral0, 180, 2)
        self.assertAlmostEqual(dihedral1, 59.26447, 2)
        dihedral2 = vectors.calculate_dihedral_angle(coords=propene['coords'], torsion=[8, 2, 1, 6], index=0)
        self.assertEqual(dihedral0, dihedral2)

        dihedral3 = vectors.calculate_dihedral_angle(coords=hydrazine['coords'], torsion=[3, 1, 2, 5], index=1)
        self.assertAlmostEqual(dihedral3, 148.31829, 2)

        dihedral2 = vectors.calculate_dihedral_angle(coords=cj_11974['coords'], torsion=[15, 18, 19, 20], index=1)
        self.assertAlmostEqual(dihedral2, 308.04758, 2)

    def test_unit_vector(self):
        """Test calculating a unit vector"""
        v1 = [1, 0, 0]
        self.assertEqual(vectors.unit_vector(v1)[0], 1.)  # trivial
        self.assertEqual(vectors.unit_vector(v1)[1], 0.)  # trivial
        self.assertEqual(vectors.unit_vector(v1)[2], 0.)  # trivial
        v2 = [1, 1, 1]
        self.assertAlmostEqual(vectors.unit_vector(v2)[0], (1 / 3) ** 0.5)
        self.assertAlmostEqual(vectors.unit_vector(v2)[1], (1 / 3) ** 0.5)
        self.assertAlmostEqual(vectors.unit_vector(v2)[2], (1 / 3) ** 0.5)

    def test_get_vector_length(self):
        """Test getting a vector's length"""

        # unit vector
        v1 = [1, 0, 0]
        self.assertEqual(vectors.get_vector_length(v1), 1)

        # a vector with 0 entries
        v1 = [0, 0, 0]
        self.assertEqual(vectors.get_vector_length(v1), 0)

        # 10D vector
        v1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertAlmostEqual(vectors.get_vector_length(v1), 19.6214169)   # default: places=7

        # 1D vector
        v1 = [2]
        self.assertEqual(vectors.get_vector_length(v1), 2)

        # a vector with small entries
        v1 = [0.0000001, 0.0000002, 0.0000003]
        self.assertAlmostEqual(vectors.get_vector_length(v1), 0.000000374165739, places=15)

        # a vector with large entries
        v1 = [100, 200, 300]
        self.assertAlmostEqual(vectors.get_vector_length(v1), 374.165738677394000)  # default: places=7


if __name__ == '__main__':
    unittest.main(testRunner=unittest.TextTestRunner(verbosity=2))
