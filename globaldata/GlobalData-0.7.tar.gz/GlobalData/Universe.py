# Universe.py

# from Globals import *
#from GlobalData import *
from Globals import *

import os, time

def Get(gd, x):
    return gd.GetX(x)

def GetCurrentDir():
## first file in current dir (with full path)
    file = os.path.join(os.getcwd(), os.listdir(os.getcwd())[0])
    return os.path.dirname(file) ## directory of file

class obj(dict):
    def __init__(self):
        self.exist = True
        self.birth = time.time()
        self.dict = {"Eyes":3, "exist":self.exist, "birth":self.birth}
        self.gd = GD
        self.root = GetCurrentDir()




o = obj()
print()
print()
print()
print()
print(getAllAtr(o))
print()
print(getDict(o))

'''
### DynamicData
### Storage
### Functionality
### Load and Represent
### Location
### Inputs - Mouse, Keyboard, Screen
### Draw
###
###
###
###
###
###
###
###
###
### SuperHearing
'''
