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


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system(items: list) -> None:
    print("Opening watering system")
    try:
        for item in items:
            water_plant(item)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")
        return


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print()
    print("Testing valid plants...")
    test_watering_system(["Tomato", "Lettuce", "Carrots"])
    print()
    print("Testing invalid plants...")
    test_watering_system(["Tomato", "lettuce", "Carrots"])
    print()
    print("Cleanup always happens, even with errors!")
