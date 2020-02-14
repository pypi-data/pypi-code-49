#!/usr/bin/env python
# coding: utf-8

# In[3]:


from imageai.Detection.Custom import DetectionModelTrainer


# In[2]:


trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()


# In[3]:


trainer.setDataDirectory(data_directory="Incision")


# In[4]:


trainer.setTrainConfig(object_names_array=["incision"], batch_size=4, num_experiments=100, train_from_pretrained_model="pretrained-yolov3.h5")


# In[6]:


trainer.trainModel()


# In[5]:



from imageai.Detection.Custom import DetectionModelTrainer


# In[6]:


trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()


# In[7]:


trainer.setDataDirectory(data_directory="Incision")


# In[8]:


from imageai.Detection.Custom import CustomObjectDetection


# In[9]:


detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()


# In[10]:


detector.setModelPath("Incision/models/detection_model-ex-018--loss-0005.172.h5") 


# In[11]:


detector.setJsonPath("Incision/json/detection_config.json")


# In[84]:


#detector.loadModel()


# In[13]:


detections = detector.detectObjectsFromImage(input_image="knee1.jpg", output_image_path="knee1-detected.jpg")


# In[14]:


for detection in detections:
    print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])
    if detection["percentage_probability"] >= 60.00:
        print(" The image uploaded is correct and has correctly identified the incision")
        
    else:
        print(" The image uploaded does not recognize an incision. Please upload again")


# In[15]:


detections


# In[16]:


print(*detections)


# In[229]:


for x in detections:
    a = x['percentage_probability']


# In[16]:


import keras
import numpy as np
import pandas as pd
from PIL import Image as img


# In[17]:


import glob
from tqdm import tqdm
import matplotlib.pyplot as plt


# In[18]:


keras.backend.set_image_data_format("channels_first")
keras.backend.image_data_format()


# In[20]:


before_train_list = glob.glob("/vlife-data/vlife-ML/Gaurav/CNN/Train/Before 1 month/*.png")


# In[21]:


after_train_list= glob.glob("/vlife-data/vlife-ML/Gaurav/CNN/Train/After 1 month/*.png")


# In[22]:


x_train = []

for i in tqdm(before_train_list):
    temp = img.open(i).resize((64, 64))
    temp = temp.convert("L")
    
    x_train.append((np.array(temp) - np.mean(temp)) / np.std(temp))
    x_train.append((np.array(temp.rotate(90)) - np.mean(temp)) / np.std(temp))
    x_train.append((np.array(temp.rotate(180)) - np.mean(temp)) / np.std(temp))
    x_train.append((np.array(temp.rotate(270)) - np.mean(temp)) / np.std(temp))
    
#    if not idx % 200:
#        print(idx)

y_train = np.tile(1, len(before_train_list)*4)


# In[23]:


for i in tqdm(after_train_list):
    temp = img.open(i).resize((64, 64))
    temp = temp.convert("L")
    
    x_train.append((np.array(temp) - np.mean(temp)) / np.std(temp))
    x_train.append((np.array(temp.rotate(90)) - np.mean(temp)) / np.std(temp))
    x_train.append((np.array(temp.rotate(180)) - np.mean(temp)) / np.std(temp))
    x_train.append((np.array(temp.rotate(270)) - np.mean(temp)) / np.std(temp))
    
y_train = np.concatenate((y_train, np.tile(0, len(after_train_list)*4))).astype("uint8")


# In[24]:


a = np.asarray(x_train)
x_train = a.reshape(a.shape[0], 1, a.shape[1], a.shape[2])


# In[25]:


del(a)


# In[26]:


LeakyReLU = keras.layers.LeakyReLU(alpha=0.01)


# In[27]:


model = keras.models.Sequential()

model.add(keras.layers.Conv2D(filters=32, kernel_size=(2, 2), input_shape=(1, 64, 64)))
model.add(LeakyReLU)
model.add(keras.layers.Dropout(rate=0.3))

model.add(keras.layers.Conv2D(filters=32, kernel_size=(3, 3)))
model.add(LeakyReLU)
model.add(keras.layers.Dropout(rate=0.3))

model.add(keras.layers.Conv2D(filters=64, activation="relu", kernel_size=(3, 3)))
model.add(keras.layers.MaxPooling2D(pool_size=(3, 3)))
model.add(keras.layers.Dropout(rate=0.3))

model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(units=12, activation="relu"))
model.add(keras.layers.Dense(units=1, activation="sigmoid"))


# In[28]:


model.compile(optimizer=keras.optimizers.SGD(), loss=keras.losses.binary_crossentropy, metrics=["binary_accuracy"])


# In[29]:


model.summary()


# In[30]:


model.fit(x=x_train, y=y_train, epochs=10, validation_split=0.1, shuffle=True)


# In[80]:


model_json=model.to_json()


# In[81]:


with open("model.json","w") as json_file:
    json_file.write(model_json)


# In[31]:


model.save_weights('model_saved.h5') 


# In[32]:


len(model.history.history["binary_accuracy"])


# In[33]:


before_test_list = glob.glob("/vlife-data/vlife-ML/Gaurav/CNN/Test/Before 1 month/*.jpg")


# In[34]:


before_test_list


# In[35]:


x_test = []

for i in tqdm(before_test_list):
    temp = img.open(i).resize((64, 64))
    temp = temp.convert("L")
    x_test.append((np.array(temp) - np.mean(temp)) / np.std(temp))


# In[36]:


a = np.asarray(x_test)
x_test = a.reshape(a.shape[0], 1, a.shape[1], a.shape[2])


# In[37]:


del(a)


# In[38]:


result = model.predict(x=x_test)


# In[39]:


idx = []
for i in before_test_list:
    idx.append(i[21:-4])


# In[40]:


result = result.reshape(result.shape[0])
result[result>0.5] = '0'
result[result<0.5] = '1'


# In[41]:


submission = {"id": idx, "label": result}


# In[42]:


pd.DataFrame(submission)


# In[43]:


from PIL import Image
from PIL import ImageTk
#user = Image.open("knee1.jpg")


# In[138]:


import matplotlib.pyplot as plt
plt.imshow(user)
plt.show()


# In[100]:


temp = []


# In[24]:


import numpy as np


# In[102]:


tempo = user.resize((64, 64))
tempo = tempo.convert("L")
temp.append((np.array(tempo) - np.mean(tempo)) / np.std(tempo))


# In[104]:


a = np.asarray(temp)
temp = a.reshape(a.shape[0], 1, a.shape[1], a.shape[2])


# In[105]:


del(a)


# In[107]:


result = model.predict(x=temp)


# In[109]:


if result > 0.5:
    print(" The image uploaded by user is of Incision less than 30 days of treatment")


# In[67]:


def incision(name_pic):
    print(" The uploaded pic by the user is:")
    pic=Image.open(name_pic)
    display(pic)
    #detector.setJsonPath("Incision/json/detection_config.json")
    detections_1 = detector.detectObjectsFromImage(input_image= name_pic, output_image_path="detected.jpg")
    detection = 0
    for x in detections_1:
        detection = x['percentage_probability']
    #print(detection)
    if detection >= 60:
        print("\n\n The image uploaded is correct and has correctly identified the incision")
        user = Image.open("detected.jpg")
        display(user)
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
        print(" The image uploaded does not recognize an incision. Please upload again")   


# In[65]:


user = Image.open("list.jpg")
user_1 = "list.jpg"


# In[68]:


incision(user_1)


# In[2]:


user2 = Image.open("after.jpg")
user1_2 = "after.jpg"


# In[69]:


incision(user1_2)


# In[8]:


from PIL import Image
from PIL import ImageTk


# In[9]:


user1 = Image.open("normal.jpg")
user1_1 = "normal.jpg"


# In[ ]:


incision(user1_1)


# In[29]:


from imageai.Detection.Custom import DetectionModelTrainer

import keras
import numpy as np
import pandas as pd
from PIL import Image as img
from PIL import ImageTk
from imageai.Detection.Custom import CustomObjectDetection

detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="Incision")
trainer.setTrainConfig(object_names_array=["incision"], batch_size=4, num_experiments=100, train_from_pretrained_model="pretrained-yolov3.h5")

detector.setModelPath("Incision/models/detection_model-ex-018--loss-0005.172.h5")
detector.setJsonPath("Incision/json/detection_config.json")


# In[28]:


import keras
import numpy as np
import pandas as pd
from PIL import Image as img

import glob
from tqdm import tqdm
import matplotlib.pyplot as plt

keras.backend.set_image_data_format("channels_first")
keras.backend.image_data_format()


# In[23]:


model = keras.models.Sequential()
LeakyReLU = keras.layers.LeakyReLU(alpha=0.01)

model.add(keras.layers.Conv2D(filters=32, kernel_size=(2, 2), input_shape=(1, 64, 64)))
model.add(LeakyReLU)
model.add(keras.layers.Dropout(rate=0.3))

model.add(keras.layers.Conv2D(filters=32, kernel_size=(3, 3)))
model.add(LeakyReLU)
model.add(keras.layers.Dropout(rate=0.3))

model.add(keras.layers.Conv2D(filters=64, activation="relu", kernel_size=(3, 3)))
model.add(keras.layers.MaxPooling2D(pool_size=(3, 3)))
model.add(keras.layers.Dropout(rate=0.3))

model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(units=12, activation="relu"))
model.add(keras.layers.Dense(units=1, activation="sigmoid"))


# In[24]:


model.compile(optimizer=keras.optimizers.SGD(), loss=keras.losses.binary_crossentropy, metrics=["binary_accuracy"])


# In[27]:


def incision(name_pic):
    print(" The uploaded pic by the user is:")
    pic=Image.open(name_pic)
    display(pic)
    #detector.setJsonPath("Incision/json/detection_config.json")
    detections_1 = detector.detectObjectsFromImage(input_image= name_pic, output_image_path="detected.jpg")
    detection = 0
    for x in detections_1:
        detection = x['percentage_probability']
    #print(detection)
    if detection >= 60:
        print("\n\n The image uploaded is correct and has correctly identified the incision")
              
    else:
        print(" The image uploaded does not recognize an incision. Please upload again")   

