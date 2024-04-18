#!/usr/bin/python3
""" You own n number of locked boxes in front of you. Each box has a number
sequentially from 0 to n - 1 and each box may contain keys to other boxes.
"""


def canUnlockAll(boxes):
    """ Write a method that determin if all boxes can be opened.
    @boxes is a list of the lists
    """
    keys = [0]
    for n in keys:
        for key in boxes[n]:
            if key not in keys and key < len(boxes):
                keys.append(key)
    return len(keys) == len(boxes)
