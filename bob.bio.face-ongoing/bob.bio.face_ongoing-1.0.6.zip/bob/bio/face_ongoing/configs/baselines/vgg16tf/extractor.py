#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tiago de Freitas Pereira <tiago.pereira@idiap.ch>

import bob.ip.tensorflow_extractor
import bob.bio.base

extractor = bob.bio.base.extractor.CallableExtractor(bob.ip.tensorflow_extractor.VGGFace())

