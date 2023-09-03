#!/usr/bin/python3
import sys


def factorize(number):
    """
    Take a number
    Args:
        number: integer
        Return: A tuple of two factors if number is pair.
            None if the number is prime
    """
    """ Print the number that beigng factorized """
    for i in range(2, int((number**0.5) + 1)):
        if number % i == 0:
            factors = (i, number // i)
            return factors
    """ Print a message if no factors were found """
    return None
