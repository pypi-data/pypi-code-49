import os
from ImageToTextLibrary.Keywords import Keywords
from ImageToTextLibrary.version import VERSION

__version__ = VERSION


class ImageToTextLibrary(Keywords):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = VERSION

    def __init__(self):
        '''ImageToTextLibrary can be imported.
        '''
        vs = VERSION
        print ("Image to Text Library imported")
