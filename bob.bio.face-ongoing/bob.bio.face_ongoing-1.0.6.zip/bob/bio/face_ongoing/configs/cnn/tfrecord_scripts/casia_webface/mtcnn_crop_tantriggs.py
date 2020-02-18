#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tue 20 Oct 2016 16:48:32 CEST

"""
This script will convert the RGB casia webface data in to tfrecord AND will append in a 
forth channel the a TanTRiggs image
"""


import bob.bio.face
#import bob.bio.htface
import bob.io.image
import bob.ip.base
import os
import numpy

from bob.bio.face.database import CasiaWebFaceBioDatabase
#casia_webface_directory = "/idiap/resource/database/CASIA-WebFace/CASIA-WebFace"
casia_webface_directory = "/idiap/temp/tpereira/databases/casia_webface/182x/raw_data_onlygood/mtcnn-crop/preprocessed/"
#original_extension=".jpg",

database = CasiaWebFaceBioDatabase(
    original_directory=casia_webface_directory,
    original_extension=".hdf5",
    protocol='pure_casia'
    )

sub_directory = 'mtcnn-crop'

# Detects the face and crops it without eye detection
#preprocessor = bob.bio.htface.preprocessor.FaceDetectMTCNN(image_size=(182, 182), margin=44, color_channel="rgb")

extractor = 'dct-blocks'

algorithm = 'pca'

groups = ["world"]
samples = database.all_files(groups=groups)


CLIENT_IDS = (str(f.client_id) for f in database.all_files())
CLIENT_IDS = list(set(CLIENT_IDS))
CLIENT_IDS = dict(zip(CLIENT_IDS, range(len(CLIENT_IDS))))

def file_to_label(f):
    return CLIENT_IDS[str(f.client_id)]

def normalize4save(img):
  return (255 * ((img - numpy.min(img)) / (numpy.max(img)-numpy.min(img)))).astype("uint8")


#/idiap/temp/tpereira/databases/casia_webface/182x/raw_data_onlygood
data_dir = "/idiap/temp/tpereira/databases/casia_webface/182x/raw_data_onlygood/mtcnn-crop/preprocessed/"
output = "/idiap/project/hface/databases/tfrecords/casia_webface/182x/tan_triggs"


data_extension = ".hdf5"
verbose = 3
shuffle = True

#data_type = "float32"
data_type = "uint8"


def reader(biofile):

    if os.path.exists(biofile.make_path(database.original_directory, database.original_extension)):
        image = bob.io.base.load(biofile.make_path(database.original_directory, database.original_extension)).astype(data_type)
        tan_triggs = normalize4save(bob.ip.base.TanTriggs()(bob.ip.color.rgb_to_gray(image)))
        tan_triggs = numpy.reshape(tan_triggs, (tan_triggs.shape[0], tan_triggs.shape[1], 1))
        data = numpy.concatenate( (bob.io.image.to_matplotlib(image),tan_triggs), axis=2).astype("uint8")
        
        label = file_to_label(biofile)
        key = str(biofile.path)
        return (data, label, key)
    else:
        return (None, None, None)



