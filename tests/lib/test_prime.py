import pytest

from problems.lib import prime


@pytest.mark.parametrize(
    "n, expected",
    [
        [1, []],
        [2, [2]],
        [3, [2, 3]],
        [4, [2, 3]],
        [9, [2, 3, 5, 7]],
        [30, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]]
    ]
)
def test_sieve_of_eratosthenes(n, expected):
    actual = prime.sieve_of_eratosthenes(n)
    assert expected == actual
