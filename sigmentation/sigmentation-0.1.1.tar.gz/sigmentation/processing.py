# This file is part of the Sigmentation project.
#    https://gitlab.com/sigmentation/sigmentation
#
# Copyright 2020 Zeyd Boukhers <zeyd@boukhers.com>
#                Matthias Lohr <mail@mlohr.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy
import os
import random


def generate(channel_count, channel_length, minmax, use_integer=False):
    """
    This function generates (N) channels sequences of the same length (L). R is an optional argument that must be a
    range such as: [min_value, max_value]. it takes an optional argument called 'use_integer' which by default false.
    """
    vec = []
    try:
        minmax.sort()
        for x in range(channel_count):
            tmp = []
            for y in range(channel_length):
                if use_integer:
                    tmp.append(random.randint(int(minmax[0]), int(minmax[1])))
                else:
                    tmp.append(random.uniform(minmax[0], minmax[1]))
            vec.append(tmp)
    except Exception as e:  # TypeError or AttributeError as e:
        e.args = ('R is an optional argument that must be a range such as: [min_value, max_value]',)
        raise
    return vec


"""
def generate (N,L,*R):
    vec=[]
    if bool(R):
        try:
            R.sort()
            for x in range (N):
                a=random.randint(R[0],R[1])
                tmp=[]
                for y in range(L):
                    tmp.append(random.uniform(-a,a*3))
                vec.append(tmp)
        except Exception as e: #TypeError or AttributeError as e:
            e.args = ('R is an optional argument that must be a range such as: [min_value, max_value]',)
            raise
    else:
        for x in range (N):
            a=random.random()
            tmp=[]
            for y in range(L):
                tmp.append(random.uniform(-a,a*3))
            vec.append(tmp)
    return vec
"""


def get_train_test(features, labels, train_ratio):
    # if train ration = 7 it means 70% of train and the remaining test
    train_feat = []
    train_labels = []
    test_feat = []
    test_labels = []
    features = numpy.array(features)
    labels = numpy.array(labels)
    classes = numpy.unique(labels)

    for the_class in classes:
        tmp = numpy.where(labels == the_class)[0]
        if not os.path.isfile(str(the_class) + '_' + str(train_ratio) + '.npy'):
            tmp = random.sample(tmp, len(tmp))
            numpy.save(str(the_class) + '_' + str(train_ratio) + '.npy', tmp)
        else:
            tmp = numpy.load(str(the_class) + '_' + str(train_ratio) + '.npy')
        sep = len(tmp) * train_ratio / 10
        train_feat.extend(features[tmp[0:sep]])
        train_labels.extend(labels[tmp[0:sep]])

        test_feat.extend(features[tmp[sep::]])
        test_labels.extend(labels[tmp[sep::]])
    return numpy.array(train_feat), numpy.array(test_feat), numpy.array(train_labels), numpy.array(test_labels)


def sampling(features, labels, sampling):
    # balance the data (random over sampling)
    P = int(sum(labels))  # number of positives
    N = int(len(labels) - sum(labels))  # number of negatives
    tmp = numpy.asarray([i for i, c in enumerate(labels) if c == 0])
    tmp1 = numpy.asarray([i for i, c in enumerate(labels) if c == 1])

    if sampling == 'down':
        # downsampling
        if N < P:
            if not os.path.isfile(sampling + str(P) + '_' + str(N) + 'N.npy'):
                tmp2 = [random.randint(0, len(tmp1) - 1) for xx in range(N)]
                numpy.save(sampling + str(P) + '_' + str(N) + 'N.npy', tmp2)
            else:
                tmp2 = numpy.load(sampling + str(P) + '_' + str(N) + 'N.npy')
            tmp1 = tmp1[tmp2]
        else:
            if not os.path.isfile(sampling + str(P) + '_' + str(N) + 'P.npy'):
                tmp2 = [random.randint(0, len(tmp) - 1) for xx in range(P)]
                numpy.save(sampling + str(P) + '_' + str(N) + 'N.npy', tmp2)
            else:
                tmp2 = numpy.load(sampling + str(P) + '_' + str(N) + 'P.npy')

            tmp = tmp[tmp2]
    elif sampling == 'over':
        # oversampling
        if N > P:
            tmp4 = len(tmp1) - 1
            tmp2 = numpy.concatenate(
                (numpy.repeat(range(tmp4 + 1), N / tmp4), [random.randint(0, tmp4) for xx in range(N % tmp4)]))
            tmp1 = tmp1[tmp2]
        else:
            tmp4 = len(tmp) - 1
            tmp2 = numpy.concatenate(
                (numpy.repeat(range(tmp4 + 1), P / tmp4), [random.randint(0, tmp4) for xx in range(P % tmp4)]))
            tmp = tmp[tmp2]
    features = numpy.concatenate((features[tmp], features[tmp1]), axis=0)
    labels = numpy.concatenate((labels[tmp], labels[tmp1]), axis=0)
    return features, labels


def extract_feat(sequence):
    x = range(len(sequence))
    tmp = stats.linregress(x, sequence)
    slope = tmp[0]
    intercept = tmp[1]
    diff = numpy.array([(slope * x[xx] + intercept) - sequence[xx] for xx in range(len(sequence))])  # see 1
    tmp1 = numpy.subtract(numpy.sign(diff[0:-1]), numpy.sign(diff[1::]))  # see 2
    tmp1 = numpy.where(tmp1 != 0)[0]
    tmp2 = numpy.diff(tmp1)
    tmp1 = numpy.add(numpy.divide(tmp2, 2), tmp1[0:-1])
    if len(tmp2) > 1:
        tmp3 = numpy.array(diff)[tmp1]
        serr = numpy.std(abs(tmp3))
        serr2 = numpy.mean(tmp3[numpy.where(tmp3 >= 0)[0]])
        serr2 = 0 if numpy.isnan(serr2) else serr2
        serr3 = numpy.mean(tmp3[numpy.where(tmp3 < 0)[0]])
        serr3 = 0 if numpy.isnan(serr3) else serr3
        frq = numpy.std(tmp2)
    else:
        serr = 0
        serr2 = 0
        serr3 = 0
        frq = 0

    err = numpy.std(numpy.multiply(diff, diff))
    err2 = numpy.mean(diff[numpy.where(diff >= 0)[0]])
    err2 = 0 if numpy.isnan(err2) else err2
    err3 = numpy.mean(diff[numpy.where(diff < 0)[0]])
    err3 = 0 if numpy.isnan(err3) else err3
    err4 = 1.0 * len(numpy.where(diff == 0)[0]) / len(diff)
    err4 = 0 if numpy.isnan(err4) else err4

    angle = float(numpy.rad2deg(numpy.arctan(slope)))

    slope2 = 1.0 * (sequence[-1] - sequence[0]) / len(sequence)
    return [numpy.mean(sequence), len(sequence), numpy.max(sequence), numpy.min(sequence), slope, intercept, err, err2, err3,
            err4, frq, serr, serr2, serr3, slope2]


def norma_max_min(seq):
    seq = numpy.array(seq)
    tmp = (max(seq) - min(seq))
    nseq = 1.0 * (seq - min(seq)) / tmp if tmp != 0 else 0 * seq
    return nseq


def norma_one_one(seq):
    seq = numpy.array(seq)
    tmp = (max(seq) - min(seq))
    nseq = (2.0 * (seq - min(seq)) / tmp) - 1 if tmp != 0 else 0 * seq
    return nseq


def standa(seq):
    seq = numpy.array(seq)
    tmp = numpy.std(seq, axis=0)
    nseq = 1.0 * (seq - numpy.mean(seq, axis=0)) / tmp if tmp != 0 else 0 * seq
    return nseq
