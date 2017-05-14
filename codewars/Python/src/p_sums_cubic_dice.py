"""Module for solution to https://www.codewars.com/kata/probabilities-for-sums-in-rolling-cubic-dice."""

from itertools import product

def rolldice_sum_prob(target_sum, no_of_dice):
    """Return a number representing the probability of rolling a number equal to
    target_sum with a given number of dice."""
    die = [1, 2, 3, 4, 5, 6]
    dice = [die for i in range(no_of_dice)]
    rolls = [pr for pr in product(*dice) if sum(pr) == target_sum]
    return len(rolls) / len(dice[0]) ** len(dice)
