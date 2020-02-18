#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tiago de Freitas Pereira <tiago.pereira@idiap.ch>


from bob.bio.face.preprocessor import FaceCrop


#########
# Preprocessor
#########
# This is the size of the image that this model expects
CROPPED_IMAGE_HEIGHT = 160
CROPPED_IMAGE_WIDTH = 160

TOP_LEFT_POS = (0, 0)
BOTTOM_RIGHT_POS = (CROPPED_IMAGE_HEIGHT, CROPPED_IMAGE_WIDTH)

# Detects the face and crops it without eye detection
preprocessor = FaceCrop(
   cropped_image_size=(CROPPED_IMAGE_HEIGHT, CROPPED_IMAGE_WIDTH),
   cropped_positions={'topleft': TOP_LEFT_POS, 'bottomright': BOTTOM_RIGHT_POS},
   color_channel='gray' 
)

