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

from .themes import Theme, Themes
import pytest


''' Themes class tests '''

def test_Themes_themes():
    themes = Themes()
    assert themes.themes == {'default': {'primary': '#0044aa', 'secondary': '#aaccff', 'on-primary': '#d7eef4', 'on-secondary': '#f9f9f9'}, 'sun': {'primary': '#d45500', 'secondary': '#ffccaa', 'on-primary': '#ffccaa', 'on-secondary': '#000000'}}




''' Theme class tests '''
def test_Theme_palette():
    theme1 = Theme()
    assert theme1.palette == {'primary': '#0044aa', 'secondary': '#aaccff', 'on-primary': '#d7eef4', 'on-secondary': '#f9f9f9'}
    theme2 = Theme(name='sun')
    assert theme2.palette == {'primary': '#d45500', 'secondary': '#ffccaa', 'on-primary': '#ffccaa', 'on-secondary': '#000000'}
