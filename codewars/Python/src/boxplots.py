"""Solution for https://www.codewars.com/kata/intro-to-statistics-part-2-boxplots/."""

from math import ceil, floor
from numbers import Real

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

    def boxplot(self, plot=BOXPLOT, precision=None):
        """Return a tuple of values to be consumed by a function to draw a type
        of Boxplot.

        plot=BOXPLOT: Return Q1, median, upper quartile Q3
        plot=BOX_AND_WHISKER: and whisker plot: Return EL, Q1, median, Q3, EL
        plot=BOX_AND_DECILE_WHISKER: Return x, D1, Q1, median, D9, y where x are
        all values below D1 and y are all values above D9
        plot=TUKEY_BOX_AND_WHISKER: Return x, OL, Q1, median, Q3, OU, y where x are
        all values below QL and y are all values above OU
