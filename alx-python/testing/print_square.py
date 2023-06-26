"""Defines a function that prints a
square with # and accepts one argument
size which must be an integer
"""


def print_square(size):
    """A function that accepts an argument
    'size' and prints a square with #
    """

    if not type(size) is int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            print("#" * size)