from mappers import abstract_mapper

class RawMapper(abstract_mapper.AbstractMapper):
    def __init__(self):
        pass

    def mapActionToCommand(self, action):
        return action

    def mapPerceptionsToPropositions(self, perceptions):
        return perceptions
