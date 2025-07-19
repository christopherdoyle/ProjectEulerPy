from problems.lib import cli, main_wrapper
from problems.lib.math_ext import big_sum_digits


def factorial(x: int):
    # recursion is foolish
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result


@main_wrapper
def main():
    return big_sum_digits(factorial(100))


if __name__ == "__main__":
    cli()
