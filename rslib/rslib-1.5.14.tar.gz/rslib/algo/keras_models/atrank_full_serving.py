import os
import json
import numpy as np
import tensorflow as tf
from tensorflow.python import keras
from tensorflow.python.keras import layers, regularizers

from tensorflow.python.keras.models import Model
from tensorflow.python.keras import backend as K
from ..sparse_dnn.DenseLayerForSparse import DenseLayerForSparse
from ..transformer.ATRank_full import ATRank
from ..layers.interaction import BiInteractionPooling


def get_model(config):
    '''

    :param config:
    :return:
    '''

    # batchsize = config['batchsize']
    # maxlen = config['maxlen']
    # class_num = config['class_num']
    # hidden_unit = config['atrank_hidden_units']
    # emb_size = config['atrank_emb_size']
    #
    # user_size = config['user_size']
    # cross_feature_num = config['cross_feature_num']
    # user_feature_num = config['user_feature_num']
    # user_feature_size = config['user_feature_size']
    # output_unit = config['output_unit']
    # seq_num = config['seq_num']
    # seq_group_index = config['atrank_seq_group']
    # target_seq = config['atrank_target_seq']
    # is_amp = config['is_amp']

    emb_size = 32
    is_amp = False
    cross_feature_num = 10000+1
    user_feature_num = 12
    user_feature_size = 100000+1
    output_unit = 2

    # role_id_input = layers.Input(batch_size=batchsize,shape=(), dtype='int32')
    # seq_id_input = layers.Input(batch_size=batchsize,shape=(seq_num, maxlen,), dtype='int32')
    # seq_time_input = layers.Input(batch_size=batchsize,shape=(seq_num, maxlen,), dtype='int32')
    # seq_time_gaps_input = layers.Input(batch_size=batchsize,shape=(seq_num, maxlen,), dtype='int32')
    # cross_feature_input = layers.Input(shape=(cross_feature_num,), dtype='float32', sparse=True)
    # cross_feature_indices = layers.Input(batch_size=batchsize,shape=(2,), dtype='int64')
    # cross_feature_values = layers.Input(batch_size=batchsize,shape=(), dtype='float32')
    user_feature_input = layers.Input(shape=(user_feature_num,), dtype='int32')
    cross_feature_indices_input = layers.Input(shape=(None, 2,), dtype='int64')
    cross_feature_values_input = layers.Input(shape=(None,), dtype='float32')
    cross_feature_indices = layers.Lambda(lambda x: tf.reshape(x, (-1, 2)))(cross_feature_indices_input)
    cross_feature_values = layers.Lambda(lambda x: tf.reshape(x, [-1]))(cross_feature_values_input)

    cross_feature_input = layers.Lambda(lambda x: tf.SparseTensor(indices=x[0], values=x[1], dense_shape=[tf.shape(user_feature_input)[0], cross_feature_num])) \
        ([cross_feature_indices, cross_feature_values])
    #

    # label_week_id_input = layers.Input(shape=(maxlen,), dtype='int32')
    #
    # seq_index_layer = layers.Lambda(lambda x: x[0][:, x[1]])
    #
    # layers_emb_user_id = layers.Embedding(input_dim=user_size, output_dim=emb_size)
    # layers_emb_sequence_feature = [layers.Embedding(input_dim=class_num, output_dim=emb_size) for _ in range(seq_num)]
    # layers_emb_sequence_b = layers.Embedding(input_dim=class_num, output_dim=1,
    #                                          embeddings_initializer=keras.initializers.Zeros())
    #
    layers_emb_fm1_user_feature = layers.Embedding(input_dim=user_feature_size, output_dim=1)
    layers_emb_fm2_user_feature = layers.Embedding(input_dim=user_feature_size, output_dim=emb_size)
    layers_FM = BiInteractionPooling()
    #
    # layers_emb_user_feature = layers.Embedding(input_dim=user_feature_size, output_dim=emb_size)
    #
    # emb_role_id = layers_emb_user_id(role_id_input)
    # dense_role_id = layers.Dense(32, activation='relu', kernel_regularizer=regularizers.l2(0.01))(emb_role_id)
    #
    dense_cross_feature = DenseLayerForSparse(cross_feature_num, 64, 'relu')(cross_feature_input)

    user_feature_1 = layers.Flatten()(layers_emb_fm1_user_feature(user_feature_input))
    user_feature_2 = layers.Flatten()(layers_FM(layers_emb_fm2_user_feature(user_feature_input)))
    user_feature = layers.Concatenate(axis=1)([user_feature_1, user_feature_2])
    #
    # # i
    # list_seq_emb = []
    # for i in target_seq:
    #     seq_i = seq_index_layer([seq_id_input, i])
    #     emb_seq_i = layers_emb_sequence_feature[0](seq_i)
    #     list_seq_emb.append(emb_seq_i)
    #
    # emb_group_target = layers.Concatenate(axis=2)(list_seq_emb) if len(list_seq_emb) > 1 else list_seq_emb[0]
    #
    # dense_group_target = layers.Dense(hidden_unit, kernel_regularizer=regularizers.l2(0.01))(emb_group_target)
    # time_mask_group_target = seq_index_layer([seq_time_input, target_seq[0]])
    #
    # emb_b_group_target = layers_emb_sequence_b(seq_index_layer([seq_id_input, target_seq[0]]))
    #
    # # seq
    # list_group_dense = []
    # list_group_time_mask = []
    # for seqs in seq_group_index:
    #     list_seq_emb = []
    #     for i in seqs:
    #         seq_i = seq_index_layer([seq_id_input, i])
    #         emb_seq_i = layers_emb_sequence_feature[i](seq_i)
    #         list_seq_emb.append(emb_seq_i)
    #
    #     emb_group_j = layers.Concatenate(axis=2)(list_seq_emb) if len(list_seq_emb) > 1 else list_seq_emb[0]
    #
    #     dense_group_j = layers.Dense(hidden_unit, kernel_regularizer=regularizers.l2(0.01))(emb_group_j)
    #     list_group_dense.append(dense_group_j)
    #
    #     time_mask_group_j = seq_index_layer([seq_time_input, seqs[0]])
    #     list_group_time_mask.append(time_mask_group_j)
    #
    # dense_all = layers.Concatenate(axis=1)(list_group_dense) if len(list_group_dense) > 1 else list_group_dense[0]
    # dense_all = layers.Dense(hidden_unit, kernel_regularizer=regularizers.l2(0.01))(dense_all)
    #
    # time_mask_all = layers.Concatenate(axis=1)(list_group_time_mask) if len(list_group_time_mask) > 1 else \
    #     list_group_time_mask[0]
    #
    # seq_embedding = ATRank(config=config)(dense_group_target, dense_all,
    #                                       mask=[time_mask_all, time_mask_group_target])
    #
    # all_feature = layers.Concatenate(axis=-1)([seq_embedding, dense_cross_feature, user_feature])
    all_feature = layers.Concatenate(axis=-1)([dense_cross_feature, user_feature])
    # output = layers.Dense(128, activation='relu', kernel_regularizer=regularizers.l2(0.01))(all_feature)
    #
    output = layers.Dense(output_unit, activation='softmax')(all_feature)

    model = Model(inputs=[user_feature_input, cross_feature_indices_input, cross_feature_values_input
                          ], outputs=[output])
    # model = Model(inputs=[role_id_input, seq_id_input, seq_time_input, seq_time_gaps_input, cross_feature_indices, cross_feature_values,
    #                       user_feature_input, label_week_id_input], outputs=[output])

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
