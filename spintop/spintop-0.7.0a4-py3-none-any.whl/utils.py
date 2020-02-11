
from contextlib import contextmanager
import cProfile, pstats, io

import yaml

def load_yaml_file(filename):
    with open(filename,'r') as readfile:
        data = readfile.read()
        return yaml.safe_load(data)
    

@contextmanager
def profiling(output_filename):
    pr = cProfile.Profile()
    pr.enable()
    try:
        yield
    finally:
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        with open(output_filename, 'w+') as profile_stream:
            ps = pstats.Stats(pr, stream=profile_stream).sort_stats(sortby)
            ps.print_stats()