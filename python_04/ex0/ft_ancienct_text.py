import sys
import typing


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return

    filename: str = sys.argv[1]

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    file_obj: typing.Optional[typing.IO[str]] = None
    try:
        file_obj = open(filename, "r")
        print("---")
        content: str = file_obj.read()
        print(content, end="")
        if content and not content.endswith("\n"):
            print()
        print("---")
        print(f"File '{filename}' closed.")
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")
    finally:
        if file_obj is not None:
            file_obj.close()


if __name__ == "__main__":
    main()
