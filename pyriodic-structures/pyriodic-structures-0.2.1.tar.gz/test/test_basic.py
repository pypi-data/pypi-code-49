import unittest
import numpy as np
import pyriodic

class TestBasic(unittest.TestCase):
    def test_any_query(self):
        structure = None
        for (structure,) in pyriodic.db.query(
                'select structure from unit_cells limit 1'):
            pass

        self.assertIsNotNone(structure)

    def test_replicate(self):
        for (structure,) in pyriodic.db.query(
                'select structure from unit_cells limit 1'):
            pass

        nx, ny, nz = 3, 5, 7
        big_structure = structure.replicate(nx, ny, nz)

        self.assertEqual(
            len(big_structure.positions), nx*ny*nz*len(structure.positions))
        self.assertEqual(
            len(big_structure.types), nx*ny*nz*len(structure.types))
        self.assertEqual(len(big_structure.positions), len(big_structure.types))

    def test_replicate_upto(self):
        for (structure,) in pyriodic.db.query(
                'select structure from unit_cells limit 1'):
            pass

        N = 17
        big_structure = structure.replicate_upto(N)

        self.assertGreaterEqual(len(big_structure.positions), N)
        self.assertGreaterEqual(len(big_structure.types), N)
        self.assertEqual(len(big_structure.positions), len(big_structure.types))

    def test_import(self):
        from pyriodic.unit_cells import cF4_Cu, cP1_Po

    def test_wrap(self):
        positions = [(0, 0, 0), (2., 0, 0)]
        types = [0, 0]
        box = [2, 2, 2, 0, 0, 0]

        structure = pyriodic.Structure(positions, types, box)
        positions = structure.add_gaussian_noise(0).positions

        np.testing.assert_allclose(positions[0], positions[1])

    def test_rescale(self):
        from pyriodic.unit_cells import cF4_Cu, cI2_W, cP1_Po
        from pyriodic.Structure import box_to_matrix

        new_struct = cF4_Cu.rescale_volume(5)
        new_V = np.linalg.det(box_to_matrix(new_struct.box))
        self.assertAlmostEqual(new_V, 5)

        new_struct = new_struct.rescale_volume(1./5)
        new_V = np.linalg.det(box_to_matrix(new_struct.box))
        self.assertAlmostEqual(new_V, 1./5)

        new_struct = cI2_W.rescale_shortest_distance(10)
        rij = new_struct.positions[1] - new_struct.positions[0]
        self.assertAlmostEqual(np.linalg.norm(rij), 10)

        new_struct = cP1_Po.rescale_shortest_distance(3)
        self.assertAlmostEqual(new_struct.box.Lx, 3)

if __name__ == '__main__':
    unittest.main()
