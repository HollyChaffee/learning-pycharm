from math import add_numbers
from person import Person

name = "Latisha"
name2 = "William"


def hello(name: str):
    print(name.upper())


def sunny_method(name):
    p = Person(name)
    print(p)


if __name__ == '__main__':
    # TODO: Fix bug
    print("Pycharm is Awesome")
    print("Hello")
    holly = "Holly"
    print(holly)
    print(add_numbers(2, 2))
    sunny_method("Johnny")
