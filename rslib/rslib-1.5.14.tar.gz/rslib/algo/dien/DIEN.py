import tensorflow as tf
from tensorflow.python.ops.rnn_cell import GRUCell
from tensorflow.python.ops.rnn_cell import LSTMCell
from tensorflow.python.ops.rnn import bidirectional_dynamic_rnn as bi_rnn
# from tensorflow.python.ops.rnn import tf.nn.dynamic_rnn
from .rnn import dynamic_rnn
from .utils import *
from .Dice import dice


class DIEN(tf.keras.layers.Layer):
    def __init__(self, config, **kwargs):
        self.supports_masking = False
        self.config = config
        super(DIEN, self).__init__()

    def call(self, item_eb, item_his_eb, item_his_eb_sum, mask=None):

        match_indices = tf.where(  # [[5, 5, 2, 5, 4],
            tf.equal(0, mask),  # [0, 5, 2, 3, 5],
            x=tf.range(tf.shape(mask)[1]) * tf.ones_like(mask),  # [5, 1, 5, 5, 5]]
            y=(tf.shape(mask)[1]) * tf.ones_like(mask))

        seq_len = tf.reduce_min(match_indices, axis=1)

        HIDDEN_SIZE = self.config['din_hidden_units']
        ATTENTION_SIZE = self.config['din_attention_units']
        mask = tf.cast(mask, tf.float32)
        item_eb = item_eb[:, 0]

        # RNN layer(-s)
        with tf.name_scope('rnn_1'):
            rnn_outputs, _ = dynamic_rnn(GRUCell(HIDDEN_SIZE), inputs=item_his_eb,
                                         sequence_length=seq_len, dtype=tf.float32,
                                         scope="gru1")
            tf.summary.histogram('GRU_outputs', rnn_outputs)

        # Attention layer
        with tf.name_scope('Attention_layer_1'):
            att_outputs, alphas = din_fcn_attention(item_eb, rnn_outputs, ATTENTION_SIZE, mask,
                                                    softmax_stag=1, stag='1_1', mode='LIST', return_alphas=True)
            tf.summary.histogram('alpha_outputs', alphas)

        with tf.name_scope('rnn_2'):
            rnn_outputs2, final_state2 = dynamic_rnn(VecAttGRUCell(HIDDEN_SIZE), inputs=rnn_outputs,
                                                     att_scores=tf.expand_dims(alphas, -1),
                                                     sequence_length=seq_len, dtype=tf.float32,
                                                     scope="gru2")
            tf.summary.histogram('GRU2_Final_State', final_state2)

        # inp = tf.concat([self.uid_batch_embedded, self.item_eb, final_state2, self.item_his_eb_sum], 1)
        # inp = tf.concat([uid_batch_embedded, item_eb, item_his_eb_sum, item_eb * item_his_eb_sum, final_state2], 1)
        inp = tf.concat([item_eb, item_his_eb_sum, item_eb * item_his_eb_sum, final_state2], 1)
        y = self.build_fcn_net(inp, use_dice=True)
        return y

    def build_fcn_net(self, inp, use_dice=False):
        bn1 = tf.layers.batch_normalization(inputs=inp, name='bn1')
        dnn1 = tf.layers.dense(bn1, 200, activation=None, name='f1')
        if use_dice:
            dnn1 = dice(dnn1, name='dice_1')
        else:
            dnn1 = prelu(dnn1, 'prelu1')

        dnn2 = tf.layers.dense(dnn1, 80, activation=None, name='f2')
        if use_dice:
            dnn2 = dice(dnn2, name='dice_2')
        else:
            dnn2 = prelu(dnn2, 'prelu2')
        dnn3 = tf.layers.dense(dnn2, 2, activation=None, name='f3')
        # self.y_hat = tf.nn.softmax(dnn3) + 0.00000001
        # return self.y_hat
        return dnn3

    # def compute_output_shape(self, input_shape):
    #     return (input_shape[0][0],input_shape[0][1])

    def compute_mask(self, input, input_mask=None):
        # need not to pass the mask to next layers
        return None
