from copy import copy


def sorted_insertion_1(iterable):
    """
    Insertion Sort 1 from Programming Pearls by Jon Bentley

    TODO(rheineke):
    A custom key function can be supplied to customise the sort order, and the
    reverse flag can be set to request the result in descending order.

    :param iterable: list of items
    :return: new list containing all items from the iterable in ascending order
    """
    result = copy(iterable)
    for i in range(len(result)):
        for j in reversed(range(1, i+1)):
            if result[j-1] < result[j]:
                break
            result[j-1], result[j] = result[j], result[j-1]

    return result


def sorted_insertion_3(iterable):
    """
    Insertion Sort 3 from Programming Pearls by Jon Bentley
    :param iterable: list of items
    :return: new list containing all items from the iterable in ascending order
    """
    result = copy(iterable)
    for i in range(len(result)):
        t = result[i]
        j = i
        for j in reversed(range(0, i+1)):
            if result[j-1] < t:
                break
            result[j] = result[j-1]
        result[j] = t

    return result


def sorted_quick_1(iterable):
    """
    QuickSort 1 from Programming Pearls by Jon Bentley
    :param iterable: list of items
    :return: new list containing all items from the iterable in ascending order
    """
    result = copy(iterable)
    _qsort_1(result, 0, len(result) - 1)
    return result


def _qsort_1(iterable, lower, upper):
    if lower >= upper:
        # At most one element; do nothing
        return
    m = lower
    for i in range(lower + 1, upper+1):
        # invariant:
        # iterable[lower+1,..., m] < iterable[lower] &&
        # iterable[m+1,..., i-1] >= iterable[l]
        if iterable[i] < iterable[lower]:
            m += 1
            iterable[m], iterable[i] = iterable[i], iterable[m]
    iterable[m], iterable[lower] = iterable[lower], iterable[m]
    # iterable[lower,...,m-1] < iterable[m] <= iterable[m+1,...,upper]
    _qsort_1(iterable, lower, m - 1)
    _qsort_1(iterable, m + 1, upper)


def sorted_quick_2(iterable):
    """
    QuickSort 2 from Programming Pearls by Jon Bentley
    :param iterable: list of items
    :return: new list containing all items from the iterable in ascending order
    """
    result = copy(iterable)
    _qsort_2(result, 0, len(result) - 1)
    return result


def _qsort_2(iterable, lower, upper):
    if lower >= upper:
        # At most one element; do nothing
        return
    m = upper + 1
    for i in reversed(range(lower, upper+1)):
        # invariant:
        # TODO(rheineke): Change invariants
        # iterable[lower+1,..., m] < iterable[lower] &&
        # iterable[m+1,..., i-1] >= iterable[l]
        if iterable[i] >= iterable[lower]:
            m -= 1
            iterable[m], iterable[i] = iterable[i], iterable[m]
    # iterable[lower,...,m-1] < iterable[m] <= iterable[m+1,...,upper]
    _qsort_2(iterable, lower, m - 1)
    _qsort_2(iterable, m + 1, upper)
