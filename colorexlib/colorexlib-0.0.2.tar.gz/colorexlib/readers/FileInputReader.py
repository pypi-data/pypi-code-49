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

from .InputReader import *

from abc import ABC, abstractmethod, abstractproperty

class FileInputReader(InputReader, ABC):

    ''' Class represents all input readers that get data from files '''

    def __init__(self, filepath):
        ''' Initialize FileInputReader object '''
        self.__filepath = filepath
        self.__data = None

    @property
    def filepath(self):
        ''' get the file path '''
        filepath = self.__filepath
        return filepath

    @property
    def data(self):
        ''' get the read data '''
        data = self.__data
        return data

    def read(self):
        ''' read the data from file '''
        pass

    def generate_datagrid(self):
        ''' generate a DataGrid object based on read file data '''
        pass

