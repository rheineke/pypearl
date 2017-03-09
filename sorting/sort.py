from copy import copy


def sorted_insertion_1(iterable):
    """
    Insertion Sort 1 from Programming Pearls by Jon Bentley
    """
    result = copy(iterable)
    for i in range(len(result)):
        for j in reversed(range(1, i+1)):
            if result[j-1] < result[j]:
                break
            result[j-1], result[j] = result[j], result[j-1]

    return result
