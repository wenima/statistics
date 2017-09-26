"""Tests for https://www.codewars.com/kata/intro-to-statistics-part-2-boxplots"""

import pytest
from itertools import chain

BOXPLOT = 'BOXPLOT'
BOX_AND_WHISKER = 'BOX_AND_WHISKER'
BOX_AND_DECILE_WHISKER = 'BOX_AND_DECILE_WHISKER'
TUKEY_BOX_AND_WHISKER = 'TUKEY_BOX_AND_WHISKER'

SEQUENCE = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 12, 13, 14, 15, 16, 17, 18, 19,
    20, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    12, 13, 14, 15, 16, 17, 18, 19, 20, 16
    ]


PERCENTILES = [
    (0.25, 12.75),
    (0.5, 16),
    (0.75, 20),
    (0.1, 6.9),
    (.9, 26.1),
]

BOXPLOTS = [
    (BOXPLOT, SEQUENCE, ('Sample', 12.75, 16, 20)),
    (BOX_AND_WHISKER, SEQUENCE, ('Sample', 1, 12.75, 16, 20, 32)),
    (BOX_AND_DECILE_WHISKER, SEQUENCE, ('Sample', [1, 2, 3, 4, 5, 6], 6.9, 12.75, 16, 20, 26.1, [27, 28, 29, 30, 31, 32])),
    (TUKEY_BOX_AND_WHISKER, SEQUENCE, ('Sample', [1, 2, 3, 4, 5], 6, 12.75, 16, 20, 26, [27, 28, 29, 30, 31, 32])),
]

BOXPLOTS_2D = [
    (BOXPLOT, [('A', 12.75, 16, 20), ('B', 13.75, 17, 21)]),
    (BOX_AND_WHISKER, [('A', 1, 12.75, 16, 20, 32), ('B', -1, 13.75, 17, 21, 34)]),
    (BOX_AND_DECILE_WHISKER, [
                                ('A', [1, 2, 3, 4, 5, 6], 6.9, 12.75, 16, 20, 26.1, [27, 28, 29, 30, 31, 32]),
                                ('B', [-1, 0, 1, 2, 3, 4], 4.9, 13.75, 17, 21, 24.1, [25, 26, 27, 28, 33, 34])
                            ]),
    (TUKEY_BOX_AND_WHISKER, [
                                ('A', [1, 2, 3, 4, 5], 6, 12.75, 16, 20, 26, [27, 28, 29, 30, 31, 32]),
                                ('B', [-1, 0, 1, 2, 3, 4, 5, 6], 7, 13.75, 17, 21, 27, [28, 33, 34])
                            ]),
]

@pytest.fixture
def stats_summary():
    """Return a new instance of StatisticalSummary class."""
    from boxplots import StatisticalSummary
    d2 = chain([d - 2 for d in SEQUENCE[:len(SEQUENCE)//2]], [d + 2 for d in SEQUENCE[len(SEQUENCE)//2:]])
    data = chain([("A", n) for n in SEQUENCE], [("B", n) for n in d2])
    new_summary = StatisticalSummary(data)
    return new_summary

@pytest.mark.parametrize("p, result", PERCENTILES)
def test_percentile(p, result):
    """Test that _percentile returns the boundary between the given quartile of
    sorted sequence of valid values.
    """
    from boxplots import StatisticalSummary
    stats_summary = StatisticalSummary(SEQUENCE)
    assert stats_summary._percentile(p, stats_summary.seq) == result

@pytest.mark.parametrize("boxplot_type, seq, result", BOXPLOTS)
def test_boxplot(boxplot_type, seq, result):
    """Test that boxplot returns correct sample data based on type of boxplot passed in."""
    from boxplots import StatisticalSummary
    stats_summary = StatisticalSummary(seq)
    assert stats_summary.boxplot(boxplot_type) == result

@pytest.mark.parametrize("boxplot_type, result", BOXPLOTS_2D)
def test_boxplot_2d(stats_summary, boxplot_type, result):
    assert stats_summary.boxplot(boxplot_type) == result
