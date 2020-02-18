#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2019 NetEase.com, Inc. All Rights Reserved.
# Copyright 2019, The NSH Recommendation Project, The User Persona Group, The Fuxi AI Lab.
"""
Transformer

Authors: wangkai02(wangkai02@corp.netease.com)
Phone: 17816029211
Date: 2019/9/11
"""

from .contrib import *
# import tensorflow_core as tf
from tensorflow_core.python.keras import backend as K


class DIN(tf.keras.layers.Layer):
    def __init__(self, config, **kwargs):
        self.supports_masking = False
        self.config = config
        super(DIN, self).__init__()

    def call(self, i_emb, h_emb, mask=None):
        hidden_units = self.config['din_hidden_units']

        mask = tf.cast(mask, tf.float32)
        i_emb = i_emb[:, 0]
        hist_i = attention(i_emb, h_emb, mask)
        # -- attention end ---

        hist_i = tf.layers.batch_normalization(inputs=hist_i)
        hist_i = tf.reshape(hist_i, [-1, hidden_units], name='hist_bn')
        hist_i = tf.layers.dense(hist_i, hidden_units, name='hist_fcn')

        u_emb_i = hist_i

        din_i = tf.concat([u_emb_i, i_emb], axis=-1)
        din_i = tf.layers.batch_normalization(inputs=din_i, name='b1')
        # d_layer_1_i = tf.layers.dense(din_i, 80, activation=tf.nn.sigmoid, name='f1')
        # d_layer_2_i = tf.layers.dense(d_layer_1_i, 40, activation=tf.nn.sigmoid, name='f2')
        d_layer_1_i = tf.layers.dense(din_i, hidden_units, activation=tf.nn.sigmoid, name='f1')
        d_layer_2_i = tf.layers.dense(d_layer_1_i, hidden_units, activation=tf.nn.sigmoid, name='f2')
        # d_layer_3_i = tf.layers.dense(d_layer_2_i, 1, activation=None, name='f3')
        logits = d_layer_2_i

        return logits

    # def compute_output_shape(self, input_shape):
    #     return (input_shape[0][0],input_shape[0][1])

    def compute_mask(self, input, input_mask=None):
        # need not to pass the mask to next layers
        return None


def attention(queries, keys, mask):
    '''
      queries:     [B, H]
      keys:        [B, T, H]
      keys_length: [B]
    '''

    queries_hidden_units = queries.get_shape().as_list()[-1]
    queries = tf.tile(queries, [1, tf.shape(keys)[1]])
    queries = tf.reshape(queries, [-1, tf.shape(keys)[1], queries_hidden_units])
    din_all = tf.concat([queries, keys, queries - keys, queries * keys], axis=-1)
    d_layer_1_all = tf.layers.dense(din_all, 80, activation=tf.nn.sigmoid, name='f1_att', reuse=tf.AUTO_REUSE)
    d_layer_2_all = tf.layers.dense(d_layer_1_all, 40, activation=tf.nn.sigmoid, name='f2_att', reuse=tf.AUTO_REUSE)
    d_layer_3_all = tf.layers.dense(d_layer_2_all, 1, activation=None, name='f3_att', reuse=tf.AUTO_REUSE)
    d_layer_3_all = tf.reshape(d_layer_3_all, [-1, 1, tf.shape(keys)[1]])
    outputs = d_layer_3_all
    # Mask
    # key_masks = tf.sequence_mask(keys_length, tf.shape(keys)[1])  # [B, T]
    key_masks= mask
    key_masks = tf.expand_dims(key_masks, 1)  # [B, 1, T]
    paddings = tf.ones_like(outputs) * (-2 ** 32 + 1)
    # outputs = tf.where(key_masks, outputs, paddings)  # [B, 1, T]
    outputs = tf.where(tf.equal(key_masks, 0), paddings, outputs)

    # Scale
    outputs = outputs / (keys.get_shape().as_list()[-1] ** 0.5)

    # Activation
    outputs = tf.nn.softmax(outputs)  # [B, 1, T]

    # Weighted sum
    outputs = tf.matmul(outputs, keys)  # [B, 1, H]

    return outputs


def attention_multi_items(queries, keys, keys_length):
    '''
      queries:     [B, N, H] N is the number of ads
      keys:        [B, T, H]
      keys_length: [B]
    '''
    queries_hidden_units = queries.get_shape().as_list()[-1]
    queries_nums = queries.get_shape().as_list()[1]
    queries = tf.tile(queries, [1, 1, tf.shape(keys)[1]])
    queries = tf.reshape(queries, [-1, queries_nums, tf.shape(keys)[1], queries_hidden_units])  # shape : [B, N, T, H]
    max_len = tf.shape(keys)[1]
    keys = tf.tile(keys, [1, queries_nums, 1])
    keys = tf.reshape(keys, [-1, queries_nums, max_len, queries_hidden_units])  # shape : [B, N, T, H]
    din_all = tf.concat([queries, keys, queries - keys, queries * keys], axis=-1)
    d_layer_1_all = tf.layers.dense(din_all, 80, activation=tf.nn.sigmoid, name='f1_att', reuse=tf.AUTO_REUSE)
    d_layer_2_all = tf.layers.dense(d_layer_1_all, 40, activation=tf.nn.sigmoid, name='f2_att', reuse=tf.AUTO_REUSE)
    d_layer_3_all = tf.layers.dense(d_layer_2_all, 1, activation=None, name='f3_att', reuse=tf.AUTO_REUSE)
    d_layer_3_all = tf.reshape(d_layer_3_all, [-1, queries_nums, 1, max_len])
    outputs = d_layer_3_all
    # Mask
    key_masks = tf.sequence_mask(keys_length, max_len)  # [B, T]
    key_masks = tf.tile(key_masks, [1, queries_nums])
    key_masks = tf.reshape(key_masks, [-1, queries_nums, 1, max_len])  # shape : [B, N, 1, T]
    paddings = tf.ones_like(outputs) * (-2 ** 32 + 1)
    outputs = tf.where(key_masks, outputs, paddings)  # [B, N, 1, T]

    # Scale
    outputs = outputs / (keys.get_shape().as_list()[-1] ** 0.5)

    # Activation
    outputs = tf.nn.softmax(outputs)  # [B, N, 1, T]
    outputs = tf.reshape(outputs, [-1, 1, max_len])
    keys = tf.reshape(keys, [-1, max_len, queries_hidden_units])
    # print outputs.get_shape().as_list()
    # print keys.get_sahpe().as_list()
    # Weighted sum
    outputs = tf.matmul(outputs, keys)
    outputs = tf.reshape(outputs, [-1, queries_nums, queries_hidden_units])  # [B, N, 1, H]
    return outputs
