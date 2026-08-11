def garden_operations(operation_number: int) -> None:
    print(f"Testing operation {operation_number}...")
    try:
        if operation_number == 0:
            print(int("abc"))
        elif operation_number == 1:
            print(1 / 0)
        elif operation_number == 2:
            file = open("/non/existent/file")
            print(file)
        elif operation_number == 3:
            print(5 + "5")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    except TypeError as e:
        print(f"Caught TypeError: {e}")
    else:
        print("Operation completed successfully")
        return


def test_error_types(elements: list) -> None:
    for element in elements:
        garden_operations(element)
    print()


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types([0, 1, 2, 3, 4])
    print("All error types tested successfully!")
