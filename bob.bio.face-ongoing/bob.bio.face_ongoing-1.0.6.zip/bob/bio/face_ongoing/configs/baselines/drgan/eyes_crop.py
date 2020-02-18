#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tiago de Freitas Pereira <tiago.pereira@idiap.ch>


from bob.bio.face.preprocessor import FaceCrop

# This is the size of the image that this model expects
CROPPED_IMAGE_HEIGHT = 96
CROPPED_IMAGE_WIDTH = 96

# eye positions for frontal images
RIGHT_EYE_POS = (28, 32)
LEFT_EYE_POS = (28, 64)

#RIGHT_EYE_POS = (20, 24)
#LEFT_EYE_POS = (20, 72)

# Detects the face and crops it without eye detection
preprocessor = FaceCrop(
    cropped_image_size=(CROPPED_IMAGE_HEIGHT, CROPPED_IMAGE_WIDTH),
    cropped_positions={'leye': LEFT_EYE_POS, 'reye': RIGHT_EYE_POS},
    color_channel='rgb'
)
