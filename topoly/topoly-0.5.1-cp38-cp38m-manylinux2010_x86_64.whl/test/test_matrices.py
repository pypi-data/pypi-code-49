""" Testing the matrix creation and drawing.

Test by Pawel Dabrowski-Tumanski
Version from 19.02.2020
"""

#!/usr/bin/python3
import os
import pytest
from topoly.topoly_knot import find_knots
from topoly import conway, plot_matrix
from topoly.params import Closure, OutputFormat
from topoly import translate_matrix, gln, alexander, find_spots

matrix_cutoff = 0.2    # the cutoff for matrix comparison
matrix_output_file = '2efv_matrix_tmp'
plot_ofile_protein = 'tmp_2efv_matrix'
output_data_file = 'tmp_matrix_1j85_knotprot'
cutoffs = [0.48, 0.6, 0.9]
expected_file = 'data/KNOTS_2efv_A'
gln_codes = {'2lfk': [(24, 51), (52, 69)], '3suk': [(39, 76), (79, 138)]}


def read_KnotProt_matrix(matrix_file):
    data = {}
    with open(matrix_file, 'r') as myfile:
        for line in myfile.readlines():
            if line[0] == '#':
                continue
            if 'UNKNOT' in line:
                return data
            d = line.split()
            ident = (int(d[0]), int(d[1]))
            data[ident] = {}
            for i in range(2, 30):
                for knot in d[i].split(','):
                    if knot == '0' or knot == '0_1':
                        continue
                    probability = 0.9 - (i - 2) * 0.03
                    data[ident][knot] = probability
    return data


def compare_output(dict1, dict2, cutoff=matrix_cutoff):
    difference = {}
    idents_all = list(set(dict1.keys()) | set(dict2.keys()))
    for ident in idents_all:
        knots_all = list(set(dict1.get(ident, {}).keys()) | set(dict2.get(ident, {}).keys()))
        for knot in knots_all:
            v1 = dict1.get(ident, {}).get(knot, 0)
            v2 = dict2.get(ident, {}).get(knot, 0)
            diff = abs(v1-v2)
            if diff > cutoff:
                if ident not in difference.keys():
                    difference[ident] = {}
                difference[ident][knot] = diff
    return difference


@pytest.mark.cuda
def test_knotnet_directly():
    print("Testing matrix calculation directly with Alexander polynomial.")
    in_file = 'data/2efv.nxyz'
    ret = find_knots(in_file.encode('utf-8'), matrix_output_file.encode('utf-8'), 2, closure=2)
    data = read_KnotProt_matrix(matrix_output_file)
    expected = read_KnotProt_matrix(expected_file)
    differences = compare_output(data, expected)
    if differences:
        print('Differences: ', differences)
    assert differences == {}
    assert ret == False
    print("========\n")
    return


# @pytest.mark.skip
def test_matrix_format():
    print("Testing different formats of matrix production with Conway polynomial.")
    result_dictionary = conway('data/1j85.pdb', matrix=True, closure=Closure.CLOSED,
                               output_format=OutputFormat.Dictionary, translate=True)
    result_knotprot = conway('data/1j85.pdb', matrix=True, closure=Closure.CLOSED,
                               output_format=OutputFormat.KnotProt, translate=True)
    result_matrix = conway('data/1j85.pdb', matrix=True, closure=Closure.CLOSED,
                               output_format=OutputFormat.Matrix, translate=True)
    conway('data/1j85.pdb', matrix=True, closure=Closure.CLOSED, output_format=OutputFormat.KnotProt,
           output_file=output_data_file, translate=True)
    with open(output_data_file, 'r') as myfile:
        result_string = myfile.read()
    print('Knots found in matrix: ', list(result_matrix.keys()))
    assert list(result_matrix.keys()) == ['3_1']

    # KnotProt output
    translated_result = translate_matrix(result_knotprot, output_format=OutputFormat.Dictionary)
    diff_dict_knot = compare_output(result_dictionary, translated_result)
    print('KnotProt output.')
    if diff_dict_knot != {}:
        print('Differences: ', diff_dict_knot)
    assert diff_dict_knot == {}


    # Matrix output
    translated_result = translate_matrix(result_matrix.get('3_1', [[]]), output_format=OutputFormat.Dictionary, knot='3_1', beg=1)
    diff_dict_knot = compare_output(result_dictionary, translated_result)
    print('Matrix output.')
    if diff_dict_knot != {}:
        print('Differences: ', diff_dict_knot)
    assert diff_dict_knot == {}

    # String output
    translated_result = translate_matrix(result_string, output_format=OutputFormat.Dictionary)
    diff_dict_knot = compare_output(result_dictionary, translated_result)
    print('String output.')
    if diff_dict_knot != {}:
        print('Differences: ', diff_dict_knot)
    assert diff_dict_knot == {}
    print("========\n")
    return


# @pytest.mark.skip
def test_matrix_plot():
    print("Testing matrix plotting with different cutoffs for Conway polynomial.")
    sizes = []
    for cutoff in cutoffs:
        print('Cutoff: ' + str(cutoff))
        ofile = 'tmp_map_cutoff_' + str(cutoff)
        conway('data/1j85.pdb', tries=10, plot_ofile=ofile, matrix_plot=True, matrix_cutoff=cutoff, translate=True)
        assert os.path.isfile('tmp_map_cutoff_' + str(cutoff) + '.png')
        sizes.append(os.path.getsize(ofile + '.png'))

    print("Sizes:\t", ', '.join([str(cutoff) + ' ' + str(size) for cutoff, size in zip(cutoffs, sizes)]))

    for k in range(len(sizes)-1):
        assert sizes[k] >= sizes[k+1]

    plot_matrix(expected_file, plot_ofile=plot_ofile_protein)
    assert os.path.isfile(plot_ofile_protein + '.png')
    return


# @pytest.mark.skip
def test_gln_matrix():
    print("Testing GLN matrix plotting.")
    for code in gln_codes.keys():
        print(code)
        f = 'data/' + code + '.pdb'
        bridges = gln_codes[code]
        plot_ofile = 'tmp_GLN_plot_' + code
        gln(f, chain1_boundary=bridges[0], chain2_boundary=bridges[1], matrix_plot=True, plot_ofile=plot_ofile)
        assert os.path.isfile(plot_ofile + '.png')
    return


def test_plamkas():
    print("Testing finding spots.")
    result = alexander('data/composite.xyz', matrix=True, closure=Closure.CLOSED, translate=True, cuda=False)
    spots = find_spots(result)
    print("Found: ", spots)
    assert set(spots.keys()) == {'3_1', '8_20 | 3_1 # 3_1'}
    assert len(spots['3_1']) == 2
    assert len(spots['8_20 | 3_1 # 3_1']) == 1
    return


def clean():
    try:
        os.remove(matrix_output_file)
        os.remove(output_data_file)
        for cutoff in cutoffs:
            os.remove('tmp_map_cutoff_' + str(cutoff) + '.png')
        os.remove(plot_ofile_protein + '.png')
        for code in gln_codes.keys():
            os.remove('tmp_GLN_plot_' + code + '.png')
    except FileNotFoundError:
        pass


if __name__ == '__main__':
    test_knotnet_directly()
    test_matrix_format()
    test_matrix_plot()
    test_gln_matrix()
    test_plamkas()
    clean()
