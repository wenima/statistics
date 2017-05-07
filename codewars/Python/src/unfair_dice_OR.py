"""Module for solution to https://www.codewars.com/kata/statistics-in-kata-1-or-case-unfair-dice."""


def mutually_exclusive(d6, n1, n2):
    """Return a string containing the probability of either n1 or n2 being rolled
    or None if input is invalid."""
    out = sanitize_input(d6)
    if out:
        return None
    p = round(sum([side[1] for side in d6 if side[0] in [n1, n2]]), 2)
    return '{:.2f}'.format(p)


def sanitize_input(d6):
    """Return an alert based on issues with dataset. Return None if no issue."""
    p = sum([l[1] for l in d6])
    if round(p, 5) != 1:
        return "Check the total probability"
