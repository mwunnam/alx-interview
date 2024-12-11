#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """
    Function that finds the minimum operation to acheive the target
    Args: n - interger
    Returns: operations - interger
    """

    if n < 0:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor

        divisor += 1

    return operations
