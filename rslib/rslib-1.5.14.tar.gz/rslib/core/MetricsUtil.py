#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2019 NetEase.com, Inc. All Rights Reserved.
# Copyright 2019, The NSH Recommendation Project, The User Persona Group, The Fuxi AI Lab.
"""
MetricsUtil

Authors: wangkai02(wangkai02@corp.netease.com)
Phone: 17816029211
Date: 2019/9/11
"""

import tensorflow as tf
import numpy as np
from sklearn.metrics import roc_auc_score


class MetricsUtil():

    def print_list(self, l):
        return '\n' + '\n'.join([str(x) for x in l]) if type(l) == type([]) else '\n' + str(l)

    def class_statistic(self, data, n):
        tmp = []
        for i in range(1, n):
            tmp.append(len([x for x in data if x.split(' ')[-1] == str(i)]))
        print("num_per_class: ", self.print_list(tmp))

    def class_statistic_common(self, data):
        tmp = {}
        topk_num = len(data[0].split(' ')[-2].split(','))
        for x in data:
            for i in range(topk_num):
                items = x.split(' ')[-2].split(',')
                tmp[items[i]] = tmp.get(items[i],0)+1
        print("num_per_class: ", self.print_list([str(x)+' '+str(tmp[x]) for x in tmp]))

    # 没有区分同一个用户的多次购买
    def gauc_all(self, data, n):
        gauc = []
        for x in data:
            pred = list(map(float, [y for y in x.split(' ')[-2].split(',')]))
            label = int(x.split(' ')[-1])
            p = pred[label]
            auc = 1 - sum([1 for x in pred if x > p]) / (n - 1)
            gauc.append(auc)
        print("gauc: ", sum(gauc) / len(gauc))

    def gauc_all_common(self, data):
        gauc = []
        for x in data:
            items_recom = [y for y in x.split(' ')[-2].split(',')]
            items_pos = [y for y in x.split(' ')[-1].split(',')]
            items_label = [1 if x in items_pos else 0 for x in items_recom]
            items_pred = [1-i/10000000 for i in range(len(items_recom))]
            if sum(items_label)>0:
                gauc.append(roc_auc_score(items_label, items_pred))
            else:
                gauc.append(0)
        print("gauc: ", sum(gauc) / len(gauc))

    def gauc_binary(self, data):
        gauc_add = 0.0
        print(len(data))
        count = 0
        for y_test, y_pred in data:
            if (y_test == 1).all() or (y_test == 0).all():
                continue
            # print(roc_auc_score(y_test, y_pred))
            gauc_add += roc_auc_score(y_test, y_pred)
            count += 1
        print("gauc: ", gauc_add / count)

    def auc_all(self, data, n):
        pred = tf.identity(list(map(float, [y for x in data for y in x.split(' ')[-2].split(',')]))[:200000])
        label = tf.identity([1 if x.split(' ')[-1] == str(j) else 0 for x in data for j in range(len(x.split(' ')[-2].split(',')))][:200000])
        auc_all_op = tf.metrics.auc(label, pred)[1]
        with tf.Session() as sess:
            sess.run(tf.local_variables_initializer())
            print("auc_all: ", self.print_list(sess.run(auc_all_op)))

    def auc_per_class(self, data, n):
        auc_op = []
        for i in range(1, n):
            tmp = [x for x in data if x.split(' ')[-1] == str(i)]
            pred = tf.identity(list(map(float, [y for x in tmp for y in x.split(' ')[-2].split(',')])))
            label = tf.identity([1 if x.split(' ')[-1] == str(j) else 0 for x in tmp for j in range(len(x.split(' ')[-2].split(',')))])
            auc_op.append(tf.metrics.auc(label, pred)[1] if len(tmp) > 1 else tf.identity(0))
        with tf.Session() as sess:
            sess.run(tf.local_variables_initializer())
            print("auc: ", self.print_list(sess.run(auc_op)))
            # print("auc_all: ", self.print_list(sess.run(auc_all_op)))

    def topk_all(self, data, n, k):
        assert np.min([int(x.split(' ')[-1]) for x in data]) > 0
        y_true = tf.identity(np.array([int(x.split(' ')[-1]) for x in data]).astype(np.int64))
        y_pred = tf.identity(np.array([list(map(float, x.split(' ')[-2].split(','))) for x in data]))
        recall_all = tf.metrics.recall_at_k(y_true, y_pred, k)[1]
        precision_all = tf.metrics.precision_at_k(y_true, y_pred, k)[1]
        with tf.Session() as sess:
            sess.run(tf.local_variables_initializer())
            print("update_recall_all_at_%s: " % (k), self.print_list(sess.run(recall_all)))
            print("update_precision_all_at_%s: " % (k), self.print_list(sess.run(precision_all)))

    def topk_all_common(self, data, k):
        recalls = []
        precisions = []
        for x in data:
            items_recom = [y for y in x.split(' ')[-2].split(',')[:k]]
            items_pos = [y for y in x.split(' ')[-1].split(',')]
            recalls.append(sum([1 if x in items_recom else 0 for x in items_pos])/len(items_pos))
            precisions.append(sum([1 if x in items_pos else 0 for x in items_recom])/len(items_recom))
        print("update_recall_all_at_%s: " % (k), sum(recalls)/len(recalls))
        print("update_precision_all_at_%s: " % (k), sum(precisions)/len(precisions))

    def topk_per_class(self, data, n, k):
        recall_op = []
        precision_op = []
        assert np.min([int(x.split(' ')[-1]) for x in data]) > 0
        for i in range(1, n):
            tmp = [x for x in data if x.split(' ')[-1] == str(i)]
            y_true = tf.identity(np.array([int(x.split(' ')[-1]) for x in tmp]).astype(np.int64))
            y_pred = tf.identity(np.array([list(map(float, x.split(' ')[-2].split(','))) for x in tmp]))
            recall_op.append(tf.metrics.recall_at_k(y_true, y_pred, k)[1] if len(tmp) > 1 else tf.identity(0))
            precision_op.append(tf.metrics.precision_at_k(y_true, y_pred, k)[1] if len(tmp) > 1 else tf.identity(0))
        with tf.Session() as sess:
            sess.run(tf.local_variables_initializer())
            print(sess.run([y_true, y_pred]))
            print("update_recall_at_%s: " % (k), self.print_list(sess.run(recall_op)))
            print("update_precision_at_%s: " % (k), self.print_list(sess.run(precision_op)))

