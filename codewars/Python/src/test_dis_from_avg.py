"""Tests for https://www.codewars.com/kata/distance-from-the-average."""

import pytest


TEST = [
    ([55, 95, 62, 36, 48], [4.2, -35.8, -2.8, 23.2, 11.2]),
    ([1, 1, 1, 1, 1], [0, 0, 0, 0, 0]),
    ([1, -1, 1, -1, 1, -1], [-1.0, 1.0, -1.0, 1.0, -1.0, 1.0]),
    ([1, -1, 1, -1, 1], [-0.8, 1.2, -0.8, 1.2, -0.8]),
    ([2, -2], [-2.0, 2.0]),
    ([1], [0]),
    ([123, -65, 32432, -353, -534], [6197.6, 6385.6, -26111.4, 6673.6, 6854.6]),
]


@pytest.mark.parametrize("l, result", TEST)
def test_distances_from_average(l, result):
    """Test that distances_from_average returns absolute distances to average."""
    from dist_from_avg import distances_from_average
    assert distances_from_average(n) == result
