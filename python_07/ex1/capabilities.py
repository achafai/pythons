"""Capability abstract interfaces for ex1 package."""

from abc import ABC, abstractmethod
from typing import Optional


class HealCapability(ABC):
    """Abstract capability interface for healing actions."""

    @abstractmethod
    def heal(self, target: Optional[str] = None) -> str:
        """Perform a healing action on a target or self."""
        pass


class TransformCapability(ABC):
    """Abstract capability interface for transformation state."""

    def __init__(self) -> None:
        """Initialize the transformation state."""
        self.is_transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        """Transform into an empowered state."""
        pass

    @abstractmethod
    def revert(self) -> str:
        """Revert to the original state."""
        pass
