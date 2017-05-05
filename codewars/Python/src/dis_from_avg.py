"""Module for solution to https://www.codewars.com/kata/distance-from-the-average."""

from operator import truediv


def distances_from_average(test_list):
    """Return a list of distances to the average in absolute terms."""
    avg = truediv(sum(test_list), len(test_list))
    return [float('{}'.format((v - avg) * - 1)) for v in test_list]
