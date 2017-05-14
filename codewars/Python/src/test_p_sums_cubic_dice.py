"""Tests for https://www.codewars.com/kata/probabilities-for-sums-in-rolling-cubic-dice"""

import pytest

TEST = [
    (11, 2, 0.0555555555),
    (8, 2, 0.1388888888),
    (8, 3, 0.0972222222222),
    (22, 3, 0),
]


@pytest.mark.parametrize("target_sum, no_of_dice, result", TEST)
def test_rolldice_sum_prob(target_sum, no_of_dice, result):
    """Test that function returns correct tuple of intercept and slope."""
    from p_sums_cubic_dice import rolldice_sum_prob
    assert rolldice_sum_prob(target_sum, no_of_dice) == pytest.approx(result)
