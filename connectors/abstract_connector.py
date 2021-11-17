from abc import ABC, abstractmethod

class AbstractConnector(ABC):
    @abstractmethod
    def perform(self, action, callback):
        pass
