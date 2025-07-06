import logging

from problems.lib import cli, main_wrapper

logger = logging.getLogger(__name__)

_LEN_CACHE = {1: 1}


def collatz(n: int) -> int:
    if n % 2 == 0:
        return n // 2
    else:
        return (3 * n) + 1


def len_of_collatz_sequence(n: int) -> int:
    if n in _LEN_CACHE:
        return _LEN_CACHE[n]
    else:
        result = 1 + len_of_collatz_sequence(collatz(n))
        _LEN_CACHE[n] = result
        return result


@main_wrapper("Largest Collatz Sequence")
def main():
    length_of_longest_sequence = 1
    n_of_longest_sequence = 1
    for n in range(1, 1_000_000):
        length_of_sequence = len_of_collatz_sequence(n)
        if length_of_sequence > length_of_longest_sequence:
            length_of_longest_sequence = length_of_sequence
            n_of_longest_sequence = n

    logger.info(
        f"Longest collatz sequence: {length_of_longest_sequence} (starting number {n_of_longest_sequence})"
    )
    return n_of_longest_sequence


if __name__ == "__main__":
    cli()
