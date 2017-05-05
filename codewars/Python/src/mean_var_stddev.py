"""Module for solution to
https://www.codewars.com/kata/mean-variance-and-standard-deviation-of-a-probability-distribution-for-discrete-variables."""


def stats_disc_distr(ll):
    """Return a list with 3 values, mean, var and standard deviation based on the input.
    The input is a list of lists and each list contains the value of a variable x
    and it's probability P(x)."""
    pass


def sanitize_input(ll):
    """Return an alert based on issues with dataset. Return None if no issue."""
    p = sum([l[1] for l in ll])
    if not all([l[0] == int(l[0]) for l in ll]):
        if p != 1:
            return "It's not a valid distribution and furthermore, one or more variable value are not integers"
        else:
            return "All the variable values should be integers"
    if p != 1:
        return "It's not a valid distribution"
