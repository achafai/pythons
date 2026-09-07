import sys
import typing


def read_archive_file(filename: str) -> list[str]:

    file_obj: typing.IO[str] | None = None
    try:
        file_obj = open(filename, "r")
        return file_obj.readlines()
    finally:
        if file_obj is not None:
            file_obj.close()


def save_archive_file(filename: str, lines: list[str]) -> None:

    out_file: typing.IO[str] | None = None
    try:
        out_file = open(filename, "w")
        for line in lines:
            out_file.write(line)
    finally:
        if out_file is not None:
            out_file.close()


def test_archive_creation(filename: str) -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")
    try:
        lines = read_archive_file(filename)
        print("---")
        for line in lines:
            print(line, end="")
        if lines and not lines[-1].endswith("\n"):
            print()
        print("---")
        print(f"File '{filename}' closed.")
    except (OSError, UnicodeError) as e:
        print(f"Error opening file '{filename}': {e}")
        return

    print("Transform data:")
    print("---")
    transformed_lines: list[str] = []
    for line in lines:
        stripped_line = line.rstrip("\r\n")
        transformed_lines.append(stripped_line + "#\n")
        print(stripped_line + "#")
    print("---")

    out_filename = input("Enter new file name (or empty):\n")
    if not out_filename.strip():
        print("Not saving data.")
        return

    print(f"Saving data to '{out_filename}'")
    try:
        save_archive_file(out_filename, transformed_lines)
        print(f"Data saved in file '{out_filename}'.")
    except (OSError, UnicodeError) as e:
        print(f"Error opening file '{filename}': {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        test_archive_creation(sys.argv[1])
