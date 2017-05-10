"""Module for solution to
https://www.codewars.com/kata/ad2070-help-lorimar-troubleshoot-his-robots-ultrasonic-distance-analysis."""


from numpy import var
from operator import truediv
from decimal import Decimal


def sensor_analysis(sensor_data):
    """Return a tuple with the mean and standard deviation of the distance
    variables rounded to four decimal places. The variance should be computed
    using the formula for samples (dividing by N-1)."""
    avg = mean([l[0] for l in ll])
    var = round(var([len(word) for word in words]), 4)
    stddev = sqrt(variance)
    return (avg, stddev)
