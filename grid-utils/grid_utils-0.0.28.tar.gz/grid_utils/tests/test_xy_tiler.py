from unittest import TestCase
import numpy as np
from grid_utils.tiler.xy_tiler import *



class TestXYTiler(TestCase):
    def gen_tiler(self):
        return XYTiler(1.0, 1.0, 10, 10)

    def gen_tiler_with_x0y0(self):
        return XYTiler(1.0, 1.0, 10, 10, 100.0, 30.0)

    def gen_tiler_with_margin(self):
        return XYTiler(1.0, 1.0, 10, 10, margin=2)

    def test_full_nx_ny(self):
        tiler1 = self.gen_tiler()
        tiler2 = self.gen_tiler_with_margin()

        self.assertEqual(tiler1.full_nx, 10)
        self.assertEqual(tiler1.full_ny, 10)
        self.assertEqual(tiler2.full_nx, 14)
        self.assertEqual(tiler2.full_ny, 14)

    def test_xy2tile(self):
        tiler = self.gen_tiler()
        self.assertEqual(tiler.xy2tile(93.501, 34.301), (93, 34, 5, 3))
        self.assertEqual(tiler.xy2tile(93.499, 34.301), (93, 34, 4, 3))

        tiler = self.gen_tiler_with_x0y0()
        self.assertEqual(tiler.xy2tile(93.501, 34.301), (-7, 4, 5, 3))

        tiler = self.gen_tiler_with_margin()
        self.assertEqual(tiler.xy2tile(93.501, 34.301), (93, 34, 7, 5))
        self.assertEqual(tiler.xy2tile(93.501, 34.301, margin=False), (93, 34, 5, 3))
        self.assertEqual(tiler.xy2tile(93.001, 34.999), (93, 34, 2, 11))

    def test_tile2xy(self):
        tiler = self.gen_tiler()
        res = tiler.tile2xy(93, 34, 5, 3, pos='center')
        self.assertAlmostEqual(res[0], 93.55)
        self.assertAlmostEqual(res[1], 34.35)
        res = tiler.tile2xy(93, 34, 5, 3, pos='lowerleft')
        self.assertAlmostEqual(res[0], 93.5)
        self.assertAlmostEqual(res[1], 34.3)
        res = tiler.tile2xy(93, 34, 5, 3, pos='upperright')
        self.assertAlmostEqual(res[0], 93.6)
        self.assertAlmostEqual(res[1], 34.4)

        tiler = self.gen_tiler_with_x0y0()
        res = tiler.tile2xy(-7, 4, 5, 3, pos='center')
        self.assertAlmostEqual(res[0], 93.55)
        self.assertAlmostEqual(res[1], 34.35)

        tiler = self.gen_tiler_with_margin()
        res = tiler.tile2xy(93, 34, 7, 5, pos='center')
        self.assertAlmostEqual(res[0], 93.55)
        self.assertAlmostEqual(res[1], 34.35)
        res = tiler.tile2xy(93, 34, 5, 3, pos='center', margin=False)
        self.assertAlmostEqual(res[0], 93.55)
        self.assertAlmostEqual(res[1], 34.35)

    def test_get_tile_xys(self):
        tiler = self.gen_tiler()
        xs, ys = tiler.get_tile_xys(93, 34)
        self.assertEqual(len(xs), 10)
        self.assertAlmostEqual(xs[0], 93.05)
        self.assertAlmostEqual(ys[-1], 34.95)

        tiler = self.gen_tiler_with_margin()
        xs, ys = tiler.get_tile_xys(93, 34)
        self.assertEqual(len(xs), 14)
        self.assertAlmostEqual(xs[0], 92.85)
        self.assertAlmostEqual(ys[-1], 35.15)
        xs, ys = tiler.get_tile_xys(93, 34, margin=False)
        self.assertEqual(len(xs), 10)
        self.assertAlmostEqual(xs[0], 93.05)
        self.assertAlmostEqual(ys[-1], 34.95)

    def test_get_tile_bbox(self):
        tiler = self.gen_tiler_with_margin()
        x1, y1, x2, y2 = tiler.get_tile_bbox(93, 34)
        self.assertAlmostEqual(x1, 93.0)
        self.assertAlmostEqual(x2, 94.0)
        self.assertAlmostEqual(y1, 34.0)
        self.assertAlmostEqual(y2, 35.0)

    def test_get_covered_tiles(self):
        tiler = self.gen_tiler_with_margin()
        tiles = tiler.get_covered_tiles(93.501, 34.301, 94.299, 34.999)
        self.assertEqual(len(tiles), 2)
        self.assertTupleEqual(tiles[0], (93, 34))
        self.assertTupleEqual(tiles[1], (94, 34))

        d = tiler.get_covered_tiles(93.501, 34.301, 94.299, 34.999, detail=True)

        self.assertEqual(d['ni'], 8)
        self.assertEqual(d['nj'], 7)
        self.assertAlmostEqual(d['xs'][0], 93.55)
        self.assertAlmostEqual(d['ys'][-1], 34.95)
        self.assertDictEqual(d['i_beg_dict'], {93: 7, 94: 2})
        self.assertDictEqual(d['i_end_dict'], {93: 12, 94: 5})
        self.assertDictEqual(d['i_offset_dict'], {93: 0, 94: 5})
        self.assertDictEqual(d['j_beg_dict'], {34: 5})
        self.assertDictEqual(d['j_end_dict'], {34: 12})
        self.assertDictEqual(d['j_offset_dict'], {34: 0})
        self.assertListEqual(d['tile_list'], [(93, 34), (94, 34)])

    def test_get_surrounding_pixels(self):
        tiler = self.gen_tiler_with_margin()

        tile_I, tile_J, I, J = tiler.get_surrounding_pixels(93, 34, 2, 2)
        self.assertTupleEqual(tile_I.shape, (3, 3))
        self.assertTupleEqual(J.shape, (3, 3))
        np.testing.assert_equal(tile_I, np.array([[92, 93, 93]]*3))
        np.testing.assert_equal(tile_J, np.array([[33, 34, 34]]*3).T)
        np.testing.assert_equal(I, np.array([[11, 2, 3]]*3))
        np.testing.assert_equal(J, np.array([[11, 2, 3]]*3).T)

        tile_I, tile_J, I, J = tiler.get_surrounding_pixels(93, 34, 9, 9, margin=False)
        self.assertTupleEqual(tile_I.shape, (3, 3))
        self.assertTupleEqual(J.shape, (3, 3))
        np.testing.assert_equal(tile_I, np.array([[93, 93, 94]]*3))
        np.testing.assert_equal(tile_J, np.array([[34, 34, 35]]*3).T)
        np.testing.assert_equal(I, np.array([[8, 9, 0]]*3))
        np.testing.assert_equal(J, np.array([[8, 9, 0]]*3).T)
