from bob.learn.tensorflow.network import inception_resnet_v1_batch_norm
from bob.learn.tensorflow.estimators import LogitsCenterLoss
from bob.learn.tensorflow.dataset.tfrecords import batch_data_and_labels_image_augmentation, shuffle_data_and_labels_image_augmentation
from bob.learn.tensorflow.utils.hooks import LoggerHookEstimator
from bob.learn.tensorflow.utils import reproducible
import os
import tensorflow as tf

# HYPER PARAMETERS
learning_rate = 0.1
data_shape = (182, 182, 3)  # size of atnt images
output_shape = (160, 160)
data_type = tf.uint8
batch_size = 90
#validation_batch_size = 50
validation_batch_size = 38
epochs = 5
embedding_validation = True
architecture=inception_resnet_v1_batch_norm

alpha=0.90
factor=0.02
steps = 2000000

model_dir = "/idiap/temp/tpereira/msceleb/inception_resnet_v1_gray/centerloss_alpha-0.90_factor-0.02/"

# 10% PRUNNED
#tf_record_path = "/idiap/project/hface/databases/tfrecords/msceleba/tfrecord_182x_hand_prunned_10%"
#n_classes = 89288

# 20% PRUNNED
#tf_record_path = "/idiap/project/hface/databases/tfrecords/msceleba/tfrecord_182x_hand_prunned_20/"
#n_classes = 88526

# 44% PRUNNED
tf_record_path = "/idiap/project/hface/databases/tfrecords/msceleba/tfrecord_182x_hand_prunned_44/"
n_classes = 87662


tf_record_path_validation = "/idiap/project/hface/databases/tfrecords/lfw/182x/RGB"

# Creating the tf record
#tfrecords_filename = [os.path.join(tf_record_path, f) for f in os.listdir(tf_record_path)]
#tfrecords_filename_validation = [os.path.join(tf_record_path_validation, f) for f in os.listdir(tf_record_path_validation)]
def train_input_fn():
    return shuffle_data_and_labels_image_augmentation(tf_record_path, data_shape, data_type, batch_size, epochs=epochs,
                                                      output_shape=output_shape,
                                                      buffer_size=2*(10**4),
                                                      random_flip=True,
                                                      random_brightness=False,
                                                      random_contrast=False,
                                                      random_saturation=False,
                                                      per_image_normalization=True,
                                                      random_rotate=True,
                                                      gray_scale=True)
        

def eval_input_fn():
    return batch_data_and_labels_image_augmentation(tf_record_path_validation, data_shape, data_type, validation_batch_size, epochs=100000,
                                                    output_shape=output_shape,
                                                    random_flip=False,
                                                    random_brightness=False,
                                                    random_contrast=False,
                                                    random_saturation=False,
                                                    per_image_normalization=True,
                                                    gray_scale=True)

session_config, run_config,_,_,_ = reproducible.set_seed(log_device_placement=False)
run_config = run_config.replace(save_checkpoints_steps=2000)
 
optimizer = tf.train.RMSPropOptimizer(learning_rate, decay=0.9, momentum=0.9, epsilon=1.0) 
estimator = LogitsCenterLoss(model_dir=model_dir,
                             architecture=architecture,
                             optimizer=optimizer,
                             n_classes=n_classes,
                             embedding_validation=embedding_validation,
                             validation_batch_size=validation_batch_size,
                             alpha=alpha,
                             factor=factor,
                             config=run_config)


hooks = [LoggerHookEstimator(estimator, 16, 300),
         tf.train.SummarySaverHook(save_steps=1000,
                                   output_dir=model_dir,
                                   scaffold=tf.train.Scaffold(),
                                   summary_writer=tf.summary.FileWriter(model_dir) )]

