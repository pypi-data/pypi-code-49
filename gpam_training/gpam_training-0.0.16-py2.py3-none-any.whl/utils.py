from tqdm import tqdm
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn import preprocessing


class GpamTokenizer:
    def __init__(self, vocab, texts):
        self.vocab = vocab
        self.texts = texts
        self.dict_vocab = {}

    def list_2_dict(self):
        id = 1
        for word in self.vocab:
            self.dict_vocab[word] = id
            id += 1

    def return_tokens(self, text):
        return text.split(" ")

    def transform_tokens(self, tokens):
        result_transform = []
        for token in tokens:
            try:
                id = self.dict_vocab[token]
                result_transform.append(id)
            except Exception:
                continue

        return result_transform

    def pad_vector(self, texts, num):
        reshape_v = []

        for each in tqdm(texts):
            if len(each) >= num:
                reshape_v.append(each[0:num])
            else:
                zeros = num - len(each)
                temp = each
                v_zeros = [0 for each in range(zeros)]
                temp.extend(v_zeros)
                reshape_v.append(temp)

        return reshape_v

    def tokenizer_with_vocab(self, num):
        self.list_2_dict()
        result_texts = []
        for i in tqdm(range(len(self.texts))):
            tokens = self.return_tokens(self.texts.iloc[i])
            result_transform = self.transform_tokens(tokens)
            result_texts.append(result_transform)

        result = self.pad_vector(result_texts, num)

        return np.matrix(result)


def binarize_pred(preds):
    new_preds = []
    for each in preds:
        num = max(each)
        new_list = np.asarray([0 for temp in range(len(each))])
        new_list[np.where(each == num)[0][0]] = 1
        new_preds.append(np.asarray(new_list))
    return new_preds


def cnn_pecas_model(n_class, max_features, sequence_len, embedding_out):
    model = keras.Sequential()
    model.add(
        keras.layers.Embedding(
            input_dim=max_features, output_dim=embedding_out, input_length=sequence_len
        )
    )

    model.add(keras.layers.Conv1D(kernel_size=4, filters=256, padding="same"))
    model.add(keras.layers.Dropout(0.5))
    model.add(keras.layers.MaxPooling1D(pool_size=2))
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(512, activation="relu"))
    model.add(keras.layers.Dropout(0.5))
    model.add(keras.layers.Dense(n_class, activation="softmax"))
    model.compile(
        loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"]
    )

    return model


def cnn_pecas_model2(n_class, max_features, sequence_len, embedding_out):
    f1_base = keras.layers.Input(shape=(sequence_len,), dtype="int32")
    text_embedding = keras.layers.Embedding(
        input_dim=max_features, output_dim=embedding_out, input_length=sequence_len
    )(f1_base)

    filter_sizes = [3, 4, 5]
    convs = []
    for filter_size in filter_sizes:
        l_conv = keras.layers.Conv1D(
            filters=256, kernel_size=filter_size, padding="same", activation="relu"
        )(text_embedding)
        l_batch = keras.layers.BatchNormalization()(l_conv)
        l_pool = keras.layers.MaxPooling1D(2)(l_conv)

        convs.append(l_pool)

    l_merge = keras.layers.Concatenate(axis=1)(convs)
    l_pool1 = keras.layers.MaxPooling1D(50)(l_merge)
    l_flat = keras.layers.Flatten()(l_pool1)
    l_dense = keras.layers.Dense(128, activation="relu")(l_flat)
    x = keras.layers.Dropout(0.5)(l_dense)
    # f1_x = Flatten()(f1_x)
    x = keras.layers.Dense(n_class, activation="softmax")(x)
    model = keras.models.Model(inputs=f1_base, outputs=x)
    # determine Loss function and Optimizer
    model.compile(
        loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"]
    )
    return model


class Y_transform:
    def __init__(self, y_all):
        self.y_all = y_all
        self.le = preprocessing.LabelEncoder()
        self.le.fit(list(set(y_all)))

    def transform(self, y):
        y_temp = self.le.transform(y)
        y_temp = np.transpose(y_temp)
        y_temp = tf.keras.utils.to_categorical(y_temp)
        return y_temp

    def classes(self):
        return self.le.classes_


class CallBack(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if logs.get("acc") and logs.get("acc") >= 0.98:
            print("\nReached 95% accuracy so cancelling training!")
            self.model.stop_training = True
