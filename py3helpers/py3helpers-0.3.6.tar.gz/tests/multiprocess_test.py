#!/usr/bin/env python
"""Testing multiprocess.py"""
########################################################################
# File: multiprocess_test.py
#  executable: multiprocess_test.py
#
# Author: Andrew Bailey
# History: 02/15/18 Created
########################################################################

import os
import numpy as np
import unittest
from py3helpers.multiprocess import *
from py3helpers.utils import captured_output


class MultiprocessTest(unittest.TestCase):
    """Test the functions in seq_tools.py"""

    @classmethod
    def setUpClass(cls):
        super(MultiprocessTest, cls).setUpClass()
        cls.HOME = '/'.join(os.path.abspath(__file__).split("/")[:-1])

    def test_multiprocess(self):
        with captured_output() as (_, _):
            max_n = 10
            worker_count = 2
            iterable = np.random.randint(1, 10, 5)
            data = multiprocess_test(iterable, max_integer=max_n, worker_count=worker_count)
            all_lengths = []
            for i, random_ints in enumerate(data):
                all_lengths.append(len(random_ints))
                self.assertLessEqual(max(random_ints), max_n)

            self.assertSequenceEqual(sorted(all_lengths), sorted(iterable))

    def test_basic_service(self):
        with captured_output() as (_, _):
            max_n = 10
            worker_count = 2
            iterable = np.random.randint(1, 10, 5)
            data = multiprocess_test_basic_service(iterable, max_integer=max_n, worker_count=worker_count)
            all_lengths = []
            for i, random_ints in enumerate(data):
                all_lengths.append(len(random_ints))
                self.assertLessEqual(max(random_ints), max_n)

            self.assertSequenceEqual(sorted(all_lengths), sorted(iterable))


def multiprocess_test(iterable, max_integer=10, worker_count=2):
    """Multiprocess for testing multiprocessing
    :return: list of lists of random numbers with max integer
    """
    test_args = {"max_integer": max_integer}
    total, failure, messages, output = run_service(example_service, iterable,
                                                   test_args, ["number"], worker_count)
    return output


def multiprocess_test_basic_service(iterable, max_integer=10, worker_count=2):
    """Multiprocess for testing multiprocessing
    :return: list of lists of random numbers with max integer
    """
    test_args = {"max_integer": max_integer}
    service = BasicService(generate_n_random_integers, service_name="multiprocess_test_basic_service")
    total, failure, messages, output = run_service(service.run, iterable,
                                                   test_args, ["number"], worker_count)
    return output


def generate_n_random_integers(number, max_integer):
    """Generate n random integers given the max integer value
    :param number: number of integers to generate
    :param max_integer: maximum integer
    """
    return np.random.randint(0, max_integer, number)


def example_service(work_queue, done_queue, service_name="example_service"):
    """
    Service used by the multiprocess module for an example of what should be created for multiprocessing
    :param work_queue: arguments to be done
    :param done_queue: errors and returns to be put
    :param service_name: name of the service
    """
    # prep
    total_handled = 0
    failure_count = 0
    mem_usages = list()

    # catch overall exceptions
    try:
        for f in iter(work_queue.get, 'STOP'):
            # catch exceptions on each element
            try:
                integers = generate_n_random_integers(**f)
                done_queue.put(integers)
            except Exception as e:
                # get error and log it
                message = "{}:{}".format(type(e), str(e))
                error = "{} '{}' failed with: {}".format(service_name, current_process().name, message)
                print("[{}] ".format(service_name) + error)
                done_queue.put(error)
                failure_count += 1

            # increment total handling
            total_handled += 1

    except Exception as e:
        # get error and log it
        message = "{}:{}".format(type(e), str(e))
        error = "{} '{}' critically failed with: {}".format(service_name, current_process().name, message)
        print("[{}] ".format(service_name) + error)
        done_queue.put(error)

    finally:
        # logging and final reporting
        print("[%s] '%s' completed %d calls with %d failures"
              % (service_name, current_process().name, total_handled, failure_count))
        done_queue.put("{}:{}".format(TOTAL_KEY, total_handled))
        done_queue.put("{}:{}".format(FAILURE_KEY, failure_count))
        if len(mem_usages) > 0:
            done_queue.put("{}:{}".format(MEM_USAGE_KEY, ",".join(map(str, mem_usages))))


if __name__ == '__main__':
    unittest.main()
