"""Tests for
https://www.codewars.com/kata/mean-variance-and-standard-deviation-of-a-probability-distribution-for-discrete-variables."""

import pytest


TEST = [
    ([[0, 0.125], [1, 0.375], [2, 0.375], [3, 0.125]], [1.5, 0.75, 0.8660254037844386]),
    ([[0.0, 0.125], [1.0, 0.375], [2.0, 0.375], [3, 0.125]], [1.5, 0.75, 0.8660254037844386]),
    ([[0.1, 0.425], [1.1, 0.375], [2, 0.375], [3, 0.125]], "It's not a valid distribution and furthermore, one or more variable value are not integers"),
]

INVALID = [
    ([[0, 0.425], [1, 0.375], [2, 0.375], [3, 0.125]], "It's not a valid distribution"),
    ([[0.1, 0.125], [1.1, 0.375], [2, 0.375], [3, 0.125]], "All the variable values should be integers"),
    ([[0.1, 0.425], [1.1, 0.375], [2, 0.375], [3, 0.125]], "It's not a valid distribution and furthermore, one or more variable value are not integers"),
]


@pytest.mark.parametrize("ll, result", TEST)
def test_stats_disc_distr(ll, result):
    """Test that function returns correct mean, var and stddev."""
    from mean_var_stddev import stats_disc_distr
    assert stats_disc_distr(ll) == result


@pytest.mark.parametrize("ll, result", INVALID)
def test_sanitize_input(ll, result):
    """Test that function returns correct warning based on invalid input."""
    from mean_var_stddev import sanitize_input
    assert sanitize_input(ll) == result
