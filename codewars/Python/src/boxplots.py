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
        seq = list(seq)
        self.labels = []
        try:
            self.labels = set([x[0] for x in seq])
        except TypeError:
            self.seq = sorted([x for x in seq if isinstance(x, Real)])
            self.n = len(self.seq)
        if len(self.labels) > 1:
            self.sequences = list(self.labels)
            self.sequences.sort()
            self.seq = []
            for label in self.sequences:
                self.seq.append((label, [x[1] for x in seq if x[0] == label and isinstance(x[1], Real)]))

    def _percentile(self, p, seq):
        """Return the boundary between the given quartile of sorted sequence of
        valid values.
        """
        k = (len(seq) - 1) * p; f = floor(k); c = ceil(k)
        return seq[int(k)] if f == c else seq[int(f)] * (c-k) + seq[int(c)] * (k-f)

    def _get_outlier_boundary(self, seq, boundary=None, direction='left'):
        """Return the index of the outlier boundary given direction."""
        print(seq, boundary)
        if direction == 'right':
            return bisect_right(seq, boundary)
        elif direction == 'left':
            return bisect_left(seq, boundary)

    def _get_boxplot_values(self, seq, plot=BOXPLOT, identifier='Sample'):
        """Return a tuple of values to be consumed by a function to draw a type
        of Boxplot.

        plot=BOXPLOT: Return Q1, median, upper quartile Q3
        plot=BOX_AND_WHISKER: and whisker plot: Return EL, Q1, median, Q3, EL
        plot=BOX_AND_DECILE_WHISKER: Return x, D1, Q1, median, Q3, D9, y where x are
        all values below D1 and y are all values above D9
        plot=TUKEY_BOX_AND_WHISKER: Return x, OL, Q1, median, Q3, OU, y where x are
        all values below QL and y are all values above OU
        """

        q1, median, q3 = self._percentile(.25, seq), self._percentile(.5, seq), self._percentile(.75, seq)
        d1, d9 = self._percentile(.1, seq), self._percentile(.9, seq)
        el, eu = min(seq), max(seq)
        iqr = q3 - q1
        ol = ceil((median - 1.5 * iqr))
        ou = floor((median + 1.5 * iqr))

        if plot == 'BOXPLOT':
            return 'Sample', q1, median, q3
        elif plot == 'BOX_AND_WHISKER':
            return 'Sample', el, q1, median, q3, eu
        elif plot == 'BOX_AND_DECILE_WHISKER':
            return 'Sample', seq[:ceil((len(seq) - 1) * .1 )], d1, q1, median, q3, d9, seq[ceil((len(seq) - 1) * .9):]
        elif plot == 'TUKEY_BOX_AND_WHISKER':
            ou_idx = self._get_outlier_boundary(seq, boundary=ou, direction='right')
            ol_idx = self._get_outlier_boundary(seq, boundary=ol, direction='left')
            print(ou_idx)
            print(ol_idx)
            return identifier, seq[:ol_idx], ol, q1, median, q3, ou, seq[ou_idx:]


    def boxplot(self, plot=BOXPLOT, precision=None):
        """Return the result of call to _get_boxplot_values and round if precision is given."""

        if len(self.labels) > 1:
            out = []
            for seq in self.seq:
                out.append(self._get_boxplot_values(seq[1], plot, seq[0]))
                print(out)
            return out
        return self._get_boxplot_values(self.seq, plot)
