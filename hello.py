from random import choices


def fruit_generator(fruits):
    """Returns back random fruit"""

    return choices(fruits)


print(fruit_generator(["apple", "cherry", "peach"]))
