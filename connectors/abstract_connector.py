from abc import ABC, abstractmethod
from enum import Enum

class ResultCode(Enum):
    SUCCESS = 1
    FAILURE = 0

class AbstractConnector(ABC):
    """Boundary between RVRepLan and the executed system or simulator."""

    @abstractmethod
    def get_initial_propositions(self):
        """Return propositions observed before the first planned action."""
        pass

    @abstractmethod
    def perform(self, action, callback):
        """Execute one action and report observed propositions through callback."""
        pass
