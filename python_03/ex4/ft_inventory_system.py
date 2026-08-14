import sys


def inventory_parsing(args: list) -> dict:
    inventory: dict = dict()
    seen: set = set()
    for arg in args:
        try:
            key, value_str = arg.split(':')
        except Exception:
            print(f"Error - invalid parameter '{arg}'")
            continue
        try:
            value = int(value_str)
        except Exception:
            print(f"Quantity error for '{key}':", end=' ')
            print(f"invalid literal for int() with base 10: '{value_str}'")
            continue
        if key in seen:
            print(f"Redundant item '{key}' - discarding")
            continue
        seen.add(key)
        inventory[key] = value
    print(f"Got inventory: {inventory}")
    return inventory


def item_portion(item: int, total: int) -> float:
    portion = item / total * 100
    return round(portion, 1)


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    args: list = sys.argv[1:]
    inv: dict = inventory_parsing(args)
    print(f"Item list: {list(inv.keys())}")
    print(f"Total quantity of the {len(inv.keys())}", end=' ')
    total_vaules = sum(inv.values())
    for key in inv.keys():
        print(f"Item {key} represents {item_portion(inv[key], total_vaules)}%")
