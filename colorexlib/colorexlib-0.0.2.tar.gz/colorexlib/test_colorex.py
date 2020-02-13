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

from .colorex import ColorExGrid
from .common.datastructures import Data, DataGrid, Tile, ColorGrid
import pytest


''' ColorExGrid tests '''
options1 = dict()
options2 = dict()

options1['source'] = ['test_webtraffic_data.csv', 'csv']
options1['title'] = 'Website Traffic 2017'
options1['subtitle'] = 'The website traffic for whatever.com in the year 2017'

options2['source'] = ['test_webtraffic_data.csv', 'csv']
options2['title'] = 'Website Traffic 2017'
options2['subtitle'] = 'The website traffic for whatever.com in the year 2017'

data = [['Month', 'Web Traffic', 'Call to actions'],
        ['January', Data(100.0), Data(50.0)],
        ['February', Data(1000.0), Data(900.0)],
        ['March', Data(14500.0), Data(8000.0)],
        ['April', Data(14500.0), Data(900.0)],
        ['May', Data(9000.0), Data(12313.0)],
        ['June', Data(15699.0), Data(54.0)],
        ['July', Data(200456.0), Data(234.0)],
        ['August', Data(34233.0), Data(512.0)],
        ['September', Data(231231.0), Data(123.0)],
        ['October', Data(128293.0), Data(543.0)],
        ['November', Data(234234.0), Data(123.0)],
        ['December', Data(111111.0), Data(445585.0)]]
title = options1['title']
subtitle = options1['subtitle']


def test_ColorExGrid_filename():
    cxg1 = ColorExGrid(options1)
    assert cxg1.filename == options1['source'][0]

def test_ColorExGrid_fileformat():
    cxg1 = ColorExGrid(options1)
    assert cxg1.fileformat == options1['source'][1]

def test_ColorExGrid_title():
    cxg1 = ColorExGrid(options1)
    assert cxg1.title == options1['title']

def test_ColorExGrid_subtitle():
    cxg1 = ColorExGrid(options1)
    assert cxg1.subtitle == options1['subtitle']


def test_ColorExGrid_theme():
    cxg1 = ColorExGrid(options1)
    cxg2 = ColorExGrid(options2)
    assert cxg1.theme == 'default'
    assert cxg2.theme == 'default'


def test_ColorExGrid_get_theme():
    cxg1 = ColorExGrid(options1)
    assert cxg1.get_theme('default') == {'primary': '#0044aa', 'secondary': '#aaccff', 'on-primary': '#d7eef4', 'on-secondary': '#f9f9f9'}
    assert cxg1.get_theme('sun') == {'primary': '#d45500', 'secondary': '#ffccaa', 'on-primary': '#ffccaa', 'on-secondary': '#000000'}


def test_ColorExGrid_generate_colorgrid():
    cxg1 = ColorExGrid(options1)
    data_grid = DataGrid({'data': data})
    colorgrid = cxg1.generate_colorgrid(data_grid)
    mock_colorgrid = ColorGrid({
        'data': data,
        'title': title,
        'subtitle': subtitle,
        'theme': cxg1.theme
    })
    assert colorgrid == mock_colorgrid


def test_ColorExGrid_generate_tile():
    cxg1 = ColorExGrid(options1)
    max_val = Data(90)
    data_item1 = Data(17.85)
    data_item2 = Data(0.9)
    
    assert cxg1.generate_tile(data_item1, max_val, '#ff0000') == Tile({'value': 17.85, 'alpha': 0.19833, 'rgb': '#ff0000'})
    assert cxg1.generate_tile(data_item2, max_val, '#ff0000') == Tile({'value': 0.9, 'alpha': 0.01, 'rgb': '#ff0000'})



def test_ColorExGrid_calculate_rgb_alpha():
    cxg1 = ColorExGrid(options1)
    max_val = Data(60)
    data_item1 = 43
    data_item2 = 98.8
    assert cxg1.calculate_rgb_alpha(data_item1, max_val) == 0.7166666666666667
    assert cxg1.calculate_rgb_alpha(data_item2, max_val) == 1.6466666666666667



def test_ColorExGrid_get_hex_from_color():
    cxg1 = ColorExGrid(options1)
    assert cxg1.get_hex_from_color('red') == '#ff0000'
    assert cxg1.get_hex_from_color('white') == '#ffffff'
    assert cxg1.get_hex_from_color('black') == '#000000'
    assert cxg1.get_hex_from_color('indigogaba') == False
    assert cxg1.get_hex_from_color('gray') == '#808080'
    assert cxg1.get_hex_from_color('grey') == '#808080'




def test_ColorExGrid_is_rgb_hex():
    cxg1 = ColorExGrid(options1)
    rgb_hex_1 = '#ff00ff'
    rgb_hex_2 = '#ff0011'
    rgb_hex_3 = '#ffzb11'
    rgb_hex_4 = '#ffaa22'
    rgb_hex_5 = 'ffaa22'
    assert cxg1.is_rgb_hex(rgb_hex_1) == True
    assert cxg1.is_rgb_hex(rgb_hex_2) == True
    assert cxg1.is_rgb_hex(rgb_hex_3) == False
    assert cxg1.is_rgb_hex(rgb_hex_4) == True
    assert cxg1.is_rgb_hex(rgb_hex_5) == False



def test_ColorExGrid_rgb_hex_to_decimal():
    cxg1 = ColorExGrid(options1)
    assert cxg1.rgb_hex_to_decimal('#ff0000') == (255,0,0)
    assert cxg1.rgb_hex_to_decimal('#000000') == (0,0,0)
    assert cxg1.rgb_hex_to_decimal('#00ff00') == (0,255,0)
    assert cxg1.rgb_hex_to_decimal('#00ff00') == (0,255,0)
    assert cxg1.rgb_hex_to_decimal('#00ffzz') == False
    assert cxg1.rgb_hex_to_decimal('22aa00') == False




def test_ColorExGrid_is_color_name():
    cxg1 = ColorExGrid(options1)
    assert cxg1.is_color_name('blue') == True
    assert cxg1.is_color_name('redigo') == False
    assert cxg1.is_color_name('red') == True
    assert cxg1.is_color_name('yellowish') == False
    assert cxg1.is_color_name('pink') == False





def test_ColorExGrid_to_html():
    # Test not implemented as success or failure of test
    # depends on creation of a HTML file.
    pass
