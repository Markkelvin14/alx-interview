#!/usr/bin/python3
""" Island Perimeter """


def island_perimeter(grid):
    """ return the perimeter of the island described in grid """
    total_perimeter = 0

    for m, row in enumerate(grid):
        for k, element in enumerate(row):
            # Check if element is land or sea
            if (element == 0):
                continue

            if (k != 0 and row[k - 1] == 0):
                total_perimeter += 1
            if (k == 0):
                total_perimeter += 1

            if (k != len(row) - 1 and row[k + 1] == 0):
                total_perimeter += 1
            if (k == len(row) - 1):
                total_perimeter += 1

            if (m != 0 and grid[m - 1][k] == 0):
                total_perimeter += 1
            if (m == 0):
                total_perimeter += 1

            if (m != len(grid) - 1 and grid[m + 1][k] == 0):
                total_perimeter += 1
            if (m == len(grid) - 1):
                total_perimeter += 1

    return total_perimeter
