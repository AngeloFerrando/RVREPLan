from abc import ABC, abstractmethod

class AbstractMapper(ABC):
    @abstractmethod
    def mapActionToCommand(self, action):
        pass

    @abstractmethod
    def mapPerceptionsToPropositions(self, perceptions):
        pass
