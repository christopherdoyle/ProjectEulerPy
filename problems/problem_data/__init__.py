from pathlib import Path

DIRECTORY = Path(__file__).parent


def get(filename: str) -> Path:
    filepath = DIRECTORY / filename
    if not filepath.is_file():
        raise ValueError(f"File not found: '{filename}'")
    return filepath
