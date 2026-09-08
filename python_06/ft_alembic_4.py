import alchemy


def main() -> None:
    print(alchemy.create_air())
    try:
        print(alchemy.create_earth())  # Intentionally not exposed
    except AttributeError as e:
        print(f"AttributeError caught as expected: {e}")


if __name__ == "__main__":
    main()
