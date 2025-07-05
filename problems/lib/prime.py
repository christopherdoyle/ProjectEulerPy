import math


def is_prime(n: int) -> bool:
    if n % 2 == 0:
        return False

    # vaguely more optimal search - just odd numbers
    for x in range(3, math.isqrt(n), 2):
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

    for i in range(2, math.isqrt(n) + 1):
        if a[i - 2]:
            j = i ** 2
            while j <= n:
                a[j - 2] = False
                j += i

    result = [i for i in range(2, n + 1) if a[i - 2]]
    return result


def nth_prime(n: int) -> int:
    if n < 1:
        raise ValueError("No")
    if n == 1:
        return 2

    i = 3
    found_primes = [2]

    while i < math.inf:
        # if i is not divisible by any of the primes we have found,
        # it must be prime
        sqrt_i = math.isqrt(i)

        is_i_prime = True
        for p in found_primes:
            if p > sqrt_i:
                # search finished
                break
            if i % p == 0:
                is_i_prime = False
                break

        if is_i_prime:
            found_primes.append(i)
            if len(found_primes) == n:
                return i
        i += 2
