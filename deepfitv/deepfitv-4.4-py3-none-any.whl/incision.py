from imageai.Detection.Custom import DetectionModelTrainer
#!wget https://github.com/OlafenwaMoses/ImageAI/releases/download/essential-v4/pretrained-yolov3.h5

#trainer.setTrainConfig(object_names_array=["incision"], batch_size=4, num_experiments=100, train_from_pretrained_model="Incision/models/pretrained-yolov3.h5")
from imageai.Detection.Custom import CustomObjectDetection
detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
from PIL import Image
import numpy as np

detector.setModelPath("Incision/models/detection_model.h5")
detector.setJsonPath("Incision/json/detection_config.json")
detector.loadModel()

from keras.models import load_model
model = load_model('Incision/models/Image_classification.h5')

class Incision:
    def __init__(self,new_pic):
        self.new_pic = new_pic
        

    def object_detection(self):
        print(" The uploaded pic by the user is:")
        pic = Image.open(self.new_pic)
        display(pic)
        # detector.setJsonPath("Incision/json/detection_config.json")
        print ("image displayed")
        detections_1 = detector.detectObjectsFromImage(input_image=self.new_pic, output_image_path="detected.jpg")
        print ("image detected")
        detection = 0
        for x in detections_1:
            detection = x['percentage_probability']
        # print(detection)
        if detection >= 60:
            print("\n\n The image uploaded is correct and has correctly identified the incision")
            user = Image.open("detected.jpg")
            display(user)
        else:
            print(" The image uploaded does not recognize an incision. Please upload again")
            

    def classify_image(self):
        print ("the image to be classified is:")
        pic = Image.open(self.new_pic)
        display(pic)
        detections_1 = detector.detectObjectsFromImage(input_image=self.new_pic, output_image_path="detected.jpg")
        detection = 0
        for x in detections_1:
            detection = x['percentage_probability']
        if detection >= 60:
            user = Image.open("detected.jpg")
            #display(user)
            temp = []
            classify = user.resize((64, 64))
            classify = classify.convert("L")
            temp.append((np.array(classify) - np.mean(classify)) / np.std(classify))
            a = np.asarray(temp)
            temp = a.reshape(a.shape[0], 1, a.shape[1], a.shape[2])
            del(a)
            result = model.predict(x=temp)
            if result > 0.5:
                print( "\n\n The incision identified in the image is less than 30 days of surgery")
            else:
                print(" \n\n The incision identified in the image is post 30 days of surgery")

        else:
            print(" The image uploaded does not recognize an incision for classification. Please upload again")
