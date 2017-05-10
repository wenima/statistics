"""Module for solution to https://www.codewars.com/kata/variance-in-a-array-of-words/python."""


from numpy import var


def variance(words):
    """Consider X as the aleatory variable that count the number of letters in a
    word. Write a function that, given an array of words (strings),
    calculate the variance of X. Max decimal of the variance : 4"""
    return round(var([len(word) for word in words]), 4)
