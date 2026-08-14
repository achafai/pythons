import sys


def inventory_parsing() -> dict:
    inventory: dict = dict()
    seen: set = set()
    for arg in sys.argv[1:]:
        if ':' not in arg:
            print(f"Error - invalid parameter '{arg}'")
        key, value_str = arg.split(':')
        try:
            value = int(value_str)
        except Exception:
            print(f"Quantity error for '{key}':", end=' ')
            print(f"invalid literal for int() with base 10: '{value}'")
            continue
        if key in seen:
            print(f"Redundant item {key} - discarding")
            continue
        seen.add(key)
        inventory[key] = value
    return inventory


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
