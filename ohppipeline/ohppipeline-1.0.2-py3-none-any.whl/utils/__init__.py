# -*- coding: utf8 -*-  

""" module in order to reduce image

:author: Clement Hottier
"""


from .imageprocessing import makemasterbias, makemasterflat, processimages, crosscorrelalign


__author__ = "Clement Hottier, Noel Robichon"
__all__ = [
        "makemasterbias",
        "makemasterflat",
        "processimages",
        "crosscorrelalign",
]
