#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tiago de Freitas Pereira <tiago.pereira@idiap.ch>

import bob.ip.tensorflow_extractor
from bob.learn.tensorflow.network import inception_resnet_v2_batch_norm
import tensorflow as tf
from bob.extension import rc
from bob.bio.face_ongoing.extractor import TensorflowEmbedding
#model_filename = "/idiap/temp/tpereira/casia_webface/inception_resnet_v2/centerloss_alpha-0.90_factor-0.02/"
#model_filename = "/idiap/temp/tpereira/msceleb/inception_resnet_v2/centerloss_alpha-0.90_factor-0.02/"
model_filename = "/idiap/project/hface/models/official_checkpoints/msceleb/inception-v2_batchnorm_rgb/"

#########
# Extraction
#########
inputs = tf.placeholder(tf.float32, shape=(1, 160, 160, 3))

# Taking the embedding
prelogits = inception_resnet_v2_batch_norm(tf.stack([tf.image.per_image_standardization(i) for i in tf.unstack(inputs)]), mode=tf.estimator.ModeKeys.PREDICT)[0]
embedding = tf.nn.l2_normalize(prelogits, dim=1, name="embedding")

extractor = TensorflowEmbedding(bob.ip.tensorflow_extractor.Extractor(model_filename, inputs, embedding))

