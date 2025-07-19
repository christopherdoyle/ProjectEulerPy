import os


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
