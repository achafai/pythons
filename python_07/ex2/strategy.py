"""Battle strategy implementations for ex2 package."""

from abc import ABC, abstractmethod

from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    """Exception raised when a strategy is invalid for a creature."""

    pass


class BattleStrategy(ABC):
    """Abstract base class for tournament battle strategies."""

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Check if the creature is suitable for this strategy."""
        pass

    @abstractmethod
    def act(self, creature: Creature) -> str:
        """Execute the strategy actions on the creature."""
        pass


class NormalStrategy(BattleStrategy):
    """Normal battle strategy suitable for any Creature."""

    def is_valid(self, creature: Creature) -> bool:
        """Return True as normal strategy is valid for any creature."""
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> str:
        """Execute basic attack action."""
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"NormalStrategy is invalid for {type(creature).__name__}."
            )
        return creature.attack()


class AggressiveStrategy(BattleStrategy):
    """Aggressive battle strategy for creatures with transform capability."""

    def is_valid(self, creature: Creature) -> bool:
        """Return True if creature possesses TransformCapability."""
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> str:
        """Execute transform, attack, and revert actions."""
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"AggressiveStrategy is invalid for {creature.name} "
                f"({type(creature).__name__}): missing TransformCapability."
            )
        if isinstance(creature, TransformCapability):
            actions = [
                creature.transform(),
                creature.attack(),
                creature.revert(),
            ]
            return "\n".join(actions)
        raise InvalidStrategyError("Creature lacks TransformCapability.")


class DefensiveStrategy(BattleStrategy):
    """Defensive battle strategy for creatures with healing capability."""

    def is_valid(self, creature: Creature) -> bool:
        """Return True if creature possesses HealCapability."""
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> str:
        """Execute attack and heal actions."""
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"DefensiveStrategy is invalid for {creature.name} "
                f"({type(creature).__name__}): missing HealCapability."
            )
        if isinstance(creature, HealCapability):
            actions = [
                creature.attack(),
                creature.heal(),
            ]
            return "\n".join(actions)
        raise InvalidStrategyError("Creature lacks HealCapability.")
