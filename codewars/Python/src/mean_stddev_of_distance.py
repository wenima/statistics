"""Module for solution to
https://www.codewars.com/kata/ad2070-help-lorimar-troubleshoot-his-robots-ultrasonic-distance-analysis."""


from numpy import mean, var
from math import sqrt
from operator import truediv
from decimal import Decimal


def sensor_analysis(sensor_data):
    """Return a tuple with the mean and standard deviation of the distance
    variables rounded to four decimal places. The variance should be computed
    using the formula for samples (dividing by N-1)."""
    distances = [data[1] for idx, data in enumerate(sensor_data)]
    avg = mean(distances)
    variance = round(var(distances, ddof=1), 4)
    stddev = round(sqrt(variance), 4)
    return (avg, stddev)
