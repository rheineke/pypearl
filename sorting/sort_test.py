import math
import time
import unittest

import pandas as pd
from copy import copy

from sorting import sort


class SortedInsertion1Test(unittest.TestCase):
    def test_example(self):
        xs = [3, 1, 4, 2]
        sorted_xs = sort.sorted_insertion_1(xs)
        self.assertEqual(sorted(xs), sorted_xs)

    def test_time_complexity(self):
        time_complexity_factor(sort.sorted_insertion_1, n2)


class SortedInsertion3Test(unittest.TestCase):
    def test_example(self):
        xs = [3, 1, 4, 2]
        sorted_xs = sort.sorted_insertion_3(xs)
        self.assertEqual(sorted(xs), sorted_xs)

    def test_time_complexity(self):
        time_complexity_factor(sort.sorted_insertion_3, n2)


class SortedQuick1Test(unittest.TestCase):
    def test_example(self):
        xs = [3, 1, 4, 2]
        sorted_xs = sort.sorted_quick_1(xs)
        self.assertEqual(sorted(xs), sorted_xs)

    def test_time_complexity(self):
        time_complexity_factor(sort.sorted_quick_1, n2)

    def test_time_complexity_identical_inputs(self):
        xs = [42] * 42
        time_complexity_factor(sort.sorted_quick_1, n2, iterable=xs)


def time_complexity_factor(sort_function, time_complexity_func, iterable=None):
    num = 1000
    data = [
        ('time', [0.] * num),
        ('n', [0] * num)
    ]
    df = pd.DataFrame.from_items(data)
    for i in range(num):
        if iterable is None:
            xs = [3, 1, 4, 2]  # Random number generation
        else:
            xs = copy(iterable)
        start = time.perf_counter()
        sorted_xs = sort_function(xs)
        end = time.perf_counter()
        df.loc[i] = [end - start, len(sorted_xs)]
    kwargs = dict(time_complexity_function=time_complexity_func)
    factor_srs = df.apply(_nanosecond_factor, axis=1, **kwargs)
    fmt = '{} Run time: {:.1f}n^2 nanoseconds'
    print(fmt.format(str(sort_function.__name__), factor_srs.mean()))


def _nanosecond_factor(srs, time_complexity_function):
    return srs['time'] * math.pow(10, 9) / time_complexity_function(srs['n'])


def n2(num_items):
    return math.pow(num_items, 2)
