"""Battle test script for ex0 package using Creature factories."""

import sys
from ex0 import AquaFactory, CreatureFactory, FlameFactory


def test_factory_capabilities(factory: CreatureFactory) -> None:
    """Verify that a factory creates base and evolved creatures,

    and that each creature can describe itself and attack.
    """
    try:
        base_creature = factory.create_base()
        evolved_creature = factory.create_evolved()

        print(base_creature.describe())
        print(base_creature.attack())
        print(evolved_creature.describe())
        print(evolved_creature.attack())
    except Exception as err:
        print(f"Error during factory verification: {err}", file=sys.stderr)


def battle_base_creatures(
    factory_a: CreatureFactory,
    factory_b: CreatureFactory,
) -> None:
    """Simulate a battle between the base creatures of two factories."""
    try:
        creature_a = factory_a.create_base()
        creature_b = factory_b.create_base()

        print(f"\n--- Battle: {creature_a.name} vs {creature_b.name} ---")
        print(creature_a.describe())
        print(creature_b.describe())
        print(creature_a.attack())
        print(creature_b.attack())
        print(
            f"{creature_a.name} and {creature_b.name} fought to a standstill!"
        )
    except Exception as err:
        print(f"Error during base creature battle: {err}", file=sys.stderr)


def main() -> None:
    """Instantiate factories and execute verification and battle scenarios."""
    try:
        flame_factory: CreatureFactory = FlameFactory()
        aqua_factory: CreatureFactory = AquaFactory()

        print("--- Verifying Flame Factory ---")
        test_factory_capabilities(flame_factory)

        print("\n--- Verifying Aqua Factory ---")
        test_factory_capabilities(aqua_factory)

        battle_base_creatures(flame_factory, aqua_factory)
    except Exception as err:
        print(f"An unexpected error occurred: {err}", file=sys.stderr)


if __name__ == "__main__":
    main()
