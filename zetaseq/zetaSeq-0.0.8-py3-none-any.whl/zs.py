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
import zetaSeq.util
import sys

def main():
    import argparse
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help='commands', dest='subparser_name')
    
    # test function
    test_parser = subparsers.add_parser('test', help='print a test string')
    test_parser.add_argument('inputfile', action='store')
    test_parser.set_defaults(func=test_me)
    
    # count aligned reads
    countAlnReads_parser = subparsers.add_parser('countAlnReads', help='Count the number of reads aligned to the reference.')
    countAlnReads_parser.add_argument('-i', '--input', help='The alignment output to count.')
    countAlnReads_parser.set_defaults(func=countAlnReads)
  
    # keep paired alignments
    keepPairAln_parser = subparsers.add_parser('keepPairAln', help='Keep only the pair alignment of a read.')
    keepPairAln_parser.add_argument('-i', '--input', type=argparse.FileType('r'), nargs='+', \
                                    default=sys.stdin, help='The alignment to be checked.')
    keepPairAln_parser.add_argument('-o', '--output', help='The paired alignment.')
    keepPairAln_parser.set_defaults(func=keepPairAln)
    
    # concat multiple biome files into one biom file, using JSON format
    concatBioms_parser = subparsers.add_parser('concatBioms', help='Concat multiple biome files into one biom file, using JSON format.')
    concatBioms_parser.add_argument('-i', '--input', type=argparse.FileType('r'), nargs='+', \
                                    default=sys.stdin, help='The biom files to be concat.')
    concatBioms_parser.add_argument('-o', '--output', help='The paired alignment.')
    concatBioms_parser.set_defaults(func=concatBioms)    
    args = parser.parse_args()
    args.func(args)

def test_me(args):    
    import zetaSeq.util
    zetaSeq.util.test_me(args)

# count the number of aligned reads
def countAlnReads(args):
    zetaSeq.util.countAlnReads(args)
    return None

# keep paired alignments
def keepPairAln(args):
    zetaSeq.util.keepPairAln(args)
    return None

# concat multiple biome files into one biom file, using JSON format
def concatBioms(args):
    zetaSeq.util.concatBioms(args)
    return None

if __name__ == '__main__':
    main()