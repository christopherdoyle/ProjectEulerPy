import pytest

from problems.lib import num_format


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, "zero"),
        (1, "one"),
        (15, "fifteen"),
        (23, "twenty-three"),
        (100, "one hundred"),
        (105, "one hundred and five"),
        (159, "one hundred and fifty-nine"),
        (390, "three hundred and ninety"),
        (1515, "one thousand five hundred and fifteen"),
    ],
)
def test_number_to_human_words(n: int, expected: str):
    actual: str = num_format.number_to_human_words(n)
    assert expected == actual
