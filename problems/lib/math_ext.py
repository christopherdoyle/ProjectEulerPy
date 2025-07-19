from functools import reduce
from operator import mul


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
