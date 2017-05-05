"""Tests for
https://www.codewars.com/kata/mean-variance-and-standard-deviation-of-a-probability-distribution-for-discrete-variables."""

import pytest


TEST = [
    [[0, 0.125], [1, 0.375], [2, 0.375], [3, 0.125]], [1.5, 0.75, 0.8660254037844386]),
]


@pytest.mark.parametrize("ll, result", TEST)
def test_stats_disc_distr(ll, result):
    """Test that function returns correct mean, var and stddev."""
    from mean_var_stddev import stats_disc_distr
    assert stats_disc_distr(ll) == result
