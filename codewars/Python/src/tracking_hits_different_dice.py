"""Module for solution to https://www.codewars.com/kata/tracking-hits-for-different-sum-values-for-different-kinds-of-dice."""

from itertools import product

def reg_sum_hits(no_of_dice, sides):
    """Return a list of list containing the sum value and the number of hits for
    given number of dice of given sides."""
    die = [x for x in range(1, sides + 1)]
    hits = []
    for sum_roll in range(no_of_dice, no_of_dice * sides + 1):
        hits.append([sum_roll, len([pr for pr in product(die, repeat=no_of_dice) if sum(pr) == sum_roll])])
    return hits

from collections import Counter

def reg_sum_hits_pythonic(n,s):
    return sorted([k,v] for k,v in Counter(map(sum,product(range(1,s+1),repeat=n))).items())
