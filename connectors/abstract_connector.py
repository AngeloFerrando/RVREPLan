from abc import ABC, abstractmethod
from enum import Enum

class ResultCode(Enum):
    SUCCESS = 1
    FAILURE = 0

class AbstractConnector(ABC):
    @abstractmethod
    def get_initial_propositions(self):
        pass
    @abstractmethod
    def perform(self, action, callback):
        pass
