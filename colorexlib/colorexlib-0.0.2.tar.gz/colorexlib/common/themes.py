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

import xml.etree.ElementTree as ET


class Themes:

    def __init__(self):
        # general theme repo.
        self.__themes = dict()


        # declare default theme.
        default = dict()
        default['primary'] = '#0044aa'
        default['secondary'] = '#aaccff'
        default['on-primary'] = '#d7eef4'
        default['on-secondary'] = '#f9f9f9'


        # declare sun theme
        sun = dict()
        sun['primary'] = '#d45500'
        sun['secondary'] = '#ffccaa'
        sun['on-primary'] = '#ffccaa'
        sun['on-secondary'] = '#000000'

    
        # add all declared themes to the repo.
        self.__themes['default'] = default
        self.__themes['sun'] = sun





    @property
    def themes(self):
        ''' returns list of in-built themes '''
        return self.__themes


















class Theme:

    def __init__(self, filename=None, name='default'):


        # prepare color palette
        self.__palette = dict()
        self.__palette['primary'] = ''
        self.__palette['secondary'] = ''
        self.__palette['on-primary'] = ''
        self.__palette['on-secondary'] = ''



        # validation of parameters
        if(filename == None and name=='default'):
            # go with default settings.
            all_themes = Themes()
            the_theme = all_themes.themes['default']
            self.__palette['primary'] = the_theme['primary']
            self.__palette['secondary'] = the_theme['secondary']
            self.__palette['on-primary'] = the_theme['on-primary']
            self.__palette['on-secondary'] = the_theme['on-secondary']

        elif(filename == None and name != 'default'):
            # go with theme name specified, using in-built theme.
            try:
                all_themes = Themes()
                the_theme = all_themes.themes[name]
                self.__palette['primary'] = the_theme['primary']
                self.__palette['secondary'] = the_theme['secondary']
                self.__palette['on-primary'] = the_theme['on-primary']
                self.__palette['on-secondary'] = the_theme['on-secondary']
            except:
                raise Exception
                        

        elif((filename != None and name == 'default') or (filename != None and name != 'default')):
            # go with the theme declared in the theme file specified.
            # read theme from theme file (XML-formatted .cxt file)
            try:
                tree = ET.parse(filename)
                root = tree.getroot()
                # extract theme data from .cxt XML file
                all_theme_colors = list(root)
                for color in all_theme_colors:
                    if(color.get('name') == 'primary'):
                        self.__palette['primary'] = color.get('value')
                        
                    elif(color.get('name') == 'secondary'):
                        self.__palette['secondary'] = color.get('value')
                        
                    elif(color.get('name') == 'on-primary'):
                        self.__palette['on-primary'] = color.get('value')
                        
                    elif(color.get('name') == 'on-secondary'):
                        self.__palette['on-secondary'] = color.get('value')

                    else:
                        continue

            except:
                raise Exception
        

        else:
            # just go with the default.
            # go with default settings.
            all_themes = Themes()
            the_theme = all_themes.themes['default']
            self.__palette['primary'] = the_theme['primary']
            self.__palette['secondary'] = the_theme['secondary']
            self.__palette['on-primary'] = the_theme['on-primary']
            self.__palette['on-secondary'] = the_theme['on-secondary']        
        




    @property
    def palette(self):
        ''' returns a dictionary color palette for the current theme '''
        return self.__palette
