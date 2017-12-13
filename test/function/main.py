import time
from marius.core import Task, TimeLine

now = time.time()
before = [now for _ in range(10)]


def func(num):
    print('task-', num, time.time() - before[num])
    before[num] = time.time()


if __name__ == '__main__':
    tl = TimeLine()
    tl.add(Task(iter([now + i for i in [2, 3, 5]]), func, 3))
    while tl.has_tasks():
        tl.wait_next()
        tl.run()
    else:
        print("all job run over")
