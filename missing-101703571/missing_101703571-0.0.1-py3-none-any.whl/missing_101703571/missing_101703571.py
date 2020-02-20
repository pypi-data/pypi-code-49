import pandas as pd
import numpy as np
import sys

def missing(file_name):
    df = pd.read_csv(file_name)
    print("Before filling in the missing values:")
    print(df)
    df = df.fillna(df.mean().iloc[0])
    print("After filling in the missing values:")
    print(df)
    

if __name__=='__main__':

    try:
        file_name = sys.argv[1]
        missing(file_name)

    except IOError:
        print('An error occurred trying to read the file.')

    except ValueError:
        print('Non-numeric data found in the file.')

    except ImportError:
        print ("NO module found")

    except EOFError:
        print('No input from user detected or end of file reached!')

    except KeyboardInterrupt:
        print('You cancelled the operation.')

    except SyntaxError:
        print("Invalid Syntax")

    except IndentationError:
        print("Dude! Indentation not specified properly.")

    except TypeError:
        print("Invalid datatype in function")

    except UnboundLocalError:
        print("No value assigned to local variable in function!")

    except KeyError:
        print("Key not found in dictionary!")

    except IndexError:
        print("Index not found in sequence!")

    except AttributeError:
        print("Failure of attribute reference or assignment.")

    except AssertionError:
        print("Failure of assert statement!")

    except ZeroDivisionError:
        print("ZeroDivisionError!!!")

    except FloatingPointError:
        print("Failure of floating point calculation.")

    except OverflowError:
        print("Maximum Limit reached!")

    except ArithmeticError:
        print("Calculation problem.")

    except:
        print('An error occurred.')
