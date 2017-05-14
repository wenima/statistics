"""Tests for https://www.codewars.com/kata/tracking-hits-for-different-sum-values-for-different-kinds-of-dice."""

import pytest

TEST = [
    (3, 4, [[3, 1], [4, 3], [5, 6], [6, 10], [7, 12], [8, 12], [9, 10], [10, 6], [11, 3], [12, 1]])
]


@pytest.mark.parametrize("target_sum, no_of_dice, result", TEST)
def test_reg_sum_hits(no_of_dice, sides, result):
    """Test that function returns correct tuple of intercept and slope."""
    from tracking_hits_different_dice import reg_sum_hits
    assert reg_sum_hits(no_of_dice, sides) == result
