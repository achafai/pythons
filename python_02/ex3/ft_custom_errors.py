class GardenError(Exception):
    def __init__(self, message: str = "General garden error"):
        self.message = message
        super().__init__(self.message)


class PlantError(GardenError):
    def __init__(self, message: str = "Plant error"):
        self.message = message
        super().__init__(self.message)


class WaterError(GardenError):
    def __init__(self, message: str = "Water error"):
        self.message = message
        super().__init__(self.message)


def check_plant_status() -> None:
    raise PlantError("The tomato plant is wilting!")


def check_water_level() -> None:
    raise WaterError("Not enough water in the tank!")


def test_custom_error() -> None:
    print("Testing PlantError...")
    try:
        check_plant_status()
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()
    print("Testing WaterError...")
    try:
        check_water_level()
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()
    print("Testing catching all garden errors...")
    try:
        check_plant_status()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        check_water_level()
    except GardenError as e:
        print(f"Caught GardenError: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    print()
    test_custom_error()
    print()
    print("All custom error types work correctly!")
