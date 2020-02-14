import os
import unittest

import camembert

DATADIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data'))
SAMPLE_BAM = os.path.join(DATADIR, 'example_no_seq_in_header.bam')
SAMPLE_BRI = SAMPLE_BAM + '.bri'


class BriTestCase(unittest.TestCase):
    def setUp(self):
        self.bri = camembert.Bri(SAMPLE_BAM)

    def tearDown(self):
        if os.path.exists(SAMPLE_BRI):
            os.remove(SAMPLE_BRI)
        del self.bri

    def test_no_bam(self):
        self.assertRaises(IOError, camembert.Bri, 'does_not_exist.bam')

    def test_build(self):
        self.bri.create()
        self.assertTrue(os.path.exists(SAMPLE_BRI))

    def test_load_no_index(self):
        self.assertRaises(IOError, self.bri.load)

    def test_load(self):
        self.bri.create()
        self.bri.load()

    def test_get_no_load(self):
        with self.assertRaises(ValueError):
            list(self.bri.get('HWI-ST216_0121:5:23:5662:111777#0'))

    def test_get_no_name(self):
        self.bri.create()
        self.bri.load()
        reads = list(self.bri.get('HWI-ST216_0121:5:23:5662:111777'))
        self.assertIs(len(reads), 0)

    def test_get(self):
        import pysam
        self.bri.create()
        self.bri.load()
        reads = list(self.bri.get('HWI-ST216_0121:5:23:5662:111777#0'))

        self.assertIs(len(reads), 1)
        self.assertIsInstance(reads[0], pysam.AlignedSegment)
        self.assertEqual(reads[0].query_name, 'HWI-ST216_0121:5:23:5662:111777#0')


if __name__ == '__main__':
    unittest.main()
