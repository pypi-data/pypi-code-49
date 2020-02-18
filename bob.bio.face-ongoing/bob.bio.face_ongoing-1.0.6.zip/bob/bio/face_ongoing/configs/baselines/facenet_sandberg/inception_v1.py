#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tiago de Freitas Pereira <tiago.pereira@idiap.ch>

from bob.bio.base.extractor import Extractor
from bob.ip.tensorflow_extractor import FaceNet

from bob.bio.base.extractor import Extractor
class FaceNetExtractor(FaceNet, Extractor):
    pass
    
#########
# Extraction
#########
extractor = FaceNetExtractor()

