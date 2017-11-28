from damocles.decr import SingletonDecorator


@SingletonDecorator
class Dog(object):
    pass


if __name__ == '__main__':
    dog1 = Dog()
    dog2 = Dog()

    assert id(dog1) == id(dog2)
