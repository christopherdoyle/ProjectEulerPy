from problems.lib import cli, main_wrapper
from problems import problem_data


@main_wrapper
def main():
    problem_fpath = problem_data.get("0067_triangle.txt")

    # rely on triangle shape, and traverse bottom up, summing the max
    # as we go (O(N))
    triangle_last_row = None
    for row in reversed(problem_fpath.read_text().splitlines()):
        if not row.strip():
            continue
        row_data = map(int, row.split(" "))
        if triangle_last_row is None:
            # first row case (only happens once)
            triangle_last_row = list(row_data)
            continue

        # add a new row to triangle by summing from the largest of
        # the 2 children in the previous row (relies on triangle shape)
        triangle_last_row = [
            x + max(triangle_last_row[col_i], triangle_last_row[col_i + 1])
            for col_i, x in enumerate(row_data)
        ]

    # we have summed all the way to the top
    assert len(triangle_last_row) == 1, "Triange not triangle shaped"
    result = triangle_last_row[0]
    return result


if __name__ == "__main__":
    cli()
