"""Module for solution to https://www.codewars.com/kata/linear-regression-of-y-on-x."""

import numpy as np
from math import sqrt, ceil
import operator as op

def regressionLine(x, y):
    """Return a tuple of intercept and slope of a given line x_coords, y_coords."""
    sum_xy = sum([xy for xy in map(op.mul, x, y)])
    sum_x_squared = sum([n ** 2 for n in x])
    slope = (len(x) * sum_xy - sum(x) * sum(y)) / (len(x) * sum_x_squared - sum(x) ** 2)
    intercept = (sum(y) - slope * sum(x)) / len(x)
    return float('{0:.4f}'.format(intercept)), float('{0:.4f}'.format(slope))
