import time
from sisyphus.core import Job, TimeLine
from sisyphus.helper import every

now = time.time()
before = [now for _ in range(10)]


def func1(num):
    print(num, time.time() - before[num])
    before[num] = time.time()


if __name__ == '__main__':
    tl = TimeLine()
    tl.add(Job(every(2), func1, 2))
    tl.add(Job(every(3), func1, 3))
    tl.add(Job(every(4), func1, 4))

    while tl.has_jobs():
        tl.wait_next()
        tl.run()
    else:
        print("all job run over")
