"""Tests for https://www.codewars.com/kata/intro-to-statistics-part-1-a-five-figure-summary/python."""


class StatisticalSummary(object):
    """Class which contains a method to return six figure version of the five number summary
    https://en.wikipedia.org/wiki/Five-number_summary.
    """

    def __init__(self, seq):
        self.seq = seq

    def five_figure_summary(self, precision=None):
        """The five figure summary gives the lower extreme, upper extreme, lower
        quartile, median, and upper quartile, all derived from the supplied sample
        data.
        """
        
