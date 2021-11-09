from abc import ABC, abstractmethod

class AbstractConnector(ABC):
    @abstractmethod
    def perform(self, action):
        pass

    @abstractmethod
    def get_propositions(self, callback):
        pass
