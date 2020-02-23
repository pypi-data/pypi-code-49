# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 12:40:41 2020

@author: oliver obst <o.obst@westernsydney.edu.au>
"""

import pkg_resources
import numpy as np
from scipy.io import loadmat


def pkg_loadmat(matfile):
    return loadmat(pkg_resources.resource_filename('sslbookdata', matfile))


def load_digit1(split, labels=10, return_X_y=False):
    if not 0 <= split < 12:
        raise ValueError('split should be a value between 0 and 11 (was: {})'.format(split))
    if labels != 10 and labels != 100:
        raise ValueError('labels can be either 10 or 100 (was: {})'.format(labels))    

    mat = pkg_loadmat('data/data1.mat')
    
    if labels == 10:
        allsplits = pkg_loadmat('data/splits1-labeled10.mat')
    else:
        allsplits = pkg_loadmat('data/splits1-labeled100.mat')

    il = allsplits['idxLabs'][split, :] - 1
    ul = allsplits['idxUnls'][split, :] - 1
    idx = np.append(il, ul)
        
    digit1 = {}
    digit1['data'] = mat['X'][idx, :]
    digit1['target'] = mat['y'][idx, :]
    digit1['labels'] = labels
    digit1['__header__'] = mat['__header__']
    digit1['__version__'] = mat['__version__']
    digit1['Creator'] = 'Olivier Chapelle, Bernhard Schölkopf, and Alexander Zien: Semi-Supervised Learning. MIT Press'
    
    if return_X_y:
        return (digit1['data'], digit1['target'])
    else:
        return digit1
    

def load_usps(split, labels=10, return_X_y=False):
    if not 0 <= split < 12:
        raise ValueError('split should be a value between 0 and 11 (was: {})'.format(split))
    if labels != 10 and labels != 100:
        raise ValueError('labels can be either 10 or 100 (was: {})'.format(labels))    
    
    mat = pkg_loadmat('data/data2.mat')
    
    if labels == 10:
        allsplits = pkg_loadmat('data/splits2-labeled10.mat')
    else:
        allsplits = pkg_loadmat('data/splits2-labeled100.mat')

    il = allsplits['idxLabs'][split, :] - 1
    ul = allsplits['idxUnls'][split, :] - 1
    idx = np.append(il, ul)
        
    usps = {}
    usps['data'] = mat['X'][idx, :]
    usps['target'] = mat['y'][idx, :]
    usps['labels'] = labels
    usps['__header__'] = mat['__header__']
    usps['__version__'] = mat['__version__']
    usps['Creator'] = 'Olivier Chapelle, Bernhard Schölkopf, and Alexander Zien: Semi-Supervised Learning. MIT Press'
    
    if return_X_y:
        return (usps['data'], usps['target'])
    else:
        return usps
    

def load_coil2(split, labels=10, return_X_y=False):
    if not 0 <= split < 12:
        raise ValueError('split should be a value between 0 and 11 (was: {})'.format(split))
    if labels != 10 and labels != 100:
        raise ValueError('labels can be either 10 or 100 (was: {})'.format(labels))    
    
    mat = pkg_loadmat('data/data3.mat')
    
    if labels == 10:
        allsplits = pkg_loadmat('data/splits3-labeled10.mat')
    else:
        allsplits = pkg_loadmat('data/splits3-labeled100.mat')

    il = allsplits['idxLabs'][split, :] - 1
    ul = allsplits['idxUnls'][split, :] - 1
    idx = np.append(il, ul)
        
    coil2 = {}
    coil2['data'] = mat['X'][idx, :]
    coil2['target'] = mat['y'][idx, :]
    coil2['labels'] = labels
    coil2['__header__'] = mat['__header__']
    coil2['__version__'] = mat['__version__']
    coil2['Creator'] = 'Olivier Chapelle, Bernhard Schölkopf, and Alexander Zien: Semi-Supervised Learning. MIT Press'
    
    if return_X_y:
        return (coil2['data'], coil2['target'])
    else:
        return coil2
    

def load_bci(split, labels=10, return_X_y=False):
    if not 0 <= split < 12:
        raise ValueError('split should be a value between 0 and 11 (was: {})'.format(split))
    if labels != 10 and labels != 100:
        raise ValueError('labels can be either 10 or 100 (was: {})'.format(labels))    
    
    mat = pkg_loadmat('data/data4.mat')
    
    if labels == 10:
        allsplits = pkg_loadmat('data/splits4-labeled10.mat')
    else:
        allsplits = pkg_loadmat('data/splits4-labeled100.mat')

    il = allsplits['idxLabs'][split, :] - 1
    ul = allsplits['idxUnls'][split, :] - 1
    idx = np.append(il, ul)
        
    bci = {}
    bci['data'] = mat['X'][idx, :]
    bci['target'] = mat['y'][idx, :]
    bci['labels'] = labels
    bci['__header__'] = mat['__header__']
    bci['__version__'] = mat['__version__']
    bci['Creator'] = 'Olivier Chapelle, Bernhard Schölkopf, and Alexander Zien: Semi-Supervised Learning. MIT Press'
    
    if return_X_y:
        return (bci['data'], bci['target'])
    else:
        return bci
    

def load_g241c(split, labels=10, return_X_y=False):
    if not 0 <= split < 12:
        raise ValueError('split should be a value between 0 and 11 (was: {})'.format(split))
    if labels != 10 and labels != 100:
        raise ValueError('labels can be either 10 or 100 (was: {})'.format(labels))    
    
    mat = pkg_loadmat('data/data5.mat')
    
    if labels == 10:
        allsplits = pkg_loadmat('data/splits5-labeled10.mat')
    else:
        allsplits = pkg_loadmat('data/splits5-labeled100.mat')

    il = allsplits['idxLabs'][split, :] - 1
    ul = allsplits['idxUnls'][split, :] - 1
    idx = np.append(il, ul)
        
    g241c = {}
    g241c['data'] = mat['X'][idx, :]
    g241c['target'] = mat['y'][idx, :]
    g241c['labels'] = labels
    g241c['__header__'] = mat['__header__']
    g241c['__version__'] = mat['__version__']
    g241c['Creator'] = 'Olivier Chapelle, Bernhard Schölkopf, and Alexander Zien: Semi-Supervised Learning. MIT Press'
    
    if return_X_y:
        return (g241c['data'], g241c['target'])
    else:
        return g241c
    

def load_coil(split, labels=10, return_X_y=False):
    if not 0 <= split < 12:
        raise ValueError('split should be a value between 0 and 11 (was: {})'.format(split))
    if labels != 10 and labels != 100:
        raise ValueError('labels can be either 10 or 100 (was: {})'.format(labels))    
    
    mat = pkg_loadmat('data/data6.mat')
    
    if labels == 10:
        allsplits = pkg_loadmat('data/splits6-labeled10.mat')
    else:
        allsplits = pkg_loadmat('data/splits6-labeled100.mat')

    il = allsplits['idxLabs'][split, :] - 1
    ul = allsplits['idxUnls'][split, :] - 1
    idx = np.append(il, ul)
        
    coil = {}
    coil['data'] = mat['X'][idx, :]
    coil['target'] = mat['y'][idx, :]
    coil['labels'] = labels
    coil['__header__'] = mat['__header__']
    coil['__version__'] = mat['__version__']
    coil['Creator'] = 'Olivier Chapelle, Bernhard Schölkopf, and Alexander Zien: Semi-Supervised Learning. MIT Press'
    
    if return_X_y:
        return (coil['data'], coil['target'])
    else:
        return coil
    

def load_g241n(split, labels=10, return_X_y=False):
    if not 0 <= split < 12:
        raise ValueError('split should be a value between 0 and 11 (was: {})'.format(split))
    if labels != 10 and labels != 100:
        raise ValueError('labels can be either 10 or 100 (was: {})'.format(labels))    
    
    mat = pkg_loadmat('data/data7.mat')
    
    if labels == 10:
        allsplits = pkg_loadmat('data/splits7-labeled10.mat')
    else:
        allsplits = pkg_loadmat('data/splits7-labeled100.mat')

    il = allsplits['idxLabs'][split, :] - 1
    ul = allsplits['idxUnls'][split, :] - 1
    idx = np.append(il, ul)
        
    g241n = {}
    g241n['data'] = mat['X'][idx, :]
    g241n['target'] = mat['y'][idx, :]
    g241n['labels'] = labels
    g241n['__header__'] = mat['__header__']
    g241n['__version__'] = mat['__version__']
    g241n['Creator'] = 'Olivier Chapelle, Bernhard Schölkopf, and Alexander Zien: Semi-Supervised Learning. MIT Press'
    
    if return_X_y:
        return (g241n['data'], g241n['target'])
    else:
        return g241n
    

def load_secstr(split, labels=100, extra_unlabeled=False, return_X_y=False):
    if not 0 <= split < 10:
        raise ValueError('split should be a value between 0 and 9 (was: {})'.format(split))
    if labels != 100 and labels != 1000 and labels != 10000:
        raise ValueError('labels can be either 100, 1000 or 10000 (was: {})'.format(labels))    
        
    def explode(Xin):
        m, d0 = Xin.shape
        ks = np.unique(Xin)
        k = len(ks)
        d1 = k * d0
        X = np.zeros((m,d1), dtype='u1')
        l = 0
        for i in range(k):
            X[:, l:l+d0] = Xin == ks[i]
            l = l + d0
        return X
    
    mat = pkg_loadmat('data/data8.mat')
    X = explode(mat['T'])

    if extra_unlabeled:
        mat2 = pkg_loadmat('data/data8extra.mat')
        Xextra = explode(mat2['T'])
        
    if labels == 100:
        allsplits = pkg_loadmat('data/splits8-labeled100.mat')
    elif labels == 1000:
        allsplits = pkg_loadmat('data/splits8-labeled1000.mat')
    else:
        allsplits = pkg_loadmat('data/splits8-labeled10000.mat')

    il = allsplits['idxLabs'][split, :] - 1
    ul = allsplits['idxUnls'][split, :] - 1
    idx = np.append(il, ul)
        
    secstr = {}
    secstr['data'] = X[idx, :]
    secstr['target'] = mat['y'][idx, :]
    secstr['labels'] = labels
    secstr['nextra'] = 0
    if extra_unlabeled:
        secstr['nextra'] = Xextra.shape[0]
        secstr['extra'] = Xextra
    secstr['__header__'] = mat['__header__']
    secstr['__version__'] = mat['__version__']
    secstr['Creator'] = 'Olivier Chapelle, Bernhard Schölkopf, and Alexander Zien: Semi-Supervised Learning. MIT Press'
    
    if return_X_y:
        if extra_unlabeled:
            return (secstr['data'], secstr['target'], secstr['extra'])
        else:
            return (secstr['data'], secstr['target'])
    else:
        return secstr


def load_text(split, labels=10, return_X_y=False):
    if not 0 <= split < 12:
        raise ValueError('split should be a value between 0 and 11 (was: {})'.format(split))
    if labels != 10 and labels != 100:
        raise ValueError('labels can be either 10 or 100 (was: {})'.format(labels))    
    
    mat = pkg_loadmat('data/data9.mat')
    
    if labels == 10:
        allsplits = pkg_loadmat('data/splits9-labeled10.mat')
    else:
        allsplits = pkg_loadmat('data/splits9-labeled100.mat')

    il = allsplits['idxLabs'][split, :] - 1
    ul = allsplits['idxUnls'][split, :] - 1
    idx = np.append(il, ul)
        
    text = {}
    text['data'] = mat['X'][idx, :]
    text['target'] = mat['y'][idx, :]
    text['labels'] = labels
    text['__header__'] = mat['__header__']
    text['__version__'] = mat['__version__']
    text['Creator'] = 'Olivier Chapelle, Bernhard Schölkopf, and Alexander Zien: Semi-Supervised Learning. MIT Press'
    
    if return_X_y:
        return (text['data'], text['target'])
    else:
        return text
