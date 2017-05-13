"""Module for solution to https://www.codewars.com/kata/linear-regression-of-y-on-x."""

from numpy import mean
from math import sqrt


def avg_var_stdev(dataset):
    """Return a tuple with 3 values, mean, var and standard deviation based on the input.
    The input is a list/array."""
    avg = mean(dataset)
    variance = sum([(dp[0] - avg) ** 2 for dp in dataset])
    stddev = sqrt(variance)
    return (avg, variance, stddev)

def regressionLine(x, y):
    """ Return the a (intercept) and b (slope) of Regression Line (Y on X)."""
    pass
