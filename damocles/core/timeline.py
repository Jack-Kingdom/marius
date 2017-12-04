import time
from threading import Thread, Condition, Lock
from .item import Item
from .wait import wait
from .utils import SingletonDecorator


@SingletonDecorator
class TimeLine(Thread):
    def __init__(self):
        super(TimeLine).__init__(name='damocles')

        self.time = 0
        self.lst = []
        self.lock = Lock()
        self.cond = Condition(Lock())

    def push(self, item):
        """
        push an item into time line
        :param item: instance of Item class
        :return: None
        """
        if not isinstance(item, Item):
            raise TypeError('item must be a instance of Item class')

        with self.lock:
            self.lst.append(item)

        with self.cond:
            self.cond.notify()

    def run(self):
        while True:
            with self.lock:
                jobs_num = len(self.lst)

            if not jobs_num:
                with self.cond:
                    self.cond.wait()

            # todo assume first is the most recent job
            todo = self.lst[0]
            interval = todo.time - time.time()
            if interval > 0:
                with self.cond:
                    self.cond.wait(interval)
            else:
                todo.func(*todo.args, **todo.kwargs)
                if todo.repeat:
                    todo.repeat -= 1
                    # pop & push
                else:
                    pass
                    # pop item
