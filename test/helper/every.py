import time
import unittest
from marius.core import Task, TimeLine
from marius.helper import every

interval = 2


@every(interval)
def func():
    return time.time()


class EveryUnitTest(unittest.TestCase):

    def test_interval(self):
        tl = TimeLine()

        last = None
        for _ in range(5):
            tl.wait_next()
            cur = tl.run()

            if last:
                self.assertEqual(interval, round(cur - last))
            last = cur
