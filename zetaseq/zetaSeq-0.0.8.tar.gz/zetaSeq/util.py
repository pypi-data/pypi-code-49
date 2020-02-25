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


#%% count the number of reads aligned to the reference.
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

#%% keep paired alignments
def keepPairAln(args):
    outputAln = args.output
    inputAln = []
    for f in args.input:
        inputAln.append(f)
    if len(inputAln) != 2:
        print('The number of files is not equal to 2.')
        return None
    else:
        pass
    # Build the query dictionary
    # Two alignments are combined into one
    
    queryDict = {}
    print('Parsing Read1 alignment ...')
    with open(inputAln[0], 'r') as f:
        for line in f:
            line = line.strip('\n').split('\t')
            line[0] = line[0].split('/')[0] # Get the Query label (stripped Read info)
            try:
                queryDict[line[0]]['r1'].append(line[1])
            except KeyError:
                queryDict[line[0]] = {'r1':[], 'r2':[]}
                queryDict[line[0]]['r1'].append(line[1])
    print('Found {0} queries in Read1 alignment.'.format(len(queryDict)))
    print('Parsing Read2 alignment ...')

    r2notinr1 = 0
    with open(inputAln[1], 'r') as f:
        for line in f:
            line = line.strip('\n').split('\t')
            line[0] = line[0].split('/')[0]
            try:
                queryDict[line[0]]['r2'].append(line[1])
            except KeyError:
                queryDict[line[0]] = {'r1':[], 'r2':[]}
                queryDict[line[0]]['r2'].append(line[1])
                r2notinr1 += 1
    print('Total queries add to {0}'.format(len(queryDict)))
    
    aln = {}
    for query, alignments in queryDict.items():
        try:
            overlap = tuple(set(alignments['r1']).intersection(set(alignments['r2'])))
            if len(overlap) > 0:
                aln[query] = overlap
        except KeyError:
            pass
    
    print('Found {0} queries in both alignment.'.format(len(aln)))
    print('\t representing {0} alignments.'.format(sum([len(i) for i in aln.values()])))
    print('Found {0} queries ONLY in Read2 alignment.'.format(r2notinr1))
    
    with open(outputAln, 'w') as f:
        for query, alignments in aln.items():
            for item in alignments:
                f.write('{0}\t{1}\n'.format(query, item))
    print('Paired alignment wrote to {0}.'.format(outputAln))
    
    return None


# concat multiple biome files into one biom file, using JSON format
def concatBioms(args):
    from biom.table import Table
    import json
    
    biomFile = args.output
    biomList = []
    for f in args.input:
        biomList.append(f)
    if len(biomList) <= 1:
        print('Found only one biom profile, will still give you a (brand) new one.')
        biomProfile = Table.from_json(json.load(biomList[0]))
        with open(biomFile, 'w') as f:
            biomProfile.to_json('Generated_by_almighty_metaSeq', f)
    else:
        print('Found {0} biom profiles under.'.format(len(biomList)))
        biomProfile = Table.from_json(json.load(biomList[0]))
    
        for f in biomList[1:]:
            biomProfile = biomProfile.concat([Table.from_json(json.load(f))])
    
        with open(biomFile, 'w') as f:
            biomProfile = biomProfile.sort()
            biomProfile.to_json('Generated_by_almighty_metaSeq', f)
        print('Concatenated {0} profiles into {1}.'.format(len(biomList), biomFile))    
    return None