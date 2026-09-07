
def secure_archive(
    filename: str, action: str = "read", content: str = ""
) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(filename, "r") as f:
                data = f.read()
            return (True, data)
        elif action == "write":
            with open(filename, "w") as f:
                f.write(content)
            return (True, "Content successfully written to file")
        else:
            return (False, f"Invalid action: '{action}'")
    except Exception as e:
        return (False, str(e))


def test_vault_security() -> None:
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    result = secure_archive("/not/existing/file", action="read")
    print(result)

    print("Using 'secure_archive' to read from an inaccessible file:")
    result = secure_archive("/etc/master.passwd", action="read")
    print(result)

    print("Using 'secure_archive' to read from a regular file:")
    read_result = secure_archive("ancient_fragment.txt", action="read")
    print(read_result)

    print("Using 'secure_archive' to write previous content to a new file:")
    if read_result[0]:
        write_result = secure_archive(
            "new_fragment.txt", action="write", content=read_result[1]
        )
        print(write_result)


if __name__ == "__main__":
    test_vault_security()
