import argparse

def p(*args, **kwargs):
    if 'formatter_class' not in kwargs:
        kwargs['formatter_class'] = argparse.ArgumentDefaultsHelpFormatter
    return argparse.ArgumentParser(*args, **kwargs)
