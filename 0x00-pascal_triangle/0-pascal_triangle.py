#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascals triangle"""

    if n <= 0:
        return []

    # Initialize an empty resulting array
    pascal = [[] for idx in range(n)]

    for lis in range(n):
        for col in range(lis + 1):
            if col < lis:
                if col == 0:
                    # The first column is always set to 1
                    pascal[lis].append(1)
                else:
                    # Calculate and append value to the current row
                    val = pascal[lis - 1][col] + pascal[lis - 1][col - 1]
                    pascal[lis].append(val)
            elif col == lis:
                # The diagonal is always set to 1
                pascal[lis].append(1)

    return pascal
