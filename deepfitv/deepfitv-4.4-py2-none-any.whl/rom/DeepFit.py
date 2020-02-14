from DF import *

import cv2

path = "knee_mov.mp4"

InitialimagePath = "frames/frame1.jpg"

FinalimagePath = "frames/frame45.jpg"

DeepFit.videotoimageconverter(path)


InitialOutput,FinalOutput = DeepFit.readFrame(InitialimagePath,FinalimagePath)

KneePoint = DeepFit.FetchingKneeKeypoint(18,InitialOutput,InitialimagePath)




InitialAnklePoints = DeepFit.FetchingAnkleKeypoints(18,InitialOutput,InitialimagePath)

FinalAnklePoints = DeepFit.FetchingAnkleKeypoints(18,FinalOutput,FinalimagePath)

angle = DeepFit.getROM(InitialAnklePoints,KneePoint,FinalAnklePoints)

print("The angle between the initial and final position of the knee is : ",angle)
    

        

