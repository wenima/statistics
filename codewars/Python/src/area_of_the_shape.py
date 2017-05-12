"""Module for solution to https://www.codewars.com/kata/area-of-a-shape."""

import numpy as np

def area_of_the_shape(f):
    """Return a number representing the area of an unknown shape inside a given square."""
    count = 0
    n = 10000
    for _ in range(n):
        x = np.random.random()
        y = np.random.random()
        if f(x, y): count += 1
    return 1 * count / n
