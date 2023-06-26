#!/usr/bin/python3
"""Defines a rectangle class inheriting from base class"""
from base import Base


class Rectangle(Base):
    """A rectangle class that inherits from base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a rectangle instance"""

        if type(width) is not int:
            raise TypeError("width must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")

        if type(height) is not int:
            raise TypeError("height must be an integer")

        if height <= 0:
            raise ValueError("height must be > 0")

        if type(x) is not int:
            raise TypeError("x must be an integer")

        if x < 0:
            raise ValueError("x must be >= 0")

        if type(y) is not int:
            raise TypeError("y must be an integer")

        if y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Returns the width of an instance"""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of an instance to value"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Returns the height of an instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of an instance to value"""
        if not type(value) == int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Returns the x of an instance"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x of an instance to value"""
        if not type(value) == int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Returns the y of an instance"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y of an instance to value"""
        if not type(value) == int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Calculates and returns the area of a rectangle instance"""

        return self.width * self.height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""

        for x in range(self.y):
            print("")

        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def update(self, *args, **kwargs):
        """Updates attrs of an instance"""

        if args and len(args) != 0:
            for i in args:
                if args.index(i) == 0:
                    self.id = args[0]
                elif args.index(i) == 1:
                    self.width = args[1]
                elif args.index(i) == 2:
                    self.height = args[2]
                elif args.index(i) == 3:
                    self.x = args[3]
                else:
                    self.y = args[4]
        else:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                elif k == 'width':
                    self.width = v
                elif k == 'height':
                    self.height = v
                elif k == 'x':
                    self.x = v
                else:
                    self.y = v

    def to_dictionary(self):
        """Returns the dictionary rep of a rectangle instance"""

        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Returns a str rep of a rectangle instance"""

        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
