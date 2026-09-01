import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return

    filename: str = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    file_obj: typing.Optional[typing.IO[str]] = None
    lines: list[str] = []

    try:
        file_obj = open(filename, "r")
        print("---")
        lines = file_obj.readlines()
        for line in lines:
            print(line, end="")
        if lines and not lines[-1].endswith("\n"):
            print()
        print("---")
        print(f"File '{filename}' closed.")
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")
        return
    finally:
        if file_obj is not None:
            file_obj.close()

    print("Transform data:")
    print("---")
    transformed_lines: list[str] = []
    for line in lines:
        stripped_line: str = line.rstrip("\r\n")
        transformed_lines.append(stripped_line + "#\n")
        print(stripped_line + "#")
    print("---")

    out_filename: str = input("Enter new file name (or empty):\n")

    if not out_filename:
        print("Not saving data.")
        return

    print(f"Saving data to '{out_filename}'")
    out_file: typing.Optional[typing.IO[str]] = None
    try:
        out_file = open(out_filename, "w")
        for line in transformed_lines:
            out_file.write(line)
        print(f"Data saved in file '{out_filename}'.")
    except Exception as e:
        print(f"Error saving to file '{out_filename}': {e}")
    finally:
        if out_file is not None:
            out_file.close()


if __name__ == "__main__":
    main()
