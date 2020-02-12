from skribot import Skribot
from skribrain import * # pinout definition

# You can configure standard connections
# by replacing the following line with
# robot = Skribot(predef='SKRIBRAIN')
robot = Skribot()

def setup():
    '''Put setup code here.'''

def loop():
    '''Put loop code here.'''

try:
    setup()
    while True:
        loop()
except KeyboardInterrupt:
    pass
