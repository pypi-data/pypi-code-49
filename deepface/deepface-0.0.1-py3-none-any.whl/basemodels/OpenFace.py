import os
from pathlib import Path
import gdown

import tensorflow as tf
import keras
from keras.models import Model, Sequential
from keras.layers import Conv2D, ZeroPadding2D, Activation, Input, concatenate
from keras.layers.core import Dense, Activation, Lambda, Flatten
from keras.layers.pooling import MaxPooling2D, AveragePooling2D
from keras.layers.merge import Concatenate
from keras.layers.normalization import BatchNormalization
from keras.models import load_model
from keras import backend as K

#---------------------------------------

def loadModel():
	myInput = Input(shape=(96, 96, 3))

	x = ZeroPadding2D(padding=(3, 3), input_shape=(96, 96, 3))(myInput)
	x = Conv2D(64, (7, 7), strides=(2, 2), name='conv1')(x)
	x = BatchNormalization(axis=3, epsilon=0.00001, name='bn1')(x)
	x = Activation('relu')(x)
	x = ZeroPadding2D(padding=(1, 1))(x)
	x = MaxPooling2D(pool_size=3, strides=2)(x)
	x = Lambda(lambda x: tf.nn.lrn(x, alpha=1e-4, beta=0.75), name='lrn_1')(x)
	x = Conv2D(64, (1, 1), name='conv2')(x)
	x = BatchNormalization(axis=3, epsilon=0.00001, name='bn2')(x)
	x = Activation('relu')(x)
	x = ZeroPadding2D(padding=(1, 1))(x)
	x = Conv2D(192, (3, 3), name='conv3')(x)
	x = BatchNormalization(axis=3, epsilon=0.00001, name='bn3')(x)
	x = Activation('relu')(x)
	Lambda(lambda x: tf.nn.lrn(x, alpha=1e-4, beta=0.75), name='lrn_2')(x)
	x = ZeroPadding2D(padding=(1, 1))(x)
	x = MaxPooling2D(pool_size=3, strides=2)(x)

	# Inception3a
	inception_3a_3x3 = Conv2D(96, (1, 1), name='inception_3a_3x3_conv1')(x)
	inception_3a_3x3 = BatchNormalization(axis=3, epsilon=0.00001, name='inception_3a_3x3_bn1')(inception_3a_3x3)
	inception_3a_3x3 = Activation('relu')(inception_3a_3x3)
	inception_3a_3x3 = ZeroPadding2D(padding=(1, 1))(inception_3a_3x3)
	inception_3a_3x3 = Conv2D(128, (3, 3), name='inception_3a_3x3_conv2')(inception_3a_3x3)
	inception_3a_3x3 = BatchNormalization(axis=3, epsilon=0.00001, name='inception_3a_3x3_bn2')(inception_3a_3x3)
	inception_3a_3x3 = Activation('relu')(inception_3a_3x3)

	inception_3a_5x5 = Conv2D(16, (1, 1), name='inception_3a_5x5_conv1')(x)
	inception_3a_5x5 = BatchNormalization(axis=3, epsilon=0.00001, name='inception_3a_5x5_bn1')(inception_3a_5x5)
	inception_3a_5x5 = Activation('relu')(inception_3a_5x5)
	inception_3a_5x5 = ZeroPadding2D(padding=(2, 2))(inception_3a_5x5)
	inception_3a_5x5 = Conv2D(32, (5, 5), name='inception_3a_5x5_conv2')(inception_3a_5x5)
	inception_3a_5x5 = BatchNormalization(axis=3, epsilon=0.00001, name='inception_3a_5x5_bn2')(inception_3a_5x5)
	inception_3a_5x5 = Activation('relu')(inception_3a_5x5)

	inception_3a_pool = MaxPooling2D(pool_size=3, strides=2)(x)
	inception_3a_pool = Conv2D(32, (1, 1), name='inception_3a_pool_conv')(inception_3a_pool)
	inception_3a_pool = BatchNormalization(axis=3, epsilon=0.00001, name='inception_3a_pool_bn')(inception_3a_pool)
	inception_3a_pool = Activation('relu')(inception_3a_pool)
	inception_3a_pool = ZeroPadding2D(padding=((3, 4), (3, 4)))(inception_3a_pool)

	inception_3a_1x1 = Conv2D(64, (1, 1), name='inception_3a_1x1_conv')(x)
	inception_3a_1x1 = BatchNormalization(axis=3, epsilon=0.00001, name='inception_3a_1x1_bn')(inception_3a_1x1)
	inception_3a_1x1 = Activation('relu')(inception_3a_1x1)

	inception_3a = concatenate([inception_3a_3x3, inception_3a_5x5, inception_3a_pool, inception_3a_1x1], axis=3)

	# Inception3b
	inception_3b_3x3 = Conv2D(96, (1, 1), name='inception_3b_3x3_conv1')(inception_3a)
	inception_3b_3x3 = BatchNormalization(axis=3, epsilon=0.00001, name='inception_3b_3x3_bn1')(inception_3b_3x3)
	inception_3b_3x3 = Activation('relu')(inception_3b_3x3)
	inception_3b_3x3 = ZeroPadding2D(padding=(1, 1))(inception_3b_3x3)
	inception_3b_3x3 = Conv2D(128, (3, 3), name='inception_3b_3x3_conv2')(inception_3b_3x3)
	inception_3b_3x3 = BatchNormalization(axis=3, epsilon=0.00001, name='inception_3b_3x3_bn2')(inception_3b_3x3)
	inception_3b_3x3 = Activation('relu')(inception_3b_3x3)

	inception_3b_5x5 = Conv2D(32, (1, 1), name='inception_3b_5x5_conv1')(inception_3a)
	inception_3b_5x5 = BatchNormalization(axis=3, epsilon=0.00001, name='inception_3b_5x5_bn1')(inception_3b_5x5)
	inception_3b_5x5 = Activation('relu')(inception_3b_5x5)
	inception_3b_5x5 = ZeroPadding2D(padding=(2, 2))(inception_3b_5x5)
	inception_3b_5x5 = Conv2D(64, (5, 5), name='inception_3b_5x5_conv2')(inception_3b_5x5)
	inception_3b_5x5 = BatchNormalization(axis=3, epsilon=0.00001, name='inception_3b_5x5_bn2')(inception_3b_5x5)
	inception_3b_5x5 = Activation('relu')(inception_3b_5x5)

	inception_3b_pool = Lambda(lambda x: x**2, name='power2_3b')(inception_3a)
	inception_3b_pool = AveragePooling2D(pool_size=(3, 3), strides=(3, 3))(inception_3b_pool)
	inception_3b_pool = Lambda(lambda x: x*9, name='mult9_3b')(inception_3b_pool)
	inception_3b_pool = Lambda(lambda x: K.sqrt(x), name='sqrt_3b')(inception_3b_pool)
	inception_3b_pool = Conv2D(64, (1, 1), name='inception_3b_pool_conv')(inception_3b_pool)
	inception_3b_pool = BatchNormalization(axis=3, epsilon=0.00001, name='inception_3b_pool_bn')(inception_3b_pool)
	inception_3b_pool = Activation('relu')(inception_3b_pool)
	inception_3b_pool = ZeroPadding2D(padding=(4, 4))(inception_3b_pool)

	inception_3b_1x1 = Conv2D(64, (1, 1), name='inception_3b_1x1_conv')(inception_3a)
	inception_3b_1x1 = BatchNormalization(axis=3, epsilon=0.00001, name='inception_3b_1x1_bn')(inception_3b_1x1)
	inception_3b_1x1 = Activation('relu')(inception_3b_1x1)

	inception_3b = concatenate([inception_3b_3x3, inception_3b_5x5, inception_3b_pool, inception_3b_1x1], axis=3)

	# Inception3c
	inception_3c_3x3 = Conv2D(128, (1, 1), strides=(1, 1), name='inception_3c_3x3_conv1')(inception_3b)
	inception_3c_3x3 = BatchNormalization(axis=3, epsilon=0.00001, name='inception_3c_3x3_bn1')(inception_3c_3x3)
	inception_3c_3x3 = Activation('relu')(inception_3c_3x3)
	inception_3c_3x3 = ZeroPadding2D(padding=(1, 1))(inception_3c_3x3)
	inception_3c_3x3 = Conv2D(256, (3, 3), strides=(2, 2), name='inception_3c_3x3_conv'+'2')(inception_3c_3x3)
	inception_3c_3x3 = BatchNormalization(axis=3, epsilon=0.00001, name='inception_3c_3x3_bn'+'2')(inception_3c_3x3)
	inception_3c_3x3 = Activation('relu')(inception_3c_3x3)

	inception_3c_5x5 = Conv2D(32, (1, 1), strides=(1, 1), name='inception_3c_5x5_conv1')(inception_3b)
	inception_3c_5x5 = BatchNormalization(axis=3, epsilon=0.00001, name='inception_3c_5x5_bn1')(inception_3c_5x5)
	inception_3c_5x5 = Activation('relu')(inception_3c_5x5)
	inception_3c_5x5 = ZeroPadding2D(padding=(2, 2))(inception_3c_5x5)
	inception_3c_5x5 = Conv2D(64, (5, 5), strides=(2, 2), name='inception_3c_5x5_conv'+'2')(inception_3c_5x5)
	inception_3c_5x5 = BatchNormalization(axis=3, epsilon=0.00001, name='inception_3c_5x5_bn'+'2')(inception_3c_5x5)
	inception_3c_5x5 = Activation('relu')(inception_3c_5x5)

	inception_3c_pool = MaxPooling2D(pool_size=3, strides=2)(inception_3b)
	inception_3c_pool = ZeroPadding2D(padding=((0, 1), (0, 1)))(inception_3c_pool)

	inception_3c = concatenate([inception_3c_3x3, inception_3c_5x5, inception_3c_pool], axis=3)

	#inception 4a
	inception_4a_3x3 = Conv2D(96, (1, 1), strides=(1, 1), name='inception_4a_3x3_conv'+'1')(inception_3c)
	inception_4a_3x3 = BatchNormalization(axis=3, epsilon=0.00001, name='inception_4a_3x3_bn'+'1')(inception_4a_3x3)
	inception_4a_3x3 = Activation('relu')(inception_4a_3x3)
	inception_4a_3x3 = ZeroPadding2D(padding=(1, 1))(inception_4a_3x3)
	inception_4a_3x3 = Conv2D(192, (3, 3), strides=(1, 1), name='inception_4a_3x3_conv'+'2')(inception_4a_3x3)
	inception_4a_3x3 = BatchNormalization(axis=3, epsilon=0.00001, name='inception_4a_3x3_bn'+'2')(inception_4a_3x3)
	inception_4a_3x3 = Activation('relu')(inception_4a_3x3)

	inception_4a_5x5 = Conv2D(32, (1,1), strides=(1,1), name='inception_4a_5x5_conv1')(inception_3c)
	inception_4a_5x5 = BatchNormalization(axis=3, epsilon=0.00001, name='inception_4a_5x5_bn1')(inception_4a_5x5)
	inception_4a_5x5 = Activation('relu')(inception_4a_5x5)
	inception_4a_5x5 = ZeroPadding2D(padding=(2,2))(inception_4a_5x5)
	inception_4a_5x5 = Conv2D(64, (5,5), strides=(1,1), name='inception_4a_5x5_conv'+'2')(inception_4a_5x5)
	inception_4a_5x5 = BatchNormalization(axis=3, epsilon=0.00001, name='inception_4a_5x5_bn'+'2')(inception_4a_5x5)
	inception_4a_5x5 = Activation('relu')(inception_4a_5x5)

	inception_4a_pool = Lambda(lambda x: x**2, name='power2_4a')(inception_3c)
	inception_4a_pool = AveragePooling2D(pool_size=(3, 3), strides=(3, 3))(inception_4a_pool)
	inception_4a_pool = Lambda(lambda x: x*9, name='mult9_4a')(inception_4a_pool)
	inception_4a_pool = Lambda(lambda x: K.sqrt(x), name='sqrt_4a')(inception_4a_pool)

	inception_4a_pool = Conv2D(128, (1,1), strides=(1,1), name='inception_4a_pool_conv'+'')(inception_4a_pool)
	inception_4a_pool = BatchNormalization(axis=3, epsilon=0.00001, name='inception_4a_pool_bn'+'')(inception_4a_pool)
	inception_4a_pool = Activation('relu')(inception_4a_pool)
	inception_4a_pool = ZeroPadding2D(padding=(2, 2))(inception_4a_pool)

	inception_4a_1x1 = Conv2D(256, (1, 1), strides=(1, 1), name='inception_4a_1x1_conv'+'')(inception_3c)
	inception_4a_1x1 = BatchNormalization(axis=3, epsilon=0.00001, name='inception_4a_1x1_bn'+'')(inception_4a_1x1)
	inception_4a_1x1 = Activation('relu')(inception_4a_1x1)

	inception_4a = concatenate([inception_4a_3x3, inception_4a_5x5, inception_4a_pool, inception_4a_1x1], axis=3)

	#inception4e
	inception_4e_3x3 = Conv2D(160, (1,1), strides=(1,1), name='inception_4e_3x3_conv'+'1')(inception_4a)
	inception_4e_3x3 = BatchNormalization(axis=3, epsilon=0.00001, name='inception_4e_3x3_bn'+'1')(inception_4e_3x3)
	inception_4e_3x3 = Activation('relu')(inception_4e_3x3)
	inception_4e_3x3 = ZeroPadding2D(padding=(1, 1))(inception_4e_3x3)
	inception_4e_3x3 = Conv2D(256, (3,3), strides=(2,2), name='inception_4e_3x3_conv'+'2')(inception_4e_3x3)
	inception_4e_3x3 = BatchNormalization(axis=3, epsilon=0.00001, name='inception_4e_3x3_bn'+'2')(inception_4e_3x3)
	inception_4e_3x3 = Activation('relu')(inception_4e_3x3)

	inception_4e_5x5 = Conv2D(64, (1,1), strides=(1,1), name='inception_4e_5x5_conv'+'1')(inception_4a)
	inception_4e_5x5 = BatchNormalization(axis=3, epsilon=0.00001, name='inception_4e_5x5_bn'+'1')(inception_4e_5x5)
	inception_4e_5x5 = Activation('relu')(inception_4e_5x5)
	inception_4e_5x5 = ZeroPadding2D(padding=(2, 2))(inception_4e_5x5)
	inception_4e_5x5 = Conv2D(128, (5,5), strides=(2,2), name='inception_4e_5x5_conv'+'2')(inception_4e_5x5)
	inception_4e_5x5 = BatchNormalization(axis=3, epsilon=0.00001, name='inception_4e_5x5_bn'+'2')(inception_4e_5x5)
	inception_4e_5x5 = Activation('relu')(inception_4e_5x5)

	inception_4e_pool = MaxPooling2D(pool_size=3, strides=2)(inception_4a)
	inception_4e_pool = ZeroPadding2D(padding=((0, 1), (0, 1)))(inception_4e_pool)

	inception_4e = concatenate([inception_4e_3x3, inception_4e_5x5, inception_4e_pool], axis=3)

	#inception5a
	inception_5a_3x3 = Conv2D(96, (1,1), strides=(1,1), name='inception_5a_3x3_conv'+'1')(inception_4e)
	inception_5a_3x3 = BatchNormalization(axis=3, epsilon=0.00001, name='inception_5a_3x3_bn'+'1')(inception_5a_3x3)
	inception_5a_3x3 = Activation('relu')(inception_5a_3x3)
	inception_5a_3x3 = ZeroPadding2D(padding=(1, 1))(inception_5a_3x3)
	inception_5a_3x3 = Conv2D(384, (3,3), strides=(1,1), name='inception_5a_3x3_conv'+'2')(inception_5a_3x3)
	inception_5a_3x3 = BatchNormalization(axis=3, epsilon=0.00001, name='inception_5a_3x3_bn'+'2')(inception_5a_3x3)
	inception_5a_3x3 = Activation('relu')(inception_5a_3x3)

	inception_5a_pool = Lambda(lambda x: x**2, name='power2_5a')(inception_4e)
	inception_5a_pool = AveragePooling2D(pool_size=(3, 3), strides=(3, 3))(inception_5a_pool)
	inception_5a_pool = Lambda(lambda x: x*9, name='mult9_5a')(inception_5a_pool)
	inception_5a_pool = Lambda(lambda x: K.sqrt(x), name='sqrt_5a')(inception_5a_pool)

	inception_5a_pool = Conv2D(96, (1,1), strides=(1,1), name='inception_5a_pool_conv'+'')(inception_5a_pool)
	inception_5a_pool = BatchNormalization(axis=3, epsilon=0.00001, name='inception_5a_pool_bn'+'')(inception_5a_pool)
	inception_5a_pool = Activation('relu')(inception_5a_pool)
	inception_5a_pool = ZeroPadding2D(padding=(1,1))(inception_5a_pool)

	inception_5a_1x1 = Conv2D(256, (1,1), strides=(1,1), name='inception_5a_1x1_conv'+'')(inception_4e)
	inception_5a_1x1 = BatchNormalization(axis=3, epsilon=0.00001, name='inception_5a_1x1_bn'+'')(inception_5a_1x1)
	inception_5a_1x1 = Activation('relu')(inception_5a_1x1)

	inception_5a = concatenate([inception_5a_3x3, inception_5a_pool, inception_5a_1x1], axis=3)

	#inception_5b
	inception_5b_3x3 = Conv2D(96, (1,1), strides=(1,1), name='inception_5b_3x3_conv'+'1')(inception_5a)
	inception_5b_3x3 = BatchNormalization(axis=3, epsilon=0.00001, name='inception_5b_3x3_bn'+'1')(inception_5b_3x3)
	inception_5b_3x3 = Activation('relu')(inception_5b_3x3)
	inception_5b_3x3 = ZeroPadding2D(padding=(1,1))(inception_5b_3x3)
	inception_5b_3x3 = Conv2D(384, (3,3), strides=(1,1), name='inception_5b_3x3_conv'+'2')(inception_5b_3x3)
	inception_5b_3x3 = BatchNormalization(axis=3, epsilon=0.00001, name='inception_5b_3x3_bn'+'2')(inception_5b_3x3)
	inception_5b_3x3 = Activation('relu')(inception_5b_3x3)

	inception_5b_pool = MaxPooling2D(pool_size=3, strides=2)(inception_5a)

	inception_5b_pool = Conv2D(96, (1,1), strides=(1,1), name='inception_5b_pool_conv'+'')(inception_5b_pool)
	inception_5b_pool = BatchNormalization(axis=3, epsilon=0.00001, name='inception_5b_pool_bn'+'')(inception_5b_pool)
	inception_5b_pool = Activation('relu')(inception_5b_pool)

	inception_5b_pool = ZeroPadding2D(padding=(1, 1))(inception_5b_pool)

	inception_5b_1x1 = Conv2D(256, (1,1), strides=(1,1), name='inception_5b_1x1_conv'+'')(inception_5a)
	inception_5b_1x1 = BatchNormalization(axis=3, epsilon=0.00001, name='inception_5b_1x1_bn'+'')(inception_5b_1x1)
	inception_5b_1x1 = Activation('relu')(inception_5b_1x1)

	inception_5b = concatenate([inception_5b_3x3, inception_5b_pool, inception_5b_1x1], axis=3)

	av_pool = AveragePooling2D(pool_size=(3, 3), strides=(1, 1))(inception_5b)
	reshape_layer = Flatten()(av_pool)
	dense_layer = Dense(128, name='dense_layer')(reshape_layer)
	norm_layer = Lambda(lambda  x: K.l2_normalize(x, axis=1), name='norm_layer')(dense_layer)

	# Final Model
	model = Model(inputs=[myInput], outputs=norm_layer)
	
	#-----------------------------------
	
	home = str(Path.home())
	
	if os.path.isfile(home+'/.deepface/weights/openface_weights.h5') != True:
		print("openface_weights.h5 will be downloaded...")
		
		url = 'https://drive.google.com/file/d/1LSe1YCV1x-BfNnfb7DFZTNpv_Q9jITxn'
		output = home+'/.deepface/weights/openface_weights.h5'
		gdown.download(url, output, quiet=False)
	
	#-----------------------------------
	
	model.load_weights(home+'/.deepface/weights/openface_weights.h5')
	
	#-----------------------------------
	
	return model