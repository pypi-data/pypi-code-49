#!/usr/bin/env python
"""Testing aws.py"""
########################################################################
# File: aws_test.py
#  executable: aws_test.py
#
# Author: Andrew Bailey
# History: 03/27/19 Created
########################################################################

import unittest
import os
import tempfile

from py3helpers.bin.merge_methyl_bed_files import *
from py3helpers.bin.methyl_bed_kmer_analysis import *
from py3helpers.utils import captured_output


class MergeMethylTests(unittest.TestCase):
    """Test merge_methyl_bed_files.py"""

    @classmethod
    def setUpClass(cls):
        super(MergeMethylTests, cls).setUpClass()
        cls.HOME = '/'.join(os.path.abspath(__file__).split("/")[:-1])
        cls.test_ref = os.path.join(cls.HOME, "test_files/ecoli_k12_mg1655.fa")
        cls.test_bed = os.path.join(cls.HOME, "test_files/test.bed")

    def test_aggregate_methylbeds(self):
        with captured_output() as (_, _):
            merged_bed = aggregate_methylbeds([self.test_bed, self.test_bed])
            self.assertSequenceEqual(merged_bed["Chromosome"]["+"]["2"], [("255,0,0", 1, 100), ("255,0,0", 1, 100)])
            self.assertSequenceEqual(merged_bed["Chromosome"]["-"]["1"], [("0,255,0", 0, 0), ("0,255,0", 0, 0)])

    def test_write_bed_file(self):
        with captured_output() as (_, _):
            merged_bed = aggregate_methylbeds([self.test_bed, self.test_bed])
            with tempfile.TemporaryDirectory() as tempdir:
                tmp_file = os.path.join(tempdir, "merge_test.bed")
                write_bed_file(merged_bed, tmp_file)
                with open(tmp_file, "r") as fh:
                    data = [x.split() for x in fh]

            self.assertEqual(len(data), 1)
            self.assertEqual(data[0][0], "Chromosome")
            self.assertEqual(data[0][9], '2')
            self.assertEqual(data[0][10], '100')

    def test_FilterBed(self):
        with captured_output() as (_, _):
            filter_bed = FilterBed()
            filter_bed.set_filter_by_coverage(0, 1000)
            filter_bed.set_filter_by_percentage(0, 100)
            filter_bed.chain_logic(filter_bed.filter_by_coverage_min_max, filter_bed.filter_by_percentage_min_min_max_max)
            self.assertTrue(filter_bed.function("", "", "", "", 10, 100))
            self.assertFalse(filter_bed.function("", "", "", "", 10, 99))
            self.assertTrue(filter_bed.function("", "", "", "", 0, 100))
            self.assertFalse(filter_bed.function("", "", "", "", -1, 100))
            self.assertTrue(filter_bed.function("", "", "", "", 0, 0))
            self.assertFalse(filter_bed.function("", "", "", "", 0, 1))

    def test_get_kmer_counts_from_reference_given_bed(self):
        with captured_output() as (_, _):
            kmer_counts = get_kmer_counts_from_reference_given_bed(self.test_ref, self.test_bed, k=5)
            for kmer in kmer_counts.keys():
                self.assertEqual(len(kmer), 5)
                self.assertIn("C", kmer)
            kmer_counts = get_kmer_counts_from_reference_given_bed(self.test_ref, self.test_bed, k=6)
            for kmer in kmer_counts.keys():
                self.assertEqual(len(kmer), 6)
                self.assertIn("C", kmer)


if __name__ == '__main__':
    unittest.main()
