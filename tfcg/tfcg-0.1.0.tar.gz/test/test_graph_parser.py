import numpy as np
import tfcg
import tensorflow as tf


def test_from_sess():
    with tf.Graph().as_default() as graph:
        model = tf.keras.Sequential()
        x = np.random.rand(128, 50)
        model.add(tf.keras.layers.Dense(36, name='dense1'))
        model.add(tf.keras.layers.Dense(16, name='dense2'))
        x_p = tf.placeholder(tf.float32, [None, 50], name='input')
        out_p = model(x_p)
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            o = sess.run(out_p, feed_dict={x_p: x})
            _ = tf.identity(o, name="output")
            parser = tfcg.from_sess(sess.graph)
    print(parser)
