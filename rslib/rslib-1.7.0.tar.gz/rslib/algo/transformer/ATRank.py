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
from tensorflow.python.keras import backend as K

class ATRank(tf.keras.layers.Layer):
    def __init__(self, config):
        self.supports_masking = False
        self.config = config
        super(ATRank, self).__init__()

    def call(self, i_emb, i_b, h_emb, mask=None):
        i_emb = i_emb[:, 0]
        i_b = i_b[:, 0]
        mask = [tf.cast(mask[0], tf.float32), tf.cast(mask[1], tf.float32)]

        num_blocks = self.config['atrank_num_blocks']
        num_heads = self.config['atrank_num_heads']
        dropout_rate = self.config['atrank_dropout_rate']
        num_units = h_emb.get_shape().as_list()[-1]

        # 序列模型
        u_emb, att, stt = attention_net(h_emb, i_emb, num_units, num_heads, num_blocks, dropout_rate, False, mask)

        logits = i_b + tf.reduce_sum(tf.multiply(u_emb, i_emb), 1, keepdims=True)
        logits = tf.reshape(logits, [32, 1])

        return logits

    # def compute_output_shape(self, input_shape):
    #     return (input_shape[0][0],input_shape[0][1])

    def compute_mask(self, input, input_mask=None):
        # need not to pass the mask to next layers
        return None


def attention_net(enc, dec, num_units, num_heads, num_blocks, dropout_rate,
                  reuse, mask):
    with tf.variable_scope("all", reuse=reuse):
        with tf.variable_scope("user_hist_group"):
            for i in range(num_blocks):
                with tf.variable_scope("num_blocks_{}".format(i)):
                    ### Multihead Attention
                    enc, stt_vec = multihead_attention(
                        queries=enc,
                        keys=enc,
                        num_units=num_units,
                        num_heads=num_heads,
                        dropout_rate=dropout_rate,
                        mask=mask,
                        scope="self_attention")

                    ### Feed Forward
                    enc = feedforward(enc,
                                      num_units=[num_units // 4, num_units],
                                      scope="feed_forward",
                                      reuse=reuse)

        dec = tf.expand_dims(dec, 1)
        with tf.variable_scope("item_feature_group"):
            for i in range(num_blocks):
                with tf.variable_scope("num_blocks_{}".format(i)):
                    mask0 = mask[1]
                    mask1 = tf.ones([tf.shape(dec)[0], 1], dtype='float32')
                    # mask0 = K.print_tensor(mask0, 'mask0 is ')
                    # mask1 = K.print_tensor(mask1, 'mask1 is ')
                    ## Multihead Attention ( vanilla attention)
                    dec, att_vec = multihead_attention(
                        queries=dec,
                        keys=enc,
                        num_units=num_units,
                        num_heads=num_heads,
                        dropout_rate=dropout_rate,
                        mask=[mask0, mask1],
                        scope="vanilla_attention"
                    )

                    ## Feed Forward
                    dec = feedforward(dec,
                                      num_units=[num_units // 4, num_units],
                                      scope="feed_forward",
                                      reuse=reuse)

        dec = tf.reshape(dec, [-1, num_units])
        return dec, att_vec, stt_vec
