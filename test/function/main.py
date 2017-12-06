import time
import functools
import itertools
from damocles import *

before = [0 for _ in range(10)]


def func1(num):
    if before[num]:
        print(num, time.time() - before[num])
    before[num] = time.time()


if __name__ == '__main__':
    now = time.time()

    tl = TimeLine()
    # tl.push(Item(functools.partial(func1, 1), (now + i for i in itertools.count(1))))
    tl.push(Item(functools.partial(func1, 2), (now + i * 5 for i in range(1, 3))))
    while True:
        try:
            tl.wait_next()
        except RuntimeError as e:
            # all job finished
            exit(0)
        else:
            tl.run()
