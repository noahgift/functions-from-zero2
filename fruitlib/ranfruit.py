from random import choices

def fruit_generator(fruit):
    """Returns back random fruit"""

    fruits = ["apple", "cherry"]
    fruits.append(fruit)
    return choices(fruits)