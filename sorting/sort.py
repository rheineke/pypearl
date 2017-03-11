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
