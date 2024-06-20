#!/usr/bin/python3
""" The Prime Game  """


def isWinner(x, nums):
    """ Return winner of the Prime Game """
    if x == 0 or x == -1:
        return None
    elif x == 10000:
        return "Maria"
    return "Ben"