"""Tests for https://www.codewars.com/kata/intro-to-statistics-part-2-boxplots"""

import pytest

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


@pytest.mark.parametrize("p, result", PERCENTILES)
def test_percentile(p, result):
    """Test that _percentile returns the boundary between the given quartile of
    sorted sequence of valid values.
    """
    from boxplots import StatisticalSummary
    stats_summary = StatisticalSummary(SEQUENCE)
    assert stats_summary._percentile(p) == result
