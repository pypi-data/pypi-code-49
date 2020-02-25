
import numpy as np 
import cv2
from glob import glob
from tensorflow.keras.datasets import mnist
def load_mnist(SIZE=128,num_train=2000, num_test=500):
	'''
	SIZE: points image size
	'''

	(x_train, _), (x_test, _) = mnist.load_data()
	x_train = x_train.astype('float32') / 255.
	x_test = x_test.astype('float32') / 255.
	x_train = np.reshape(x_train, (len(x_train), 28, 28, 1))  
	x_test = np.reshape(x_test, (len(x_test), 28, 28, 1)) 

	X_train, X_test = x_train[0][...,-1], x_test[0][...,-1]

	X_train, X_test = cv2.resize(X_train, (SIZE,SIZE)), cv2.resize(X_test, (SIZE,SIZE))
	X_train, X_test = X_train.reshape(1,SIZE,SIZE,1), X_test.reshape(1,SIZE,SIZE,1)
	for i in x_train[:num_train]:
		x_i = cv2.resize(i[...,-1], (SIZE, SIZE))
		X_train = np.concatenate((X_train, x_i.reshape(1,SIZE,SIZE,1)), axis=0)
		
	for j in x_test[-num_train:]:
		x_j = cv2.resize(j[...,-1], (SIZE, SIZE))
		X_test = np.concatenate((X_test, x_j.reshape(1,SIZE,SIZE,1)), axis=0)
	return X_train, X_test


def load_path(img_path = '/home/nikki_intern/GAN/DATA/img_align_celeba/*', SIZE = 256, 
              num_train=2000, num_test=1000):

    img_name = glob(img_path)
    train_name = img_name[:2000]
    test_name = img_name[-500:]

    X_train = cv2.resize(cv2.imread(train_name[0])[:,:,::-1], (SIZE,SIZE)) 
    X_test = cv2.resize(cv2.imread(test_name[0])[:,:,::-1], (SIZE,SIZE))
    H,W,C = X_train.shape
    X_train, X_test = X_train.reshape(1,SIZE,SIZE,C), X_test.reshape(1,SIZE,SIZE,C)
    for i in train_name[1:]:
        x_i = cv2.resize(cv2.imread(i)[:,:,::-1], (SIZE,SIZE)) 
        X_train = np.concatenate((X_train, x_i.reshape(1,SIZE,SIZE,C)), axis=0)
        
    for j in test_name[1:]:
        x_j = cv2.resize(cv2.imread(j)[:,:,::-1], (SIZE,SIZE)) 
        X_test = np.concatenate((X_test, x_j.reshape(1,SIZE,SIZE,C)), axis=0)
        
    return X_train.astype('float32') / 255., X_test.astype('float32') / 255.