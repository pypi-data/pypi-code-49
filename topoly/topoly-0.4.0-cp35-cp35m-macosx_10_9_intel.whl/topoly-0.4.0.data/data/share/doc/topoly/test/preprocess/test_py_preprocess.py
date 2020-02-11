#!/usr/bin/python3
import os
import sys

from topoly.topoly_preprocess import chain_read, close_chain_2points


in_file = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + '/t31_numbered_cut.xyz')

def test_chain_read_and_close():
    print("Reading chain from: " + str(in_file))
    chain, unable = chain_read(in_file.encode('utf-8'))
    assert unable == False
    assert chain[1]['A']['x'] == 0.0780421837759
    assert chain[1]['A']['z'] == 0.0776457135308

    res, chain_out = close_chain_2points(chain)
    assert res == 0
    assert len(chain_out)>38
