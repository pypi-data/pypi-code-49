#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tiago de Freitas Pereira <tiago.pereira@idiap.ch>


import bob.bio.face
import bob.bio.base
from bob.bio.face.preprocessor import FaceCrop
from bob.bio.face.annotator import BobIpMTCNN, BobIpDlib, BobIpFacedetect , FixedCrop

#########
# Preprocessor
#########
# This is the size of the image that this model expects
CROPPED_IMAGE_HEIGHT = 160
CROPPED_IMAGE_WIDTH = 160

TOP_LEFT_POS = (0, 0)
BOTTOM_RIGHT_POS = (CROPPED_IMAGE_HEIGHT, CROPPED_IMAGE_WIDTH)

annotator = bob.bio.base.annotator.FailSafe(annotators=[BobIpMTCNN(), BobIpDlib(), BobIpFacedetect(), FixedCrop()], required_keys=['topleft', 'bottomright'])

cropped_positions = dict()
cropped_positions['topleft'] = (0, 0)
cropped_positions['bottomright'] = (160, 160)
preprocessor = bob.bio.face.preprocessor.FaceCrop(cropped_image_size=(160, 160),
                                                  cropped_positions=cropped_positions,
                                                  annotator=annotator,
                                                  color_channel='rgb',)

