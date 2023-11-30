#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers 
    representing the Pascal’s triangle of n:
    """

    if n <= 0:
        return []

    
    """ initialize an empty resulting array """
    pascal = [[] for idx in range(n)]

    for lis in range(n):
        for col in range(lis+1):
            if(col < lis):
                if(col == 0):
                    """ the first column is always set to 1 """
                    pascal[lis].append(1)
                else:
                    pascal[lis].append(pascal[lis-1][col] + pascal[lis-1][col-1])
            elif(col == lis):
                """ the diagonal is always set to 1 """
                pascal[lis].append(1)

    return pascal
