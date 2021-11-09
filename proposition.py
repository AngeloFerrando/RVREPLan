class Proposition(object):
    def __init__(self, truth, functor, args):
        self._truth = truth
        self.functor = fucntor
        self.args = args
    def __str__(self):
        res = ''
        if not self._truth:
            res = res + 'not_'
        res = res + self._functor
        if args:
            aux_args = [str(arg) for arg in args]
            res = res + '(' + ','.join(aux_args) + ')'
        return res
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)
