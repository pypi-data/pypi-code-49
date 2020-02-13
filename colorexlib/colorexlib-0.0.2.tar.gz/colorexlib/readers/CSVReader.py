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
from ..common.datastructures import Data, DataGrid
import csv
from .FileInputReader import FileInputReader

class CSVReader(FileInputReader):

    ''' CSV data reader for a CSV data file '''

    def __init__(self, filepath):
        ''' Initialize CSVReader object '''
        self.__filepath = filepath
        self.__data = list()
        self.read()
        self.prepare()


    @property
    def data(self):
        ''' get CSV data '''
        data = self.__data
        return data


    @property
    def filepath(self):
        ''' get the file path '''
        filepath = self.__filepath
        return filepath


    def read(self):
        ''' read the CSV file '''
        filepath = self.__filepath
        self.__data = list()
        with open(filepath) as csv_file:
            reader = csv.reader(csv_file, delimiter=",")
            for row in reader:
                self.__data.append(self.rowToFloat(row))


    def generate_datagrid(self):
        ''' generate a DataGrid object based on CSV file data '''
        data = self.__data
        new_data = list()
        for row in data:
            new_row = list()
            for item in row:
                if(type(item) is float):
                    new_row.append(Data(item))
                else:
                    new_row.append(item)
            new_data.append(new_row)
                               
        data_grid = DataGrid({"data": new_data})
        return data_grid
        



    def rowToFloat(self, row):
        ''' convert numeric data in row to float data type '''
        r = list()
        for item in row:
            try:
                data_item = Data(float(item)) 
                r.append(data_item)
            except:
                r.append(item)
        return r



    def convert_val_to_float(self, x):
        ''' formats value as a float, if it is actually numeric '''
        try:
            return float(x)
        except:
            return x



    def prepare(self):
        ''' process the read CSV data '''
        data = self.__data
        pData = list()
        for row in data:
            pData.append(list(
                map(self.convert_val_to_float,row)))
        self.__data = pData


