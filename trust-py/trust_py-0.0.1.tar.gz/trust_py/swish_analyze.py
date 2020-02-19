"""
Code to run analysis of IMBD with different activation functions and to get plots to which iterate different parameters to 
compare accuracy score

First section is creating the various activation functions with tensorflow
Second section is functions to clean data and build tensorflow model
Third section is after the __main__ and is code prepropcessing and then the various iteration functions for the different parameters
"""
import tensorflow as tf
from keras.datasets import imdb
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import os

#### CREATE CUSTOM ACTIVATION FUNCTIONS
def arctan(x):
    return tf.math.atan(x)

def gaussian(x):
    return tf.convert_to_tensor(np.exp(-np.power(x,2)))

def identity(x):
    return x

def ISRU(x, alpha=1):
    return tf.convert_to_tensor(x/(tf.math.sqrt(1+alpha*x**2)))

def PRELU(x, alpha=1):
    return tf.where(x <= 0, alpha*x, x)

def swish(x, beta=1):
    return (x * tf.keras.activations.sigmoid(beta * x))

def trust(x, beta=2):
    x = tf.where(x == 0, .1, x)
    x = tf.where(x == 1, .9, x)
    return tf.convert_to_tensor(1/(1+((x/(1-x))**(-beta))))

tf.keras.utils.get_custom_objects().update({'arctan': tf.keras.layers.Activation(arctan)})
tf.keras.utils.get_custom_objects().update({'gaussian': tf.keras.layers.Activation(gaussian)})
tf.keras.utils.get_custom_objects().update({'identity': tf.keras.layers.Activation(identity)})
tf.keras.utils.get_custom_objects().update({'ISRU': tf.keras.layers.Activation(ISRU)})
tf.keras.utils.get_custom_objects().update({'PRELU': tf.keras.layers.Activation(PRELU)})
tf.keras.utils.get_custom_objects().update({'swish': tf.keras.layers.Activation(swish)})
tf.keras.utils.get_custom_objects().update({'trust': tf.keras.layers.Activation(trust)})

def ngram_vectorize(texts, labels, k_features=20000):
    '''
    Vectorize data and labels with TfidfVectorizer

    texts: Series [Array of numbers converted from words]
    labels: Series [1 and 0 representing positive and negative sentiment]
    k_features: int [number of unique words]
    '''
    kwargs = {
        'ngram_range': (1, 2),
        'dtype': 'int32',
        'strip_accents': 'unicode',
        'decode_error': 'replace',
        'analyzer': 'word',
        'min_df': 2,
    }
    # Learn Vocab from train texts and vectorize train and val sets
    tfidf_vectorizer = TfidfVectorizer(**kwargs)
    transformed_texts = tfidf_vectorizer.fit_transform(texts)

    selector = SelectKBest(f_classif, k=min(k_features, transformed_texts.shape[1]))
    selector.fit(transformed_texts, labels)
    transformed_texts = selector.transform(transformed_texts).astype('float32')
    return transformed_texts


def build_model(X_train, X_test, y_train, y_test, ACTIVATION_FUNC, UNITS, LAYERS, EPOCHS, BATCH_SIZE, LEARNING_RATE, DROPOUT_RATE):
    '''
    Function to predict classification problem given parameters

    X_train: DataFrame [Training Set]
    X_test: DataFrame [Test Set]
    y_train: Series [Train Labels]
    y_test: Series [Test Labels]
    ACTIVATION_FUNC: str [Activation Function for Dense Layers... Last layer is sigmoid]
    UNITS: int [Number of nodes in each layer]
    LAYERS: int [Number of layers in model]
    EPOCHS: int [Number of Epochs to run]
    BATCH_SIZE: int [How large is each batch]
    LEARNING_RATE: float [What is learning rate for gradient descent]
    DROPOUT_RATE: float [Dropout rate for layers]
    '''
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dropout(
        rate=DROPOUT_RATE, input_shape=X_train.shape[1:]))
    for _ in range(LAYERS-1):
        model.add(tf.keras.layers.Dense(units=UNITS, activation=ACTIVATION_FUNC))
        model.add(tf.keras.layers.Dropout(rate=DROPOUT_RATE))
    model.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))
    optimizer = tf.keras.optimizers.Adam(lr=LEARNING_RATE)
    model.compile(optimizer=optimizer,loss='binary_crossentropy', metrics=['accuracy'])
    callbacks = [tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=2)]
    history = model.fit(X_train, y_train, epochs=EPOCHS, validation_data=(X_test, y_test), verbose=1, batch_size=BATCH_SIZE, callbacks=callbacks)
    score = model.evaluate(X_test, y_test, verbose=100)
    return score[1]


if __name__ == '__main__':

    save_dir = os.path.join(os.getcwd(), 'saved_models')
    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)

    # PARAMETERS
    k_features = 20000
    DROPOUT_RATE = 0.2
    UNITS = 64
    LAYERS = 3
    EPOCHS = 5
    BATCH_SIZE = 128
    LEARNING_RATE = 1e-3
    ACTIVATION_FUNC = 'trust'
    iterations = 10

    # PULL AND CLEAN DATA
    INDEX_FROM = 3
    train, test = imdb.load_data(index_from=INDEX_FROM)
    train_x, train_y = train
    test_x, test_y = test
    word_to_id = imdb.get_word_index()
    word_to_id = {k: (v+INDEX_FROM-1) for k, v in word_to_id.items()}
    word_to_id["<PAD>"] = 0
    word_to_id["<START>"] = 1
    word_to_id["<UNK>"] = 2
    word_to_id["<UNUSED>"] = 3
    id_to_word = {value: key for key, value in word_to_id.items()}

    data_train = pd.DataFrame([train_x, train_y], index=['review', 'sentiment']).T
    data_test = pd.DataFrame([test_x, test_y], index=['review', 'sentiment']).T
    data = data_train.append(data_test)
    data['review'] = data['review'].apply(lambda row: ' '.join(id_to_word[idx] for idx in row[1:]))

    # PREPROCESS DATA
    vectorizer = CountVectorizer()
    vect_texts = vectorizer.fit_transform(list(data['review']))
    vect_data = ngram_vectorize(data['review'], data['sentiment'], k_features=k_features)
    X = vect_data.toarray()
    y = (np.array(data['sentiment']))
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)
    y_train = np.asarray(y_train).astype('float32')
    y_test = np.asarray(y_test).astype('float32')

    # ITERATION
    # ACTIVATION FUCNTIONS
    model_type = 'IMDB_Activation'
    activation_functions = ['arctan', 'elu', 'gaussian', 'identity', 'ISRU', 'PRELU', 'relu', 'sigmoid', 'tanh', 'softplus', 'swish', 'trust']
    activation_frame = pd.DataFrame(columns=activation_functions, index=np.arange(iterations))
    for ACTIVATION_FUNC in activation_functions:
        for i in range(iterations):
            activation_frame[ACTIVATION_FUNC].iloc[i] = build_model(X_train, X_test, y_train, y_test, ACTIVATION_FUNC, UNITS, LAYERS, EPOCHS, BATCH_SIZE, LEARNING_RATE, DROPOUT_RATE)
    activation_frame.to_csv(os.path.join(save_dir, model_type+'.csv'))

    # Batch Size
    model_type = 'IMDB_Batch'
    batch_list = [64, 128, 256, 512]
    activation_functions = ['arctan', 'gaussian', 'identity','ISRU', 'sigmoid', 'tanh', 'softplus', 'trust']
    batch_list_frame = pd.DataFrame(columns=batch_list, index=activation_functions).T
    for ACTIVATION_FUNC in activation_functions:
        # print(ACTIVATION_FUNC)
        for BATCH_SIZE in batch_list:
            accuracy_score = []
            for i in range(iterations):
                accuracy_score.append(build_model(X_train, X_test, y_train, y_test, ACTIVATION_FUNC,UNITS, LAYERS, EPOCHS, BATCH_SIZE, LEARNING_RATE, DROPOUT_RATE))
            batch_list_frame.loc[BATCH_SIZE,ACTIVATION_FUNC] = np.median(accuracy_score)
    batch_list_frame.to_csv(os.path.join(save_dir, model_type+'.csv'))

    # Learning Rates
    model_type = 'IMDB_Learning'
    learning_list = [1e-5, 1e-4, 1e-3, 1e-2, 1e-1]
    activation_functions = ['arctan', 'gaussian', 'identity','ISRU', 'sigmoid', 'tanh', 'softplus', 'trust']
    learning_list_frame = pd.DataFrame(columns=learning_list, index=activation_functions).T
    for ACTIVATION_FUNC in activation_functions:
        # print(ACTIVATION_FUNC)
        for LEARNING_RATE in learning_list:
            accuracy_score = []
            for i in range(iterations):
                accuracy_score.append(build_model(X_train, X_test, y_train, y_test, ACTIVATION_FUNC,UNITS, LAYERS, EPOCHS, BATCH_SIZE, LEARNING_RATE, DROPOUT_RATE))
            learning_list_frame.loc[LEARNING_RATE,ACTIVATION_FUNC] = np.median(accuracy_score)
    learning_list_frame.to_csv(os.path.join(save_dir, model_type+'.csv'))

    # Dropout Rate
    model_type = 'IMDB_Dropout'
    dropout_list = [.2, .3, .4, .5, .6, .7]
    activation_functions = ['arctan', 'gaussian', 'identity','ISRU', 'sigmoid', 'tanh', 'softplus', 'trust']
    dropout_list_frame = pd.DataFrame(columns=dropout_list, index=activation_functions).T
    for ACTIVATION_FUNC in activation_functions:
        # print(ACTIVATION_FUNC)
        for DROPOUT_RATE in dropout_list:
            accuracy_score = []
            for i in range(iterations):
                accuracy_score.append(build_model(X_train, X_test, y_train, y_test, ACTIVATION_FUNC,UNITS, LAYERS, EPOCHS, BATCH_SIZE, LEARNING_RATE, DROPOUT_RATE))
            dropout_list_frame.loc[DROPOUT_RATE,ACTIVATION_FUNC] = np.median(accuracy_score)
    dropout_list_frame.to_csv(os.path.join(save_dir, model_type+'.csv'))

    # Dense Units
    model_type = 'IMDB_Dense'
    dense_list = [50, 100, 250, 500, 750, 1000]
    activation_functions = ['arctan', 'gaussian', 'identity','ISRU', 'sigmoid', 'tanh', 'softplus', 'trust']
    dense_list_frame = pd.DataFrame(
        columns=dense_list, index=activation_functions).T
    for ACTIVATION_FUNC in activation_functions:
        # print(ACTIVATION_FUNC)
        for UNITS in dense_list:
            accuracy_score = []
            for i in range(iterations):
                accuracy_score.append(build_model(X_train, X_test, y_train, y_test, ACTIVATION_FUNC,UNITS, LAYERS, EPOCHS, BATCH_SIZE, LEARNING_RATE, DROPOUT_RATE))
            dense_list_frame.loc[UNITS, ACTIVATION_FUNC] = np.median(accuracy_score)
    dense_list_frame.to_csv(os.path.join(save_dir, model_type+'.csv'))
