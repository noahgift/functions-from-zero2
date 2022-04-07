import click
from fruitlib.ranfruit import fruit_generator


@click.command()
@click.option("--fruit", help="Fruit to add")
def genfruit(fruit):
    """Pass in additional fruit"""

    chosen_random_fruit = fruit_generator(fruit)
    if fruit in chosen_random_fruit:
        click.echo(
            click.style(
                f"Your choice was randomly selected: {fruit}", fg="red", bold=True
            )
        )
    else:
        click.echo(
            click.style(f"Here is your random fruit {chosen_random_fruit}", fg="green")
        )


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    genfruit()
