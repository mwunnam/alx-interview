#!/usr/bin/python3
"""Function to Rotate a n x n matrix 90 degress clockwise"""


def rotate_2d_matrix(matrix):
    """Function that rotates a n x n 2D matrix 90 degrees clockwise"""
    n = len(matrix)

    def rotate_layer(i):
        """Function that will do the rotation"""
        for j in range(i, n - i - 1):
            top = matrix[i][j]

            """Move Left to Top"""
            matrix[i][j] = matrix[n - 1 - j][i]

            """Move Bottom to Left"""
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]

            """Move Right to Bottom"""
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]

            """Move Top to Right"""
            matrix[j][n - 1 - i] = top

    for i in range(n // 2):
        rotate_layer(i)
