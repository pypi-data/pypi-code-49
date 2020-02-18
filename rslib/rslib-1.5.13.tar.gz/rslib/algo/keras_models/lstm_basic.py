#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2019 NetEase.com, Inc. All Rights Reserved.
# Copyright 2019, The NSH Recommendation Project, The User Persona Group, The Fuxi AI Lab.
"""
keras_lstm

Authors: wangkai02(wangkai02@corp.netease.com)
Phone: 17816029211
Date: 2019/9/11
"""

import tensorflow as tf

from tensorflow.python.keras import layers, regularizers
from tensorflow.python.keras.backend import _constant_to_tensor, epsilon
from tensorflow.python.keras.models import Model
from tensorflow.python.keras import backend as K

from rslib.algo.layers.interaction import BiInteractionPooling
from rslib.core.LossUtil import masked_categorical_crossentropy, zzn_loss
from ..sparse_dnn.DenseLayerForSparse import DenseLayerForSparse


def get_model(config):
    activation = 'relu'
    maxlen = config['maxlen']
    class_num = config['class_num']
    hidden_unit = config['lstm_hidden_units']
    emb_size = config['lstm_emb_size']

    user_size = config['user_size']
    cross_feature_num = config['cross_feature_num']
    user_feature_num = config['user_feature_num']
    user_feature_size = config['user_feature_size']
    output_unit = config['output_unit']
    seq_num = config['seq_num']
    # seq_group_index = config['atrank_seq_group']
    # target_seq = config['atrank_target_seq']
    is_amp = config['is_amp']
    is_serving = config['is_serving']

    role_id_input = layers.Input(shape=(), dtype='int32')
    seq_id_input = layers.Input(shape=(seq_num, maxlen,), dtype='int32')
    seq_time_input = layers.Input(shape=(seq_num, maxlen,), dtype='int32')
    seq_time_gaps_input = layers.Input(shape=(seq_num, maxlen,), dtype='int32')
    if is_serving:
        cross_feature_indices_input = layers.Input(shape=(None, 2,), dtype='int64')
        cross_feature_values_input = layers.Input(shape=(None,), dtype='float32')
        cross_feature_indices = layers.Lambda(lambda x: tf.reshape(x, (-1, 2)))(cross_feature_indices_input)
        cross_feature_values = layers.Lambda(lambda x: tf.reshape(x, [-1]))(cross_feature_values_input)
        cross_feature_input = layers.Lambda(lambda x: tf.SparseTensor(indices=x[0], values=x[1], dense_shape=[tf.shape(seq_id_input)[0], cross_feature_num])) \
            ([cross_feature_indices, cross_feature_values])
    else:
        cross_feature_input = layers.Input(shape=(cross_feature_num,), dtype='float32', sparse=True)
    user_feature_input = layers.Input(shape=(user_feature_num,), dtype='int32')
    output_mask_input = layers.Input(shape=(output_unit,), dtype='float32')
    cur_time_input = layers.Input(shape=(), dtype='int32')

    # layers_emb_user_id = layers.Embedding(input_dim=user_size, output_dim=emb_size)
    # emb_role_id = layers_emb_user_id(role_id_input)

    seq_index_layer = layers.Lambda(lambda x: x[0][:, x[1]])

    seqs_lstm = []
    for i in range(seq_num):
        seq_i = seq_index_layer([seq_id_input, i])
        seq_i_embeddings = layers.Embedding(class_num, emb_size, mask_zero=True)(seq_i)
        seq_i_lstm = layers.LSTM(units=hidden_unit)(seq_i_embeddings)
        seqs_lstm.append(seq_i_lstm)

    seqs_embeddings = layers.Concatenate(axis=-1)(seqs_lstm) if len(seqs_lstm)>1 else seqs_lstm[0]

    cross_feature = DenseLayerForSparse(cross_feature_num, hidden_unit, activation)(cross_feature_input)

    layers_emb_fm1_user_feature = layers.Embedding(input_dim=user_feature_size, output_dim=1)
    layers_emb_fm2_user_feature = layers.Embedding(input_dim=user_feature_size, output_dim=emb_size)
    layers_FM = BiInteractionPooling()
    user_feature_1 = layers.Flatten()(layers_emb_fm1_user_feature(user_feature_input))
    user_feature_2 = layers.Flatten()(layers_FM(layers_emb_fm2_user_feature(user_feature_input)))
    user_feature = layers.Concatenate(axis=1)([user_feature_1, user_feature_2])

    all_feature = layers.Concatenate(axis=-1)([seqs_embeddings, cross_feature, user_feature])
    # output = layers.Dense(output_unit, activation='softmax')(all_feature)

    output = layers.Dense(output_unit)(all_feature)
    if is_serving:
        output = tf.sigmoid(output)
    else:
        paddings = tf.ones_like(output) * (-2 ** 32 + 1)
        output = tf.where(tf.equal(output_mask_input, 0), paddings, output)
        output = tf.sigmoid(output)

    # output = tf.multiply(tf.exp(output), output_mask)
    # output = output / tf.reduce_sum(output, -1, True)
    # epsilon_ = _constant_to_tensor(epsilon(), output.dtype.base_dtype)
    # output = tf.clip_by_value(output, epsilon_, 1. - epsilon_)

    if is_serving:
        model = Model(inputs=[role_id_input, seq_id_input, seq_time_input, seq_time_gaps_input, cross_feature_indices_input, cross_feature_values_input,
                              user_feature_input, cur_time_input], outputs=[output])
    else:
        model = Model(inputs=[role_id_input, seq_id_input, seq_time_input, seq_time_gaps_input, cross_feature_input,
                              user_feature_input, output_mask_input, cur_time_input], outputs=[output])

    # for layer in model.layers:
    #     if hasattr(layer, 'kernel_regularizer'):
    #         layer.kernel_regularizer = regularizers.l2(0.000001)

    opt = tf.keras.optimizers.Adam()
    # opt = tf.keras.optimizers.SGD(0.1)
    if is_amp:
        opt = tf.train.experimental.enable_mixed_precision_graph_rewrite(opt)
    loss_dict = {'1': 'mean_squared_error'}
    # loss = zzn_loss
    # loss = 'categorical_crossentropy'
    loss = 'binary_crossentropy'
    model.compile(loss=loss_dict.get(str(output_unit), loss),
                  optimizer=opt,
                  metrics=['binary_accuracy'])

    sess = K.get_session()
    sess.run(tf.compat.v1.local_variables_initializer())
    sess.run(tf.compat.v1.global_variables_initializer())
    sess.run(tf.compat.v1.tables_initializer())
    print(model.summary())
    return model
