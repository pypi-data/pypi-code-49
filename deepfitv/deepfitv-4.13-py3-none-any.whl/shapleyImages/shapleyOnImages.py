import keras
import pickle
import sklearn
import warnings
import numpy as np
import pandas as pd
from os import listdir
from PIL import Image
import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.image import imread
warnings.filterwarnings("ignore")
MEM_DIR = './'
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
import os
import keras
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam

from Shapley import ShapNN
from DShap import DShap
from shap_utils import *
from utils import resize_and_crop



class ShapleyOnImages:

    """def __init__(self,image_path1,image_path2,remove_noise=5):
        self.image_path1 = image_path1
        self.image_path2 = image_path2
        self.remove_noise = remove_noise"""

    def shapleOnImages(image_path1,image_path2,remove_noise):
        print(image_path1," ",image_path2," ",remove_noise)
        IMAGE_PATH = image_path1 #Replace with your own path to downloaded images
        Before_images = list()
        for filename in os.listdir(IMAGE_PATH):
            if filename.endswith("_resized.jpg") or filename.endswith("_resized.JPG") or filename.endswith("_resized.jpeg"):
                try:
                    im = Image.open(os.path.join(IMAGE_PATH,filename))
                    im = im.convert(mode="L") #convert to grayscale
                    im = resize_and_crop(im) #resize and crop each picture to be 100px by 100px
                    Before_images.append(np.reshape(im, [10000]))
                except Exception as e:
                    pass #print(e)

        Before_images=np.asarray(Before_images,dtype=float)
        Before_images/=255 #rescale to be 0-1
        print("Before_images:",Before_images.shape)


        Before_images_df = pd.DataFrame(Before_images)

        label_Before = []
        for i in range(0,len(Before_images_df)):
            label_Before.append(1)
        Before_images_df['Target'] = label_Before
        Before_images_df.to_csv('before.csv',index=False)

        IMAGE_PATH = image_path2 #Replace with your own path to downloaded images
        After_images = list()
        for filename in os.listdir(IMAGE_PATH):
            if filename.endswith("_resized.jpg") or filename.endswith("_resized.JPG") or filename.endswith("_resized.jpeg"):
                try:
                    im = Image.open(os.path.join(IMAGE_PATH,filename))
                    im = im.convert(mode="L") #convert to grayscale
                    im = resize_and_crop(im) #resize and crop each picture to be 100px by 100px
                    After_images.append(np.reshape(im, [10000]))
                except Exception as e:
                    pass #print(e)

        After_images=np.asarray(After_images,dtype=float)
        After_images/=255 #rescale to be 0-1
        print("After_images:",After_images.shape)

        After_images_df = pd.DataFrame(After_images)

        label_After = np.random.randint(1, size=100)

        After_images_df['Target'] = label_After

        both = [Before_images_df,After_images_df]
        all_images_df = pd.concat(both,ignore_index=True)


        all_images_df1=all_images_df.sample(frac=1,random_state=0)

        x = all_images_df1.iloc[:,:-1]
        y = all_images_df1.iloc[:,[-1]]

        len_df = len(all_images_df1)
        train_len = int(len_df*80/100)
        test_len = len_df - train_len


        x_train=x.head(train_len)
        y_train=y.head(train_len)
        x_test=x.tail(test_len)
        y_test=y.tail(test_len)
        x_train = x_train.values
        y_train = y_train.values


        x_test = x_test.as_matrix()
        y_test = y_test.as_matrix()

        Y_train = []
        for i in y_train:
            Y_train.extend(i)

        Y_test = []
        for i in y_test:
            Y_test.extend(i)

        Y_train = np.asarray(Y_train)
        Y_test = np.asarray(Y_test)

        #Data Shapley

        model = 'logistic'
        problem = 'classification'
        num_test = 10000
        directory = './tempLog_for_ImageShap'

        import shutil
        shutil.rmtree(directory, ignore_errors=True)


        dshap = DShap(x_train, Y_train, x_test, Y_test, num_test, sources=None, model_family=model, metric='accuracy',
                      directory=directory, seed=0)
        dshap.run(100, 0.1,g_run=False, loo_run=False)

        print(dshap.merge_results())

        dataTMC = pd.DataFrame({'Column1': dshap.vals_tmc[:]})
        dataTMC1=dataTMC.sort_values(by='Column1')


        dataTMC1['Column1'].quantile([0,0.25,0.5,0.75])

        dataNEG_TMC = dataTMC[(dataTMC['Column1']<0)]

        drop_list_TMC = list(dataNEG_TMC.index.values)

        TMC_val=pd.DataFrame(dshap.vals_tmc)

        TMC_val.rename(columns = {0:'TMC_score'}, inplace = True)

        modDf_TMC =all_images_df1[:-1].drop(drop_list_TMC)

        modDf_TMC.reset_index(level=0,inplace=True)

        df_TMCval=pd.concat([modDf_TMC,TMC_val],axis=1)

        df_TMCval=df_TMCval.sort_values(by='TMC_score',ascending=False)

        df_TMCval=df_TMCval.dropna()

        noise_removed_size = len_df - (int(len_df * remove_noise/100))

        df_TMCval = df_TMCval.head(noise_removed_size)

        print("Before Shapley : ",all_images_df1.shape, "After Shapley : ", df_TMCval.shape)
        return df_TMCval
