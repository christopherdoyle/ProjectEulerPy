# Sum Square Difference
from problems.lib import cli, main_wrapper


def sum_of_squares(n):
    return sum(i**2 for i in range(1, n + 1))


def square_of_sum(n):
    sum_to_n = int((n * (n + 1)) / 2)
    return sum_to_n**2


@main_wrapper
def main():
    return abs(sum_of_squares(100) - square_of_sum(100))


if __name__ == "__main__":
    cli()
