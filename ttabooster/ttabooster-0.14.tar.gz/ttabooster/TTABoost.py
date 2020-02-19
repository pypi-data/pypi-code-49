import numpy as np

from tensorflow.keras.models import Model

import tensorflow as tf
from tensorflow.python.keras.utils.data_utils import Sequence
import pandas as pd
from sklearn.cluster import AgglomerativeClustering

import csv
import gc

config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True  # dynamically grow the memory used on the GPU
config.log_device_placement = True  # to log device placement (on which device the operation ran)
sess = tf.compat.v1.Session(config=config)


class AugSequence(Sequence):
    def __init__(self, x_set, batch_size=32, augmentations=lambda image: image, layer_name='flatten'):
        self.x = x_set
        self.batch_size = batch_size
        self.augment = augmentations
        self.layer_name = layer_name

    def __len__(self):
        return int(np.ceil(len(self.x) / float(self.batch_size)))

    def __getitem__(self, idx):
        batch_x = self.x[idx * self.batch_size:(idx + 1) * self.batch_size]
        # batch_y = self.y[idx * self.batch_size:(idx + 1) * self.batch_size]

        return np.stack([self.augment(image=x)["image"] for x in batch_x], axis=0)


class TTABooster:
    def __init__(self, model, n_tta=30, k=10, batch_size=100, augmentations=[], reduction='ttabooster'):
        print("TTABoost ctor")
        self.model = model
        self.n_tta = n_tta
        self.k = k
        self.batch_size = batch_size
        self.augmentations = augmentations

    @staticmethod
    def top_k_accuracy(y_true, y_pred, k=1):
        '''From: https://github.com/chainer/chainer/issues/606

        Expects both y_true and y_pred to be one-hot encoded.
        '''
        argsorted_y = np.argsort(y_pred)[:, -k:]
        return np.any(argsorted_y.T == y_true.argmax(axis=1), axis=0).mean()

    @staticmethod
    def chunker(seq, size):
        return (seq[pos:pos + size] for pos in range(0, len(seq), size))

    def features_and_probs(self, x_chunck):
        layer_name = self.layer_name  # TODO: Extract the last layer name from the model
        intermediate_layer_model = Model(inputs=self.model.input,
                                         outputs=[self.model.get_layer(layer_name).output, self.model.output])
        valid_gen = AugSequence(x_set=x_chunck, batch_size=self.batch_size, augmentations=self.augmentations[0])
        # TODO: Make AugSequence work with multiple functions
        intermediate_output = intermediate_layer_model.predict(valid_gen, workers=1,
                                                               steps=len(x_chunck) * self.n_tta / self.batch_size
                                                               )
        embeddings, probs = intermediate_output[0], intermediate_output[1]
        del intermediate_output
        ## values ndarray will be of the shape (len(x_chuck),n_tta*n_classes) - for each sample, the predictions of all it's ttas
        sample_probs = probs[0:len(x_chunck),
                       :]  # Init the array with the first sample result (of all augmnetations)
        for i in range(self.n_tta - 1):  # Fill with rest of samples
            sample_probs = np.hstack([sample_probs, probs[(i + 1) * len(x_chunck):len(x_chunck) * (i + 2), :]])
        sample_features = embeddings[0:len(x_chunck), :]
        del probs
        gc.collect()
        for i in range(self.n_tta - 1):
            # gc.collect()
            sample_features = np.hstack(
                [sample_features, embeddings[(i + 1) * len(x_chunck):len(x_chunck) * (i + 2), :]])
        del embeddings
        gc.collect()
        return sample_features, sample_probs

    def predict(self, x, chunk_size=100):
        boost_ens = pd.DataFrame()
        all_ens = pd.DataFrame()
        random_ens = pd.DataFrame()
        
        for index, x_chunck in enumerate(TTABooster.chunker(x, chunk_size)):
            print("Started chunk", index, "of size", chunk_size)
            y_pred = self.model.predict(x_chunck, batch_size=self.batch_size, verbose=1)
            sample_features, sample_probs = self.features_and_probs(x_chunck)
            random_sample_probs = sample_probs[:, 0:sample_probs.shape[1] * self.k]

            for i in range(sample_features.shape[0]):
                AC = AgglomerativeClustering(n_clusters=self.k, linkage='average', affinity='cosine').fit(
                    np.stack([sample_features[i:i + 1, x:x + sample_features.shape[1]] for x in
                              range(0, sample_features.shape[1], sample_features.shape[1])],
                             axis=1).reshape(self.n_tta, sample_features.shape[1]))
                temp = pd.DataFrame(
                    np.stack(
                        [sample_probs[i:i + 1, x:x + sample_probs.shape[1]] for x in range(0, sample_probs.shape[1], sample_probs.shape[1])],
                        axis=1).reshape(self.n_tta, sample_probs.shape[1]))

                temp = temp.append(pd.DataFrame(y_pred[i, :]).T)
                AC.labels_ = np.hstack((AC.labels_, 999))
                temp['label'] = AC.labels_
                temp.drop_duplicates(subset='label', inplace=True)
                temp.drop('label', axis=1, inplace=True)
                boost_ens = boost_ens.append(pd.DataFrame(temp.mean(axis=0))[0])
                all_ens = all_ens.append(pd.DataFrame(temp.mean(axis=0))[0])
                if i % 1000 == 0:
                    print(i)

            for i in range(random_sample_probs.shape[0]):
                random_temp = pd.DataFrame(
                    np.stack([random_sample_probs[i:i + 1, x:x + sample_probs.shape[1]] for x in
                              range(0, random_sample_probs.shape[1], sample_probs.shape[1])],
                             axis=1).reshape(self.k, sample_probs.shape[1]))

                random_temp = random_temp.append(pd.DataFrame(y_pred[i, :]).T)
                random_ens = random_ens.append(pd.DataFrame(random_temp.mean(axis=0))[0])

        return boost_ens.values, all_ens.values, random_ens.values

    def benchmark_results(self, x, y):
        results = {}
        print("Predicting without tta...")
        y_pred = self.model.predict(x, batch_size=self.batch_size, verbose=1)
        no_tta_acc_top_1, no_tta_acc_top_5 = TTABooster.top_k_accuracy(y, y_pred, k=1), TTABooster.top_k_accuracy(y,
                                                                                                                  y_pred,
                                                                                                                  k=5)
        results['No TTA'] = {'top1': no_tta_acc_top_1, 'top5': no_tta_acc_top_5}

        print("Predicting with tta selection ...")
        y_pred_ttaboost, y_pred_tta_all, y_pred_random_tta = self.predict(x)
        tta_boost_acc_top_1, tta_boost_acc_top_5 = TTABooster.top_k_accuracy(y, y_pred_ttaboost,
                                                                             k=1), TTABooster.top_k_accuracy(y,
                                                                                                             y_pred_ttaboost,
                                                                                                             k=5)
        results['TTABoost'] = {'top1': tta_boost_acc_top_1, 'top5': tta_boost_acc_top_5}

        print("Predicting with random tta selection ...")
        random_tta_acc_top_1, random_tta_acc_top_5 = TTABooster.top_k_accuracy(y, y_pred_random_tta,
                                                                               k=1), TTABooster.top_k_accuracy(y,
                                                                                                               y_pred_random_tta,
                                                                                                               k=5)
        results['Random TTA'] = {'top1': random_tta_acc_top_1, 'top5': random_tta_acc_top_5}

        print("Predicting with all tta...")
        all_tta_acc_top_1, all_tta_acc_top_5 = TTABooster.top_k_accuracy(y, y_pred_tta_all,
                                                                         k=1), TTABooster.top_k_accuracy(y,
                                                                                                         y_pred_tta_all,
                                                                                                         k=5)
        results['All TTA'] = {'top1': all_tta_acc_top_1, 'top5': all_tta_acc_top_5}

        self.save_benchmark_result(results)

    def save_benchmark_result(self, results, results_file='benchmark-results.csv'):
        with open(results_file, 'a+', newline='') as csvfile:
            fieldnames = ['TTA_method', 'top1', 'top5', 'Notes']
            res_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            res_writer.writeheader()

            for method_name, accuracies in results.items():
                res_writer.writerow({'TTA_method': method_name,
                                     'top1': accuracies['top1'],
                                     'top5': accuracies['top5'],
                                     'Notes': ''})
