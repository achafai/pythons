import sys
import typing


def read_cyber_archive(filename: str) -> str:

    file_obj: typing.IO[str] | None = None
    try:
        file_obj = open(filename, "r")
        return file_obj.read()
    finally:
        if file_obj is not None:
            file_obj.close()


def test_ancient_text(filename: str) -> None:
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")
    try:
        content = read_cyber_archive(filename)
        print("---")
        print(content, end="")
        if content and not content.endswith("\n"):
            print()
        print("---")
        print(f"File '{filename}' closed.")
    except (OSError, UnicodeError) as e:
        print(f"Error opening file '{filename}': {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        test_ancient_text(sys.argv[1])
