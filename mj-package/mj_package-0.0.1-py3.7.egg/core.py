"""
    This package owns personnal and useful machine learning
    functions.

    Use :

    >>> from mj_package import proclamer
    >>> proclamer()
"""

# WHAT YOU CAN IMPORT
__all__=['proclamer','add','sub']

# CODE
from datetime import datetime

def proclamer()-> None:
    """
        Just an example....
    """
    text =  "We are the [%s] " % datetime.now()
    print(text)

def add(a:float,b:float)->float:
    """
        Addition...
    """
    return(a+b)

def sub(a:float,b:float)->float:
    """
        Addition...
    """
    return(a-b)

def nothing():
    print("hello_word")

if __name__=="__main__":
    main()

