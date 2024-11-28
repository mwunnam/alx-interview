#!/usr/bin/python3
"""Locked Boxes"""


def canUnlockAll(boxes):
    """
    Functiont to find if all boxes can be unlocked
    param: boxes which will be a list of list
    return: True if all boxes can be unlocked
    """

    n = len(boxes)
    opened = [False] * n
    opened[0] = True

    keys = set(boxes[0])

    while keys:
        key = keys.pop()
        if 0 <= key < n and not opened[key]:
            opened[key] = True
            keys.update(boxes[key])

    return all(opened)
