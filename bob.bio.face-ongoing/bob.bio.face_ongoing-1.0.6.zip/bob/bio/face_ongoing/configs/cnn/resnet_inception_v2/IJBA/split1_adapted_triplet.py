#from bob.learn.tensorflow.network.InceptionResnetV2_for_adaptation import inception_resnet_v2
from bob.learn.tensorflow.network.InceptionResnetV2 import inception_resnet_v2

from bob.learn.tensorflow.estimators import Triplet
from bob.learn.tensorflow.loss import triplet_loss
from bob.learn.tensorflow.dataset.tfrecords import batch_data_and_labels_image_augmentation, shuffle_data_and_labels_image_augmentation
from bob.learn.tensorflow.utils.hooks import LoggerHookEstimator
from bob.learn.tensorflow.dataset.triplet_image import shuffle_data_and_labels_image_augmentation as triplet_batch
import os
import tensorflow as tf


learning_rate = 0.01
data_shape = (182, 182, 3)  # size of atnt images
output_shape = (160, 160)
data_type = tf.uint8
batch_size = 16
validation_batch_size = 250
epochs = 10
n_classes = 332
embedding_validation = True

steps = 2000000

model_dir = "/idiap/temp/tpereira/msceleb/ijba/resnet_inception_v2/split1_adapted_triplet/"
tf_record_path = "/idiap/temp/tpereira/bob.bio.face-ongoing/IJBA/tfrecords/raw_data/compare/split1/preprocessed_jpg/"
tf_record_path_validation = "/idiap/project/hface/databases/tfrecords/lfw/182x/"


last_checkpoint = "/idiap/temp/tpereira/msceleb/dbscan_face_prunning/official_checkpoints/resnet_inception_v2/centerloss_alpha-0.95_factor-0.02_lr-0.01/"
extra_checkpoint = {"checkpoint_path": last_checkpoint,
                    "scopes": dict({"InceptionResnetV2/": "InceptionResnetV2/"}),
                    "is_trainable": True
                   }

# Creating the tf record
tfrecords_filename = [os.path.join(tf_record_path, f) for f in os.listdir(tf_record_path)]
tfrecords_filename_validation = [os.path.join(tf_record_path_validation, f) for f in os.listdir(tf_record_path_validation)]

def train_input_fn():
    from bob.bio.face.database import IJBABioDatabase
    database = IJBABioDatabase()
    objects = database.objects(groups="world")        

    #client_ids = list(set([str(f.client_id) for f in objects]))
    client_ids = list(set([f.client_id for f in objects]))

    keys = dict()
    for k,i in zip(client_ids, range(len(client_ids))):
        keys[k] = i
    
    filenames = [o.make_path(tf_record_path, ".jpg") for o in objects]      
    labels = [keys[o.client_id] for o in objects]
    
    return triplet_batch(filenames, labels, data_shape, data_type, batch_size, epochs=epochs, output_shape=output_shape,
                         random_flip=True, random_brightness=False, random_contrast=False, random_saturation=False, gray_scale=False)
        

def eval_input_fn():
    return batch_data_and_labels_image_augmentation(tfrecords_filename_validation, data_shape, data_type, validation_batch_size, epochs=1,
                                                      output_shape=output_shape,
                                                      random_flip=False,
                                                      random_brightness=False,
                                                      random_contrast=False,
                                                      random_saturation=False,
                                                      per_image_normalization=True)

run_config = tf.estimator.RunConfig()
run_config = run_config.replace(save_checkpoints_steps=1000)

estimator = Triplet(model_dir=model_dir,
                    architecture=inception_resnet_v2,
                    optimizer=tf.train.GradientDescentOptimizer(learning_rate),
                    loss_op=triplet_loss,
                    validation_batch_size=validation_batch_size,
                    extra_checkpoint=extra_checkpoint)

#LoggerHookEstimator(estimator, 16, 300)
hooks = [
         tf.train.SummarySaverHook(save_steps=1000,
                                   output_dir=model_dir,
                                   scaffold=tf.train.Scaffold(),
                                   summary_writer=tf.summary.FileWriter(model_dir) )]

