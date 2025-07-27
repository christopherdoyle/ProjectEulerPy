import logging

from problems.lib import cli, main_wrapper
from problems.lib.math_ext import factorial, digits_to_int

logger = logging.getLogger(__name__)


@main_wrapper
def main():
    target = 1_000_000 - 1
    result = []
    n = target
    # keep track of all the digits --- we can only use each digit once!
    digits = list(range(10))
    # advance LTR along the number and put the biggest number we
    # can in that slot
    for i in range(0, 10):
        # how many permutations of the ith digit fits inside target?
        digits_index, n = divmod(n, factorial(10 - i - 1))
        # pop the digit, can't use it again
        digit = digits.pop(digits_index)
        result.append(digit)
    return digits_to_int(result)


if __name__ == "__main__":
    cli()
