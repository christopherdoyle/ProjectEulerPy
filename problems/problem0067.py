import os

from problems.lib import cli, main_wrapper
from problems import problem_data


def readlines_reverse(filepath, encoding="utf-8", chunk_size=4096):
    """Yields lines from a file in reverse order."""
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
                yield line.decode(encoding)
        # yield anything left in the buffer
        if buffer:
            yield buffer.decode(encoding)


@main_wrapper
def main():
    problem_fpath = problem_data.get("0067_triangle.txt")

    # rely on triangle shape, and traverse bottom up, summing the max
    # as we go (O(N))
    triangle_last_row = None
    for row in readlines_reverse(problem_fpath):
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
