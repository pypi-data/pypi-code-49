#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    handlers.py: This python script implements util classes and functions 
    for the handle logs via the logging standard library.
"""


# standard library(ies)
import logging 

# 3rd party package(s)
from tqdm import tqdm 


class TqdmHandler(logging.StreamHandler):

    def __init__(self):
        logging.StreamHandler.__init__(self)


    def emit(self, *args, **kwargs):
        msg = self.format(*args, **kwargs)
        tqdm.write(msg)
        