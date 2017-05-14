"""Tests for https://www.codewars.com/kata/linear-regression-of-y-on-x"""

import pytest

TEST = [
    ([25,30,35,40,45,50], [78,70,65,58,48,42], (114.381, -1.4457)),
    ([56,42,72,36,63,47,55,49,38,42,68,60], [147,125,160,118,149,128,150,145,115,140,152,155], (80.7777, 1.138)),
]


@pytest.mark.parametrize("x, y, result", TEST)
def test_regressionLine(x, y, result):
    """Test that function returns correct tuple of intercept and slope."""
    from linear_regression import regressionLine
    assert regressionLine(x, y) == result

@pytest.mark.parametrize("x, y, result", TEST)
def test_regressionLine_numpy(x, y, result):
    """Test that function returns correct tuple of intercept and slope."""
    from linear_regression import regressionLine_numpy
    assert regressionLine_numpy(x, y) == result


@pytest.mark.parametrize("x, y, result", TEST)
def test_regressionLine_scipy(x, y, result):
    """Test that function returns correct tuple of intercept and slope."""
    from linear_regression import regressionLine_scipy
    assert regressionLine_scipy(x, y) == result
