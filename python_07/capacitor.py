"""Capacitor test script for ex1 package testing capabilities."""

import sys
from ex1 import (
    HealCapability,
    HealingCreatureFactory,
    TransformCapability,
    TransformCreatureFactory,
)


def test_healing_creatures() -> None:
    """Test healing creature factory and creature capabilities."""
    try:
        healing_factory = HealingCreatureFactory()

        base_creature = healing_factory.create_base()
        evolved_creature = healing_factory.create_evolved()

        print("--- Testing Base Healing Creature ---")
        print(base_creature.describe())
        print(base_creature.attack())
        if isinstance(base_creature, HealCapability):
            print(base_creature.heal())

        print("\n--- Testing Evolved Healing Creature ---")
        print(evolved_creature.describe())
        print(evolved_creature.attack())
        if isinstance(evolved_creature, HealCapability):
            print(evolved_creature.heal())
    except Exception as err:
        print(f"Error testing healing creatures: {err}", file=sys.stderr)


def test_transform_creatures() -> None:
    """Test transform creature factory and creature capabilities."""
    try:
        transform_factory = TransformCreatureFactory()

        base_creature = transform_factory.create_base()
        evolved_creature = transform_factory.create_evolved()

        for creature in (base_creature, evolved_creature):
            print(f"\n--- Testing Transforming Creature: {creature.name} ---")
            print(creature.describe())
            print(creature.attack())
            if isinstance(creature, TransformCapability):
                print(creature.transform())
                print(creature.attack())
                print(creature.revert())
    except Exception as err:
        print(f"Error testing transform creatures: {err}", file=sys.stderr)


def main() -> None:
    """Run the test scenarios for ex1 capabilities."""
    try:
        test_healing_creatures()
        test_transform_creatures()
    except Exception as err:
        print(f"Unexpected error in main execution: {err}", file=sys.stderr)


if __name__ == "__main__":
    main()
