#!/usr/bin/python3
from time import time

import pytest

from topoly import yamada, homfly, alexander, conway, jones, blmho, kauffman_bracket, kauffman_polynomial, Closure, TopolyException
algos = [
            alexander,
            #yamada,
            homfly,
            #conway,
            #jones,
            #blmho,
            #kauffman_bracket,
            #kauffman_polynomial
]

#@pytest.mark.skip
def test_algos():
    #file_pdb = 'data/1j85.pdb'
    file_cif = 'data/1j85.cif'
    #file_cif = 'data/6i7s.cif'
    #file_pdb = 'data/6i7s.pdb'
    for algo in algos:
        try:
            t0 = time()
            res = algo.__name__, ' : ', algo(file_cif, matrix=False, closure=Closure.TWO_POINTS, tries=100, #matrix_plot=True,
                                             #output_file=algo.__name__+'.txt',
                                             plot_ofile=algo.__name__, translate=True,
                                             run_parallel=False, parallel_workers=None)
            print(res)
            assert res[2].get('3_1', 0)>=0.35
            if res[2].get('3_1', 0)<0.5:
                print('WARNING!!!', algo.__name__, ' - 3_1 probability < 0.5')
            t = time()-t0
            print('Done {0} in {1} s.'.format(algo.__name__, round(t, 3)))
        except TopolyException as ve:
            print(algo.__name__, ' : ' + str(ve))
