import os
import json
import numpy as np
import tensorflow as tf
from tensorflow_core.python import keras
from tensorflow_core.python.keras import layers
from tensorflow.python.keras.models import Model
from tensorflow.python.keras import backend as K
from ..sparse_dnn.DenseLayerForSparse import DenseLayerForSparse
from ..transformer.ATRank import ATRank
from tensorflow.python.keras.engine.base_layer import Layer



def get_model(config):
    '''
    get a basic atrank model.
    :param config: the config of the basic atrank model.
    :return: model
    '''
    maxlen = config['maxlen']
    class_num = config['class_num']
    hidden_unit = config['atrank_hidden_units']
    emb_size = config['atrank_emb_size']

    user_size = config['user_size']
    cross_feature_num = config['cross_feature_num']
    user_feature_num = config['user_feature_num']
    user_feature_size = config['user_feature_size']
    output_unit = config['output_unit']
    seq_num = config['seq_num']
    # seq_group_index = config['atrank_seq_group']
    # target_seq = config['atrank_target_seq']
    is_amp = config['is_amp']

    role_id_input = layers.Input(shape=(), dtype='int32')
    seq_id_input = layers.Input(shape=(seq_num, maxlen,), dtype='int32')
    seq_time_input = layers.Input(shape=(seq_num, maxlen,), dtype='int32')
    seq_time_gaps_input = layers.Input(shape=(seq_num, maxlen,), dtype='int32')
    cross_feature_input = layers.Input(shape=(cross_feature_num,), dtype='float32', sparse=True)
    user_feature_input = layers.Input(shape=(user_feature_num,), dtype='int32')
    label_week_id_input = layers.Input(shape=(maxlen,), dtype='int32')

    seq_index_layer = layers.Lambda(lambda x: x[0][:, x[1]])

    seq_id_i = seq_index_layer([seq_id_input, -1])
    seq_id_hist = seq_index_layer([seq_id_input, 0])
    seq_time_hist = seq_index_layer([seq_time_input, 0])

    item_embedding = layers.Embedding(input_dim=config['class_num'], output_dim=emb_size)
    item_b_embedding = layers.Embedding(input_dim=config['class_num'], output_dim=1,
                                        embeddings_initializer=keras.initializers.Zeros())

    i_emb = item_embedding(seq_id_i)
    i_b_emb = item_b_embedding(seq_id_i)
    h_emb = item_embedding(seq_id_hist)

    i_emb = layers.Dense(config['atrank_hidden_units'])(i_emb)
    h_emb = layers.Dense(config['atrank_hidden_units'])(h_emb)

    output = ATRank(config=config)(i_emb, i_b_emb, h_emb,
                                   mask=[seq_time_hist, seq_time_hist])
    output = layers.Dense(output_unit, activation='softmax')(output)
    model = Model(inputs=[role_id_input, seq_id_input, seq_time_input, seq_time_gaps_input, cross_feature_input,
                          user_feature_input, label_week_id_input], outputs=[output])

    opt = tf.keras.optimizers.Adam()
    # opt = tf.keras.optimizers.SGD(0.01)
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
