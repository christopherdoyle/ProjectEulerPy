import string

from problems.lib import cli, main_wrapper
from problems import problem_data


def load_names(fp) -> list[str]:
    return fp.read_text().replace('"', "").split(",")


@main_wrapper
def main():
    names = load_names(problem_data.get("0022_names.txt"))
    # precompute all the alphabet values
    alph = {c: ord(c) - 64 for c in string.ascii_uppercase}
    total = sum(
        i * sum(map(alph.get, name)) for i, name in enumerate(sorted(names), start=1)
    )
    return total


if __name__ == "__main__":
    cli()
