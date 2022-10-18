from abc import ABC, abstractmethod

class AbstractConnector(ABC):
    @abstractmethod
    def get_initial_propositions(self):
        pass
    @abstractmethod
    def perform(self, action, callback):
        pass
