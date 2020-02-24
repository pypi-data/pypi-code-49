import concurrent.futures
import itertools
import math
import threading
import time
import unittest

import iterlist

range_size = 10
half_range = int(math.ceil(range_size / 2))


class TestGetItem(unittest.TestCase):
    def test_incremental(self):
        lazy = iterlist.IterList(range(range_size))
        for i in range(range_size):
            lazy[i]
            self.assertEqual(len(lazy._list), i + 1)
        self.assertEqual(len(lazy), range_size)
        for a, b in zip(lazy._list, range(range_size)):
            self.assertEqual(a, b)

    def test_all_at_once(self):
        lazy = iterlist.IterList(range(range_size))
        lazy[range_size - 1]
        self.assertEqual(len(lazy._list), range_size)

    def test_negative_index(self):
        lazy = iterlist.IterList(range(range_size))
        for i in range(range_size):
            self.assertEqual(lazy[-(i + 1)], range_size - i - 1)

    def test_slice_copy(self):
        lazy = iterlist.IterList(range(range_size))
        slz = lazy[:]
        self.assertEqual(len(slz), range_size)
        self.assertEqual(len(lazy._list), range_size)

    def test_slice_from_implicit_zero(self):
        lazy = iterlist.IterList(range(range_size))
        slz = lazy[:half_range]
        self.assertEqual(len(slz), half_range)
        self.assertEqual(len(lazy._list), half_range)

    def test_slice_from_explicit_zero(self):
        lazy = iterlist.IterList(range(range_size))
        slz = lazy[0:half_range]
        self.assertEqual(len(slz), half_range)
        self.assertEqual(len(lazy._list), half_range)

    def test_slice_from_positive(self):
        lazy = iterlist.IterList(range(range_size))
        slz = lazy[1:half_range]
        self.assertEqual(len(slz), half_range-1)
        self.assertEqual(len(lazy._list), half_range)

    def test_slice_from_positive_to_end(self):
        lazy = iterlist.IterList(range(range_size))
        slz = lazy[2:]
        self.assertEqual(len(slz), range_size-2)
        self.assertEqual(len(lazy._list), range_size)

    def test_slice_from_negative(self):
        lazy = iterlist.IterList(range(range_size))
        slz = lazy[-2:]
        self.assertEqual(len(slz), 2)
        self.assertEqual(len(lazy._list), range_size)

    def test_slice_from_negative_stop(self):
        lazy = iterlist.IterList(range(range_size))
        slz = lazy[-3:-1]
        self.assertEqual(len(slz), 2)
        self.assertEqual(len(lazy._list), range_size)

    def test_slice_reversed(self):
        orig = list(range(range_size))
        lazy = iterlist.IterList(orig)
        neg_slz = lazy[half_range::-1]
        self.assertEqual(neg_slz, orig[half_range::-1])
        self.assertEqual(len(neg_slz), half_range + 1)
        self.assertEqual(len(lazy._list), half_range + 1)

    def test_slice_reversed_by_1(self):
        orig = list(range(range_size))
        lazy = iterlist.IterList(orig)
        neg_slz = lazy[half_range:0:-1]
        self.assertEqual(neg_slz, orig[half_range:0:-1])
        self.assertEqual(len(neg_slz), half_range)
        self.assertEqual(len(lazy._list), half_range + 1)

    def test_slice_by_2(self):
        lazy = iterlist.IterList(range(range_size))
        exp_size = int(math.floor(half_range / 2))
        slz = lazy[0:half_range:2]
        self.assertEqual(len(slz), exp_size)
        self.assertLessEqual(len(lazy._list), half_range)

    def test_slice_reversed_by_2(self):
        orig = list(range(range_size))
        lazy = iterlist.IterList(orig)
        exp_size = int(math.floor((half_range + 1) / 2))
        neg_slz = lazy[half_range::-2]
        self.assertEqual(neg_slz, orig[half_range::-2])
        self.assertEqual(len(neg_slz), exp_size)
        self.assertEqual(len(lazy._list), half_range + 1)

    def test_slice_empty_case(self):
        lazy = iterlist.IterList(range(range_size))
        empty_slz = lazy[0:half_range:-1]
        self.assertEqual(empty_slz, [])
        self.assertEqual(len(lazy._list), 0)
        empty_slz2 = lazy[half_range:0]
        self.assertEqual(empty_slz2, [])
        self.assertEqual(len(lazy._list), 0)

class TestSetItem(unittest.TestCase):
    def test_zero_out(self):
        lazy = iterlist.IterList(range(range_size))
        for i in range(range_size):
            lazy[i] = 0
        for i in range(range_size):
            self.assertEqual(lazy[i], 0)

    def test_slice_assign(self):
        lazy = iterlist.IterList(range(range_size))
        seq = list(range(range_size))
        lazy[2:5] = [10,20,30,40,50,60]
        seq[2:5] = [10,20,30,40,50,60]
        for i, e in enumerate(seq):
            self.assertEqual(lazy[i], e) 

    def test_negative_slice_assign(self):
        lazy = iterlist.IterList(range(range_size))
        seq = list(range(range_size))
        lazy[-2:-5] = [10,20,30,40,50,60]
        seq[-2:-5] = [10,20,30,40,50,60]
        for i, e in enumerate(seq):
            self.assertEqual(lazy[i], e) 
        

class TestDelItem(unittest.TestCase):
    def test_remove_middle(self):
        lazy = iterlist.IterList(range(range_size))
        del lazy[4]
        self.assertEqual(lazy[3] + 2, lazy[4])


class TestLen(unittest.TestCase):
    def test_lens(self):
        seq = list(range(10))
        self.assertEqual(len(seq), len(iterlist.IterList(seq)))


class TestContains(unittest.TestCase):
    def test_range(self):
        range_min = 10
        range_max = 20
        lazy = iterlist.IterList(range(range_min, range_max))
        for i in range(range_min, range_max):
            self.assertTrue(i in lazy)
        for i in range(0, range_min):
            self.assertFalse(i in lazy)
        for i in range(range_max, range_max + 10):
            self.assertFalse(i in lazy)

class TestBool(unittest.TestCase):
    def test_for_false(self):
        self.assertFalse(iterlist.IterList(range(0)))
        self.assertFalse(iterlist.IterList([]))

    def test_for_true(self):
        self.assertTrue(iterlist.IterList(range(1)))
        self.assertTrue(iterlist.IterList([1]))

    def test_for_true_already_consumed(self):
        lazy = iterlist.IterList(range(2))
        self.assertEqual(len(lazy._list), 0)
        lazy[0]
        self.assertEqual(len(lazy._list), 1)
        self.assertTrue(lazy)
        self.assertEqual(len(lazy._list), 1)


class TestExtend(unittest.TestCase):
    def test_two_range(self):
        lazy = iterlist.IterList(range(10))
        lazy[3]
        lazy.extend(range(10, 20))
        for i in range(20):
            self.assertEqual(lazy[i], i)

    def test_iadd(self):
        lazy = iterlist.IterList(range(10))
        lazy[3]
        lazy += range(10, 20)
        for i in range(20):
            self.assertEqual(lazy[i], i)

class TestRepr(unittest.TestCase):
    def test_tuple_simple(self):
        lazy = iterlist.IterTuple(range(3))
        self.assertEqual(repr(lazy), '(0, 1, 2)')

    def test_list_simple(self):
        lazy = iterlist.IterList(range(3))
        self.assertEqual(repr(lazy), '[0, 1, 2]')

class TestEquality(unittest.TestCase):
    def test_should_equal_tuple(self):
        a = iterlist.IterTuple(range(3))
        b = iterlist.IterTuple(range(3))
        self.assertTrue(a == b)
        self.assertFalse(a != b)

    def test_should_equal_list(self):
        a = iterlist.IterList(range(3))
        b = iterlist.IterList(range(3))
        self.assertTrue(a == b)
        self.assertFalse(a != b)

    def test_totally_different(self):
        a = iterlist.IterList(range(3))
        b = iterlist.IterList(range(3, 10))
        self.assertFalse(a == b)
        self.assertEqual(len(a._list), 1)
        self.assertEqual(len(b._list), 1)
        self.assertTrue(a != b)

    def test_different_length(self):
        a = iterlist.IterList(range(range_size))
        b = iterlist.IterList(range(range_size + 1))
        self.assertFalse(a == b)
        self.assertTrue(a != b)

    def test_with_list(self):
        a = iterlist.IterList(range(range_size))
        b = iterlist.IterTuple(range(range_size))
        c = list(range(range_size))
        # IterList/IterTuple equality: never equal even with same contents
        self.assertTrue(a != b)
        self.assertFalse(a == b)
        # IterList/list equality
        self.assertTrue(a == c)
        self.assertFalse(a != c)
        # IterTuple/list equality
        self.assertTrue(b != c)
        self.assertFalse(b == c)

    def test_with_tuple(self):
        a = iterlist.IterList(range(range_size))
        b = iterlist.IterTuple(range(range_size))
        c = tuple(range(range_size))
        # IterList/IterTuple equality: never equal even with same contents
        self.assertTrue(a != b)
        self.assertFalse(a == b)
        # IterList/tuple equality
        self.assertTrue(a != c)
        self.assertFalse(a == c)
        # IterTuple/tuple equality
        self.assertTrue(b == c)
        self.assertFalse(b != c)

    def test_with_str(self):
        a = "this is a test"
        b = iterlist.IterList(a)
        self.assertTrue(a != b)
        self.assertFalse(a == b)
        self.assertTrue(list(a) == b)
        self.assertFalse(list(a) != b)

    def test_with_non_iterable(self):
        a = iterlist.IterList([])
        b = iterlist.IterTuple([])
        c = iterlist.CachedIterator([])
        d = 0
        self.assertFalse(a == d)
        self.assertTrue(a != d)
        self.assertFalse(b == d)
        self.assertTrue(b != d)
        self.assertFalse(c == d)
        self.assertTrue(c != d)

    def test_with_bare_iterable(self):
        a = iterlist.IterList(range(range_size))
        b = (v for v in range(range_size))
        self.assertFalse(a == b)
        self.assertTrue(a != b)
        # checking equality shouldn't have collapsed the generator
        b2 = list(b)
        self.assertTrue(a == b2)
        self.assertFalse(a != b2)

    def test_with_bare_iterable_different_length(self):
        a = iterlist.IterList(range(range_size))
        b = (v for v in range(range_size + 1))
        self.assertFalse(a == b)
        self.assertTrue(a != b)
        # checking equality shouldn't have collapsed the generator
        b2 = list(b)
        self.assertFalse(a == b2)
        self.assertTrue(a != b2)

class TestReversed(unittest.TestCase):
    def test_backwards_range(self):
        lazy = iterlist.IterList(range(range_size))
        for i, v in zip(range(9, -1, -1), reversed(lazy)):
            self.assertEqual(i, v)

    def test_in_place(self):
        lazy = iterlist.IterList(range(range_size))
        lazy.reverse()
        for i, v in zip(range(9, -1, -1), lazy):
            self.assertEqual(i, v)


class TestSort(unittest.TestCase):
    def test_sort(self):
        lazy = iterlist.IterList(range(range_size))
        lazy.sort()
        for i in range(len(lazy) - 1):
            self.assertLess(lazy[i], lazy[i] + 1) 

class TestPop(unittest.TestCase):
    def test_pop_default(self):
        lazy = iterlist.IterList(range(range_size))
        for i in range(range_size):
            self.assertEqual(len(lazy), range_size - i)
            self.assertEqual(lazy.pop(), range_size - i - 1)
            self.assertEqual(len(lazy), range_size - i - 1)


class TestIndex(unittest.TestCase):
    def test_index(self):
        lazy = iterlist.IterList(range(range_size))
        self.assertEqual(lazy.index(5), 5)
        self.assertEqual(len(lazy._list), 6)
        self.assertRaises(ValueError, lazy.index, 10)
        self.assertRaises(ValueError, lazy.index, -1)

    def test_index_with_bounds(self):
        lazy = iterlist.IterList(range(range_size))
        self.assertEqual(lazy.index(9, 5), 9)
        self.assertEqual(lazy.index(2, 0, -2), 2)
        self.assertEqual(lazy.index(5, -7, -2), 5)

    def test_negative_index_wraps(self):
        lazy = iterlist.IterList(range(range_size))
        with self.assertRaises(IndexError):
                self.assertEqual(lazy.index(9, -2*range_size), 9)
        

class TestCount(unittest.TestCase):
    def test_count(self):
        lazy = iterlist.IterList(
            itertools.chain.from_iterable([i]*i for i in range(range_size)))
        for i in range(range_size):
            self.assertEqual(i, lazy.count(i))

class TestRemove(unittest.TestCase):
    def test_remove(self):
        lazy = iterlist.IterList(range(range_size))
        for i in range(range_size):
            lazy.remove(i)
        self.assertEqual(len(lazy), 0)

    def test_remove_fails(self):
        lazy = iterlist.IterList(range(range_size))
        for i in range(range_size, range_size*2):
            self.assertRaises(ValueError, lazy.remove, i)

class TestInsert(unittest.TestCase):
    def test_insert(self):
        lazy = iterlist.IterList(range(range_size))
        lazy.insert(2, 'a')
        self.assertEqual(lazy[2], 'a')
        lazy.insert(10, 'b')
        self.assertEqual(lazy[10], 'b')

    def test_insert_negative(self):
        lazy = iterlist.IterList(range(range_size))
        lazy.insert(-1, 'c')
        self.assertEqual(lazy[-2], 'c')


class TestAppend(unittest.TestCase):
    def test_append(self):
        lazy = iterlist.IterList(range(range_size // 2))
        for i in range(range_size // 2, range_size):
            lazy.append(i)
        for i, j in zip(lazy, range(range_size)):
            self.assertEqual(i, j)

class TestClear(unittest.TestCase):
    def test_unevaluated(self):
        lazy = iterlist.IterList(range(range_size))
        lazy.clear()
        self.assertEqual(len(lazy), 0)

    def test_evaluated(self):
        lazy = iterlist.IterList(range(range_size))
        len(lazy)
        lazy.clear()
        self.assertEqual(len(lazy), 0)

    def test_clear_and_add(self):
        lazy = iterlist.IterList(range(range_size))
        lazy.clear()
        self.assertEqual(len(lazy), 0)
        lazy.extend(range(range_size))
        self.assertEqual(len(lazy), range_size)

class TestLessThan(unittest.TestCase):
    def test_simple(self):
        a = iterlist.IterList(range(1, range_size + 1))
        b = iterlist.IterList(range(range_size))
        self.assertTrue(b < a)
        self.assertFalse(a < b)

    def test_uneven(self):
        a = iterlist.IterList(range(range_size))
        b = iterlist.IterList(range(range_size - 1))
        self.assertTrue(b < a)
        self.assertFalse(a < b)

    def test_unordered(self):
        a = iterlist.IterList([1,9])
        b = iterlist.IterList([2, -1])
        self.assertTrue(a < b)
        self.assertFalse(b < a)

    def test_with_list(self):
        a = iterlist.IterList(range(range_size))
        b = iterlist.IterTuple(range(range_size))
        c = list(range(-1, range_size-1))
        d = list(range(1, range_size+1))
        e = list(range(range_size))
        self.assertTrue(a < d)
        self.assertFalse(a < c)
        self.assertFalse(a < e)
        # cannot compare IterList and tuple
        with self.assertRaises(TypeError):
            self.assertTrue(b < d)
        with self.assertRaises(TypeError):
            self.assertFalse(b < c)
        with self.assertRaises(TypeError):
            self.assertFalse(b < e)
        try:
            self.assertFalse(d < a)
            # XXX: doesn't actually do less than, always False
            self.assertFalse(c < a)
            self.assertFalse(e < a)
        except TypeError:
            # cannot compare list and IterList on py3
            pass

    def test_with_tuple(self):
        a = iterlist.IterTuple(range(range_size))
        b = iterlist.IterList(range(range_size))
        c = tuple(range(-1, range_size-1))
        d = tuple(range(1, range_size+1))
        e = tuple(range(range_size))
        self.assertTrue(a < d)
        self.assertFalse(a < c)
        self.assertFalse(a < e)
        # cannot compare IterList and tuple
        with self.assertRaises(TypeError):
            self.assertTrue(b < d)
        with self.assertRaises(TypeError):
            self.assertFalse(b < c)
        with self.assertRaises(TypeError):
            self.assertFalse(b < e)
        try:
            self.assertFalse(d < a)
            # XXX: doesn't actually do less than, always False
            self.assertFalse(c < a)
            self.assertFalse(e < a)
        except TypeError:
            # cannot compare tuple and IterTuple on py3
            pass



class TestIter(unittest.TestCase):
    def test_iter_unconsumed(self):
        orig = list(range(range_size))
        lazy = iterlist.IterList(orig)
        for ix, v in enumerate(lazy):
            self.assertEqual(v, orig[ix])

    def test_iter_partial_consumed(self):
        orig = list(range(range_size))
        lazy = iterlist.IterList(orig)
        lazy[2]
        self.assertEqual(len(lazy._list), 3)
        for ix, v in enumerate(lazy):
            self.assertEqual(v, orig[ix])

    def test_iter_consume_while_iter(self):
        orig = list(range(range_size))
        lazy = iterlist.IterList(orig)
        for ix, v in enumerate(lazy):
            if ix == 3:
                lazy[5]
                self.assertEqual(len(lazy._list), 6)
            self.assertEqual(v, orig[ix])


class TestConcurrentAccess(unittest.TestCase):
    def test_multiple_iterators_with_lock(self, lock=True, delay=0.005, n_threads=5):
        orig = list(range(range_size))
        delay_generator = (ix for ix in orig if time.sleep(delay) is None)
        lazy = iterlist.IterTuple(delay_generator, lock=lock)
        with concurrent.futures.ThreadPoolExecutor(n_threads) as tp:
            future_results = [tp.submit(lambda: [x for x in lazy]) for _ in
                              range(n_threads)]
            results = [f.result() for f in future_results]
        for r in results:
            self.assertEqual(r, orig)

    def test_multiple_iterators_no_lock(self):
        with self.assertRaises(ValueError) as ve:
            self.test_multiple_iterators_with_lock(lock=False)
        self.assertIn("generator already executing", str(ve.exception))

    def test_multiple_iterators_pass_lock(self):
        lock = threading.RLock()
        self.test_multiple_iterators_with_lock(lock=lock)


if __name__ == '__main__':
    unittest.main()
