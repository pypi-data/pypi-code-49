import os
import unittest
import numpy as np
import imgio
import rawpipe


thisdir = os.path.dirname(__file__)


class RegressionTest(unittest.TestCase):

    def test_fullpipe(self):
        print("\nConfirming bit-exact output of basic ISP blocks...")
        bayer_pattern = "RGGB"
        gamma_mode = "sRGB"
        blacklevel = 256
        whitelevel = None
        wb = [1.7, 2.4]
        ccm = np.array([[ 0.9, 0.4, -0.3],   # noqa
                        [-0.2, 1.1,  0.1],   # noqa
                        [ 0.0,-0.4,  1.4]])  # noqa
        expected, maxval = imgio.imread(os.path.join(thisdir, "expected.ppm"))
        raw = np.fromfile(os.path.join(thisdir, "input.raw"), dtype=np.uint16)
        raw = raw.reshape(expected.shape[:2])
        self.assertEqual(raw.shape[0], expected.shape[0])
        self.assertEqual(raw.shape[1], expected.shape[1])
        alg = rawpipe.Algorithms(verbose=True)
        raw = alg.linearize(raw, blacklevel, whitelevel)
        raw = alg.demosaic(raw, bayer_pattern)
        raw = alg.wb(raw, wb)
        raw = alg.ccm(raw, ccm)
        raw = alg.gamma(raw, gamma_mode)
        raw = alg.quantize(raw, maxval, expected.dtype)
        self.assertEqual(np.count_nonzero(expected - raw), 0)


if __name__ == "__main__":
    unittest.main()
