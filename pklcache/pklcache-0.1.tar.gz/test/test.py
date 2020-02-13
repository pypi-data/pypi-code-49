"""
Run some tests
"""

from pklcache import cache
import os


if __name__ == '__main__':

    
    ######### TEST 1 ########

    # Remove cache file if present
    fname = "test_cache.pkl"
    if os.path.isfile(fname):
        os.remove(fname)

    @cache(fname)
    def foo():
        ret = [(69,96), "who cares about types", 42, [4,2,0]]
        return ret

    # Call foo two times, the first is executed and saves the 
    # result on disk, the second time it just loads the data
    ret = foo()  
    ret_cached = foo()

    assert(ret==ret_cached)
    print("Test 1: OK")

