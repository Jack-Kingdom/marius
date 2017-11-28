from damocles.decr import SingletonDecorator


@SingletonDecorator
class Dog(object):
    def bite(self):
        print('wong! wong!')


if __name__ == '__main__':
    dog1 = Dog()
    dog2 = Dog()

    print(id(dog1))
    print(id(dog2))
    assert id(dog1) == id(dog2)
