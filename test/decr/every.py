import time
from marius.core import Task, TimeLine
from marius.helper import every

now = time.time()
before = [now for _ in range(10)]


def func1(num):
    print(num, time.time() - before[num])
    before[num] = time.time()


if __name__ == '__main__':
    tl = TimeLine()
    tl.add(Task(every(2), func1, 2))
    tl.add(Task(every(3), func1, 3))
    tl.add(Task(every(4), func1, 4))

    while tl.has_tasks():
        tl.wait_next()
        tl.run()
    else:
        print("all job run over")