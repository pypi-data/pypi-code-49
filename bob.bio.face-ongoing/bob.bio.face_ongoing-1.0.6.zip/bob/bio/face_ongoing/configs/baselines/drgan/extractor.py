#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tiago de Freitas Pereira <tiago.pereira@idiap.ch>

from bob.ip.tensorflow_extractor import DrGanMSUExtractor
from bob.bio.base.extractor import CallableExtractor
    
#########
# Extraction
#########

extractor = CallableExtractor(DrGanMSUExtractor())
