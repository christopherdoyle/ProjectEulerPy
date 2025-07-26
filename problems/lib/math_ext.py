import math

from functools import reduce
from operator import mul
from typing import Literal, Iterator


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def prod(xs) -> int:
    return reduce(mul, xs, 1)


def big_sum_digits(x: int) -> int:
    # avoiding str, because.
    def digits(n):
        while n:
            n, r = divmod(n, 10)
            yield r

    return sum(digits(x))


def proper_divisors(x: int) -> Iterator[int]:
    if x <= 0:
        raise NotImplementedError("Require x>0")

    yield 1

    if x == 1:
        return

    sqrt_x = math.isqrt(x)
    for i in range(2, sqrt_x + 1):
        quot, rem = divmod(x, i)
        if rem == 0:
            yield i
            if quot != i:
                yield quot


def properness(x: int) -> Literal[-1, 0, 1]:
    """Analyzes the "properness" of the given number, returning
    0 if it is a proper number, -1 if it is a deficient number,
    and +1 if it is an abundant number.
    """
    sum_of_proper_divisors = sum(proper_divisors(x))
    if sum_of_proper_divisors < x:
        return -1
    elif sum_of_proper_divisors > x:
        return 1
    else:
        return 0
