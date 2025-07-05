import math


def is_prime(n: int) -> bool:
    if n % 2 == 0:
        return False

    # vaguely more optimal search - just odd numbers
    for x in range(3, math.floor(math.sqrt(n)), 2):
        if n % x == 0:
            return False

    return True


def sieve_of_eratosthenes(n: int) -> list[int]:
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Pseudocode
    if n < 0:
        raise ValueError("No")
    if n == 0 or n == 1:
        return []
    if n == 2:
        return [2]

    # represents if integers 2..n are prime
    a = [True] * (n - 1)

    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if a[i - 2]:
            j = i ** 2
            while j <= n:
                a[j - 2] = False
                j += i

    result = [i for i in range(2, n + 1) if a[i - 2]]
    return result
