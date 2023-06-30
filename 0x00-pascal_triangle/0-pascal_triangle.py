#!/usr/bin/python3
"""A function def pascal_triangle(n): that returns a
   list of lists of integers representing the Pascal’s triangle of
"""


def pascal_triangle(n):
    """
    List of lists of integers representing the Pascal triangle of n
    """
    if n <= 0:
        return []

    results = []
    for x in range(n):
        base = [1]
        for z in range(x):
            base.append(sum(results[-1][z:z+2]))
        results.append(base)
    return results
