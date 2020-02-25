import cv2
import numpy as np
from random import randint
import math

protoFile = "pose/coco/pose_deploy_linevec.prototxt"
weightsFile = "pose/coco/pose_iter_440000.caffemodel"
nPoints = 18

# COCO Output Format

keypointsMapping = ['Nose', 'Neck', 'R-Sho', 'R-Elb', 'R-Wr', 'L-Sho', 
                    'L-Elb', 'L-Wr', 'R-Hip', 'R-Knee', 'R-Ank', 'L-Hip', 
                    'L-Knee', 'L-Ank', 'R-Eye', 'L-Eye', 'R-Ear', 'L-Ear']

POSE_PAIRS = [[1,2], [1,5], [2,3], [3,4], [5,6], [6,7],
              [1,8], [8,9], [9,10], [1,11], [11,12], [12,13],
              [1,0], [0,14], [14,16], [0,15], [15,17],
              [2,17], [5,16]]

# index of pafs correspoding to the POSE_PAIRS
# e.g for POSE_PAIR(1,2), the PAFs are located at indices (31,32) of output, Similarly, (1,5) -> (39,40) and so on.
mapIdx = [[31,32], [39,40], [33,34], [35,36], [41,42], [43,44], 
          [19,20], [21,22], [23,24], [25,26], [27,28], [29,30], 
          [47,48], [49,50], [53,54], [51,52], [55,56], 
          [37,38], [45,46]]

colors = [ [0,100,255], [0,100,255], [0,255,255], [0,100,255], [0,255,255], [0,100,255],
         [0,255,0], [255,200,100], [255,0,255], [0,255,0], [255,200,100], [255,0,255],
         [0,0,255], [255,0,0], [200,200,0], [255,0,0], [200,200,0], [0,0,0]]





    
class DeepFit():    


        def videotoimageconverter(path):

            vidObj = cv2.VideoCapture(path)


            # Used as counter variable
            count = 0

            # checks whether frames were extracted
            success = 1
            
            
            if not os.path.exists('frames'):
                os.makedirs('frames')

            while success:

                # vidObj object calls read
                # function extract frames
                success, image = vidObj.read()
                try:
                    # block raising an exception
                    cv2.imwrite("frames/frame%d.jpg" % count, image)

                except:
                    pass # doing nothing on exception

                # Saves the frames with frame-count

                count += 1
            
            for i in range(0,count-1):
                img  = Image.open("frames/frame%d.jpg" % i)
                imgplot = plt.imshow(img)
                plt.show()
                

        def readFrame(a,b):

                image1 = cv2.imread(a)
                image2 = cv2.imread(b)
                InitialframeWidth = image1.shape[1]
                InitialframeHeight = image1.shape[0]
                FinalframeWidth = image2.shape[1]
                FinalframeHeight = image2.shape[0]

                Initialnet = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)
                finalnet = cv2.dnn.readNetFromCaffe(protoFile, weightsFile) 
                # Fix the input Height and get the width according to the Aspect Ratio
                inHeight = 368
                InitialinWidth = int((inHeight/InitialframeHeight)*InitialframeWidth)
                FinalinWidth = int((inHeight/FinalframeHeight)*FinalframeWidth)

                InitialinpBlob = cv2.dnn.blobFromImage(image1, 1.0 / 255, (InitialinWidth, inHeight),
                                          (0, 0, 0), swapRB=False, crop=False)
                FinalinpBlob = cv2.dnn.blobFromImage(image2, 1.0 / 255, (FinalinWidth, inHeight),
                                          (0, 0, 0), swapRB=False, crop=False)

                Initialnet.setInput(InitialinpBlob)
                finalnet.setInput(FinalinpBlob)
                Intialoutput = Initialnet.forward()
                Finaloutput = finalnet.forward()
                return Intialoutput,Finaloutput



        def getKeypoints(probMap, threshold=0.1):

            mapSmooth = cv2.GaussianBlur(probMap,(3,3),0,0)

            mapMask = np.uint8(mapSmooth>threshold)
            keypoints = []

            #find the blobs
            contours, _ = cv2.findContours(mapMask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            #for each blob find the maxima
            for cnt in contours:
                blobMask = np.zeros(mapMask.shape)
                blobMask = cv2.fillConvexPoly(blobMask, cnt, 1)
                maskedProbMap = mapSmooth * blobMask
                _, maxVal, _, maxLoc = cv2.minMaxLoc(maskedProbMap)
                keypoints.append(maxLoc + (probMap[maxLoc[1], maxLoc[0]],))

            return keypoints


        def FetchingAnkleKeypoints(nPoints,output,imagePath):

            detected_keypoints = []
            keypoints_list = np.zeros((0,3))
            keypoint_id = 0
            threshold = 0.1
            image1 = cv2.imread(imagePath)
            for part in range(nPoints):
                probMap = output[0,part,:,:]
                probMap = cv2.resize(probMap, (image1.shape[1], image1.shape[0]))
            #     plt.figure()
            #     plt.imshow(255*np.uint8(probMap>threshold))
                keypoints = DeepFit.getKeypoints(probMap, threshold)
                if keypointsMapping[part] == 'R-Ank' :
                    print(keypoints[0][:2])
                    return keypoints[0][:2]
                    break

                #"print(type())
                keypoints_with_id = []
                for i in range(len(keypoints)):
                    keypoints_with_id.append(keypoints[i] + (keypoint_id,))
                    keypoints_list = np.vstack([keypoints_list, keypoints[i]])
                    keypoint_id += 1

                detected_keypoints.append(keypoints_with_id)



        def FetchingKneeKeypoint(nPoints,output,imagePath):

                detected_keypoints = []
                keypoints_list = np.zeros((0,3))
                keypoint_id = 0
                threshold = 0.1
                image1 = cv2.imread(imagePath)
                for part in range(nPoints):
                    probMap = output[0,part,:,:]
                    probMap = cv2.resize(probMap, (image1.shape[1], image1.shape[0]))
                #     plt.figure()
                #     plt.imshow(255*np.uint8(probMap>threshold))
                    keypoints = DeepFit.getKeypoints(probMap, threshold)
                    if keypointsMapping[part] == 'R-Knee' :
                        print(keypoints[1][:2])
                        return keypoints[1][:2]
                        break

                    #"print(type())
                    keypoints_with_id = []
                    for i in range(len(keypoints)):
                        keypoints_with_id.append(keypoints[i] + (keypoint_id,))
                        keypoints_list = np.vstack([keypoints_list, keypoints[i]])
                        keypoint_id += 1

                    detected_keypoints.append(keypoints_with_id)




        def getROM(a,b,c):


                ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
                if ang < 0:
                    ROM =  ang + 360  
                else: 
                    ROM = ang
                return ROM

