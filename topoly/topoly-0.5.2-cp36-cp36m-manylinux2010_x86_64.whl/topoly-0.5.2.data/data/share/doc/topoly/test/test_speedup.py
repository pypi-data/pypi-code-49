""" The test of the speedup of polynomial calculation. For Alexander, Conway and Jones polynomial, tested are parameters
run_parallel, parallel_workers, density, and for Alexander cuda-generated speedup.

Test by Pawel Dabrowski-Tumanski.
e-mail p.dabrowski@cent.uw.edu.pl
12.02.2020"""

from topoly import alexander, conway, jones
from topoly.manipulation import check_cuda
from topoly.params import Closure
import time
import os
import pytest

f = 'data/31.xyz'

polynomials = {'Alexander': alexander, 'Conway': conway, 'Jones': jones}
cutoff = 0.1


def compare_dictionaries(dict1, dict2, cutoff=cutoff):
    difference = {}
    idents_all = list(set(dict1.keys()) | set(dict2.keys()))
    for ident in idents_all:
        knots_all = list(set(dict1.get(ident, {}).keys()) | set(dict2.get(ident, {}).keys()))
        for knot in knots_all:
            if '-' in knot:
                continue
            v1 = dict1.get(ident, {}).get(knot, 0)
            v2 = dict2.get(ident, {}).get(knot, 0)
            diff = abs(v1-v2)
            if diff > cutoff:
                if ident not in difference.keys():
                    difference[ident] = {}
                difference[ident][knot] = diff
    return difference


# @pytest.mark.skip
def test_speedup_parallel():
    print("Parallel speedup test.")
    times = {}
    results = {}

    for key in polynomials.keys():
        print(key)
        times[key] = []
        results[key] = []
        workers = []

        # bare calculation
        t = time.time()
        results[key].append(polynomials[key](f, run_parallel=False, translate=True, closure=Closure.CLOSED,
                                             matrix=True, chiral=False))
        times[key].append(time.time()-t)
        workers.append(1)

        # # partial speedup
        t = time.time()
        results[key].append(polynomials[key](f, parallel_workers=2, translate=True, closure=Closure.CLOSED,
                                             matrix=True, chiral=False))
        times[key].append(time.time()-t)
        workers.append(2)

        # full speedup
        t = time.time()
        results[key].append(polynomials[key](f, translate=True, closure=Closure.CLOSED, matrix=True, chiral=False))
        times[key].append(time.time()-t)
        workers.append(os.cpu_count())

        print("Workers\t Times")
        for worker_num, t in zip(workers, times[key]):
            print(str(worker_num) + '\t' + str(t))

        for k in range(len(times[key])-1):
            assert results[key][k] == results[key][k+1]
    print("\n========\n")
    return

# @pytest.mark.skip
def test_speedup_density():
    print("Density speedup test.")
    # note that higher density does not need necessarily mean speed, as after first calculation, the second one, more
    # detailed (density=1) is performed for selected points
    times = {}
    results = {}
    for key in polynomials.keys():
        print(key)
        times[key] = []
        results[key] = []
        densities = []

        # density 1 - whole matrix
        t = time.time()
        results[key].append(polynomials[key](f, matrix=True, cuda=False, density=1, translate=True,
                                             closure=Closure.CLOSED, chiral=False))
        times[key].append(time.time() - t)
        densities.append(1)
        # print(results[key][-1])

        # density 5
        t = time.time()
        results[key].append(polynomials[key](f,  matrix=True, cuda=False, density=5, translate=True,
                                             closure=Closure.CLOSED, chiral=False))
        times[key].append(time.time() - t)
        densities.append(5)
        # print(results[key][-1])

        # in this case does not speed up the calculations!
        # # density 10
        # t = time.time()
        # results[key].append(polynomials[key](f,  matrix=True, cuda=False, density=10, translate=True,
        #                                      closure=Closure.CLOSED, chiral=False))
        # times[key].append(time.time() - t)

        print("Densities\t Times")
        for density, t in zip(densities, times[key]):
            print(str(density) + '\t' + str(t))

        for k in range(len(times[key])-1):
            assert results[key][k] == results[key][k+1]
        print("\n========\n")
    return

# @pytest.mark.skip
@pytest.mark.cuda
def test_speedup_cuda():
    print("CUDA speedup test.")
    times = []
    results = []
    densities = []

    # no CUDA
    t = time.time()
    results.append(alexander(f, cuda=False, matrix=True, translate=True, closure=Closure.CLOSED))
    times.append(time.time() - t)
    densities.append('No CUDA')

    # with CUDA
    t = time.time()
    results.append(alexander(f, cuda=True, matrix=True, translate=True, closure=Closure.CLOSED))
    times.append(time.time()-t)
    densities.append(1)

    # with CUDA and density=5
    t = time.time()
    results.append(alexander(f, cuda=True, matrix=True, translate=True, closure=Closure.CLOSED, density=5))
    times.append(time.time()-t)
    densities.append(5)

    # print("Results: ", results)
    print("Densities\t Times")
    for density, t in zip(densities, times):
        print(str(density) + '\t' + str(t))

    for k in range(len(times) - 1):
        diff = compare_dictionaries(results[k], results[k+1])
        assert diff == {}
    print("\n========\n")
    return


if __name__ == '__main__':
    test_speedup_parallel()
    test_speedup_density()
    if check_cuda():
        test_speedup_cuda()
    else:
        print("No CUDA detected. Omitting the CUDA test.")

