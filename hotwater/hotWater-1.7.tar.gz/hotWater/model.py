# -*- coding: utf-8 -*-
import numpy as np
import pickle
import copy
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
from itertools import combinations
from Bio.PDB import *
import matplotlib as mpl
mpl.use('pdf')
import matplotlib.pyplot as plt
import tensorflow as tf




def water_glue_model(L=18,K=4, n=1):
    '''
    '''
    import keras
    import neural_structured_learning as nsl
    from keras.layers.pooling import GlobalMaxPooling1D
    from keras.models import Sequential,Model
    from keras.layers import Dense,Activation,Dropout,Flatten
    from keras.layers.convolutional import Conv1D
    from keras.layers import Input, Embedding, Dense
    from keras.layers.normalization import BatchNormalization
    from keras.regularizers import l1,l2
    from keras.optimizers import SGD,RMSprop,Adam
    import tensorflow as tf
    #config = tf.ConfigProto(device_count={"CPU": 64})
    #keras.backend.tensorflow_backend.set_session(tf.Session(config=config))

    def residual_unit(nb_fil,f_len,ar,indx,residual='yes'):
        def f(input_node):
            bn1 = tf.keras.layers.BatchNormalization(name='BatchNormalization_'+indx+'_1')(input_node)
            act1 = tf.keras.layers.Activation('relu',name='relu_'+indx+'_1')(bn1)
            conv1= tf.keras.layers.Conv1D(nb_fil, f_len,dilation_rate=ar,kernel_regularizer=l2(0.0005), padding='same',name='conv1d_'+indx+'_1')(act1)
            bn2 = tf.keras.layers.BatchNormalization(name='BatchNormalization_'+indx+'_2')(conv1)
            act2 = tf.keras.layers.Activation('relu',name='relu_'+indx+'_2')(bn2)
            conv2= tf.keras.layers.Conv1D(nb_fil, f_len,dilation_rate=ar,kernel_regularizer=l2(0.0005),padding='same',name='conv1d_'+indx+'_2')(act2)
            if residual=='yes':
              output_node = tf.keras.layers.add([conv2, input_node])
            else:
              output_node = conv2
            return output_node
        return f
    num_vectors=50
    num_atoms = 30
    n_dim=3
    N=np.asarray([n,n])  #Depth of the model
    input0 = tf.keras.layers.Input(shape=(num_vectors,3), name='atom_vectors')
    input1 = tf.keras.layers.Input(shape=(num_vectors,num_atoms),name='beta')
    conv1 = tf.keras.layers.Conv1D(L, 1,kernel_regularizer=l2(0.0005), name='1d_conv1')(input0)
    conv2 = tf.keras.layers.Conv1D(L, 1,kernel_regularizer=l2(0.0005), name='1d_conv2')(input1)     
    merge1=tf.keras.layers.concatenate([conv1, conv2],name='merge12a')
    merge2=tf.keras.layers.concatenate([conv1, conv2],name='merge12b')
    conv=tf.keras.layers.Conv1D(L, K, name='1d_conv_reduce',kernel_regularizer=l2(0.0005),padding='same')(merge1) # see if 1 better or W
    skip=tf.keras.layers.Conv1D(L, K, name='1d_skip_reduce',padding='same')(merge2) # see if 1 better or W    
    for i in range(len(N)):
        for j in range(N[i]):
            conv = residual_unit(L, K, 1,'residual_'+str(i)+'_'+str(j),residual='yes')(conv)
        conv_for_skip = tf.keras.layers.Conv1D(L, 1,kernel_regularizer=l2(0.0005),name='convforskip'+str(i))(conv)    
        skip = tf.keras.layers.add([skip, conv_for_skip],name='skip'+str(i))
    conv = residual_unit(L, 1, 1,'residual_final',residual='yes')(skip)
    conv= tf.keras.layers.Conv1D(1, 1,padding='same',kernel_regularizer=l2(0.0005), activation='sigmoid',name='conv_final')(conv)
    output0=tf.keras.layers.GlobalMaxPooling1D(name='output')(conv)
    model=tf.keras.Model(inputs=[input0,input1],outputs=[output0])
    adv_config = nsl.configs.make_adv_reg_config(multiplier=0.2, adv_step_size=0.05)
    adv_model = nsl.keras.AdversarialRegularization(model, label_keys=['output'], adv_config=adv_config )
    adv_model.compile(optimizer='sgd',loss='binary_crossentropy',metrics=['accuracy'])
    return adv_model



