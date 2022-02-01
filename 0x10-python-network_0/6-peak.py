#!/usr/bin/python3
"""Peak finding algorithm with the lowest complexity."""


def find_peak(list_of_integers):
    """Returns a peak in a list of unsorted integers."""
    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    if (size == 1):
        return list_of_integers[0]
    if (size == 2):
        return max(list_of_integers)

    pivot = int(size / 2)
    peak = list_of_integers[pivot]

    if (peak > list_of_integers[pivot - 1]
            and peak > list_of_integers[pivot + 1]):
        return peak
    elif peak < list_of_integers[pivot - 1]:
        return find_peak(list_of_integers[:pivot])
    else:
        return find_peak(list_of_integers[pivot + 1:])
