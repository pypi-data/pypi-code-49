#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tiago de Freitas Pereira <tiago.pereira@idiap.ch>

from bob.bio.base.extractor import Extractor
from bob.ip.pytorch_extractor import CNN8Extractor

class CNN8(CNN8Extractor, Extractor):
    pass

extractor = CNN8()
