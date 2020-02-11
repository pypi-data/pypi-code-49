# SpectroscPy 0.0.0
# SpectroscPy is a script package developed by and containing contributions from

    # Karen Oda Hjorth Dundas
    # Magnus Ringholm
    # Yann Cornation
    # Benedicte Ofstad

# The package is released under a LGPL licence.
# For questions, please contact on karen.o.dundas@uit.no

from spectroscpy import read_openrsp_tensor_file, remove_whitespaces, get_redundant_indices, rspProperty
import pytest
import os

def test_rspProperty():

    order = 4
    operator = ['GEO', 'EL', 'EL', 'EL']
    components = [12, 3, 3, 3]
    frequencies = [0.0, -0.2, 0.1, 0.1]

    prop = rspProperty(order, operator, components, frequencies)

    assert order == prop.order
    for i in range(order):
        assert operator[i] == prop.operator[i]
        assert components[i] == prop.components[i]
        assert frequencies[i] == prop.frequencies[i]


def test_get_redundant_indices():

    order = 4
    operator = ['GEO', 'EL', 'EL', 'EL']
    components = [12, 3, 3, 3]
    frequencies = [0.0, -0.2, 0.1, 0.1]

    prop = rspProperty(order, operator, components, frequencies)

    index = (1, 1, 1, 2)

    ref_redundant_indices = [(0, 0, 0, 1), (0, 0, 1, 0)]

    redundant_indices = get_redundant_indices(prop, index)

    assert len(ref_redundant_indices) == len(redundant_indices)

    for i in range(len(redundant_indices)):
        assert len(ref_redundant_indices[i]) == len(redundant_indices[i])

        for j in range(len(redundant_indices[i])):
            assert ref_redundant_indices[i][j] == redundant_indices[i][j]

    index = (1, 1, 2, 3)

    ref_redundant_indices = [(0, 0, 1, 2), (0, 0, 2, 1)]

    redundant_indices = get_redundant_indices(prop, index)

    assert len(ref_redundant_indices) == len(redundant_indices)

    for i in range(len(redundant_indices)):
        assert len(ref_redundant_indices[i]) == len(redundant_indices[i])

        for j in range(len(redundant_indices[i])):
            assert ref_redundant_indices[i][j] == redundant_indices[i][j]

    index = (1, 1, 3, 3)

    ref_redundant_indices = [(0, 0, 2, 2)]

    redundant_indices = get_redundant_indices(prop, index)

    assert len(ref_redundant_indices) == len(redundant_indices)

    for i in range(len(redundant_indices)):
        assert len(ref_redundant_indices[i]) == len(redundant_indices[i])

        for j in range(len(redundant_indices[i])):
            assert ref_redundant_indices[i][j] == redundant_indices[i][j]

    index = (6, 1, 1, 3)

    ref_redundant_indices = [(5, 0, 0, 2), (5, 0, 2, 0)]

    redundant_indices = get_redundant_indices(prop, index)

    assert len(ref_redundant_indices) == len(redundant_indices)

    for i in range(len(redundant_indices)):
        assert len(ref_redundant_indices[i]) == len(redundant_indices[i])

        for j in range(len(redundant_indices[i])):
            assert ref_redundant_indices[i][j] == redundant_indices[i][j]

    order = 3
    operator = ['GEO', 'EL', 'EL']
    components = [12, 3, 3]
    frequencies = [0.0, 0.0, 0.0]

    prop = rspProperty(order, operator, components, frequencies)

    index = (2, 1, 3)

    ref_redundant_indices = [(1, 0, 2), (1, 2, 0)]

    redundant_indices = get_redundant_indices(prop, index)

    assert len(ref_redundant_indices) == len(redundant_indices)

    for i in range(len(redundant_indices)):
        assert len(ref_redundant_indices[i]) == len(redundant_indices[i])

        for j in range(len(redundant_indices[i])):
            assert ref_redundant_indices[i][j] == redundant_indices[i][j]

    order = 2
    operator = ['GEO', 'GEO']
    components = [12, 12]
    frequencies = [0.0, 0.0]

    prop = rspProperty(order, operator, components, frequencies)

    index = (11, 12)

    ref_redundant_indices = [(10, 11), (11, 10)]

    redundant_indices = get_redundant_indices(prop, index)

    assert len(ref_redundant_indices) == len(redundant_indices)

    for i in range(len(redundant_indices)):
        assert len(ref_redundant_indices[i]) == len(redundant_indices[i])

        for j in range(len(redundant_indices[i])):
            assert ref_redundant_indices[i][j] == redundant_indices[i][j]


def test_remove_whitespaces():

    ref_string = 'VERSION'

    data_dir = '{0}/'.format(os.path.dirname(__file__))
    tensor_file = data_dir + 'hf_H2O2.rsp_tensor'
    f = open(tensor_file, 'r')

    red_string = remove_whitespaces(f)

    assert ref_string == red_string


# tensors is not tested, but indirectly through other functions
def test_read_openrsp_tensor_file():

    data_dir = '{0}/'.format(os.path.dirname(__file__))
    tensor_file = data_dir + 'hf_H2O2.rsp_tensor'

    num_properties = 10
    ref_order = [4, 4, 4, 2, 3, 3, 3, 3, 1, 2]
    ref_operator = [['GEO', 'EL', 'EL', 'EL'], ['GEO', 'EL', 'EL', 'EL'], ['GEO', 'EL', 'EL', 'EL'], \
                    ['GEO', 'EL'], ['GEO', 'EL', 'EL'], ['GEO', 'EL', 'EL'], ['GEO', 'EL', 'EL'], \
                    ['EL', 'EL', 'EL'], ['EL'], ['GEO', 'GEO']]
    ref_components = [[12, 3, 3, 3], [12, 3, 3, 3], [12, 3, 3, 3], [12, 3], [12, 3, 3], [12, 3, 3], \
                      [12, 3, 3],  [3, 3, 3], [3], [12, 12]]
    ref_frequencies = [[0.0, -0.2, 0.1, 0.1], [0.0, 0.0, 0.0, 0.0], [0.0, -0.2, 0.1, 0.1], [0.0, 0.0], \
                       [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, -0.1, 0.1], [-0.3, 0.1, 0.2], [0.0], \
                       [0.0, 0.0]]

    redundant_properties, tensors = read_openrsp_tensor_file(tensor_file)

    assert num_properties == len(redundant_properties) == len(tensors)

    for i in range(num_properties):
        assert ref_order[i] == redundant_properties[i].order

        for j in range(len(ref_operator[i])):
            assert ref_operator[i][j] == redundant_properties[i].operator[j]
            assert ref_components[i][j] == redundant_properties[i].components[j]
            assert ref_frequencies[i][j] == pytest.approx(redundant_properties[i].frequencies[j], 1.0e-80)
