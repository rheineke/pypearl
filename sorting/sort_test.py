import math
import time
import unittest

import pandas as pd

from sorting import sort


class SortedInsertion1Test(unittest.TestCase):
    def test_example(self):
        xs = [3, 1, 4, 2]
        sorted_xs = sort.sorted_insertion_1(xs)
        self.assertEqual(sorted(xs), sorted_xs)

    def test_time_complexity(self):
        time_complexity_factor(sort.sorted_insertion_1)


class SortedInsertion3Test(unittest.TestCase):
    def test_example(self):
        xs = [3, 1, 4, 2]
        sorted_xs = sort.sorted_insertion_3(xs)
        self.assertEqual(sorted(xs), sorted_xs)

    def test_time_complexity(self):
        time_complexity_factor(sort.sorted_insertion_3)


class SortedQuick1Test(unittest.TestCase):
    def test_example(self):
        xs = [3, 1, 4, 2]
        sorted_xs = sort.sorted_quick_1(xs)
        self.assertEqual(sorted(xs), sorted_xs)

    def test_time_complexity(self):
        time_complexity_factor(sort.sorted_quick_1)


def time_complexity_factor(sort_function):
    num = 1000
    data = [
        ('time', [0.] * num),
        ('n', [0] * num)
    ]
    df = pd.DataFrame.from_items(data)
    for i in range(num):
        xs = [3, 1, 4, 2]  # Random number generation
        start = time.perf_counter()
        sorted_xs = sort_function(xs)
        end = time.perf_counter()
        df.loc[i] = [end - start, len(sorted_xs)]
    factor_srs = df.apply(_nanosecond_factor, axis=1)
    print('Run time: {:.1f}n^2 nanoseconds'.format(factor_srs.mean()))


def _nanosecond_factor(srs):
    return srs['time'] * math.pow(10, 9) / math.pow(srs['n'], 2)
