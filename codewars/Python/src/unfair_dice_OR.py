"""Module for solution to https://www.codewars.com/kata/statistics-in-kata-1-or-case-unfair-dice."""


def mutually_exclusive(d6, n1, n2):
    """Return 2 strings, the first containing the probability of either n1 or n2
    being rolled and the second stating the expected outcome or issue with the input."""
    pass


def sanitize_input(d6):
    """Return an alert based on issues with dataset. Return None if no issue."""
    p = sum([l[1] for l in d6])
    if round(p, 5) != 1:
        return "Check the total probability")
