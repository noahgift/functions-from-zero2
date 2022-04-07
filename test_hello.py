from hello import fruit_generator


def test_fruit_generator():
    """Tests Fruit"""

    fruits = ["apple", "cherry"]
    assert fruits[0] or fruits[1] in fruit_generator(fruits)
