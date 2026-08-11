def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise ValueError("{temp} is too hot for plants (max 40)°C")
    elif temp < 0:
        raise ValueError("{temp} is too cold for plants (min 0)°C")
    return temp


def test_temperature(item: str) -> None:
    try:
        print(f"input data is: '{item}'")
        output = input_temperature(item)
        print(f"Temperature is now {output}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print()


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    print()
    items = ["25", "abc", "100", "-50"]
    for item in items:
        test_temperature(item)
    print("All tests completed - program didn't crash!")
