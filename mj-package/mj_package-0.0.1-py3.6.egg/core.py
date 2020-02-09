"""
    This package owns personnal and useful machine learning
    functions.

    Use :

    >>> from mj_package import proclamer
    >>> proclamer()
"""

# WHAT YOU CAN IMPORT
__all__=['proclamer']

# CODE
from datetime import datetime

def proclamer()-> None:
    """
        Just an example....
    """
    text =  "We are the [%s] " % datetime.now()
    print(text)

if __name__=="__main__":
    proclamer()

