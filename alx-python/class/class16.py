#!/usr/bin/python3
"""Defines Square class"""


class Square:
    """A Square class"""

    def __init__(self, size=0):
        """Initializes a square instance

        argument:
            size: size arg must be an integer
            and not less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

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

    def area(self):
        """A method that returns the current square area"""
        return self.__size**2
    
    def __lt__(self, other):
        """Reps the less than char comparison of two square instances"""
        return self.area() < other.area()

    def __le__(self, other):
        """Reps the less than equal to symbol comparison of two square instances"""
        return self.area() <= other.area()

    def __eq__(self, other):
        """Reps the equal to symbol comparison of two square instances"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Reps the not equal to symbol comparison of two square instances"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Reps the greater than char comparison of two square instances"""
        return self.area() > other.area()
    
    def __ge__(self, other):
        """Reps the greater than equal symbol comparison of two square instances"""
        return self.area() >= other.area()
    
s_5 = Square(5)
s_6 = Square(6)

if s_5 < s_6:
    print("Square 5 < Square 6")
if s_5 <= s_6:
    print("Square 5 <= Square 6")
if s_5 == s_6:
    print("Square 5 == Square 6")
if s_5 != s_6:
    print("Square 5 != Square 6")
if s_5 > s_6:
    print("Square 5 > Square 6")
if s_5 >= s_6:
    print("Square 5 >= Square 6")


# alx-higher_level_programming/0x06-python-classes