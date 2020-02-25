#!/usr/bin/env python
"""Testing classification.py"""
########################################################################
# File: classification_test.py
#  executable: classification_test.py
#
# Author: Andrew Bailey
# History: 12/19/18 Created
########################################################################

import sys
import numpy as np
import pandas as pd

import os
import unittest
import tempfile
import datetime
from sklearn import preprocessing
from py3helpers.classification import *
from py3helpers.utils import get_random_strings, captured_output


def generate_random_label_prob_data(n_row, column_names):
    """Generate random labels for random probability data given size and column names
    :param n_row: number of rows
    :param column_names: names of different classes
    :return: label_data , prob_data
    """
    n_col = len(column_names)
    total_points = n_col * n_row
    data = pd.DataFrame(np.random.random(total_points).reshape(n_row, n_col), columns=column_names)
    rand_prob_data = data.div(data.sum(axis=1), axis=0)

    data = pd.DataFrame(np.random.random(total_points).reshape(n_row, n_col), columns=column_names)
    new_prob_data = data.div(data.sum(axis=1), axis=0)
    # if binary data, convert input data to 1d
    if n_col == 2:
        column_names.append(" ")
        label_data = pd.DataFrame(preprocessing.label_binarize(new_prob_data.idxmax(axis=1), classes=column_names),
                                  columns=column_names)[column_names[:n_col]]
    else:
        label_data = pd.DataFrame(preprocessing.label_binarize(new_prob_data.idxmax(axis=1), classes=column_names),
                                  columns=column_names)
    return label_data, rand_prob_data


def generate_50_50_prob_data(n_row, column_names):
    """Generate random labels for 50-50 probability data given size and column names
    :param n_row: number of rows
    :param column_names: names of different classes
    :return: label_data , prob_data
    """
    n_col = len(column_names)
    total_points = n_col * n_row
    data = pd.DataFrame(np.ones(total_points).reshape(n_row, n_col), columns=column_names)
    rand_prob_data = data.div(data.sum(axis=1), axis=0)

    data = pd.DataFrame(np.random.random(total_points).reshape(n_row, n_col), columns=column_names)
    new_prob_data = data.div(data.sum(axis=1), axis=0)
    # if binary data, convert input data to 1d
    if n_col == 2:
        column_names.append(" ")
        label_data = pd.DataFrame(preprocessing.label_binarize(new_prob_data.idxmax(axis=1), classes=column_names),
                                  columns=column_names)[column_names[:n_col]]
    else:
        label_data = pd.DataFrame(preprocessing.label_binarize(new_prob_data.idxmax(axis=1), classes=column_names),
                                  columns=column_names)
    return label_data, rand_prob_data


def generate_perfect_label_prob_data(n_row, column_names):
    """Generate random labels for random probability data given size and column names
    :param n_row: number of rows
    :param column_names: names of different classes
    :return: label_data , prob_data
    """
    n_col = len(column_names)
    total_points = n_col * n_row
    data = pd.DataFrame(np.random.random(total_points).reshape(n_row, n_col), columns=column_names)
    rand_prob_data = data.div(data.sum(axis=1), axis=0)
    # if binary data, convert input data to 1d
    if n_col == 2:
        column_names.append(" ")
        label_data = pd.DataFrame(preprocessing.label_binarize(rand_prob_data.idxmax(axis=1), classes=column_names),
                                  columns=column_names)[column_names[:n_col]]
    else:
        label_data = pd.DataFrame(preprocessing.label_binarize(rand_prob_data.idxmax(axis=1), classes=column_names),
                                  columns=column_names)
    return label_data, rand_prob_data


class ClassificationTests(unittest.TestCase):
    """Test the functions in classification.py"""

    @classmethod
    def setUpClass(cls):
        super(ClassificationTests, cls).setUpClass()
        cls.HOME = '/'.join(os.path.abspath(__file__).split("/")[:-1])
        cls.label_names = get_random_strings(50, 10)

        cls.label_data, cls.prob_data = generate_random_label_prob_data(50, list("ABCD"))
        cls.cm_h = ClassificationMetrics(cls.label_data, cls.prob_data, label_ids=cls.label_names)
        cls.label_data2, cls.prob_data2 = generate_perfect_label_prob_data(50, list("AB"))
        cls.perfect_binary = ClassificationMetrics(cls.label_data2, cls.prob_data2, label_ids=cls.label_names)
        cls.label_data3, cls.prob_data3 = generate_50_50_prob_data(50, list("AB"))
        cls.fifty_fifty = ClassificationMetrics(cls.label_data3, cls.prob_data3, label_ids=cls.label_names)

    def test_initialization(self):
        with captured_output() as (_, _):
            self.assertIsInstance(self.perfect_binary, ClassificationMetrics)
            self.assertIsInstance(self.cm_h, ClassificationMetrics)

    def test_get_fp_ids(self):
        with captured_output() as (_, _):
            ids = self.cm_h.get_fp_ids("A")
            self.assertEqual(len(ids), self.cm_h.get_n_fps("A"))
            ids = self.cm_h.get_fp_ids("A", threshold=0)
            self.assertEqual(len(ids), self.cm_h.get_n_fps("A", threshold=0))
            ids = self.perfect_binary.get_fp_ids("A")
            self.assertEqual(len(ids), 0)
            ids = self.perfect_binary.get_fp_ids("A", threshold=0)
            names = [self.label_names[i] for i in range(len(self.label_data2["A"])) if self.label_data2["A"][i] == 0]
            self.assertEqual(set(ids), set(names))

    def test_get_n_fps(self):
        with captured_output() as (_, _):
            ids = self.perfect_binary.get_n_fps("A")
            self.assertEqual(ids, 0)
            ids = self.perfect_binary.get_n_fps("B")
            self.assertEqual(ids, 0)

    def test_get_tp_ids(self):
        with captured_output() as (_, _):
            ids = self.cm_h.get_tp_ids("A")
            self.assertEqual(len(ids), self.cm_h.get_n_tps("A"))
            ids = self.cm_h.get_tp_ids("A", threshold=0)
            self.assertEqual(len(ids), self.cm_h.get_n_tps("A", threshold=0))
            ids = self.perfect_binary.get_tp_ids("A", threshold=1)
            self.assertEqual(len(ids), 0)
            names = [self.label_names[i] for i in range(len(self.label_data2["A"])) if self.label_data2["A"][i] == 1]
            ids = self.perfect_binary.get_tp_ids("A", threshold=0)
            self.assertEqual(set(ids), set(names))

    def test_get_n_tps(self):
        with captured_output() as (_, _):
            n_tps = self.perfect_binary.get_n_tps("A", threshold=1)
            self.assertEqual(n_tps, 0)
            n_tps = self.perfect_binary.get_n_tps("B", threshold=1)
            self.assertEqual(n_tps, 0)
            n_tps = self.cm_h.get_n_tps("A", threshold=0)
            names = [self.label_names[i] for i in range(len(self.label_data["A"])) if self.label_data["A"][i] == 1]
            self.assertEqual(n_tps, len(names))

    def test_get_fn_ids(self):
        with captured_output() as (_, _):
            ids = self.cm_h.get_fn_ids("A")
            self.assertEqual(len(ids), self.cm_h.get_n_fns("A"))
            ids = self.cm_h.get_fn_ids("A", threshold=0)
            self.assertEqual(len(ids), self.cm_h.get_n_fns("A", threshold=0))
            ids = self.perfect_binary.get_fn_ids("A")
            self.assertEqual(len(ids), 0)
            names = [self.label_names[i] for i in range(len(self.label_data2["A"])) if self.label_data2["A"][i] == 1]
            ids = self.perfect_binary.get_fn_ids("A", threshold=1)
            self.assertEqual(set(ids), set(names))

    def test_get_n_fns(self):
        with captured_output() as (_, _):
            n_fns = self.perfect_binary.get_n_fns("A")
            self.assertEqual(n_fns, 0)
            n_fns = self.perfect_binary.get_n_fns("B")
            self.assertEqual(n_fns, 0)
            n_fns = self.cm_h.get_n_fns("A", threshold=1)
            names = [self.label_names[i] for i in range(len(self.label_data["A"])) if self.label_data["A"][i] == 1]
            self.assertEqual(n_fns, len(names))

    def test_get_tn_ids(self):
        with captured_output() as (_, _):
            ids = self.cm_h.get_tn_ids("A")
            self.assertEqual(len(ids), self.cm_h.get_n_tns("A"))
            ids = self.cm_h.get_tn_ids("A", threshold=0)
            self.assertEqual(len(ids), self.cm_h.get_n_tns("A", threshold=0))
            ids = self.perfect_binary.get_tn_ids("A", threshold=0)
            self.assertEqual(len(ids), 0)
            names = [self.label_names[i] for i in range(len(self.label_data2["A"])) if self.label_data2["A"][i] == 0]
            ids = self.perfect_binary.get_tn_ids("A")
            self.assertEqual(set(ids), set(names))

    def test_get_n_tns(self):
        with captured_output() as (_, _):
            n_tns = self.perfect_binary.get_n_tns("A", threshold=0)
            self.assertEqual(n_tns, 0)
            n_tns = self.perfect_binary.get_n_tns("B", threshold=0)
            self.assertEqual(n_tns, 0)
            n_tns = self.cm_h.get_n_tns("A", threshold=1)
            names = [self.label_names[i] for i in range(len(self.label_data["A"])) if self.label_data["A"][i] == 0]
            self.assertEqual(n_tns, len(names))

    def test_confusion_matrix_again(self):
        with captured_output() as (_, _):
            fns = self.perfect_binary.get_n_fns("A")
            fps = self.perfect_binary.get_n_fps("A")
            tps = self.perfect_binary.get_n_tps("A")
            tns = self.perfect_binary.get_n_tns("A")

            binary_confusion = self.perfect_binary.confusion_matrix()
            self.assertEqual(binary_confusion[1][1], tns)
            self.assertEqual(binary_confusion[0][1], fps)
            self.assertEqual(binary_confusion[1][0], fns)
            self.assertEqual(binary_confusion[0][0], tps)

    def test_get_n_samples(self):
        with captured_output() as (_, _):
            fns = self.cm_h.get_n_fns("A")
            fps = self.cm_h.get_n_fps("A")
            tps = self.cm_h.get_n_tps("A")
            tns = self.cm_h.get_n_tns("A")
            self.assertEqual(fns+tns+tps+fps, 50)

    def test_plot_calibration_curve(self):
        with captured_output() as (_, _):
            label_data, prob_data = generate_random_label_prob_data(50, list("AB"))
            cm_h = ClassificationMetrics(label_data, prob_data)

            with tempfile.TemporaryDirectory() as tempdir:
                new_file = os.path.join(tempdir, "test.png")
                cm_h.plot_calibration_curve(class_n="A", save_fig_path=new_file)
                self.assertTrue(os.path.exists(new_file))

    def test_plot_calibration_curve2(self):
        with captured_output() as (_, _):
            label_data, prob_data = generate_perfect_label_prob_data(50, list("AB"))
            cm_h = ClassificationMetrics(label_data, prob_data)

            with tempfile.TemporaryDirectory() as tempdir:
                new_file = os.path.join(tempdir, "test.png")
                cm_h.plot_calibration_curve(class_n="A", save_fig_path=new_file)
                self.assertTrue(os.path.exists(new_file))

    def test_plot_calibration_curve3(self):
        with captured_output() as (_, _):
            label_data, prob_data = generate_perfect_label_prob_data(50, list("ABC"))
            cm_h = ClassificationMetrics(label_data, prob_data)

            with tempfile.TemporaryDirectory() as tempdir:
                new_file = os.path.join(tempdir, "test.png")
                cm_h.plot_calibration_curve(class_n="A", save_fig_path=new_file)
                self.assertTrue(os.path.exists(new_file))

    def test_confusion_matrix(self):
        with captured_output() as (_, _):
            label_data, prob_data = generate_perfect_label_prob_data(50, list("ABCD"))
            cm_h = ClassificationMetrics(label_data, prob_data)

            perfect_confusion = cm_h.confusion_matrix()
            for x in range(4):
                self.assertTrue(perfect_confusion[x][x] != 0)
                a = {0, 1, 2, 3} - {x}
                for y in a:
                    self.assertTrue(perfect_confusion[x][y] == 0)

    def test_plot_roc(self):
        with captured_output() as (_, _):
            label_data, prob_data = generate_perfect_label_prob_data(50, list("AB"))
            cm_h = ClassificationMetrics(label_data, prob_data)

            with tempfile.TemporaryDirectory() as tempdir:
                new_file = os.path.join(tempdir, "test.png")
                cm_h.plot_roc(class_n="A", save_fig_path=new_file)
                self.assertTrue(os.path.exists(new_file))

    def test_plot_precision_recall(self):
        with captured_output() as (_, _):
            label_data, prob_data = generate_perfect_label_prob_data(50, list("AB"))
            cm_h = ClassificationMetrics(label_data, prob_data)

            with tempfile.TemporaryDirectory() as tempdir:
                new_file = os.path.join(tempdir, "test.png")
                cm_h.plot_precision_recall(class_n="A", save_fig_path=new_file)
                self.assertTrue(os.path.exists(new_file))

    def test_plot_micro_average_precision_score(self):
        with captured_output() as (_, _):
            label_data, prob_data = generate_perfect_label_prob_data(50, list("AB"))
            cm_h = ClassificationMetrics(label_data, prob_data)

            with tempfile.TemporaryDirectory() as tempdir:
                new_file = os.path.join(tempdir, "test.png")
                cm_h.plot_micro_average_precision_score(save_fig_path=new_file)
                self.assertTrue(os.path.exists(new_file))

    def test_plot_multiclass_precision_recall(self):
        with captured_output() as (_, _):
            label_data, prob_data = generate_perfect_label_prob_data(50, list("ABC"))
            cm_h = ClassificationMetrics(label_data, prob_data)

            with tempfile.TemporaryDirectory() as tempdir:
                new_file = os.path.join(tempdir, "test.png")
                cm_h.plot_multiclass_precision_recall(save_fig_path=new_file)
                self.assertTrue(os.path.exists(new_file))

    def test_plot_multiclass_roc2(self):
        with captured_output() as (_, _):
            label_data, prob_data = generate_perfect_label_prob_data(50, list("ABC"))
            cm_h = ClassificationMetrics(label_data, prob_data)

            with tempfile.TemporaryDirectory() as tempdir:
                new_file = os.path.join(tempdir, "test.png")
                cm_h.plot_multiclass_roc(save_fig_path=new_file)
                self.assertTrue(os.path.exists(new_file))

    def test_recall(self):
        with captured_output() as (_, _):
            recall = self.perfect_binary.recall(class_n="A", threshold=0.5)
            tpr = self.perfect_binary.true_positive_rate(class_n="A", threshold=0.5)
            sens = self.perfect_binary.sensitivity(class_n="A", threshold=0.5)
            self.assertEqual(sens, 1)
            self.assertEqual(tpr, 1)
            self.assertEqual(recall, 1)

    def test_true_negatives_rate(self):
        with captured_output() as (_, _):
            true_negatives_rate = self.perfect_binary.true_negative_rate(class_n="A", threshold=0.5)
            self.assertEqual(true_negatives_rate, 1)

    def test_false_negatives_rate(self):
        with captured_output() as (_, _):
            false_negatives_rate = self.perfect_binary.false_negative_rate(class_n="A", threshold=0.5)
            self.assertEqual(false_negatives_rate, 0)

    def test_false_positive_rate(self):
        with captured_output() as (_, _):
            false_positive_rate = self.perfect_binary.false_positive_rate(class_n="A", threshold=0.5)
            self.assertEqual(false_positive_rate, 0)

    def test_positive_likelihood_ratio(self):
        with captured_output() as (_, _):
            positive_likelihood_ratio = self.perfect_binary.positive_likelihood_ratio(class_n="A", threshold=0.5)
            self.assertEqual(positive_likelihood_ratio, np.inf)

    def test__get_index_from_threshold(self):
        with captured_output() as (_, _):
            threshold = 0.5
            for x in np.linspace(0, 1, 20):
                index = self.perfect_binary._get_index_from_threshold("A", threshold)
                answer = None
                for x in range(len(self.perfect_binary.thresholds["A"])):
                    if self.perfect_binary.thresholds["A"][x] > threshold:
                        continue
                    else:
                        answer = x - 1
                        break
                self.assertEqual(answer, index)

    def test_plot_confusion_matrix(self):
        with captured_output() as (_, _):
            with tempfile.TemporaryDirectory() as tempdir:
                temp_path = os.path.join(tempdir, "test.png")
                self.perfect_binary.plot_confusion_matrix(save_fig_path=temp_path)
                self.assertTrue(os.path.exists(temp_path))
                temp_path = os.path.join(tempdir, "test2.png")
                self.fifty_fifty.plot_confusion_matrix(threshold=0.50001, save_fig_path=temp_path)
                self.assertTrue(os.path.exists(temp_path))

    def test_get_confusion_matrix(self):
        with captured_output() as (_, _):
            c_matrix = self.perfect_binary.get_confusion_matrix()
            self.assertEqual(c_matrix[0][1], 0)
            self.assertEqual(c_matrix[1][0], 0)

    def test_plot_probability_distribution(self):
        with captured_output() as (_, _):
            with tempfile.TemporaryDirectory() as tempdir:
                temp_path = os.path.join(tempdir, "test.png")
                self.perfect_binary.plot_probability_hist("A", save_fig_path=temp_path)
                self.assertTrue(os.path.exists(temp_path))


if __name__ == '__main__':
    unittest.main()
