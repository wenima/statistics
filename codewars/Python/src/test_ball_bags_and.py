"""Tests for https://www.codewars.com/kata/statistics-in-kata-2-and-case-ball-bags."""

import pytest


TEST = [
    ([["red","blue","yellow","green","red","blue","yellow","green","red","blue"],["red","blue"],True], 0.090),
    ([["red","blue","yellow","green","red","blue","yellow","green","red","blue"],["red","red"],True], 0.090),
    ([["red","red","yellow","green","red","red","yellow","green","red","red"],["blue","blue"],True], 0),
    ([["red","blue","yellow","green","red","blue","yellow","green","red","blue"],["red","blue"],False], 0.100),
    ([["red","blue","yellow","green","red","blue","yellow","green","red","blue"],["red","red"],False], 0.067),
]

@pytest.mark.parametrize("d6, n1, n2, result", TEST)
def test_ball_probability(balls, result):
    """Test that function returns correct probability."""
    from ball_bags_and import ball_probability
    assert ball_probability(balls) == result
