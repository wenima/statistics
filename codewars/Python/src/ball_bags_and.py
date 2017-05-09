"""Module for solution to https://www.codewars.com/kata/statistics-in-kata-2-and-case-ball-bags."""

from collections import defaultdict

def ball_probability(balls):
    """Return a float representing the probability of drawing 2 balls out of a bag
    with 10 balls matching the color of 2 given balls."""
    d = defaultdict(int)
    bag, given_balls, putback = balls
    ball1, ball2 = given_balls

    for ball in bag:
        d[ball] += 1

    p_ball1 = float(d[ball1] / len(bag))
    if not putback:
        d[ball1] -= 1
    p_ball2 = float(d[ball2] / (len(bag) - 0 if putback else len(bag) - 1))
    p_ball1_and_ball2 = p_ball1 * p_ball2
    return round(p_ball1_and_ball2, 3)
