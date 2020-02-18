#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tue 20 Oct 2016 16:48:32 CEST

import bob.bio.face
from bob.bio.face.preprocessor import FaceCrop
import bob.io.image
import os

casia_webface_directory = "/idiap/resource/database/IJB-A/"
data_dir = "/idiap/temp/tpereira/bob.bio.face-ongoing/IJBA/tfrecords/raw_data/compare/split1/preprocessed/"
output = "/idiap/temp/tpereira/bob.bio.face-ongoing/IJBA/tfrecords/split1/split1"
data_extension = ".hdf5"


from bob.bio.face.database import IJBABioDatabase
database = IJBABioDatabase(
    original_directory=casia_webface_directory,
    original_extension=".png",
    protocol='compare_split1'
    )
sub_directory = 'compare/split1'

## CROPING

# This is the size of the image that this model expects
CROPPED_IMAGE_HEIGHT = 182
CROPPED_IMAGE_WIDTH = 182

TOP_LEFT_POS = (0, 0)
BOTTOM_RIGHT_POS = (CROPPED_IMAGE_HEIGHT, CROPPED_IMAGE_WIDTH)

# Detects the face and crops it without eye detection
preprocessor = FaceCrop(
   cropped_image_size=(CROPPED_IMAGE_HEIGHT, CROPPED_IMAGE_WIDTH),
   cropped_positions={'topleft': TOP_LEFT_POS, 'bottomright': BOTTOM_RIGHT_POS},
   color_channel='rgb' 
)

extractor = 'dct-blocks'

algorithm = 'gmm'

groups = ["world"]
samples = database.all_files(groups=groups)
client_ids = list(set([str(f.client_id) for f in samples]))
keys = dict()
for k,i in zip(client_ids, range(len(client_ids))):
    keys[str(k)] = i

def file_to_label(f):
    return keys[str(f.client_id)]

verbose = 3
shuffle = True

#data_type = "float32"
data_type = "uint8"


def reader(biofile):
    
    if os.path.exists(biofile.make_path(data_dir, data_extension)):
        data = bob.io.image.to_matplotlib(bob.io.base.load(biofile.make_path(data_dir, data_extension)).astype(data_type))
        
        label = file_to_label(biofile)
        key = str(biofile.path)
        return (data, label, key)
    else:
        return (None, None, None)

