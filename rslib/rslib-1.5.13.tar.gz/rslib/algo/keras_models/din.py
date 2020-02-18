import os
import json
import numpy as np
import tensorflow as tf

from tensorflow_core.python import keras
from tensorflow_core.python.keras import layers, regularizers

from tensorflow.python.keras.models import Model
from tensorflow.python.keras import backend as K

# from rslib.algo.layers.sequence import AttentionSequencePoolingLayer
from ..sparse_dnn.DenseLayerForSparse import DenseLayerForSparse
from ..transformer.DIN import DIN
from ..layers.interaction import BiInteractionPooling


def get_model(config):
    '''

    :param config:
    :return:
    '''
    maxlen = config['maxlen']
    class_num = config['class_num']
    hidden_unit = config['din_hidden_units']
    emb_size = config['din_emb_size']

    user_size = config['user_size']
    cross_feature_num = config['cross_feature_num']
    user_feature_num = config['user_feature_num']
    user_feature_size = config['user_feature_size']
    output_unit = config['output_unit']
    seq_num = config['seq_num']
    seq_group_index = config['din_seq_group']
    target_seq = config['din_target_seq']
    is_amp = config['is_amp']

    role_id_input = layers.Input(shape=(), dtype='int32')
    seq_id_input = layers.Input(shape=(seq_num, maxlen,), dtype='int32')
    seq_time_input = layers.Input(shape=(seq_num, maxlen,), dtype='int32')
    seq_time_gaps_input = layers.Input(shape=(seq_num, maxlen,), dtype='int32')
    cross_feature_input = layers.Input(shape=(cross_feature_num,), dtype='float32', sparse=True)
    user_feature_input = layers.Input(shape=(user_feature_num,), dtype='int32')
    label_week_id_input = layers.Input(shape=(maxlen,), dtype='int32')

    seq_index_layer = layers.Lambda(lambda x: x[0][:, x[1]])

    layers_emb_user_id = layers.Embedding(input_dim=user_size, output_dim=emb_size)
    layers_emb_sequence_feature = [layers.Embedding(input_dim=class_num, output_dim=emb_size) for _ in range(seq_num)]
    layers_emb_sequence_b = layers.Embedding(input_dim=class_num, output_dim=1,
                                             embeddings_initializer=keras.initializers.Zeros())

    layers_emb_user_feature = layers.Embedding(input_dim=user_feature_size, output_dim=emb_size)

    emb_role_id = layers_emb_user_id(role_id_input)
    dense_role_id = layers.Dense(32, activation='relu')(emb_role_id)

    dense_cross_feature = DenseLayerForSparse(cross_feature_num, 64, 'relu')(cross_feature_input)

    user_feature = layers.Flatten()(layers_emb_user_feature(user_feature_input))

    # i
    list_seq_emb = []
    for i in target_seq:
        seq_i = seq_index_layer([seq_id_input, i])
        emb_seq_i = layers_emb_sequence_feature[0](seq_i)
        list_seq_emb.append(emb_seq_i)

    emb_group_target = layers.Concatenate(axis=-1)(list_seq_emb) if len(list_seq_emb) > 1 else list_seq_emb[0]
    dense_group_target = emb_group_target

    # seq
    list_group_dense = []
    list_group_time_mask = []
    seq_group_index = [[0]]
    for seqs in seq_group_index:
        for i in seqs:
            seq_i = seq_index_layer([seq_id_input, i])
            emb_seq_i = layers_emb_sequence_feature[i](seq_i)
            list_group_dense.append(emb_seq_i)

        time_mask_group_j = seq_index_layer([seq_time_input, seqs[0]])
        list_group_time_mask.append(time_mask_group_j)

    dense_all = layers.Concatenate(axis=-1)(list_group_dense) if len(list_group_dense) > 1 else list_group_dense[0]
    time_mask_all = layers.Concatenate(axis=1)(list_group_time_mask) if len(list_group_time_mask) > 1 else \
        list_group_time_mask[0]

    seq_embedding = DIN(config=config)(dense_group_target, dense_all, mask=time_mask_all)

    all_feature = layers.Concatenate(axis=-1)([seq_embedding, dense_cross_feature, user_feature, seq_index_layer([dense_group_target, 0])])
    output = all_feature
    # output = layers.Dense(128, activation='relu')(all_feature)

    output = layers.Dense(output_unit, activation='softmax')(output)

    model = Model(inputs=[role_id_input, seq_id_input, seq_time_input, seq_time_gaps_input, cross_feature_input,
                          user_feature_input, label_week_id_input], outputs=[output])

    for layer in model.layers:
        if hasattr(layer, 'kernel_regularizer'):
            layer.kernel_regularizer = regularizers.l2(0.000001)

    opt = tf.keras.optimizers.Adam()
    # opt = tf.keras.optimizers.SGD()

    if is_amp:
        opt = tf.train.experimental.enable_mixed_precision_graph_rewrite(opt)
    loss_dict = {'1': 'mean_squared_error'}
    model.compile(loss=loss_dict.get(str(output_unit), 'categorical_crossentropy'),
                  optimizer=opt,
                  metrics=['accuracy'])

    sess = K.get_session()
    sess.run(tf.compat.v1.local_variables_initializer())
    sess.run(tf.compat.v1.global_variables_initializer())
    sess.run(tf.compat.v1.tables_initializer())
    print(model.summary())
    return model
