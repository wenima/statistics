"""Tests for https://www.codewars.com/kata/intro-to-statistics-part-1-a-five-figure-summary/python."""

import pytest

@pytest.fixture
def fiv_fig_summary_class():
    """Return a new instance of StatisticalSummary class."""
    from five_figure_summary import StatisticalSummary
    new_summary = StatisticalSummary(range(0, 7))
    return new_summary

def test_five_figure_summary(fiv_fig_summary_class):
    """Test that five_figure_summary returns correct values."""
    assert fiv_fig_summary_class.five_figure_summary(2) == (7, 0, 6, 1.5, 3, 4.5)
