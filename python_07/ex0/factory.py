from abc import ABC, abstractmethod

from ex0.creature import Aquabub, Creature, Flameling, Pyrodon, Torragon


class CreatureFactory(ABC):
    """Abstract class for factory creating family creatures."""

    @abstractmethod
    def create_base(self) -> Creature:
        """Create and return the base Creature."""
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Create and return the evolved Creature."""
        pass


class FlameFactory(CreatureFactory):
    """Factory for Flame family creatures."""

    def create_base(self) -> Creature:
        """Create a Flameling instance."""
        try:
            return Flameling()
        except Exception as err:
            raise RuntimeError(
                f"Failed to create base Flame creature: {err}"
            ) from err

    def create_evolved(self) -> Creature:
        """Create a Pyrodon instance."""
        try:
            return Pyrodon()
        except Exception as err:
            raise RuntimeError(
                f"Failed to create evolved Flame creature: {err}"
            ) from err


class AquaFactory(CreatureFactory):
    """Factory for Aqua family creatures."""

    def create_base(self) -> Creature:
        """Create an Aquabub instance."""
        try:
            return Aquabub()
        except Exception as err:
            raise RuntimeError(
                f"Failed to create base Aqua creature: {err}"
            ) from err

    def create_evolved(self) -> Creature:
        """Create a Torragon instance."""
        try:
            return Torragon()
        except Exception as err:
            raise RuntimeError(
                f"Failed to create evolved Aqua creature: {err}"
            ) from err
