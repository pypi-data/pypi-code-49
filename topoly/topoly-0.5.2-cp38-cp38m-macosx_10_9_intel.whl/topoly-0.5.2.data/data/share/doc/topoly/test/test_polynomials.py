""" Testing the polynomials on idealized and real data.

Test by Pawel Dabrowski-Tumanski
Version from 17.02.2020
"""

from topoly import alexander, conway, jones, homfly, yamada, kauffman_bracket, kauffman_polynomial, blmho
from topoly.params import Closure
import pytest
from time import time

curves = {'+3_1': 'data/31.xyz', '-3_1': 'data/m31.xyz', '4_1': 'data/41.xyz', '+5_2': 'data/52.xyz',
          '-5_2': 'data/m52.xyz', '+6_1': 'data/61.xyz', '-6_1': 'data/m61.xyz'}
algorithms = {'Alexander': alexander, 'Conway': conway, 'Jones': jones, 'HOMFLY-PT': homfly, 'Yamada': yamada,
               'Kauffman Bracket': kauffman_bracket, 'Kauffman Polynomial': kauffman_polynomial, 'BLM/Ho': blmho}

# the algorithms which last too long for proteins (for now hopefully)...
exclusions = ['Kauffman Bracket']
achiral = ['Alexander', 'Conway', 'BLM/Ho']
files = {('1j85', 'A'): '+3_1', ('2k0a', 'A'): '-3_1', ('5vik', 'A'): '4_1', ('2len', 'A'): '-5_2', ('3bjx', 'A'): '+6_1'}


def prepare_polynomials_closed():
    polynomials = {}
    for algorithm in algorithms.keys():
        polynomials[algorithm] = {}
        for curve in curves.keys():
            try:
                polynomials[algorithm][curve] = list(algorithms[algorithm](curves[curve], closure=Closure.CLOSED, translate=True, chiral=True))[0]
            except IndexError:
                polynomials[algorithm][curve] = 'Error'
    print('Results:')
    print('\t'.join(['Algorithm'] + list(curves.keys())))
    for algorithm in algorithms.keys():
        print('\t'.join([algorithm] + [polynomials[algorithm][curve] for curve in list(curves.keys())]))
    print('========')
    return polynomials


def prepare_polynomials_proteins():
    polynomials = {}
    times = {}
    for algorithm in algorithms.keys():
        if algorithm in exclusions:
            continue
        polynomials[algorithm] = {}
        times[algorithm] = {}
        for pdb, chain in files.keys():
            print(algorithm, pdb, chain)
            t0 = time()
            polynomials[algorithm][pdb] = algorithms[algorithm]('data/' + pdb + '.pdb', tries=100, translate=True, chiral=True, max_cross=25)
            times[algorithm][pdb] = time() - t0
    print('Results:')
    print(' '.join(['Algorithm'] + [pdb + '(' + chain + ')' for pdb, chain in files.keys()]))
    for algorithm in algorithms.keys():
        if algorithm in exclusions:
            continue
        print('\t'.join([algorithm] + [str(polynomials[algorithm][pdb]) + ' (' + str(round(times[algorithm][pdb], 3)) + 's)' for pdb, chain in list(files.keys())]))
    print('========')
    return polynomials


@pytest.mark.skip
def test_polynomials():
    print("Testing the polynomials on idealized data")
    polynomials = prepare_polynomials_closed()
    for algorithm in algorithms.keys():
        if algorithm in exclusions:
            continue
        for curve in curves.keys():
            if algorithm not in achiral:
                assert polynomials[algorithm][curve] == curve
            else:
                assert polynomials[algorithm][curve] == curve.replace('-', '').replace('+', '')
    return


# @pytest.mark.skip
def test_real_data():
    print("Testing the polynomials on real protein structures")
    polynomials = prepare_polynomials_proteins()
    for algorithm in algorithms.keys():
        if algorithm in exclusions:
            continue
        for pdb, chain in files.keys():
            res = files[(pdb, chain)]
            if algorithm in achiral:
                res = files[(pdb, chain)].replace('-', '').replace('+', '')
            if polynomials[algorithm][pdb].get(res, 0) < 0.5:
                print("Warning! Structure " + pdb + ' (' + chain + '), knot ' + res + ' with probability ' +
                      str(polynomials[algorithm][pdb].get(res, 'Error')) + ' in algorithm ' + algorithm)
            assert polynomials[algorithm][pdb].get(res, 0) > 0
    return


if __name__ == '__main__':
    test_polynomials()
    test_real_data()
