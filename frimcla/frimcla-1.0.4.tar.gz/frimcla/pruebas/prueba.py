from __future__ import print_function

from sklearn import metrics
from imutils import paths
from frimcla import prediction

import json


#Este archivo se usa para calcular los accuracies de los modelos con los conjuntos de test. Asi calculamos realmente
# el % de acierto que tiene cada uno de los modelos y si realmente funciona como se ha marcado en el entrenamiento.


# from frimcla.shallowmodels import classificationModelFactory, modelFactory
# print(classificationModelFactory.ListClassificationModels())
# print(modelFactory.listFeatureExtractors())

outputPath = "/home/magarcd/Escritorio/output/PRUEBAMULTICLASEEnsemble"
datasetPath= "/MiasNBMRecortadas"
featureExtractors = []
datasetName = datasetPath[datasetPath.rfind("/")+1:]
print(outputPath + "/" + datasetName +'/ConfModel.json')

imagePaths = "/home/magarcd/Escritorio/dataset/MiasNBMRecortadasTest"

with open(outputPath + "/" + datasetName +'/ConfModel.json') as data:
    datos = json.load(data)


extractors = datos["featureExtractors"]
classifiers = ["GradientBoost",
                "RandomForest",
                "SVM",
                "KNN",
                "LogisticRegression",
                "MLP"
            ]
# classifiers = datos["featureExtractors"][0]["classificationModels"][0]

for ex in extractors:
    featureExtractor = [str(ex["model"]), ex["params"]]
    featureExtractors.append(featureExtractor)

# prediction.prediction([extractors[0]["model"],extractors[0]["params"]], classifiers, imagePaths, outputPath, datasetName)

del extractors

# Poner la ruta de las imagenes para que luego el metodo se encargue de listar las imagenes de la carpeta y se puedan tratar
# prediction.predictionEnsemble(featureExtractors, classifiers, imagePaths, outputPath, datasetName)

auxPath = outputPath + "/" + datasetName
filePrediction = auxPath +"/predictionResults (copia).csv"
predictions = []
groundTruth = []

imagenesTest = []

csvfile = open(filePrediction, "r")
csvfile.readline()
for line in csvfile:
    line = line.split(",") #Esto se utiliza por que se puede sacar la clase real por la carpeta en la que tenemos contenida la imagen que se estudia
    # realclass = line[0].split(":")[0]
    # print(realclass)
    # if(str(realclass) =="Uninfected"):
    #     groundTruth.append(1)
    # else:
    #     groundTruth.append(0)
    # line = line.split("\n")[0]
    predictions.append(line[1][1:-1])
    # imagenesTest.append(line[0])

# groundTruthFile = auxPath + "/mias.txt"
# groundTruth = []
# csvfile2 = open(groundTruthFile, "r")
# file = open(auxPath +"/groundtruthTEST.csv", "w")
# for line in csvfile2:
#     line = line.split(" ")
#     if str(line[0]) in imagenesTest:
#         if (str(line[2])=="NORM"):
#             file.write(line[0] + "," + " NORMAL\n")
#         elif str(line[3])=="B":
#             file.write(line[0] + "," + " BENING\n")
#         else:
#             file.write(line[0] + "," + " MALIGNANT\n")
#


groundTruthFile = auxPath + "/groundtruthTEST.csv"
groundTruth = []
csvfile2 = open(groundTruthFile, "r")
for line in csvfile2:
    line = line.split(",")
    groundTruth.append(line[1][1:-1])

    # if (str(line[1])=="dog\n"):
    #     groundTruth.append(1)
    # else:
    #     groundTruth.append(0)




    # for image in imagePaths:
    #     image =image[image.rfind("/")+1:]
    #     if (image.split(".")[0]==line[0]):
    #         if (line[2]=="dog\r\n"):
    #             groundTruth.append(1)
    #         else:
    #             groundTruth.append(0)

# print("Ground Truth")
# print (groundTruth)
# print("Predictions")
# print(predictions)
f = open(auxPath + "/TESTaccuracy.txt","w")
f.write("Ground Truth\n")
f.write(groundTruth)
f.write("\nPredictions\n")
f.write(predictions)
f.write(str(metrics.confusion_matrix(groundTruth, predictions)))

# f.write("Auroc\n")
# f.write(str(metrics.roc_auc_score(groundTruth, predictions)))
f.write("\nAccuracy\n")
f.write(str(metrics.accuracy_score(groundTruth,predictions)))

#
# print(metrics.roc_auc_score(groundTruth, predictions))
# print(metrics.accuracy_score(groundTruth,predictions))
#

#
#
#
# outputPath = "../output"
# datasetName= "/dataAugmentation"
#
# auxPath = outputPath + datasetName
# filePrediction = auxPath +"/predictionResults.csv"
# predictions = []
# csvfile = open(filePrediction, "r")
# csvfile.readline()
# for line in csvfile:
#     line = line.split(",")
#     predictions.append(int(line[1]))
#
#
#
#
# groundTruthFile = "../test_GroundTruth.csv"
# groundTruth = []
# csvfile2 = open(groundTruthFile, "r")
# csvfile2.readline()
# for line in csvfile2:
#     line = line.split(",")
#     groundTruth.append(int(float(line[1])))
#
# print("Ground Truth")
# print (groundTruth)
# print("Predictions")
# print(predictions)
#
# print(metrics.roc_auc_score(groundTruth, predictions))
# print(metrics.accuracy_score(groundTruth,predictions))