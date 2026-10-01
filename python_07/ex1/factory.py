"""Factory classes for creating capability-enabled creatures."""

from ex0.creature import Creature
from ex0.factory import CreatureFactory
from ex1.creature import Bloomelle, Morphagon, Shiftling, Sproutling


class HealingCreatureFactory(CreatureFactory):
    """Factory for creating Healing family creatures."""

    def create_base(self) -> Creature:
        """Create a Sproutling instance."""
        try:
            return Sproutling()
        except Exception as err:
            raise RuntimeError(
                f"Failed to create base Healing creature: {err}"
            ) from err

    def create_evolved(self) -> Creature:
        """Create a Bloomelle instance."""
        try:
            return Bloomelle()
        except Exception as err:
            raise RuntimeError(
                f"Failed to create evolved Healing creature: {err}"
            ) from err


class TransformCreatureFactory(CreatureFactory):
    """Factory for creating Transform family creatures."""

    def create_base(self) -> Creature:
        """Create a Shiftling instance."""
        try:
            return Shiftling()
        except Exception as err:
            raise RuntimeError(
                f"Failed to create base Transform creature: {err}"
            ) from err

    def create_evolved(self) -> Creature:
        """Create a Morphagon instance."""
        try:
            return Morphagon()
        except Exception as err:
            raise RuntimeError(
                f"Failed to create evolved Transform creature: {err}"
            ) from err
