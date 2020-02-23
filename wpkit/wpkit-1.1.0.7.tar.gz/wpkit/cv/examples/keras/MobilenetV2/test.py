import keras
import numpy as np
from keras.applications import mobilenet_v2
from keras.models import Model,load_model
from keras.preprocessing import image
from keras import backend as K
from keras.layers import Dense, GlobalAveragePooling2D,Input
from keras.callbacks import ModelCheckpoint
from keras.optimizers import Adam,SGD
import os,cv2,glob
# from train import load_data

valdir='/home/ars/disk/chaoyuan/dataset/汽车分类/颜色/car_color_dataset/val'


class Predictor:
    def __init__(self,weights_path='model.h5'):
        model = load_model(weights_path)
        self.model=model
        self.tar_imsize = (224, 224)
        self.classes=os.listdir(valdir)
        self.classes.sort()
    def predict_from_file(self,f):
        im = cv2.imread(f)
        return self.predict(im)
    def predict(self,im):
        im=self.preprocess(im)
        y=self.model.predict(im)[0]
        return self.decode_y(y)
    def decode_y(self,y):
        k=np.argmax(y)
        return self.classes[k]
    def preprocess(self,im):
        im = cv2.resize(im, self.tar_imsize)
        im = np.array(im).astype(np.float)
        return np.array([im])
    def load_img(self,f):
        im = cv2.imread(f)
        im = cv2.resize(im, self.tar_imsize)
        im = np.array(im).astype(np.float)
        return np.array([im])
    def print_modeL_structure(self):
        model=self.model
        for i, layer in enumerate(model.layers):
            print(i, layer.name)

def test_dir():
    data_dir=valdir
    # data_dir='/home/ars/work/trainval/gongzhang/train'
    # data_dir='data/train'
    model_path='model.h5'
    P=Predictor(weights_path=model_path)
    classes =os.listdir(data_dir)
    classes.sort()
    total,correct=0,0
    for i,cls in enumerate(classes):
        cls_dir=data_dir+'/'+cls
        fs=glob.glob(cls_dir+'/*.jpg')
        cls_total,cls_correct=0,0
        for f in fs:
            y=P.predict_from_file(f)
            total+=1
            cls_total+=1
            if y==cls:
                correct+=1
                cls_correct+=1
        if not cls_total:
            continue
        cls_acc=cls_correct/cls_total
        print('class %s accuracy: %s/%s=%s'%(cls,cls_correct,cls_total,cls_acc))
    acc=correct/total
    print('accuracy: %s/%s=%s'%(correct,total,acc))

if __name__ == '__main__':
    test_dir()
