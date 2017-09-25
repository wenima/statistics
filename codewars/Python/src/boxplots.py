"""Solution for https://www.codewars.com/kata/intro-to-statistics-part-2-boxplots/."""

from math import ceil, floor
from numbers import Real
from bisect import bisect_left, bisect_right

BOXPLOT = 'BOXPLOT'

class StatisticalSummary(object):
    """Class which contains a various statistical methods.

    n: number of valid numeric values in sequence
    lower extreme EL: smallest value in n
    upper extreme EU: largest value in n
    median: centre value of sorted sequence
    lower quartile Q1: boundary value between 1st and 2nd quarters of a sorted sequence
    upper quartile Q3: boundary value between 3rd and 4th quarters of a sorted sequence
    first decile D1: boundary value between the 1st and 2nd tenths of a sorted sequence
    last decile D9: boundard value between the 9th and 10th tenths of a sorted sequence
    inter quartile range IQR: Q3 - Q1
    lower outlier boundary OL: smallest value > M - 1.5 * IQR
    largest outlier boundard OU: largest value < M + 1.5 * IQR
    """

    def __init__(self, seq):
        self.seq = sorted([x for x in seq if isinstance(x, Real)])
        self.n = len(self.seq)

    def _percentile(self, p):
        """Return the boundary between the given quartile of sorted sequence of
        valid values.
        """
        seq = self.seq
        k = (len(seq) - 1) * p; f = floor(k); c = ceil(k)
        return seq[int(k)] if f == c else seq[int(f)] * (c-k) + seq[int(c)] * (k-f)

    def _get_outlier_boundary(self, boundary=None, direction='left'):
        """Return the index of the outlier boundary given direction."""
        if direction == 'right':
            return bisect_right(self.seq, boundary)
        elif direction == 'left':
            return bisect_left(self.seq, boundary)

    def boxplot(self, plot=BOXPLOT, precision=None):
        """Return a tuple of values to be consumed by a function to draw a type
        of Boxplot.

        plot=BOXPLOT: Return Q1, median, upper quartile Q3
        plot=BOX_AND_WHISKER: and whisker plot: Return EL, Q1, median, Q3, EL
        plot=BOX_AND_DECILE_WHISKER: Return x, D1, Q1, median, Q3, D9, y where x are
        all values below D1 and y are all values above D9
        plot=TUKEY_BOX_AND_WHISKER: Return x, OL, Q1, median, Q3, OU, y where x are
        all values below QL and y are all values above OU
        """

        q1, median, q3 = self._percentile(.25), self._percentile(.5), self._percentile(.75)
        d1, d9 = self._percentile(.1), self._percentile(.9)
        el, eu = min(self.seq), max(self.seq)
        iqr = q3 - q1
        ol = ceil((median - 1.5 * iqr))
        ou = floor((median + 1.5 * iqr))


        if plot == 'BOXPLOT':
            return 'Sample', q1, median, q3
        elif plot == 'BOX_AND_WHISKER':
            return 'Sample', el, q1, median, q3, eu
        elif plot == 'BOX_AND_DECILE_WHISKER':
            return 'Sample', self.seq[:ceil((len(self.seq) - 1) * .1 )], d1, q1, median, q3, d9, self.seq[ceil((len(self.seq) - 1) * .9):]
        elif plot == 'TUKEY_BOX_AND_WHISKER':
            ou_idx = self._get_outlier_boundary(boundary=ou, direction='right')
            ol_idx = self._get_outlier_boundary(boundary=ol, direction='left')
            return 'Sample', self.seq[:ol_idx], ol, q1, median, q3, ou, self.seq[ou_idx:]
