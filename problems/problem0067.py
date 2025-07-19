import os
from functools import reduce

from problems.lib import cli, main_wrapper
from problems import problem_data


def ident(line):
    return line


def readlines_reverse(filepath, encoding="utf-8", chunk_size=4096, line_fn=None):
    """Yields lines from a file in reverse order."""
    if line_fn is None:
        line_fn = ident

    with open(filepath, "rb") as f:
        # start at the end of the file and read upwards in chunks
        f.seek(0, os.SEEK_END)
        position = f.tell()
        buffer = b""
        while position > 0:
            read_size = min(chunk_size, position)
            position -= read_size
            f.seek(position)
            chunk = f.read(read_size)
            buffer = chunk + buffer
            lines = buffer.split(b"\n")
            # keep the first (possibly incomplete) line in buffer
            buffer = lines[0]
            for line in reversed(lines[1:]):
                yield line_fn(line.decode(encoding))
        # yield anything left in the buffer
        if buffer:
            yield line_fn(buffer.decode(encoding))


def parse_line(line: str) -> list[int]:
    if not line.strip():
        return []
    result = list(map(int, line.split(" ")))
    return result


def imp_solution(line_iter):
    # rely on triangle shape, and traverse bottom up, summing the max
    # as we go (O(N))
    triangle_last_row = None
    for row in line_iter:
        if not row:
            continue

        if triangle_last_row is None:
            # first row case (only happens once)
            triangle_last_row = row
            continue

        # add a new row to triangle by summing from the largest of
        # the 2 children in the previous row (relies on triangle shape)
        triangle_last_row = [
            x + max(triangle_last_row[col_i], triangle_last_row[col_i + 1])
            for col_i, x in enumerate(row)
        ]

    # we have summed all the way to the top
    assert len(triangle_last_row) == 1, "Triange not triangle shaped"
    result = triangle_last_row[0]
    return result


def func_solution(line_iter):
    return (
        reduce(
            lambda xs, ys: [
                y + max(xs[col_i], xs[col_i + 1]) for col_i, y in enumerate(ys)
            ],
            filter(lambda x: bool(x), line_iter),
        )
    )[0]


@main_wrapper
def main():
    problem_fpath = problem_data.get("0067_triangle.txt")
    line_iter = readlines_reverse(problem_fpath, line_fn=parse_line)
    return func_solution(line_iter)


if __name__ == "__main__":
    cli()
