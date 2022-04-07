from random import choices
import fire

def fruit_generator(fruit):
    """Returns back random fruit"""

    fruits = ["apple", "cherry"]
    fruits.append(fruit)
    print(f"You added this fruit {fruit}")
    print(f"Randomly selecting from all fruits {fruits}")
    return choices(fruits)


if __name__ == '__main__':
    fire.Fire(fruit_generator)
