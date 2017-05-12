"""Tests for https://www.codewars.com/kata/area-of-a-shape."""

import pytest


TEST = [
    (circular_area - 0.25 * math.pi, EPSILON)
    (full_shape - 1, EPSILON),
]



@pytest.mark.parametrize("f, result", TEST)
def test_area_of_the_shape(f, result):
    """Test that function returns correct probability."""
    from area_of_the_shape import area_of_the_shape
    assert area_of_the_shape(f) <= result
