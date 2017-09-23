"""Solution for https://www.codewars.com/kata/intro-to-statistics-part-2-boxplots/."""

from math import ceil, floor
from numbers import Real

class StatisticalSummary(object):
    """Class which contains a various statistical methods.
    """

    def __init__(self, seq):
        self.seq = sorted([x for x in seq if isinstance(x, Real)])
        self.n = len(self.seq)

    def _percentile(self, p):
        """Return the boundary between the given quartile of sorted sequence of
        valid values.
        """
        seq = self.seq
        k = (len(seq)-1) * p; f = floor(k); c = ceil(k)
        return seq[int(k)] if f == c else seq[int(f)] * (c-k) + seq[int(c)] * (k-f)
