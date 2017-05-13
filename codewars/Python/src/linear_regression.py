"""Module for solution to https://www.codewars.com/kata/linear-regression-of-y-on-x."""

import numpy as np
from math import sqrt

def regressionLine(x, y):
    """Return a tuple of intercept and slope of a given line x, y."""
    x_deltas = np.diff(x)
    y_deltas = np.diff(y)
    slopes = [y_delta/x_delta for x_delta, y_delta in zip(x_deltas, y_deltas)]
    
