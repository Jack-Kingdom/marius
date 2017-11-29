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
        self.delay = delay
        self.repeat = repeat
        self.args = args
        self.kwargs = kwargs

        self.time = delay