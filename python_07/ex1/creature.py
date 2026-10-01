"""Concrete creature classes with specific capabilities for ex1 package."""

from typing import Optional

from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    """Concrete base Creature with healing capability."""

    def __init__(self, name: str = "Sproutling") -> None:
        """Initialize Sproutling."""
        super().__init__(name=name, creature_type="Healing")

    def attack(self) -> str:
        """Perform Sproutling attack."""
        return f"{self.name} uses Vine Whip!"

    def heal(self, target: Optional[str] = None) -> str:
        """Perform Sproutling healing action."""
        if target:
            return f"{self.name} heals {target} with Photosynthesis!"
        return f"{self.name} heals itself with Photosynthesis!"


class Bloomelle(Creature, HealCapability):
    """Concrete evolved Creature with healing capability."""

    def __init__(self, name: str = "Bloomelle") -> None:
        """Initialize Bloomelle."""
        super().__init__(name=name, creature_type="Healing")

    def attack(self) -> str:
        """Perform Bloomelle attack."""
        return f"{self.name} uses Petal Storm!"

    def heal(self, target: Optional[str] = None) -> str:
        """Perform Bloomelle healing action."""
        if target:
            return f"{self.name} casts Solar Recovery on {target}!"
        return f"{self.name} casts Solar Recovery on itself!"


class Shiftling(Creature, TransformCapability):
    """Concrete base Creature with transformation capability."""

    def __init__(self, name: str = "Shiftling") -> None:
        """Initialize Shiftling."""
        Creature.__init__(self, name=name, creature_type="Transform")
        TransformCapability.__init__(self)

    def transform(self) -> str:
        """Transform into shifted state."""
        self.is_transformed = True
        return f"{self.name} transforms into Shadow Form!"

    def revert(self) -> str:
        """Revert back to normal state."""
        self.is_transformed = False
        return f"{self.name} reverts back to normal form."

    def attack(self) -> str:
        """Perform attack, boosted if transformed."""
        if self.is_transformed:
            return f"{self.name} attacks with Shadow Strike (Boosted)!"
        return f"{self.name} attacks with Quick Swipe!"


class Morphagon(Creature, TransformCapability):
    """Concrete evolved Creature with transformation capability."""

    def __init__(self, name: str = "Morphagon") -> None:
        """Initialize Morphagon."""
        Creature.__init__(self, name=name, creature_type="Transform")
        TransformCapability.__init__(self)

    def transform(self) -> str:
        """Transform into titan state."""
        self.is_transformed = True
        return f"{self.name} transforms into Titan Mode!"

    def revert(self) -> str:
        """Revert back to normal state."""
        self.is_transformed = False
        return f"{self.name} reverts back to standard mode."

    def attack(self) -> str:
        """Perform attack, boosted if transformed."""
        if self.is_transformed:
            return f"{self.name} attacks with Titan Beam (Empowered)!"
        return f"{self.name} attacks with Energy Pulse!"
