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

from .datastructures import Data, Tile, DataGrid, ColorGrid
import pytest


''' Data class tests '''

def test_Data_value():
    data = Data(28)
    assert data.value == 28



def test_Data___str__():
    data = Data(78)
    assert data.__str__() == 'Data(78)'


def test_Data___repr__():
    data = Data(91)
    assert data.__repr__() == 'Data(91)'




''' Tile class tests '''

def test_Tile_value():
    options = dict()
    options['value'] = 87
    options['alpha'] = 0.87
    options['rgb'] = 'ff9988'
    tile = Tile(options)
    assert tile.value == 87


def test_Tile_alpha():
    options = dict()
    options['value'] = 87
    options['alpha'] = 0.87
    options['rgb'] = 'ff9988'
    tile = Tile(options)
    assert tile.alpha == 0.87



def test_Tile_rgb():
    options = dict()
    options['value'] = 87
    options['alpha'] = 0.87
    options['rgb'] = 'ff9988'
    tile = Tile(options)
    assert tile.rgb == 'ff9988'


def test_Tile_options():
    options = dict()
    options['value'] = 87
    options['alpha'] = 0.87
    options['rgb'] = 'ff9988'
    tile = Tile(options)
    assert tile.options == {'value': 87, 'alpha':
        0.87, 'rgb': 'ff9988'}


def test_Tile_set_alpha():
    options = dict()
    options['value'] = 87
    options['alpha'] = 0.87
    options['rgb'] = 'ff9988'
    tile = Tile(options)
    assert tile.alpha == 0.87
    tile.alpha = 0.56
    assert tile.alpha == 0.56


def test_Tile_set_rgb():
    options = dict()
    options['value'] = 87
    options['alpha'] = 0.87
    options['rgb'] = 'ff9988'
    tile = Tile(options)
    assert tile.rgb == 'ff9988'
    tile.rgb = 'ffaa22'
    assert tile.rgb == 'ffaa22'



def test_Tile___str__():
    options = dict()
    options['value'] = 87
    options['alpha'] = 0.87
    options['rgb'] = 'ff9988'
    tile = Tile(options)
    assert tile.__str__() == "Tile({'value': 87, 'alpha': 0.87, 'rgb': 'ff9988'})"





def test_Tile___repr__():
    options = dict()
    options['value'] = 87
    options['alpha'] = 0.87
    options['rgb'] = 'ff9988'
    tile = Tile(options)
    assert tile.__repr__() == "Tile({'value': 87, 'alpha': 0.87, 'rgb': 'ff9988'})"



def test_Tile___lt__():
    optionsA = dict()
    optionsA['value'] = 87
    optionsA['alpha'] = 0.87
    optionsA['rgb'] = 'ff9988'
    tileA = Tile(optionsA)

    optionsB = dict()
    optionsB['value'] = 54
    optionsB['alpha'] = 0.13
    optionsB['rgb'] = 'ff1122'
    tileB = Tile(optionsB)

    assert tileA.__lt__(tileB) == False



def test_Tile___gt__():
    optionsA = dict()
    optionsA['value'] = 87
    optionsA['alpha'] = 0.87
    optionsA['rgb'] = 'ff9988'
    tileA = Tile(optionsA)

    optionsB = dict()
    optionsB['value'] = 54
    optionsB['alpha'] = 0.13
    optionsB['rgb'] = 'ff1122'
    tileB = Tile(optionsB)

    assert tileA.__gt__(tileB) == True



def test_Tile___le__():
    optionsA = dict()
    optionsA['value'] = 54
    optionsA['alpha'] = 0.87
    optionsA['rgb'] = 'ff9988'
    tileA = Tile(optionsA)

    optionsB = dict()
    optionsB['value'] = 54
    optionsB['alpha'] = 0.13
    optionsB['rgb'] = 'ff1122'
    tileB = Tile(optionsB)

    assert tileA.__le__(tileB) == True


def test_Tile___ge__():
    optionsA = dict()
    optionsA['value'] = 64
    optionsA['alpha'] = 0.87
    optionsA['rgb'] = 'ff9988'
    tileA = Tile(optionsA)

    optionsB = dict()
    optionsB['value'] = 54
    optionsB['alpha'] = 0.13
    optionsB['rgb'] = 'ff1122'
    tileB = Tile(optionsB)

    assert tileA.__ge__(tileB) == True


def test_Tile___eq__():
    optionsA = dict()
    optionsA['value'] = 64
    optionsA['alpha'] = 0.87
    optionsA['rgb'] = 'ff9988'
    tileA = Tile(optionsA)

    optionsB = dict()
    optionsB['value'] = 54
    optionsB['alpha'] = 0.13
    optionsB['rgb'] = 'ff1122'
    tileB = Tile(optionsB)

    assert tileA.__eq__(tileB) == False

    optionsA = dict()
    optionsA['value'] = 100
    optionsA['alpha'] = 0.87
    optionsA['rgb'] = 'ff9988'
    tileA = Tile(optionsA)

    optionsB = dict()
    optionsB['value'] = 100
    optionsB['alpha'] = 0.13
    optionsB['rgb'] = 'ff1122'
    tileB = Tile(optionsB)

    assert tileA.__eq__(tileB) == True



''' DataGrid class tests '''

data = [[1,4,5,8],[9,0,8,8],[3,6,5,1],[1,4,1,9]]
data2 = [['c1','c2','c3','c4'],[9,0,8,8],[3,6,5,1],[1,4,1,9]]
maxes_each_cols = [9,6,8,9]
size = 16
shape = {'rows': 4, 'cols': 4}

def test_DataGrid_grid():
    options = dict()
    options['data'] = data
    dg = DataGrid(options)
    assert dg.grid == data


def test_DataGrid_size():
    options = dict()
    options['data'] = data
    dg = DataGrid(options)
    assert dg.size == size



def test_DataGrid_shape():
    options = dict()
    options['data'] = data
    dg = DataGrid(options)
    assert dg.shape == shape



def test_DataGrid_rows():
    options = dict()
    options['data'] = data
    dg = DataGrid(options)
    assert dg.rows == shape['rows']

    


def test_DataGrid_cols():
    options = dict()
    options['data'] = data
    dg = DataGrid(options)
    assert dg.cols == shape['cols']



def test_DataGrid_get_data():
    options = dict()
    options['data'] = data
    dg = DataGrid(options)
    assert dg.get_data(2,2) == 5
    assert dg.get_data(1,2) == 8
    assert dg.get_data(3,3) == 9



def test_DataGrid_calculate_max_values_by_cols():
    options = dict()
    options['data'] = data
    dg = DataGrid(options)
    max_values = dg.calculate_max_values_by_cols()
    assert max_values == maxes_each_cols
    




def test_DataGrid_max_by_column_label():
    options = dict()
    options['data'] = data2
    dg = DataGrid(options)
    max_value = dg.max_by_column_label('c2')
    assert max_value == 6




def test_DataGrid_max_by_column_index():
    options = dict()
    options['data'] = data2
    dg = DataGrid(options)
    max_value = dg.max_by_column_index(1)
    assert max_value == 6


def test_DataGrid___calculate_size():
    # this method not tested as it is a private member of DataGrid class.
    pass



def test_DataGrid___calculate_shape():
    # this method not tested as it is a private member of DataGrid class.
    pass



def test_DataGrid___str__():
    options = dict()
    options['data'] = data2
    dg = DataGrid(options)
    dg_str = dg.__str__()
    assert dg_str == "DataGrid([['c1', 'c2', 'c3', 'c4'], [9, 0, 8, 8], [3, 6, 5, 1], [1, 4, 1, 9]])"




def test_DataGrid__repr__():
    options = dict()
    options['data'] = data2
    dg = DataGrid(options)
    dg_str = dg.__repr__()
    assert dg_str == "DataGrid([['c1', 'c2', 'c3', 'c4'], [9, 0, 8, 8], [3, 6, 5, 1], [1, 4, 1, 9]])"


def test_DataGrid___eq__():
    optionsA = dict()
    optionsB = dict()
    optionsC = dict()
    
    optionsA['data'] = data
    optionsB['data'] = data
    optionsC['data'] = data2
    
    dgA = DataGrid(optionsA)
    dgB = DataGrid(optionsB)
    dgC = DataGrid(optionsC)
    
    assert dgA == dgB
    assert dgA != dgC
    assert dgB != dgC





''' ColorGrid class tests '''
colorgrid_title = "A Title"
colorgrid_subtitle = "This is a subtitle"
colorgrid_theme = "default"
colorgrid_data = [
  ['Month', 'Web Traffic', 'Call to actions'],
  ['January',
   Tile({'value': 100.0, 'alpha': 0.0004269235038465808, 'rgb': (0, 128, 0)}),
   Tile({'value': 50.0, 'alpha': 0.00011221203586296667, 'rgb': (0, 128, 0)})],
  ['February',
   Tile({'value': 1000.0, 'alpha': 0.0042692350384658075, 'rgb': (0, 128, 0)}),
   Tile({'value': 900.0, 'alpha': 0.0020198166455334, 'rgb': (0, 128, 0)})],
  ['March',
   Tile({'value': 14500.0, 'alpha': 0.06190390805775421, 'rgb': (0, 128, 0)}),
   Tile({'value': 8000.0, 'alpha': 0.017953925738074666, 'rgb': (0, 128, 0)})],
  ['April',
   Tile({'value': 14500.0, 'alpha': 0.06190390805775421, 'rgb': (0, 128, 0)}),
   Tile({'value': 900.0, 'alpha': 0.0020198166455334, 'rgb': (0, 128, 0)})],
  ['May',
   Tile({'value': 9000.0, 'alpha': 0.03842311534619227, 'rgb': (0, 128, 0)}),
   Tile({'value': 12313.0, 'alpha': 0.02763333595161417, 'rgb': (0, 128, 0)})],
  ['June',
   Tile({'value': 15699.0, 'alpha': 0.06702272086887472, 'rgb': (0, 128, 0)}),
   Tile({'value': 54.0, 'alpha': 0.00012118899873200399, 'rgb': (0, 128, 0)})],
  ['July',
   Tile({'value': 200456.0, 'alpha': 0.855793778870702, 'rgb': (0, 128, 0)}),
   Tile({'value': 234.0, 'alpha': 0.000525152327838684, 'rgb': (0, 128, 0)})],
  ['August',
   Tile({'value': 34233.0, 'alpha': 0.1461487230718, 'rgb': (0, 128, 0)}),
   Tile({'value': 512.0, 'alpha': 0.0011490512472367787, 'rgb': (0, 128, 0)})],
  ['September',
   Tile({'value': 231231.0, 'alpha': 0.9871794871794872, 'rgb': (0, 128, 0)}),
   Tile({'value': 123.0, 'alpha': 0.00027604160822289797, 'rgb': (0, 128, 0)})],
  ['October',
   Tile({'value': 128293.0, 'alpha': 0.5477129707898939, 'rgb': (0, 128, 0)}),
   Tile({'value': 543.0, 'alpha': 0.001218622709471818, 'rgb': (0, 128, 0)})],
  ['November',
   Tile({'value': 234234.0, 'alpha': 1.0, 'rgb': (0, 128, 0)}),
   Tile({'value': 123.0, 'alpha': 0.00027604160822289797, 'rgb': (0, 128, 0)})],
  ['December',
   Tile({'value': 111111.0, 'alpha': 0.47435897435897434, 'rgb': (0, 128, 0)}),
   Tile({'value': 445585.0, 'alpha': 1.0, 'rgb': (0, 128, 0)})]]




def test_colorgrid_grid():
    color_grid = ColorGrid({'data': colorgrid_data,
    'title': colorgrid_title, 'subtitle': colorgrid_subtitle,
    'theme': colorgrid_theme})
    assert color_grid.grid == colorgrid_data
    


def test_colorgrid_size():
    color_grid = ColorGrid({'data': colorgrid_data,
    'title': colorgrid_title, 'subtitle': colorgrid_subtitle,
    'theme': colorgrid_theme})
    assert color_grid.size == 39


def test_colorgrid_shape():
    color_grid = ColorGrid({'data': colorgrid_data,
    'title': colorgrid_title, 'subtitle': colorgrid_subtitle,
    'theme': colorgrid_theme})
    assert color_grid.shape == {'rows': 13, 'cols': 3}


def test_colorgrid_rows():
    color_grid = ColorGrid({'data': colorgrid_data,
    'title': colorgrid_title, 'subtitle': colorgrid_subtitle,
    'theme': colorgrid_theme})
    assert color_grid.rows == 13


def test_colorgrid_cols():
    color_grid = ColorGrid({'data': colorgrid_data,
    'title': colorgrid_title, 'subtitle': colorgrid_subtitle,
    'theme': colorgrid_theme})
    assert color_grid.cols == 3


def test_colorgrid_title():
    color_grid = ColorGrid({'data': colorgrid_data,
    'title': colorgrid_title, 'subtitle': colorgrid_subtitle,
    'theme': colorgrid_theme})
    assert color_grid.title == colorgrid_title


def test_colorgrid_subtitle():
    color_grid = ColorGrid({'data': colorgrid_data,
    'title': colorgrid_title, 'subtitle': colorgrid_subtitle,
    'theme': colorgrid_theme})
    assert color_grid.subtitle == colorgrid_subtitle


def test_colorgrid_get_tile():
    color_grid = ColorGrid({'data': colorgrid_data,
    'title': colorgrid_title, 'subtitle': colorgrid_subtitle,
    'theme': colorgrid_theme})
    tile1 = Tile({'value': 15699.0, 'alpha': 0.06702272086887472, 'rgb': (0, 128, 0)})
    tile2 = Tile({'value': 900.0, 'alpha': 0.0020198166455334, 'rgb': (0, 128, 0)})
    assert color_grid.get_tile(6,1) == tile1
    assert color_grid.get_tile(4,2) == tile2


def test_colorgrid___calculate_size():
    # This class member not tested as it is declared as private.
    pass


def test_colorgrid___str__():
    color_grid = ColorGrid({'data': colorgrid_data,
    'title': colorgrid_title, 'subtitle': colorgrid_subtitle,
    'theme': colorgrid_theme})
    str_cg = "ColorGrid([['Month', 'Web Traffic', 'Call to actions'], ['January', Tile({'value': 100.0, 'alpha': 0.0004269235038465808, 'rgb': (0, 128, 0)}), Tile({'value': 50.0, 'alpha': 0.00011221203586296667, 'rgb': (0, 128, 0)})], ['February', Tile({'value': 1000.0, 'alpha': 0.0042692350384658075, 'rgb': (0, 128, 0)}), Tile({'value': 900.0, 'alpha': 0.0020198166455334, 'rgb': (0, 128, 0)})], ['March', Tile({'value': 14500.0, 'alpha': 0.06190390805775421, 'rgb': (0, 128, 0)}), Tile({'value': 8000.0, 'alpha': 0.017953925738074666, 'rgb': (0, 128, 0)})], ['April', Tile({'value': 14500.0, 'alpha': 0.06190390805775421, 'rgb': (0, 128, 0)}), Tile({'value': 900.0, 'alpha': 0.0020198166455334, 'rgb': (0, 128, 0)})], ['May', Tile({'value': 9000.0, 'alpha': 0.03842311534619227, 'rgb': (0, 128, 0)}), Tile({'value': 12313.0, 'alpha': 0.02763333595161417, 'rgb': (0, 128, 0)})], ['June', Tile({'value': 15699.0, 'alpha': 0.06702272086887472, 'rgb': (0, 128, 0)}), Tile({'value': 54.0, 'alpha': 0.00012118899873200399, 'rgb': (0, 128, 0)})], ['July', Tile({'value': 200456.0, 'alpha': 0.855793778870702, 'rgb': (0, 128, 0)}), Tile({'value': 234.0, 'alpha': 0.000525152327838684, 'rgb': (0, 128, 0)})], ['August', Tile({'value': 34233.0, 'alpha': 0.1461487230718, 'rgb': (0, 128, 0)}), Tile({'value': 512.0, 'alpha': 0.0011490512472367787, 'rgb': (0, 128, 0)})], ['September', Tile({'value': 231231.0, 'alpha': 0.9871794871794872, 'rgb': (0, 128, 0)}), Tile({'value': 123.0, 'alpha': 0.00027604160822289797, 'rgb': (0, 128, 0)})], ['October', Tile({'value': 128293.0, 'alpha': 0.5477129707898939, 'rgb': (0, 128, 0)}), Tile({'value': 543.0, 'alpha': 0.001218622709471818, 'rgb': (0, 128, 0)})], ['November', Tile({'value': 234234.0, 'alpha': 1.0, 'rgb': (0, 128, 0)}), Tile({'value': 123.0, 'alpha': 0.00027604160822289797, 'rgb': (0, 128, 0)})], ['December', Tile({'value': 111111.0, 'alpha': 0.47435897435897434, 'rgb': (0, 128, 0)}), Tile({'value': 445585.0, 'alpha': 1.0, 'rgb': (0, 128, 0)})]])"
    assert color_grid.__str__() == str_cg


def test_colorgrid___repr__():
    color_grid = ColorGrid({'data': colorgrid_data,
    'title': colorgrid_title, 'subtitle': colorgrid_subtitle,
    'theme': colorgrid_theme})
    repr_cg = "ColorGrid([['Month', 'Web Traffic', 'Call to actions'], ['January', Tile({'value': 100.0, 'alpha': 0.0004269235038465808, 'rgb': (0, 128, 0)}), Tile({'value': 50.0, 'alpha': 0.00011221203586296667, 'rgb': (0, 128, 0)})], ['February', Tile({'value': 1000.0, 'alpha': 0.0042692350384658075, 'rgb': (0, 128, 0)}), Tile({'value': 900.0, 'alpha': 0.0020198166455334, 'rgb': (0, 128, 0)})], ['March', Tile({'value': 14500.0, 'alpha': 0.06190390805775421, 'rgb': (0, 128, 0)}), Tile({'value': 8000.0, 'alpha': 0.017953925738074666, 'rgb': (0, 128, 0)})], ['April', Tile({'value': 14500.0, 'alpha': 0.06190390805775421, 'rgb': (0, 128, 0)}), Tile({'value': 900.0, 'alpha': 0.0020198166455334, 'rgb': (0, 128, 0)})], ['May', Tile({'value': 9000.0, 'alpha': 0.03842311534619227, 'rgb': (0, 128, 0)}), Tile({'value': 12313.0, 'alpha': 0.02763333595161417, 'rgb': (0, 128, 0)})], ['June', Tile({'value': 15699.0, 'alpha': 0.06702272086887472, 'rgb': (0, 128, 0)}), Tile({'value': 54.0, 'alpha': 0.00012118899873200399, 'rgb': (0, 128, 0)})], ['July', Tile({'value': 200456.0, 'alpha': 0.855793778870702, 'rgb': (0, 128, 0)}), Tile({'value': 234.0, 'alpha': 0.000525152327838684, 'rgb': (0, 128, 0)})], ['August', Tile({'value': 34233.0, 'alpha': 0.1461487230718, 'rgb': (0, 128, 0)}), Tile({'value': 512.0, 'alpha': 0.0011490512472367787, 'rgb': (0, 128, 0)})], ['September', Tile({'value': 231231.0, 'alpha': 0.9871794871794872, 'rgb': (0, 128, 0)}), Tile({'value': 123.0, 'alpha': 0.00027604160822289797, 'rgb': (0, 128, 0)})], ['October', Tile({'value': 128293.0, 'alpha': 0.5477129707898939, 'rgb': (0, 128, 0)}), Tile({'value': 543.0, 'alpha': 0.001218622709471818, 'rgb': (0, 128, 0)})], ['November', Tile({'value': 234234.0, 'alpha': 1.0, 'rgb': (0, 128, 0)}), Tile({'value': 123.0, 'alpha': 0.00027604160822289797, 'rgb': (0, 128, 0)})], ['December', Tile({'value': 111111.0, 'alpha': 0.47435897435897434, 'rgb': (0, 128, 0)}), Tile({'value': 445585.0, 'alpha': 1.0, 'rgb': (0, 128, 0)})]])"
    assert color_grid.__repr__() == repr_cg


