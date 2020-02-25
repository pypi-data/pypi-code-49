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

def main():
    import argparse
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help='commands', dest='subparser_name')
    
    # test function
    test_parser = subparsers.add_parser('test', help='print a test string')
    test_parser.add_argument('inputfile', action='store')
    test_parser.set_defaults(func=test_me)
    print(parser.parse_args())
    
    args = parser.parse_args()
    args.func(args)

def test_me():    
    import zetaSeq.util
    zetaSeq.util.test_me()

if __name__ == '__main__':
    main()