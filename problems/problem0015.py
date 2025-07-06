"""The trivial mathemtical solution is from 40 choose 20,
but that is boring.
"""

import logging

from problems.lib import cli, main_wrapper

logger = logging.getLogger(__name__)

_CACHE = {}


def count_routes_from_origin(x: int, y: int) -> int:
    # x increases to the right; y increases to the down
    # There is only one route to any cell in the first row or first column
    if x == 0 or y == 0:
        return 1

    if (x, y) in _CACHE:
        return _CACHE[(x, y)]

    n = count_routes_from_origin(x - 1, y) + count_routes_from_origin(x, y - 1)
    logger.debug(f"Routes from ({x}, {y}): {n}")
    _CACHE[(x, y)] = n
    return n


@main_wrapper("Lattice Paths")
def main():
    result = count_routes_from_origin(20, 20)
    return result


if __name__ == "__main__":
    cli()
