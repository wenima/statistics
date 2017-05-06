"""Tests for https://www.codewars.com/kata/statistics-in-kata-1-or-case-unfair-dice."""

import pytest


TEST = [
    (([[3,0.4],[4,0.1],[1,0.01],[2,0.09],[5,0.2],[6,0.1]],1,6, (None, "Check the total probability")),
    ([[1,0.1],[2,0.14],[3,0.16],[4,0.2],[5,0.15],[6,0.25]],1,4), ("0.30", "Expected 0.30")),
    ([[1,0.6],[2,0.1001],[3,0.0999],[4,0.1],[5,0.05],[6,0.05]],3,4), ("0.20", "Expected 0.20")),
    ([[6,0.25],[1,0.1],[3,0.16],[2,0.14],[5,0.15],[4,0.2]],1,6), ("0.35", "Expected 0.35")),
    ([[3,0.4],[4,0.1],[1,0.01],[2,0.09],[5,0.2],[6,0.2]],1,6), ("0.21", "Expected 0.21")),
]

INVALID = [
    ([[3,0.4],[4,0.1],[1,0.01],[2,0.09],[5,0.2],[6,0.1]], "Check the total probability"),
]


@pytest.mark.parametrize("d6, n1, n2, result", TEST)
def test_mutually_exclusive(d6, n1, n2, result):
    """Test that function returns correct probability."""
    from unfair_dice_OR import mutually_exclusive
    assert mutually_exclusive(d6, n1, n2) == result


@pytest.mark.parametrize("d6, result", INVALID)
def test_sanitize_input(d6, result):
    """Test that function returns correct warning based on invalid input."""
    from unfair_dice_OR import sanitize_input
    assert sanitize_input(d6) == result
