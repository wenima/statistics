"""Solution for https://www.codewars.com/kata/intro-to-statistics-part-1-a-five-figure-summary/python."""

from math import modf
from numbers import Real

class StatisticalSummary(object):
    """Class which contains a method to return six figure version of the five number summary
    https://en.wikipedia.org/wiki/Five-number_summary.
    """

    def __init__(self, seq):
        self.seq = sorted([x for x in seq if isinstance(x, Real)])
        self.n = len(self.seq)

    def five_figure_summary(self, precision=None):
        """Return number of valid samples, lower extreme, upper extreme, lower
        quartile, median, and upper quartile.
        """
        low = min(self.seq)
        high = max(self.seq)

        if precision:
            return (round(self.n, precision), round(low, precision), round(high, precision), round(self._get_quartile(25), precision), round(self._get_quartile(50), precision)
                    , round(self._get_quartile(75), precision))
        return (self.n, low, high, self._get_quartile(25), self._get_quartile(50), self._get_quartile(75))

    def _get_quartile(self, q):
        """Return the 25th, 50th or 75th based on Freund and Perles's method."""
        n = self.n
        if q == 50:
            idx = idx = (n - 1) // 2
            if not n % 2:
                return (self.seq[idx] + self.seq[idx + 1]) / 2
            else:
                return self.seq[idx]
        elif q == 25:
            idx = ((n + 3) / 4) - 1
        else:
            idx = (3 * n + 1) / 4 - 1
        frac, idx = modf(idx)
        idx = int(idx)
        return self.seq[idx] + (self.seq[idx + 1] - self.seq[idx]) * frac
