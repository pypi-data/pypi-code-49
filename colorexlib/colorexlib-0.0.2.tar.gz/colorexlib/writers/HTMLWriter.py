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

from .FileOutputWriter import FileOutputWriter
from Cheetah.Template import Template

class HTMLWriter(FileOutputWriter):

    ''' Class that handles writing to HTML output files '''

    def __init__(self, filepath, color_grid):
        ''' Initialize HTMLWriter object '''
        super().__init__(filepath, color_grid)
        self.dirs = dict()

    def write(self, options):
        ''' write the ColorGrid to output HTML file '''
        filepath = self.filepath
        output_file = open(filepath, "w")
        template_filename = options['template']
        template_file = open(template_filename, 'r')
        template_str = template_file.read()
        template = Template(template_str,
            searchList=[{'color_grid': self.color_grid.grid[1:],
                         'column_labels': self.color_grid.grid[0],
                         'title': self.color_grid.title,
                         'subtitle': self.color_grid.subtitle,
                         'theme': self.color_grid.theme}])
        output_file.write(str(template))
        output_file.close()
