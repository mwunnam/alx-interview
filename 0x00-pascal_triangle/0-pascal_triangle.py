#!/usr/bin/python3
"""
Pascal Triangle
"""


def pascal_triangle(n):
    """
    function to generate pascal's triangle
    Params: n (integer)
    Return: List
    """
    triangle = []
    if n <= 0:
        return triangle

    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            row.extend([last_row[j] + last_row[j + 1] for j in range(
                       len(last_row) - 1)])
            row.append(1)
        triangle.append(row)
    return triangle