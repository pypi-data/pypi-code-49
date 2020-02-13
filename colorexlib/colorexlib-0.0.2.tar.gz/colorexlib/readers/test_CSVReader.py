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

from .CSVReader import CSVReader
from ..common.datastructures import Data, DataGrid
import pytest


''' CSVReader tests '''

csv_filepath = 'test_website_traffic.csv'
csv_reader = CSVReader(csv_filepath)
csv_data = [['Month', 'Web Traffic', 'Call to actions'],
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
csv_datagrid = DataGrid({'data': csv_data})

def test_CSVReader_data():
    data = csv_reader.data
    assert data == csv_data


def test_CSVReader_filepath():
    filepath = csv_reader.filepath
    assert filepath == csv_filepath


def test_CSVReader_read():
    csv_reader.read()
    assert csv_reader.data != []
    assert csv_reader.data != None
    data = csv_reader.data
    assert data == csv_data



def test_CSVReader_generate_datagrid():
    datagrid = csv_reader.generate_datagrid()
    assert csv_datagrid == datagrid
    assert csv_datagrid.__str__() == datagrid.__str__()



def test_CSVReader_rowToFloat():
    mock_row = ['China', 459, 320, 10, 'Shanghai']
    mock_row_after = ['China', Data(459.0), Data(320.0), Data(10.0), 'Shanghai']
    new_row = csv_reader.rowToFloat(mock_row)
    assert new_row == mock_row_after




def test_CSVReader_convert_val_to_float():
    float_val1 = 32.407
    float_val2 = 4.9867
    float_val3 = 90.909

    assert str(float_val1) == '32.407'
    assert str(float_val2) == '4.9867'
    assert str(float_val3) == '90.909'



def test_CSVReader_prepare():
    csv_reader.prepare()
    csv_reader_data = csv_reader.data
    assert csv_reader_data == csv_data
    
