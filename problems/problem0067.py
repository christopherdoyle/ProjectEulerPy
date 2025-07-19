from problems.lib import cli, main_wrapper
from problems import problem_data


@main_wrapper
def main():
    problem_fpath = problem_data.get("0067_triangle.txt")

    # rely on triangle shape, and traverse bottom up, summing the max
    # as we go (O(N))
    triangle = []
    for row in reversed(problem_fpath.read_text().splitlines()):
        if row == "":
            continue
        row_data = map(int, row.split(" "))
        if not triangle:
            # first row case (only happens once)
            triangle.append(list(row_data))
            continue

        # add a new row to triangle by summing from the largest of
        # the 2 children in the previous row (relies on triangle shape)
        triangle.append(
            [
                x + max(triangle[-1][col_i], triangle[-1][col_i + 1])
                for col_i, x in enumerate(row_data)
            ]
        )

    # we have summed all the way to the top
    assert len(triangle[-1]) == 1, "Triange not triangle shaped"
    result = triangle[-1][0]
    return result


if __name__ == "__main__":
    cli()
