# all the unique numbers we need
_NUMBERS = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}


def number_to_human_words(n: int):
    if n == 0:
        return "zero"

    if n >= 100_000:
        raise NotImplementedError()

    thousands, remainder = divmod(n, 1000)
    hundreds, remainder = divmod(remainder, 100)
    tens, ones = divmod(remainder, 10)

    parts = []
    if thousands:
        parts.append(f"{_NUMBERS[thousands]} thousand")
    if hundreds:
        parts.append(f"{_NUMBERS[hundreds]} hundred")
    if tens == 1:
        parts.append(_NUMBERS[(tens * 10) + ones])
    elif tens > 1:
        tens_str = _NUMBERS[tens * 10]
        if ones:
            # e.g. "twenty-three", but not "twenty-zero"
            tens_str += "-" + _NUMBERS[ones]
        parts.append(tens_str)
    elif ones:
        parts.append(_NUMBERS[ones])

    if len(parts) > 1:
        parts.insert(len(parts) - 1, "and")

    return " ".join(parts)
