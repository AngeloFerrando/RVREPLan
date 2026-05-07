import json

class Proposition(object):
    """Grounded predicate instance tracked in the execution snapshot."""

    def __init__(self, truth, functor, args):
        self._truth = truth
        self._functor = functor
        self._args = args

    def __str__(self):
        """Return the monitor/log representation, prefixing false facts with not_."""
        res = ''
        if not self._truth:
            res = res + 'not_'
        res = res + self._functor
        if self._args:
            aux_args = [str(arg) for arg in self._args]
            res = res + ',' + ','.join(aux_args)
        return res

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

    def __eq__(self, other):
        if isinstance(other, Proposition):
            if self._truth != other._truth or self._functor != other._functor:
                return False
            for i in range(0, len(self._args)):
                if self._args[i] != other._args[i]:
                    return False
            return True
        else:
            return False

    def __ne__(self, other):
        return (not self.__eq__(other))

    def __hash__(self):
        return hash(self.__repr__())

    def __repr__(self):
        return 'Proposition({t}, {f}, {a})'.format(t=self._truth, f=self._functor, a=self._args)
