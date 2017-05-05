"""Module for solution to https://www.codewars.com/kata/distance-from-the-average."""

from operator import truediv
from decimal import Decimal


def distances_from_average(test_list):
    """Return a list of distances to the average in absolute terms."""
    avg = truediv(sum(test_list), len(test_list))
    return [round(float((v - avg) * - 1), 2) for v in test_list]
