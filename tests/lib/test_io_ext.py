from problems.lib import io_ext


class TestReadlinesReverse:
    def test_empty_file(self, tmp_path):
        fp = tmp_path / "file.txt"
        fp.touch()
        assert list(io_ext.readlines_reverse(fp)) == []

    def test_small_file_reads_in_reverse(self, tmp_path):
        fp = tmp_path / "file.txt"
        fp.write_text("Once\nUpon\nA\nTime\nThere\nWas\nA\nBig\nSpaceship\n")
        result = io_ext.readlines_reverse(fp)
        assert hasattr(result, "__iter__")
        assert hasattr(result, "__next__")
        assert list(result) == [
            "",
            "Spaceship",
            "Big",
            "A",
            "Was",
            "There",
            "Time",
            "A",
            "Upon",
            "Once",
        ]

    def test_line_fn(self, tmp_path):
        fp = tmp_path / "file.txt"
        fp.write_text("a\nc\nm\ny")
        result = io_ext.readlines_reverse(fp, line_fn=str.upper)
        assert next(result) == "Y"
        assert next(result) == "M"
        assert next(result) == "C"
        assert next(result) == "A"
