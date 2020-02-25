# tensorflow2.0
import tensorflow as tf
from tensorflow.keras import Input,Model
from tensorflow.keras.layers import Conv2D,MaxPooling2D, UpSampling2D


class CAE:
	def __init__(self,w, h, input_channel):
	 self.w, self.h, self.input_channel = w, h, input_channel

	def compile(self):
		input_img = Input(shape=(self.w,self.h,self.input_channel))
		x = Conv2D(16, (3, 3),strides=(2,2), activation='relu', padding='same')(input_img)
		x = Conv2D(8, (3, 3), strides=(2,2), activation='relu', padding='same')(x)
		encoded = Conv2D(8, (3, 3), strides=(2,2), activation='relu', padding='same')(x)

		x = Conv2D(8, (3, 3), activation='relu', padding='same')(encoded)
		t_b, t_h,t_w, t_c = x.shape
		x = tf.image.resize(x, ( t_w*2, t_h*2))
		x = Conv2D(8, (3, 3), activation='relu', padding='same')(x)
		t_b, t_h,t_w, t_c = x.shape
		x = tf.image.resize(x, ( t_w*2, t_h*2))
		x = Conv2D(16, (3, 3), activation='relu', padding='same')(x)
		t_b, t_h,t_w, t_c = x.shape
		x = tf.image.resize(x, ( t_w*2, t_h*2))
		decoded = Conv2D(1, (3, 3), activation='sigmoid', padding='same')(x)

		self.autoencoder = Model(input_img, decoded)
		self.autoencoder.compile(optimizer='adam', loss='binary_crossentropy') 
	
	def fit(self,x_train, x_test, epochs=5, batch_size=128):

		self.autoencoder.fit(x_train, x_train,
						epochs=epochs,
						batch_size=batch_size,
						shuffle=True,
						validation_data=(x_test, x_test)
					)


def TEST(SIZE=64):
	'''
	SIZE: Specify image size
	'''
	import sys
	sys.path.append('../..')
	from Utils.load_data import load_mnist
	import matplotlib.pyplot as plt
	x_train, x_test = load_mnist(SIZE=SIZE)
	tb,th,tw,tc = x_test.shape
	w, h, input_channel = th,tw,1
	cae = CAE(w, h, input_channel)
	cae.compile()
	cae.fit(x_train, x_test,epochs=1)

	decoded_imgs = cae.autoencoder.predict(x_test[:20])

	n = 5                                        
	plt.figure(figsize=(10, 4))
	for i in range(1,n+1):
		# display original
		ax = plt.subplot(2, n, i)
		plt.imshow(x_test[i].reshape(w,h))
		plt.gray()
		ax.get_xaxis().set_visible(False)
		ax.get_yaxis().set_visible(False)

		# display reconstruction
		ax = plt.subplot(2, n,i+n)
		plt.imshow(decoded_imgs[i].reshape(w,h))
		plt.gray()
		ax.get_xaxis().set_visible(False)
		ax.get_yaxis().set_visible(False)
	plt.show()
if __name__=='__main__':
	TEST()