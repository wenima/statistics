"""Tests for https://www.codewars.com/kata/variance-in-a-array-of-words/python."""

import pytest


TEST = [
    (['Hello', 'world'], 0),
    (['Hi', 'world'], 2.25),
]

@pytest.mark.parametrize("words, result", TEST)
def test_variance(words, result):
    """Test that function returns correct var."""
    from var_array_words import variance
    assert variance(words) == result
