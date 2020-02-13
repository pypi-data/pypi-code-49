'''

Copyright 2019 Louis Ronald

Permission is hereby granted, free of charge, to any person 
obtaining a copy of this software and associated documentation 
files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, 
publish, distribute, sublicense, and/or sell copies of the Software, 
and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be 
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES 
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
DEALINGS IN THE SOFTWARE.



'''

from .HTMLWriter import HTMLWriter
from ..common.datastructures import Data, DataGrid, Tile, ColorGrid
import pytest


''' HTMLWriter tests '''

color_grid_options = dict()
color_grid_options['title'] = 'First ColorGrid'
color_grid_options['subtitle'] = 'This is my first ColorGrid'
color_grid_options['data'] = [['Month', 'Web Traffic', 'Call to actions'], ['January', Tile({'value': 100.0, 'alpha': 0.0004269235038465808, 'rgb': (0, 128, 0)}), Tile({'value': 50.0, 'alpha': 0.00011221203586296667, 'rgb': (0, 128, 0)})], ['February', Tile({'value': 1000.0, 'alpha': 0.0042692350384658075, 'rgb': (0, 128, 0)}), Tile({'value': 900.0, 'alpha': 0.0020198166455334, 'rgb': (0, 128, 0)})], ['March', Tile({'value': 14500.0, 'alpha': 0.06190390805775421, 'rgb': (0, 128, 0)}), Tile({'value': 8000.0, 'alpha': 0.017953925738074666, 'rgb': (0, 128, 0)})], ['April', Tile({'value': 14500.0, 'alpha': 0.06190390805775421, 'rgb': (0, 128, 0)}), Tile({'value': 900.0, 'alpha': 0.0020198166455334, 'rgb': (0, 128, 0)})], ['May', Tile({'value': 9000.0, 'alpha': 0.03842311534619227, 'rgb': (0, 128, 0)}), Tile({'value': 12313.0, 'alpha': 0.02763333595161417, 'rgb': (0, 128, 0)})], ['June', Tile({'value': 15699.0, 'alpha': 0.06702272086887472, 'rgb': (0, 128, 0)}), Tile({'value': 54.0, 'alpha': 0.00012118899873200399, 'rgb': (0, 128, 0)})], ['July', Tile({'value': 200456.0, 'alpha': 0.855793778870702, 'rgb': (0, 128, 0)}), Tile({'value': 234.0, 'alpha': 0.000525152327838684, 'rgb': (0, 128, 0)})], ['August', Tile({'value': 34233.0, 'alpha': 0.1461487230718, 'rgb': (0, 128, 0)}), Tile({'value': 512.0, 'alpha': 0.0011490512472367787, 'rgb': (0, 128, 0)})], ['September', Tile({'value': 231231.0, 'alpha': 0.9871794871794872, 'rgb': (0, 128, 0)}), Tile({'value': 123.0, 'alpha': 0.00027604160822289797, 'rgb': (0, 128, 0)})], ['October', Tile({'value': 128293.0, 'alpha': 0.5477129707898939, 'rgb': (0, 128, 0)}), Tile({'value': 543.0, 'alpha': 0.001218622709471818, 'rgb': (0, 128, 0)})], ['November', Tile({'value': 234234.0, 'alpha': 1.0, 'rgb': (0, 128, 0)}), Tile({'value': 123.0, 'alpha': 0.00027604160822289797, 'rgb': (0, 128, 0)})], ['December', Tile({'value': 111111.0, 'alpha': 0.47435897435897434, 'rgb': (0, 128, 0)}), Tile({'value': 445585.0, 'alpha': 1.0, 'rgb': (0, 128, 0)})]]
color_grid = ColorGrid(color_grid_options)
mock_output_filepath = 'myfile_mock.html'


def test_HTMLWriter_filepath():
    html_writer = HTMLWriter(mock_output_filepath, color_grid_options)
    assert html_writer.filepath == mock_output_filepath

def test_HTMLWriter_color_grid():
    html_writer = HTMLWriter(mock_output_filepath, color_grid_options)
    print(html_writer.color_grid)
    assert html_writer.color_grid['data'] == color_grid_options['data']


def test_HTMLWriter_write():
    # This method not tested, but success of this is creation of actual HTML file
    pass

