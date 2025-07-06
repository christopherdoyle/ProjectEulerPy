import logging

from problems.lib import main_wrapper

logger = logging.getLogger(__name__)


def is_pythagorean_triplet(a, b, c):
    return (a**2) + (b**2) == c**2


def find():
    for a in range(1, 999):
        for b in range(1, 999):
            c = 1000 - a - b
            if is_pythagorean_triplet(a, b, c):
                return a, b, c


@main_wrapper
def main():
    a, b, c = find()
    logger.info(f"Found Pythagorean triplet: a={a}, b={b}, c={c}")
    return a * b * c
