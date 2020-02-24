from __future__ import absolute_import
import argparse
import pandas as pd
import os
import json
import numpy as np
import h5py
import _pickle
from sklearn.model_selection import KFold
from .utils.conf import Conf
from .Comparing import compare_methods_h5py, prepareModel
from .StatisticalAnalysis.statisticalAnalysis import statisticalAnalysis
from .shallowmodels.classificationModelFactory import classificationModelFactory


featureExtractors = [["googlenet"] , ["hog"],["overfeat", "[-3]"],["inception", "False"],
      ["xception", "False"], ["densenet"],["lab888"], ["lab444","4,4,4"], ["hsv888"], ["hsv444","4,4,4"], ["haralick"], ["hog"], ["vgg16", "False"], ["vgg19", "False"],["resnet", "False"], ["haarhog"]]


pathAux = "/home/magarcd/Escritorio/output/MiasRecortadas"
filePathAux = pathAux + "/results/kfold-comparison_bestClassifiers.csv"
alpha = 0.05
import time
for fe in featureExtractors:
        #time.sleep(2)
        if not(os.path.isfile(filePathAux)):
            '''break
            #fileResults = open(filePathAux, "w")
        else:'''
            if not(os.path.exists(pathAux + "/results")):
                os.makedirs(filePathAux[:filePathAux.rfind("/")])
            fileResults = open(filePathAux, "w")
            for j in range(int(10)):
                fileResults.write(","+str(j))
            fileResults.write("\n")
	KFoldComparisionPathAccuracy = pathAux + "/results/kfold-comparison_"+fe[0] + ".csv"
	filePath = pathAux + "/results/StatisticalComparison_" + fe[0] + ".txt"

	statisticalAnalysis(KFoldComparisionPathAccuracy,filePath, fileResults, alpha, False)
fileResults.close()


filePath2 = pathAux + "/results/StatisticalComparison_bestClassifiers.txt"
fileResults2 = open(pathAux + "/results/bestExtractorClassifier.csv", "w")
statisticalAnalysis(pathAux + "/results/kfold-comparison_bestClassifiers.csv", filePath2, fileResults2, alpha, False)
fileResults2.close()
