#!/usr/bin/python3
'''Function to calculate the perimeter of an island'''


def island_perimeter(grid):
    '''
        Function is to calculate the perimeter of an island
        para: grid - A 2 dimentional list
        Return: The parameter of the island
    '''
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                '''Each land cell has an initial of perieter 4'''
                perimeter += 4

                '''Checking for cell above'''
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

                '''Checking for cell on the left'''
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
