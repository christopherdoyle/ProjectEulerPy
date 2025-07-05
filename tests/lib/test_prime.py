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


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 2),
        (2, 3),
        (10001, 104743)
    ]
)
def test_nth_prime(n, expected):
    actual = prime.nth_prime(n)
    assert expected == actual
