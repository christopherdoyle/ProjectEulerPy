# Smallest Multiple
from problems.lib.math_ext import lcm
from problems.lib import cli, main_wrapper


def find_smallest_multiple(n: int):
    """Finds the smallest number that is divisible by all numbers
    from 1..n (inclusive).
    """
    result = 1
    for i in range(2, n + 1):
        result = lcm(result, i)
    return result


@main_wrapper
def main():
    return find_smallest_multiple(20)


if __name__ == "__main__":
    cli()
