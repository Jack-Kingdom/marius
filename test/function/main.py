import time
from marius.core import Task, TimeLine

now = time.time()


def func(num):
    print('task-{0}'.format(num))


if __name__ == '__main__':
    tl = TimeLine()
    tl.add(Task(iter([now + i for i in [2, 3, 5]]), func, 3))
    while tl.has_tasks():
        tl.wait_next()
        tl.run()
    else:
        print("all job run over")
