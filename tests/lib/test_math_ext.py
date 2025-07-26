import pytest
from typing import Literal

from problems.lib import math_ext


@pytest.mark.parametrize(
    "x, expected",
    [
        (1, [1]),
        (2, [1]),
        (3, [1]),
        (4, [1, 2]),
        (5, [1]),
        (6, [1, 2, 3]),
        (16, [1, 2, 4, 8]),
        (25, [1, 5]),
        (28, [1, 2, 4, 7, 14]),
    ],
)
def test_proper_divisors(x: int, expected: list[int]):
    actual = list(math_ext.proper_divisors(x))
    actual.sort()
    assert expected == actual


@pytest.mark.parametrize(
    "x, expected",
    [
        (28, 0),
        (12, 1),
    ],
)
def test_properness(x: int, expected: Literal[-1, 0, 1]):
    actual = math_ext.properness(x)
    assert expected == actual
