from data.proposition import *

class Snapshot(object):
    def __init__(self, problem_file):
        self._propositions = set()
        self._goals = set()
        with open(problem_file, 'r') as input:
            content = input.read()
        init = content.index(':init')
        endInit = content.index('(:goal (and')
        for prop in content[init+5:endInit].split(')'):
            prop = prop.replace('(', '').replace(')', '').replace('\n', '').strip()
            if not prop: continue
            if 'not' in prop:
                self._propositions.add(Proposition(False, prop[prop.index('not')+4:prop.index(' ', prop.index('not')+4)].strip(), prop[prop.index(' ', prop.index('not')+4)+1:].split(' ')))
            else:
                self._propositions.add(Proposition(True, prop[:prop.index(' ')], prop[prop.index(' ')+1:].split(' ')))
        for goal in content[endInit+11:].split(')'):
            goal = goal.replace('(', '').replace(')', '').replace('\n', '').strip()
            if not goal: continue
            self._goals.add(Proposition(True, goal[:goal.index(' ')], goal[goal.index(' ')+1:].split(' ')))
    def update(self, propositions):
        for prop in propositions:
            # self._propositions.discard(Proposition(prop._truth, prop._functor, prop._args))
            self._propositions.discard(Proposition(not prop._truth, prop._functor, prop._args))
            # props_to_remove = []
            # print(prop)
            # for prop1 in self._propositions:
            #     if prop1._functor == prop._functor:
            #         props_to_remove.append(prop1)
            # print(props_to_remove)
            # self._propositions = self._propositions.difference(props_to_remove)
            self._propositions.add(prop)
            self._goals.discard(prop)
    def get_props(self):
        return self._propositions
    def __str__(self):
        res = '(:init\n'
        for prop in self._propositions:
            res = res + '  (' + str(prop).replace(',', ' ') + ')\n'
        res = res + ')\n'
        res = res + '(:goal (and\n'
        for goal in self._goals:
            res = res + '  (' + str(goal).replace(',', ' ') + ')\n'
        res = res + '))'
        return res
