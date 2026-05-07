from abc import ABC, abstractmethod

class AbstractMapper(ABC):
    """Translate between planner-level objects and system-level representations."""

    @abstractmethod
    def mapActionToCommand(self, action):
        """Convert an RVRepLan action into the command expected by a connector."""
        pass

    @abstractmethod
    def mapPerceptionsToPropositions(self, perceptions):
        """Convert system perceptions into propositions consumed by monitors."""
        pass
