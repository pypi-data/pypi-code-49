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
from scipy.signal import find_peaks


def feature_extract(sequences):
    # return [[[i,len(sequence[i])]+slope_angle(sequence[i]) for i in range(len(sequence))] for sequence in sequences
    return [[i, len(sequence[i])] + slope_angle(sequence[i]) for sequence in sequences for i in range(len(sequence))]


# This function takes one dimentional sequence (inp) and interpolates it into the new length (new_len)
def interpolate(inp, new_len):
    delta = float(new_len - 1) / (len(inp) - 1)
    a = [inp[int(x / delta)] if (int(x / delta) == numpy.float32(x / float(delta))) else inp[int(x / delta)] + (
                ((x / float(delta)) - (int(x / delta))) * (inp[int(x / delta) + 1] - inp[int(x / delta)])) for x in
         range(new_len)]
    return (a)


# This function takes one dimentional sequence or a subsequence (sequence) and compute its 1) mean value, 2) length, 3) trend in terms of angle and 4) mean of squre errors.
def slope_angle(sequence):
    x = range(len(sequence))
    tmp = stats.linregress(x, sequence)
    slope = tmp[0]
    intercept = tmp[1]
    err = numpy.mean([numpy.power((slope * x[xx] + intercept) - sequence[xx], 2) for xx in range(len(sequence))])
    angle = float(numpy.rad2deg(numpy.arctan(slope)))
    return [numpy.mean(sequence), len(sequence), angle, err]


def slope_angle2(sequence):
    x = range(len(sequence))
    tmp = stats.linregress(x, sequence)
    slope = tmp[0]
    intercept = tmp[1]
    diff = [(slope * x[xx] + intercept) - sequence[xx] for xx in range(len(sequence))]  # see 1
    tmp1 = numpy.subtract(numpy.sign(diff[0:-1]), numpy.sign(diff[1::]))  # see 2
    tmp1 = numpy.where(tmp1 != 0)[0]
    tmp2 = numpy.diff(tmp1)
    tmp1 = numpy.add(numpy.divide(tmp2, 2), tmp1[0:-1])
    serr = numpy.std(abs(numpy.array(diff)[tmp1])) if len(tmp2) > 1 else 0
    frq = numpy.std(tmp2) if len(tmp2) > 1 else 0
    err = numpy.mean(numpy.multiply(diff, diff))
    # err=numpy.exp(err)*numpy.exp(frq)*numpy.exp(serr)
    err = (err + 1) * (frq + 1) * (serr + 1)
    angle = float(numpy.rad2deg(numpy.arctan(slope)))
    return [numpy.mean(sequence), len(sequence), angle, err]


def fft_measure(sequence):
    vec = interpolate(sequence, 30)  # sequence#
    nvec = numpy.array(vec)  # norma_one_one(vec) #numpy.array(vec)#
    # nvec=numpy.array(numpy.sin(numpy.deg2rad(vec)))
    N = len(nvec)
    sp = numpy.fft.fft(nvec)
    freq = numpy.fft.fftfreq(nvec.shape[-1])
    # almf=2.0/N *numpy.power(sp.real[0:N//2],2)  #almost fourier
    almf = 2.0 / N * numpy.sqrt(numpy.power(sp.real[0:N // 2], 2) + numpy.power(sp.imag[0:N // 2], 2))
    # find peaks
    peaks, p = find_peaks(almf, height=0.001)

    '''
    nvec2=nvec*90#nvec#
    svec=numpy.sin(nvec2)  #sinus
    sp = numpy.fft.fft(svec)
    almf2=2.0/N *abs(sp.real[0:N//2])  #almost fourier
    peaks2, p2 = find_peaks(almf2, height=0.1)

    p2=numpy.sum(p2['peak_heights'])/10.0 if len(p2['peak_heights'])>0 else len(sequence)/1000.0
    '''
    # p=numpy.sum(p['peak_heights']) if len(p['peak_heights'])>0 else 0
    p = numpy.max(p['peak_heights']) if len(p['peak_heights']) > 0 else 0  # p2

    return p


# This function computes the positions of separators that divide a sequence of length (length) into a number (split) of equal parts
def get_start(split, length):
    return [0] + [(length / split) * (tmp + 1) for tmp in range(split - 1)] + [length]


# This function takes a multivariate sequence (sequences) and extract seubsequences from each of its sequence given the positions of separators (start). The separators are similarly applied to all sequences. In case the sequence is one dimentional, the input must be between square brackets: [sequences]
def get_sub_sequences(sequences, start):
    return [[sequence[start[tmp - 1]:start[tmp]] for tmp in range(1, len(start))] for sequence in sequences]


# This function compute the parameters that define the constraints of the minimization. It output a list of four vectors, where their length correspond to the length of the seprators without considering the begiing and the end of the sequence. the first vector consists of the seprators (without 0 and length). The second and third vectors represent the minimum and maximum values, respectively, that the new separator must not exceed. The last vector stores the step that each separator is allowed to take. This function takes as input the list of separators (start), the minimum lengh (min_length) of each subsequence and the initial step.
def get_param(start, min_length, initial_step):  # initial step
    return [[start[tmp] for tmp in range(1, len(start) - 1)],
            [start[tmp - 1] + min_length for tmp in range(1, len(start) - 1)],
            [start[tmp + 1] - min_length for tmp in range(1, len(start) - 1)],
            [initial_step for tmp in range(1, len(start) - 1)]]


# This function updates the parameters (param) in a specific position given the new last separators.
def update_param(param, position, start, min_length):
    # param[-1][position]=abs(param[0][position]-start[position+1])
    param[0][position] = start[position + 1]
    if position <= (len(param[0]) - 2):
        param[1][position + 1] = param[0][position] + min_length
    if position > 0:
        param[2][position - 1] = param[0][position] - min_length
    return param


# This function computes the list of values that a separator i (position) has already taken with the current values of the remaining separators. The reason is to avoid generating the same combination of separators. The function takes the list of all generated separators (all_strt), the current separator (strt) and the the position (position).
def get_repeat(all_strt, strt, position):
    if bool(all_strt):
        a = numpy.array(all_strt[:])
        b = numpy.copy(strt)  # b=strt[:]
        a[:, position + 1] = 0
        b[position + 1] = 0
        y = list(filter(lambda x: b == list(x[1]), enumerate(a)))
        rep = [all_strt[c[0]][position + 1] for c in y]
    else:
        rep = []
    return rep


# This is the main fucntion that minimize the search process given a multi dimentional sequence (sequence), the maximum number of divisions (max_split), where this number of separators (split) = max_split+1. It takes also the minimum length (min_length) that a subsequence must take and the initial step (step) each separator is allowed to take. In addition, the number of times after convergence (conv) must also be given.
def minimize(sequence, max_split, min_length, step, conv):
    start_time = time.time()
    length = int(sequence.shape[1])
    err = float('inf')
    conv1 = 0
    split = 1  # 1 means that the sequence is not divided.
    best_ssqs = []
    while ((conv1 < conv) & (split <= max_split)):
        strt = get_start(split=split, length=length)
        ssqs = get_sub_sequences(sequences=sequence, start=strt)
        new_err = numpy.mean(sum(numpy.array([[slope_angle(tmp)[-1] for tmp in ssq] for ssq in ssqs])))
        diff_err = new_err / err
        if diff_err >= 1:
            conv1 += 1
        else:
            conv1 = 0
            best_strt = strt[:]
            best_ssqs = ssqs[:]
            err = new_err
        split += 1
    param = get_param(start=strt, min_length=min_length, initial_step=step)

    conv2 = 0
    err1 = err
    all_strt = []
    while conv2 < conv:
        for tmp1 in range(len(param[0])):
            conv3 = 0
            while conv3 < conv:
                strt = best_strt[:]
                expt = get_repeat(all_strt, strt, tmp1)
                rng = range(max([param[0][tmp1] - param[-1][tmp1], param[1][tmp1]]),
                            min([param[0][tmp1] + param[-1][tmp1], param[2][tmp1]]))
                rng = list(filter(lambda x: x not in expt, rng))
                if bool(rng):
                    strt[tmp1 + 1] = random.choice(rng)
                    all_strt.append(strt)
                    ssqs = get_sub_sequences(sequences=sequence, start=strt)
                    new_err = numpy.mean(sum(numpy.array([[slope_angle(tmp)[-1] for tmp in ssq] for ssq in ssqs])))
                    diff_err = new_err / err
                    if diff_err >= 1:
                        conv3 += 1
                    else:
                        conv3 = 0
                        best_strt = strt[:]
                        best_ssqs = ssqs[:]
                        param = update_param(param=param, position=tmp1, start=best_strt, min_length=min_length)
                        err = new_err

                else:
                    conv3 = conv
        diff_err = err / err1
        if diff_err >= 1:
            conv2 += 1
        else:
            conv2 = 0
            err1 = err
    exec_time = time.time() - start_time
    return best_strt, best_ssqs, exec_time
