## Marius
--------

Light weight job scheduling tool with more performance and scalability.


### Installation

```shell
pip install marius
```

### Usage Example

```python
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
```

### TODO
1. add automatic test support
2. add more helper function
3. add doc

### Welcome to contribute
Feel free to open a issue or start a pull request. 
You are welcome.