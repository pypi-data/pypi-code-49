# -*- coding: utf-8 -*-
import copy
import math
import os
from collections import Counter, OrderedDict

import numpy as np
import pandas as pd
import scipy as sci

import sklearn as sk
from sklearn import preprocessing
from sklearn.feature_extraction.text import TfidfVectorizer

import tensorflow as tf
import torch as torch




def main():
  print("os.getcwd", os.getcwd())
  print(np, np.__version__) 
  print(tf, tf.__version__)




test_list =[
  "python model_gluon/gluon_automl.py",
  "python model_gluon/gluon_deepar.py",
  "python model_gluon/gluon_ffn.py",

  ###
  "python model_keras/01_deepctr.py",


  ###
  "python model_keras/01_deepctr.py",


  ###
  "python model_tf/1_lstm.py",


  ###
  "python model_tch/nbeats.py",



]


for cmd in test_list :
    print(cmd)
    os.system( cmd , flush=True)



if __name__ == "__main__":
    main()





