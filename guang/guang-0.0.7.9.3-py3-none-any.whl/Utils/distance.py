import numpy as np
import Levenshtein # pip install python-Levenshtein

'''
Some common distance function
'''

def euclidean_dist(vec1, vec2):

    assert vec1.shape == vec2.shape 
    return np.sqrt(np.sum((vec1 - vec2) ** 2))


def manhattan_dist(vec1, vec2):

    return np.sum(np.abs(vec1 - vec2))


def chebyshev_dist(vec1, vec2):

    return np.max(np.abs(vec1 - vec2))

def minkowski_dist(vec1, vec2, p=2):
    """
    inputParam: p
    return distance,
    while p=1: dist = manhattan_dist
    while p=2: dist = euclidean_dist
    while p=inf: dist = chebyshev_dist
    """
    s = np.sum(np.power(vec2 - vec1, p))
    return np.power(s,1/p)


def cosine_dist(vec1, vec2):

    # np.linalg.norm(vec, ord=1) 计算p=1范数,默认p=2
    return (vec1.T @ vec2)/(np.linalg.norm(vec1) * np.linalg.norm(vec2))


def distance(a, b):
    '''字符串距离'''
    return Levenshtein.ratio(a, b)


def hamming_dist(x, y):
    return np.sum(x != y) / len(x)


def jaccard_simil_coef():
    pass