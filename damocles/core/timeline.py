import heapq
from threading import Thread
from .item import Item
from .wait import wait


class TimeLine(Thread):
    def __init__(self):
        super(TimeLine).__init__(name='damocles')

        self.time = 0
        self.lst = []

    def push(self, item):
        """
        push an item into time line
        :param item: instance of Item class
        :return: None
        """
        if not isinstance(item, Item):
            raise TypeError('item must be a instance of Item class')

        if not self.head:
            self.head = item
        else:
            if item.time < self.head:
                item.next = self.head
                self.head = item
            else:
                tmp = self.head

                while tmp.time < item.time and tmp.next:
                    tmp = tmp.next

                item.next = tmp.next
                tmp.next = item

    def run(self):

        # interval = self.head
        from queue import PriorityQueue