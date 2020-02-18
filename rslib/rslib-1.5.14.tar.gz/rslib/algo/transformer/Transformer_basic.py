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

class Transformer_basic(tf.keras.layers.Layer):
    def __init__(self, config):
        self.supports_masking = False
        self.config = config
        super(Transformer_basic, self).__init__()

    def call(self, x, mask=None):
        # Embedding
        enc_embed_input = x[0]
        # time = x[1]
        # time_gap = x[2]
        hidden_units = self.config['transformer_hidden_units']
        mask = [tf.cast(mask[0],tf.float32),tf.cast(mask[1],tf.float32)]

        print('[transformer_model] enc_input', enc_embed_input.get_shape())
        with tf.variable_scope("encoder"):
            enc = enc_embed_input

            # temporal position encoding
            temporal_pe = None

            enc += positional_encoding(enc_embed_input,
                                        num_units=hidden_units,
                                        scale=False,
                                        scope="enc_pe")

            # Dropout
            if self.config['transformer_is_training']:
                enc = tf.layers.dropout(enc,
                                        rate=self.config['transformer_dropout_rate'],
                                        training=tf.convert_to_tensor(self.config['transformer_is_training']))
            # Blocks
            for i in range(self.config['transformer_num_blocks']):
                with tf.variable_scope("num_blocks_{}".format(i)):
                    enc, align_score = multihead_attention(queries=enc,
                                                            keys=enc,
                                                            num_units=hidden_units,
                                                            num_heads=self.config['transformer_num_heads'],
                                                            dropout_rate=self.config['transformer_dropout_rate'],
                                                            is_training=self.config['transformer_is_training'],
                                                            mask = mask)
                    enc = feedforward(enc, num_units=[4 * hidden_units, hidden_units])

            query_encoding = tf.keras.layers.GlobalAveragePooling1D()(enc)
            enc3 = tf.reshape(query_encoding, [-1, hidden_units])

        return enc3

    # def compute_output_shape(self, input_shape):
    #     return (input_shape[0][0],input_shape[0][1])

    def compute_mask(self, input, input_mask=None):
        # need not to pass the mask to next layers
        return None
