#!/usr/bin/env python3

# http://ascii-table.com/ansi-escape-sequences.php
# https://jonasjacek.github.io/colors/

import sys,os,re,gc
             
#_________________________________________________
class Colours(object):
    '''
    colours that work on unix and pythonista (ios)
    '''

    class __Colours(object):
        
        colours = {
            'Black'  : '\033[30m',
            'Red'    : '\033[31m',
            'Green'  : '\033[32m',
            'Orange' : '\033[33m',
            'Blue'   : '\033[34m',
            'Purple' : '\033[35m',
            'Teal'   : '\033[36m',
            'White'  : '\033[37m',
        }
        
        background = {
            'Black'  : '\033[40m',
            'Red'    : '\033[41m',
            'Green'  : '\033[42m',
            'Orange' : '\033[43m',
            'Blue'   : '\033[44m',
            'Purple' : '\033[45m',
            'Teal'   : '\033[46m',
            'White'  : '\033[47m',
        } 
        
        pythonista = {
            'Black'  : (0,0,0),
            'Red'    : (1,0,0),
            'Green'  : (0,1,0),
            'Orange' : (0.8,0.8,0),
            'Blue'   : (0,0,1),
            'Purple' : (1,0,1),
            'Teal'   : (0.5,0.5,1),
            'White'  : (1,1,1),    
        }
        
        colours['Off'] = '\033[0m'
        pythonista['Off'] = (1,1,1)
        
        fonts = {
            'bold'      : '\033[1m',
            'italics'   : '\033[3m',
            'underline' : '\033[4m',
            'strikeout' : '\033[9m',
            'normal'    : '\033[0m',
        }

        fonts['Off'] = '\033[0m'
        
        def __init__(self, colour=True, html=False):
            
            self.colour = colour
            self.html = html
            
            self.reversed = dict()
            for key, val in self.colours.items():
                self.reversed[val] = key
            
            self.stnof = dict()
            for key, val in self.fonts.items():
                self.stnof[val] = key
                    
            self.splitter = re.compile('(\033\[\d+m)')
                        
        def __del__(self):
            pass
            
        def start(self):
            '''
            override sys.stdout, used to allow pythonista to show colours streamed
            '''
            if self.sys_stdout_write: return
            if self.sys_stderr_write: return
            
            try:
                import console
                self.console = console
                #raise Error('skip')
                
                self.sys_stdout_write = sys.stdout.write
                sys.stdout.write = self.stdout_write
                
                self.sys_stderr_write = sys.stderr.write
                sys.stderr.write = self.stderr_write
            except:
                self.pythonista.clear()
                
        def stop(self):
            '''
            undo sys.stdout override
            '''
            if hasattr(self,'sys_stdout_write'):
                sys.stdout.write = self.sys_stdout_write
            if hasattr(self,'sys_stderr_write'):
                sys.stderr.write = self.sys_stderr_write
        
        def write(self, text):
            bits = self.splitter.split(text)
            for bit in bits:
                escape = False
                if bit in self.reversed.keys():
                    colour = self.reversed[bit]
                    cmap = self.pythonista[colour]
                    self.console.set_color(*cmap)
                    escape = True
                if bit in self.stnof.keys():
                    font = self.stnof[bit]
                    self.console.set_font(font)
                    escape = True   
                if not escape:
                    self.sys_stdout_write(bit)
                               
        def stdout_write(self, text):
            '''
            override sys.stdout with colour fixed escape sequences
            '''
            self.write(text)
    
        def stderr_write(self, text):
            '''
            make red sys.stderr look orange
            '''
            self.console.set_color(
                *self.pythonista['Orange']
            ) 
            self.write(text)        
            self.console.set_color(
                *self.pythonista['Off']
            )
        
        def __getattr__(self, name):
            '''
            get colour priperty by name
            '''
            if name not in self.colours.keys():
                return
                
            if self.html:
                if name == 'Off':
                    return '</font>'
                else:
                    return '<font color="%s">'%name
            if self.colour:
                return self.colours[name]
            else:
                return ''
                

    instance = None
    
    def __new__(cls, *args, **kwargs): 
        '''
        singleton pattern
        '''
        # __new__ always a classmethod
        if not Colours.instance:
            Colours.instance = Colours.__Colours(*args, **kwargs)
        for key in ['html','colour']:
            if key in kwargs.keys():
                setattr(Colours.instance,key,kwargs[key])
        return Colours.instance
        
    def __getattr__(self, name):
        return getattr(self.instance, name)
        
    def __setattr__(self, name):
        return setattr(self.instance, name)    
       
#_________________________________________________
def main():
    colours = Colours(colour=True)
    #colours.start()
   
    for colour in colours.colours.keys():
        if not colour.startswith('_'):
            sys.stdout.write(''.join([
                getattr(colours,colour),
                colour,
                colours.Off,
                '\n',
            ]))  
    for font in colours.fonts.keys():
        sys.stdout.write(''.join([
            colours.fonts[font],
            font,
            colours.fonts['Off'],
            '\n',
        ]))
    sys.stderr.write('\nno red errors here\n')
    
    #colours.stop()
    return
    
#_________________________________________________
if __name__ == '__main__': main()
