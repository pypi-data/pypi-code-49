# coding: utf-8
"""
Author:
    Weichen Shen,wcshen1994@163.com

Reference:
    [1] Feng Y, Lv F, Shen W, et al. Deep Session Interest Network for Click-Through Rate Prediction[J]. arXiv preprint arXiv:1905.06482, 2019.(https://arxiv.org/abs/1905.06482)

"""

import tensorflow as tf

from tensorflow.python.keras.initializers import RandomNormal
from tensorflow.python.keras.layers import (Concatenate, Dense, Embedding,
                                            Flatten, Input)
from tensorflow.python.keras.models import Model
from tensorflow.python.keras.regularizers import l2

from rslib.algo.transformer.contrib import multihead_attention, feedforward
from ..layers.core import DNN, PredictionLayer
from ..layers.sequence import (AttentionSequencePoolingLayer, BiasEncoding,
                               BiLSTM, Transformer)
from ..layers.utils import concat_func


class DSIN(tf.keras.layers.Layer):
    def __init__(self, config, **kwargs):
        self.supports_masking = False
        self.config = config
        super(DSIN, self).__init__()

    def call(self, item_eb, item_his_eb, mask=None):
        item_eb = item_eb[:, 0]
        item_eb = item_eb[:, tf.newaxis]

        hist_emb_size = 32

        match_indices = tf.where(  # [[5, 5, 2, 5, 4],
            tf.equal(0, mask),  # [0, 5, 2, 3, 5],
            x=tf.range(tf.shape(mask)[1]) * tf.ones_like(mask),  # [5, 1, 5, 5, 5]]
            y=(tf.shape(mask)[1]) * tf.ones_like(mask))

        seq_len = tf.reduce_min(match_indices, axis=1)[:,tf.newaxis]

        mask = [tf.cast(mask, tf.float32), tf.cast(mask, tf.float32)]

        num_units = self.config['din_hidden_units']
        num_heads = 8
        num_blocks = 2
        dropout_rate = 0

        u_emb = [attention_net(item_his_eb[i], item_his_eb[i], num_units, num_heads, num_blocks, dropout_rate, False, mask, i) for i in range(3)]
        # sess_fea = tf.concat(tf.reduce_mean(u_emb, axis=1, keep_dims=True), 1)
        print(tf.shape(u_emb[0]))
        sess_fea = tf.concat([tf.reduce_mean(x, 1, keep_dims=True) for x in u_emb], 1)

        interest_attention_layer = AttentionSequencePoolingLayer(att_hidden_units=(64, 16), weight_normalization=True)(
            [item_eb, sess_fea, seq_len])

        lstm_outputs = BiLSTM(num_units, layers=2, res_layers=0, dropout_rate=0.0)(sess_fea)
        lstm_attention_layer = AttentionSequencePoolingLayer(att_hidden_units=(64, 16), weight_normalization=True)(
            [item_eb, lstm_outputs, seq_len])

        return Flatten()(interest_attention_layer), Flatten()(lstm_attention_layer)


def attention_net(enc, dec, num_units, num_heads, num_blocks, dropout_rate,
                  reuse, mask, i):
    with tf.variable_scope("all" + str(i), reuse=reuse):
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

        # enc = tf.reshape(enc, [-1, num_units])
        return enc
