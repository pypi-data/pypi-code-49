import keras
import numpy as np
from keras.applications import mobilenet_v2
from keras.models import Model
from keras.preprocessing import image
from keras import backend as K
from keras.layers import Dense, GlobalAveragePooling2D,Input
from keras.callbacks import ModelCheckpoint
from keras.optimizers import Adam,SGD
import os,cv2,glob
####################################################
def main():
    data_dir = '/home/ars/disk/chaoyuan/dataset/汽车分类/颜色/car_color_dataset/train'
    num_classes = len(os.listdir(data_dir))
    tar_imsize = (224, 224)
    model_save_path = 'model.h5'
    train(
        data_dir=data_dir,
        model_save_path=model_save_path,
        num_classes=num_classes,
        tar_imsize=tar_imsize
    )
####################################################
def load_data(data_dir, num_classes,tar_imsize):
    classes = os.listdir(data_dir)
    classes.sort()
    xs, ys = [], []
    for i, cls in enumerate(classes):
        cls_dir = data_dir + "/" + cls
        fs = glob.glob(cls_dir + '/*.jpg')
        for f in fs:
            im = cv2.imread(f)
            im = cv2.resize(im, tar_imsize)
            im = np.array(im).astype(np.float)
            xs.append(im)
            y = keras.utils.to_categorical(i, num_classes=num_classes)
            ys.append(y)
    xs = np.array(xs).astype(np.float)
    ys = np.array(ys).astype(np.float)
    print('shape x,y:%s,%s' % (xs.shape, ys.shape))
    return xs, ys
def train(data_dir,model_save_path,num_classes,tar_imsize):

    ####################################################
    # data_dir='/home/ars/work/trainval/shenqingbiao/imgs'
    checkpoint = ModelCheckpoint(filepath=model_save_path,
                                 monitor='loss',
                                 verbose=1,
                                 save_best_only=True, mode='auto')
    callbacks = [checkpoint]
    ####################################################
    Inp = Input((224, 224, 3))
    base_model = keras.applications.mobilenet_v2.MobileNetV2(include_top=False, weights='imagenet', classes=2,
                                                             input_tensor=Inp)

    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    predictions = Dense(num_classes, activation='softmax')(x)
    model = Model(inputs=base_model.input, outputs=predictions)
    for i, layer in enumerate(base_model.layers):
        print(i, layer.name)
    model.compile(optimizer=Adam(lr=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

    ####################################################
    xs, ys = load_data(data_dir, num_classes,tar_imsize)
    model.fit(x=xs, y=ys, batch_size=8, validation_split=0.2, epochs=15, shuffle=True, callbacks=callbacks)

if __name__ == '__main__':
    # train()
    main()