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



class Data:

    ''' Represents a single data item in a data grid ''' 

    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        ''' value of the data item '''
        return self.__value

    def __str__(self):
        return 'Data(' + str(self.__value) + ')'

    def __repr__(self):
        return 'Data(' + str(self.__value) + ')'


    def __lt__(self, data):
        if(self.__value < data.value):
            return True
        else:
            return False


    def __gt__(self, data):
        if(self.__value > data.value):
            return True
        else:
            return False


    def __le__(self, data):
        if(self.__value <= data.value):
            return True
        else:
            return False


    def __ge__(self, data):
        if(self.__value >= data.value):
            return True
        else:
            return False


    def __eq__(self, data):
        if(self.__value == data.value):
            return True
        else:
            return False










class Tile:

    ''' Represents a single tile in a tile grid '''

    def __init__(self, options):
        '''Initialize a single Tile object '''
        self.__value = options['value']
        self.__alpha = options['alpha']
        self.__rgb = options['rgb']
        self.__options = options

    @property
    def value(self):
        ''' get the value '''
        return self.__value
    
    @property
    def alpha(self):
        ''' get the alpha value '''
        return self.__alpha

    @property
    def rgb(self):
        ''' get the RGB color code '''
        return self.__rgb

    @property
    def options(self):
        ''' get tile options '''
        return self.__options

    @alpha.setter
    def alpha(self, value):
        ''' set the alpha value '''
        self.__alpha = value

    @rgb.setter
    def rgb(self, value):
        ''' set the rgb color code '''
        self.__rgb = value


    def __str__(self):
        return 'Tile(' + str(self.__options) + ')'


    def __repr__(self):
        return 'Tile(' + str(self.__options) + ')'


    def __lt__(self, tile):
        if(self.__value < tile.value):
            return True
        else:
            return False


    def __gt__(self, tile):
        if(self.__value > tile.value):
            return True
        else:
            return False


    def __le__(self, tile):
        if(self.__value <= tile.value):
            return True
        else:
            return False


    def __ge__(self, tile):
        if(self.__value >= tile.value):
            return True
        else:
            return False


    def __eq__(self, tile):
        if(self.__value == tile.value):
            return True
        else:
            return False

    





class DataGrid(object):

    def __init__(self, options):
        ''' Initialize DataGrid object '''
        self.__grid = options['data']
        self.__size = self.__calculate_size(self.__grid)
        self.__shape = self.__calculate_shape(self.__grid)
        self.__rows = self.__shape['rows']
        self.__cols = self.__shape['cols']


    @property
    def grid(self):
        ''' Get data grid (list of lists) '''
        return self.__grid


    @property
    def size(self):
        ''' get the size of grid '''
        return self.__size


    @property
    def shape(self):
        ''' get the shape of grid '''
        return self.__shape

    @property
    def rows(self):
        ''' get the rows of grid '''
        return self.__rows

    @property
    def cols(self):
        ''' get the cols of grid '''
        return self.__cols


    def get_data(self, row, col):
        ''' get value by row, col '''
        item = self.__grid[row][col]
        return item


    def calculate_max_values_by_cols(self):
        ''' get list of maximum values for each numeric column '''
        grid = self.__grid
        max_values = list()
        for index in range(len(grid[0])):
            max_val = self.max_by_column_index(index)
            max_values.append(max_val)
        return max_values


    def max_by_column_label(self, label):
        ''' get maximum value of column by label '''
        try:
            labels = self.__grid[0]
            index = labels.index(label)
            return self.max_by_column_index(index)
        except:
            return False


    def max_by_column_index(self, index):
        ''' get maximum value of column by index '''
        values = list()
        for row in self.__grid[1:]:
            try:
                values.append(row[index])
            except:
                continue
        if(len(values)==0):
            return 0
        else:
            return max(values)


    
    
    def __calculate_size(self, grid):
        ''' calculates size of the grid '''
        size = 0
        for row in grid:
            size += len(row)
        return size



    def __calculate_shape(self, grid):
        ''' calculates the shape of the grid '''
        rows = 0
        cols = 0
        rows = len(grid)
        cols = len(grid[0])
        return {'rows': rows, 'cols': cols}

    

    def __str__(self):
        return 'DataGrid(' + str(self.__grid) + ')'



    def __repr__(self):
        return 'DataGrid(' + str(self.__grid) + ')'



    def __eq__(self, data_grid):
        if(self.__grid == data_grid.grid):
            return True
        else:
            return False





class ColorGrid(object):

    def __init__(self, options):
        ''' Initialize ColorGrid object '''
        self.__grid = options['data']
        self.__size = self.__calculate_size(self.__grid)
        self.__shape = self.__calculate_shape(self.__grid)
        self.__rows = self.__shape['rows']
        self.__cols = self.__shape['cols']
        self.__title = options['title']
        self.__subtitle = options['subtitle']
        try:
            self.__theme = options['theme']
        except:
            self.__theme = 'default'

    @property
    def grid(self):
        ''' get colorgrid data (list of lists) '''
        return self.__grid


    @property
    def size(self):
        ''' get size of color grid '''
        return self.__size

    @property
    def shape(self):
        ''' get shape of color grid '''
        return self.__shape

    @property
    def rows(self):
        ''' get number of rows in color grid '''
        return self.__rows

    @property
    def cols(self):
        ''' get number of cols in color grid '''
        return self.__cols


    @property
    def title(self):
        ''' get title of the color grid '''
        return self.__title


    @property
    def subtitle(self):
        ''' get subtitle of the color grid '''
        return self.__subtitle


    @property
    def theme(self):
        ''' get theme dictionary of options '''
        return self.__theme



    def get_tile(self, row, col):
        ''' get a specific tile by row, column '''
        return self.__grid[row][col]


    def __calculate_size(self, grid):
        ''' calculate size of the color grid '''
        size = 0
        for row in grid:
            size += len(row)
        return size


    def __calculate_shape(self, grid):
        ''' calculate the shape of the color grid '''
        rows = 0
        cols = 0
        rows = len(grid)
        cols = len(grid[0])
        return {'rows': rows, 'cols': cols}



    def __str__(self):
        return 'ColorGrid(' + str(self.__grid) + ')'



    def __repr__(self):
        return 'ColorGrid(' + str(self.__grid) + ')'


    def __eq__(self, color_grid):
        if(self.__grid == color_grid):
            return True
        else:
            return False
