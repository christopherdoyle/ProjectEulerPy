from typing import Iterable


def iterlen(xs: Iterable) -> int:
    return sum(1 for _ in xs)
