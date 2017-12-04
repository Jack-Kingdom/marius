import time


class Item(object):
    def __init__(self, func, delay, repeat, *args, **kwargs):
        """

        :param func: function that to be run
        :param delay: time delay, unit: seconds
        :param repeat: repeat how many times, endless if value less than zero
        :param args: func's args
        :param kwargs: func's kwargs
        """
        assert callable(func)
        assert delay > 0
        assert isinstance(repeat, int)

        self.func = func
        self.time = time.time() + delay
        self.repeat = repeat
        self.args = args
        self.kwargs = kwargs

    def __eq__(self, other):
        if not isinstance(other, Item):
            raise TypeError('only Item object can be compare.')

        return self.time == other.time
