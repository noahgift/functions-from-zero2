from fruitlib.ranfruit import fruit_generator
import fire


def fruit_generator_cli(fruit):
    """Returns back random fruit"""

    fruits = fruit_generator(fruit)
    print(f"You added this fruit {fruit}")
    return fruits


if __name__ == "__main__":
    fire.Fire(fruit_generator_cli)
