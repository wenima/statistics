"""Tests for https://www.codewars.com/kata/tracking-hits-for-different-sum-values-for-different-kinds-of-dice."""

import pytest

TEST = [
    (3, 4, [[3, 1], [4, 3], [5, 6], [6, 10], [7, 12], [8, 12], [9, 10], [10, 6], [11, 3], [12, 1]]),
    (4, 4, [
            [4, 1], [5, 4], [6, 10], [7, 20], [8, 31], [9, 40], [10, 44], [11, 40], [12, 31], [13, 20],
            [14, 10], [15, 4], [16, 1]
            ]),
    (3, 6, [
            [3, 1], [4, 3], [5, 6], [6, 10], [7, 15], [8, 21], [9, 25], [10, 27], [11, 27], [12, 25],
            [13, 21], [14, 15], [15, 10], [16, 6], [17, 3], [18, 1]
            ]),
    (4, 6, [
            [4, 1], [5, 4], [6, 10], [7, 20], [8, 35], [9, 56], [10, 80], [11, 104], [12, 125],
            [13, 140], [14, 146], [15, 140], [16, 125], [17, 104], [18, 80],
            [19, 56], [20, 35], [21, 20], [22, 10], [23, 4], [24, 1]
            ]),
]


@pytest.mark.parametrize("no_of_dice, sides, result", TEST)
def test_reg_sum_hits(no_of_dice, sides, result):
    """Test that function returns correct tuple of intercept and slope."""
    from tracking_hits_different_dice import reg_sum_hits
    assert reg_sum_hits(no_of_dice, sides) == result
