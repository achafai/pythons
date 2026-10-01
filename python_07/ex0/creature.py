from abc import ABC, abstractmethod


class Creature(ABC):
    """Abstract base class representing a Creature."""

    def __init__(self, name: str, creature_type: str) -> None:
        """Initialize a Creature with a name and type."""
        if not isinstance(name, str) or not isinstance(creature_type, str):
            raise TypeError("Name and creature_type must be strings.")
        if not name.strip() or not creature_type.strip():
            raise ValueError("Name and creature_type cannot be empty.")
        self.name: str = name
        self.type: str = creature_type

    @abstractmethod
    def attack(self) -> str:
        """Perform a creature attack."""
        pass

    def describe(self) -> str:
        """Return a standardized description message for the creature."""
        return f"{self.name} is a {self.type} type Creature."


class Flameling(Creature):
    """Concrete base Creature for the Flame family."""

    def __init__(self, name: str = "Flameling") -> None:
        """Initialize Flameling."""
        super().__init__(name=name, creature_type="Flame")

    def attack(self) -> str:
        """Perform Flameling attack."""
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    """Concrete evolved Creature for the Flame family."""

    def __init__(self, name: str = "Pyrodon") -> None:
        """Initialize Pyrodon."""
        super().__init__(name=name, creature_type="Flame")

    def attack(self) -> str:
        """Perform Pyrodon attack."""
        return f"{self.name} uses Flamethrower!"


class Aquabub(Creature):
    """Concrete base Creature for the Aqua family."""

    def __init__(self, name: str = "Aquabub") -> None:
        """Initialize Aquabub."""
        super().__init__(name=name, creature_type="Aqua")

    def attack(self) -> str:
        """Perform Aquabub attack."""
        return f"{self.name} uses Water Gun!"


class Torragon(Creature):
    """Concrete evolved Creature for the Aqua family."""

    def __init__(self, name: str = "Torragon") -> None:
        """Initialize Torragon."""
        super().__init__(name=name, creature_type="Aqua")

    def attack(self) -> str:
        """Perform Torragon attack."""
        return f"{self.name} uses Hydro Pump!"
