import sys
import typing


def read_archive_file(filename: str) -> list[str]:
    file_obj: typing.Optional[typing.IO[str]] = None
    try:
        file_obj = open(filename, "r")
        return file_obj.readlines()
    finally:
        if file_obj is not None:
            file_obj.close()


def save_archive_file(filename: str, lines: list[str]) -> None:
    out_file: typing.Optional[typing.IO[str]] = None
    try:
        out_file = open(filename, "w")
        for line in lines:
            out_file.write(line)
    finally:
        if out_file is not None:
            out_file.close()


def test_stream_management(filename: str) -> None:
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
    except Exception as e:
        print(f"[STDERR] Error opening file '{filename}': {e}", file=sys.stderr)
        return

    print("Transform data:")
    print("---")
    transformed_lines: list[str] = []
    for line in lines:
        stripped_line = line.rstrip("\r\n")
        transformed_lines.append(stripped_line + "#\n")
        print(stripped_line + "#")
    print("---")

    print("Enter new file name (or empty):", flush=True)
    out_filename = sys.stdin.readline().rstrip("\r\n")

    if not out_filename:
        print("Not saving data.")
        return

    print(f"Saving data to '{out_filename}'")
    try:
        save_archive_file(out_filename, transformed_lines)
        print(f"Data saved in file '{out_filename}'.")
    except Exception as e:
        print(f"[STDERR] Error opening file '{out_filename}': {e}", file=sys.stderr)
        print("Data not saved.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        test_stream_management(sys.argv[1])
