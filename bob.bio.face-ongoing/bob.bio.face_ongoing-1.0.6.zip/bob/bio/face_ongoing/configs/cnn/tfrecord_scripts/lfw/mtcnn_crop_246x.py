#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tue 20 Oct 2016 16:48:32 CEST

"""
This script will convert the RGB casia webface data in to tfrecord AND will append in a 
forth channel the a TanTRiggs image
"""


import bob.bio.face
import bob.bio.htface
import bob.io.image
import bob.ip.base
import os
import numpy
import bob.db.lfw
from bob.bio.face.database import LFWBioDatabase

def get_pairs(all_pairs, match=True):

    #enroll = []
    #probe = []
    samples = []
    for p in all_pairs:
        if p.is_match == match:
            samples.append(p.enroll_file)
            samples.append(p.probe_file)

    return samples


lfw_directory = "/idiap/temp/tpereira/databases/LFW/246x/mtcnn-crop/preprocessed/"
#lfw_directory = "/idiap/resource/database/lfw/all_images"

sub_directory = 'mtcnn-crop'

# Detects the face and crops it without eye detection
preprocessor = bob.bio.htface.preprocessor.FaceDetectMTCNN(image_size=(246, 246), margin=44, color_channel="rgb")

extractor = 'dct-blocks'

algorithm = 'pca'

groups = ["world"]

data_dir = lfw_directory 
output = "/idiap/project/hface/databases/tfrecords/lfw/246x/RGB/lfw_pairs"


# Loading LFW models
database = bob.db.lfw.Database(original_directory=data_dir,
                               original_extension=".hdf5")
                               
#database = LFWBioDatabase(
#    original_directory=lfw_directory,
#    annotation_type='funneled',
#    protocol='view1')
                               
                               
                               
samples = get_pairs(database.pairs(protocol="view1"), match=True)
client_ids = list(set([f.client_id for f in samples]))
client_ids = dict(zip(client_ids, range(len(client_ids))))


def file_to_label(f):
    return client_ids[str(f.client_id)]


data_extension = ".hdf5"
verbose = 3
shuffle = False

#data_type = "float32"
data_type = "uint8"


def reader(biofile):
    if os.path.exists(biofile.make_path(database.original_directory, database.original_extension)):
        data = bob.io.base.load(biofile.make_path(database.original_directory, database.original_extension)).astype(data_type)
        
        label = file_to_label(biofile)
        key = str(biofile.path)
        return (data, label, key)
    else:
        return (None, None, None)


