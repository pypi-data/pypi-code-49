# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 18:41:57 2020

@author: eternal_demon
"""

import pandas as pd
import numpy as np
import oremover as ore
import sys


def main():
    ore.oremover(sys.argv[1])

if (__name__ == "__main__"):
    main()
