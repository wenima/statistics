"""Tests for https://www.codewars.com/kata/intro-to-statistics-part-1-a-five-figure-summary/python."""


class StatisticalSummary(object):
    """Class which contains a method to return six figure version of the five number summary
    https://en.wikipedia.org/wiki/Five-number_summary.
    """

    def __init__(self, seq):
        self.seq = seq
        self.seq = sorted([x for x in seq])

    def five_figure_summary(self, precision=None):
        """Return number of valid samples, lower extreme, upper extreme, lower
        quartile, median, and upper quartile.
        """

        n = len(self.seq)
        low = min(self.seq)
        high = max(self.seq)

        median_idx = median_idx = (len(self.seq) - 1) // 2
        if not len(self.seq) % 2:
            median = (self.seq[median_idx] + self.seq[median_idx + 1]) / 2
        else:
            median = self.seq[median_idx]

        lq_idx = int(median_idx) // 2
        if len(self.seq) % 2:
            lq = (self.seq[lq_idx] + self.seq[lq_idx + 1]) / 2
        else:
            lq = self.seq[lq_idx]

        uq_idx = (median_idx + len(self.seq) - 1) // 2
        if len(self.seq) % 2:
            uq = (self.seq[uq_idx] + self.seq[uq_idx + 1]) / 2
        else:
            uq = self.seq[uq_idx]

        return (n, low, high, lq, median, uq)
