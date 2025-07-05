# Smallest Multiple
from problems.lib.math_ext import lcm


def find_smallest_multiple(n: int):
    """Finds the smallest number that is divisible by all numbers
    from 1..n (inclusive).
    """
    result = 1
    for i in range(2, n + 1):
        result = lcm(result, i)
    return result


print(find_smallest_multiple(20))
