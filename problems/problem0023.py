import logging


from problems.lib import cli, main_wrapper
from problems.lib.math_ext import properness

logger = logging.getLogger(__name__)


@main_wrapper
def main():
    # build a list of abundant numbers that could possible
    # be used to sum to another number within the known
    # range. not it is sorted ascending by construction.
    logger.info("Building list of abundant numbers")
    available_abundant_numbers = []
    for i in range(1, 28123 + 1):
        if properness(i) == 1:
            available_abundant_numbers.append(i)

    smallest_abundant_number = available_abundant_numbers[0]
    # given in problem statement
    assert smallest_abundant_number == 12

    logger.info(f"Found {len(available_abundant_numbers)} abundant numbers")

    logger.info("Finding abundant pairs in range")
    abundant_pairs = set()
    for i, a1 in enumerate(available_abundant_numbers):
        for a2 in available_abundant_numbers[i:]:
            if (x := a1 + a2) <= 21823:
                abundant_pairs.add(x)
            else:
                break

    return sum(i for i in range(1, 21823 + 1) if i not in abundant_pairs)


if __name__ == "__main__":
    cli()
