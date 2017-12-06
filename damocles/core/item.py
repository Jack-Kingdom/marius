class Item(object):
    def __init__(self, func, sequence):
        """
        wrap a function into a Item
        :param func:
            function that to be run,
            partial it before if func has arguments
        :param sequence:
            a generator of unix time
        """
        if not callable(func):
            raise ValueError('func must be callable')

        self.time = next(sequence)
        self.sequence = sequence
        self.func = func

    def __lt__(self, other):
        if not isinstance(other, Item):
            raise TypeError('only Item object can be compare.')

        return self.time < other.time
