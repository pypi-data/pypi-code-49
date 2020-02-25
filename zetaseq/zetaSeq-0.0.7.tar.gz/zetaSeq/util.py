#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 10:36:47 2018

Coders who love to comment their code are unlikely to have bad luck.

@author: Zewei Song
@email: songzewei@genomics.cn
"""
#%
from __future__ import print_function
from __future__ import division

def test_me(args):
    from zetaSeq import io as seqIO
    seqIO.test_me()
    print('Inputfile assigned as {0}'.format(args.inputfile))

def concat_biom():
    pass


# coun the number of reads aligned to the reference.
# Reads may align to more than one record.
def countAlnReads(args):
    inputFile = args.input
    
    reads = {}
    with open(inputFile, 'r') as f:
        for line in f:
            line = line.strip('\n').split('\t')
            currentRead = line[0]
            reads[currentRead] = reads.get(currentRead, 0) + 1    
    
    print('There are {0} reads in the alignment {1}.'.format(len(reads), inputFile))
    return None