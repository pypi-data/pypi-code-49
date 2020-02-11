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

import contextlib
import functools
import multiprocessing
import numpy
import random
import time
from .optimization import get_sub_sequences, fft_measure


def crossover(parent1, parent2, option='Single', position=None):
    """
    This function crossover two parents into two childs given one or two position points. position must be a list even
    if it consists of only one position point. If no position point is given, the function choose one randomly.
    Note that both parents must have the same lenth that denotes the number of variables (separators)
    """
    child1 = None
    child2 = None
    prob = random.random()
    if prob <= 0.6:
        if option == 'Single':
            if position is None:
                position = [random.randint(1, min(len(parent1), len(parent2)) - 1)]
            if len(position) == 1:
                child1 = list(parent1[0:position[0]]) + list(parent2[position[0]::])
                child2 = list(parent2[0:position[0]]) + list(parent1[position[0]::])
            else:
                child1 = list(parent1[0:position[0]]) + list(parent2[position[0]:position[1]]) + list(
                    parent1[position[1]::])
                child2 = list(parent2[0:position[0]]) + list(parent1[position[0]:position[1]]) + list(
                    parent2[position[1]::])
        elif option == 'Uniform':
            mask = random.sample(range(0, len(parent1)), random.randint(0, len(parent1) - 1))
            child1 = numpy.array(parent1)
            child2 = numpy.array(parent2)
            child1[mask] = child2[mask]
            tmp = numpy.array(parent1)
            child2[mask] = tmp[mask]
        elif option == 'Similar':
            child1 = numpy.array(parent1)
            child2 = numpy.array(parent2)
            mask = numpy.where(child1 != child2)[0]
            child1[mask] = numpy.rint(numpy.mean([child1[mask], child2[mask]], axis=0))
            child2 = []
    else:
        child1 = parent1
        child2 = parent2
    return [child1, child2]


def mutation(parent, min_length, min_split, max_split):
    try:
        prob = random.random()
        if prob <= 0.7:
            mask = [x for x in range(1, len(parent) - 2) if random.random() <= 0.3]
            for x in mask:
                parent[x] = random.randint(parent[x - 1] + min_length, parent[x + 1] - min_length)
        # remove one
        elif (prob <= 0.85) & (len(parent - 1) > min_split):
            tmp = random.randint(1, len(parent) - 2)
            parent = parent[0:tmp] + parent[tmp + 1::]
        # add one
        elif (prob <= 1) & (len(parent - 1) < max_split):
            # tmp=numpy.argmax(numpy.diff(parent))
            tmp = selection(numpy.diff(parent),
                            1)  # draw where to add new seprataor based on the distance between two old ones.
            parent = parent[0:tmp + 1] + [
                random.randint(parent[tmp] + min_length, parent[tmp + 1] - min_length)] + parent[tmp + 1::]

    except:
        parent = []
    return parent


# This function tries to force the vector to respect the constraints. Otherwise it reject it.
def chromosome_validation(parent, min_length):
    tmp = numpy.where(numpy.diff(parent) < min_length)[0]
    parent = [int(numpy.mean([parent[x - 1], parent[x + 1]])) if (x in tmp) else parent[x] for x in range(len(parent))]
    tmp = numpy.where(numpy.diff(parent) < min_length)[0]
    parent = parent if not bool(list(tmp)) else []
    return parent


def generate_population(size, min_split, max_split, min_length, length):
    if length / max_split < min_length:
        print
        'min_lenth is larger. Please check max_split, min_length and length'
    population = []
    # for i in range(size):
    while len(population) < size:
        split = random.randint(min_split, max_split)
        values = [0] * (split - 1)
        param = [[(i + 1) * min_length for i in range(split - 1)],
                 [length - ((split - i - 1) * min_length) for i in range(split - 1)]]
        xx = random.sample(range(split - 1), split - 1)
        for x in xx:
            values[x] = random.randint(param[0][x], param[1][x])
            if x > 0:
                # param[1][x-1]= values[x]-min_length
                param[1][0:x] = [min(param[1][y], values[x] - (min_length * (x - y))) for y in range(0, x)]
            if x < len(xx) - 1:
                # param[0][x+1]= values[x]+min_length
                param[0][x + 1::] = [max(param[0][y], values[x] + (min_length * (y - x))) for y in
                                     range(x + 1, len(xx))]
        values = [0] + values + [length]
        if values not in population:
            population.append(values)
    return population


def fitness(strt, sequence):
    ssqs = get_sub_sequences(sequences=sequence, start=strt)
    # return -numpy.mean(sum(numpy.array([[slope_angle2(tmp)[-1] for tmp in ssq] for ssq in ssqs])))
    # return 1./numpy.mean(sum(numpy.array([[slope_angle2(tmp)[-1] for tmp in ssq] for ssq in ssqs])))
    # return 1./numpy.mean(sum(numpy.array([[slope_angle2(standa(interpolate(tmp,10)))[-1] for tmp in ssq] for ssq in ssqs])))
    return 1. / numpy.mean(sum(numpy.array([[slope_angle2(tmp)[-1] for tmp in ssq] for ssq in ssqs])))


def fitness2(strt, sequence):
    ssqs = get_sub_sequences(sequences=sequence, start=strt)

    tmp = [1.0 * len(ssq) / len(sequence[0]) for ssq in ssqs[0]]
    # entropy= -sum([tmp1*numpy.log2(tmp1) for tmp1 in tmp])
    entropy = [-tmp1 * numpy.log2(tmp1) for tmp1 in tmp]

    # tmp=numpy.sum(numpy.array([[fft_measure(tmp) for tmp in ssq] for ssq in ssqs]))
    # tmp=numpy.sum(sum(numpy.array([[fft_measure(tmp) for tmp in ssq] for ssq in ssqs])))
    tmp = sum(numpy.array([[fft_measure(tmp) for tmp in ssq] for ssq in ssqs]))
    res = sum([1.0 * tmp[i] / entropy[i] for i in range(len(tmp))])
    # res=1.0*sum(tmp)*sum(entropy)

    return res

    # return numpy.mean(sum(numpy.array([[fft_measure(tmp) for tmp in ssq] for ssq in ssqs])))#*fitness(strt,sequence)


def selection(fitnesses, num):
    p_fitnesses = numpy.copy(fitnesses)
    tmp = numpy.cumsum(p_fitnesses)
    sel = []
    while ((len(sel) < num) & (len(sel) < len(tmp))):
        tmp1 = numpy.argmax((tmp - random.uniform(0, tmp[-1])) > 0)
        # sel=sel+[tmp1] if tmp1 not in sel else sel
        if tmp1 not in sel:
            sel = sel + [tmp1]
            # p_fitnesses[tmp1]=p_fitnesses[tmp1]*0.8   # this one will have half chance (as before) to be picked again
    return sel, p_fitnesses


@contextlib.contextmanager
def poolcontext(*args, **kwargs):
    pool = multiprocessing.Pool(*args, **kwargs)
    yield pool
    pool.terminate()


def gen_alg(sequences, size_population, min_split, max_split, min_length, conv, max_iteration, **kwrds):
    start_time = time.time()
    length = int(sequences.shape[1])
    max_split = min(max_split, int(length / min_length) - 1)  # adapt max_split given the total length of the sequence
    min_split = min(min_split, max_split)
    channels = int(sequences.shape[0])
    population = kwrds['population'] if 'population' in kwrds else generate_population(size_population, min_split,
                                                                                       max_split, min_length, length)
    pool = poolcontext(multiprocessing.cpu_count())
    with poolcontext(processes=multiprocessing.cpu_count()) as pool:
        fitnesses = pool.map(functools.partial(fitness2, sequence=sequences), [popul for popul in population])
    pool.close()
    i_conv = 0
    i = 0
    a_population = []
    a_population.extend(population)
    while ((i_conv < conv) & (i < max_iteration) & (2 * len(population) > size_population)):
        n_population = []
        count = 0
        # re-generate new population
        pair_fitnesses = numpy.copy(fitnesses)
        while ((len(n_population) < size_population) & (count < size_population * 3)):
            count += 1
            pair, pair_fitnesses = selection(pair_fitnesses, 2)
            [parent_1, parent_2] = numpy.array(population)[pair]
            children = crossover(parent_1, parent_2)
            children = [chromosome_validation(child, min_length) for child in children if len(child) > 0]
            children = [mutation(child, min_length, min_split, max_split) for child in children if bool(child)]
            # n_population=n_population+[child for child in children if bool(child)]
            n_population = n_population + [child for child in children if (
                        (child not in n_population) & (child not in a_population) & (len(child) > min_split - 1))]

        pool = poolcontext(multiprocessing.cpu_count())
        with poolcontext(processes=multiprocessing.cpu_count()) as pool:
            n_fitnesses = pool.map(functools.partial(fitness2, sequence=sequences), [popul for popul in n_population])
        pool.close()

        if max(n_fitnesses + [0]) > max(fitnesses):
            i_conv = 0
        else:
            i_conv += 1

        tmp = numpy.concatenate((fitnesses, n_fitnesses))
        tmp2 = population + n_population

        # draw population that has to be alive based on their weights. Even those with lower weights are allowed to be drawn but with lower probability.
        tmp3, _ = selection(tmp, min([size_population, len(
            tmp)]) - 1)  # we draw thz size-1 because the other one is the chromosom with the highest weight and has to be alive (it can occur twice).
        tmp3 = tmp3 + [numpy.argmax(tmp)]
        fitnesses = tmp[tmp3]
        population = [tmp2[tmp] for tmp in tmp3]

        # since those chromosoms are already generated, they should not be re-generated
        a_population.extend([tmp4 for tmp4 in tmp2 if tmp4 not in a_population])
        # a_population.extend([tmp4 for tmp4 in population if tmp4 not in a_population])

        i += 1
    bst = numpy.argmax(fitnesses)
    # print('execution time = ' + str(time.time() - start_time) + ' Number of iteration = ' + str(i) + ' Convergence = ' + str(i_conv)
    return population, bst
