from data.proposition import *

class Snapshot(object):
    def __init__(self, problem_file):
        self._propositions = set()
        self._goals = set()
        with open(problem_file, 'r') as input:
            content = input.read()
        init = content.index(':init')
        endInit = content.index('(:goal (and')
        for prop in content[init+5:endInit].split('\n'):
            prop = prop.replace('(', '').replace(')', '').replace('\n', '').strip()
            if not prop: continue
            self._propositions.add(Proposition(True, prop[:prop.index(' ')], prop[prop.index(' ')+1:].split(' ')))
        for goal in content[endInit+11:].split('\n'):
            goal = goal.replace('(', '').replace(')', '').replace('\n', '').strip()
            if not goal: continue
            self._goals.add(Proposition(True, goal[:goal.index(' ')], goal[goal.index(' ')+1:].split(' ')))
    def update(self, propositions):
        for prop in propositions:
            self._propositions.discard(Proposition(not prop._truth, prop._functor, prop._args))
            self._propositions.add(prop)
            self._goals.discard(prop)
    def __str__(self):
        res = '(:init\n'
        for prop in self._propositions:
            res = res + '  (' + str(prop).replace(',', ' ') + ')\n'
        res = res + ')\n'
        res = res + '(:goal (and\n'
        for goal in self._goals:
            res = res + '  (' + str(goal).replace(',', ' ') + ')\n'
        res = res + ')'
        return res
