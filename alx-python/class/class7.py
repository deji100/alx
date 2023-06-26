class Square:
    """A Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square instance

        arguments:
            size: size arg must be an integer
            and not less than 0

            position: position arg must be a tuple
            with two integers
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        self.__position = position

    @property
    def size(self):
        """A getter method that retrieves private size attribut"""

        return self.__size

    @size.setter
    def size(self, value):
        """A setter method that sets a new property for size"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """A getter method that retrieves private size attribut"""

        return self.__position

    @position.setter
    def position(self, value):
        """A setter method that sets a new property for size"""

        if not isinstance(value, tuple) or not len(value) == 2 or \
                not all([isinstance(x, int) for x in value]) or \
                not all([z >= 0 for z in value]):
            raise TypeError("position must be a tuple of 2 positive \
                     integers")
        else:
            self.__position = value

    def area(self):
        """A method that returns the current square area"""

        return self.__size**2

    def my_print(self):
        """Prints the size with #"""

        if self.__size > 0:
            for i in range(self.__size):
                if self.__position[1] > 0:
                    print("_" * self.__position[0], end="")
                else:
                    print(" " * self.__position[0], end="")
                print("#" * self.__size)
        else:
            print()

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")