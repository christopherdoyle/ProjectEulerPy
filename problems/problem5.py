# Smallest Multiple
import logging
from functools import reduce
from itertools import chain
from operator import mul

from lib.logging import setup as logging_setup
from lib.prime import sieve_of_eratosthenes


logger = logging.getLogger(__name__)


def find_smallest_multiple(n: int):
    """Finds the smallest number that is divisible by all numbers
    from 1..n (inclusive).
    """
    primes_in_range = sieve_of_eratosthenes(n)
    composites_in_range = [
        # start from 4 because 1 is a dud, 2 and 3 are prime
        i for i in range(4, n + 1)
        if i not in primes_in_range
    ]
    upper_limit = reduce(mul, range(1, n + 1), 1)
    logger.info(f"Searching up to upper limit {upper_limit}")

    candidate = n
    while candidate <= upper_limit:
        # slightly more efficient to check for prime divisible first?
        for i in chain(primes_in_range, composites_in_range):
            if candidate % i:
                break
        else:
            # we didn't hit a break, therefore success
            return candidate
        candidate += 1

    raise AssertionError("Math failed")


logging_setup()
print(find_smallest_multiple(20))
