def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    a = "25"
    b = "abc"
    try:
        print(f"input data is: '{a}'")
        output = input_temperature(a)
        print(f"Temperature is now {output}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print()
    try:
        print(f"input data is: '{b}'")
        output = input_temperature(b)
        print(f"Temperature is now {output}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature()
    print()
    print("All tests completed - program didn't crash!")
